#

import logging
import svgwrite


class Rect(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contain(self, point):
        pass


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GraphRender(object):
    def __init__(self, graph, padding=(0,0,0,10)):
        self.__log = logging.getLogger("yati.render")
        #
        self.__graph = graph
        #
        self.__padding_top, self.__padding_right, self.__padding_bottom, self.__padding_left = padding
        self.__width, self.__height = self.__graph.get_size()

    def _renderGroupTitle(self, svg, group, pos):
        """ Render group title
        """
        group_name = group.name
        group_height = 30
        #
        svg.add(svgwrite.shapes.Rect(insert=(self.__padding_left, pos.y + 0), size=(self.__width - (self.__padding_left), group_height), fill="#F6F5F3"))
        svg.add(svgwrite.text.Text(group_name, insert=(self.__padding_left + 0, pos.y + group_height)))
        #
        pos.y += group_height

    def _renderLineTitle(self, svg, line, pos):
        line_name = line.name
        svg.add(svgwrite.text.Text(line_name, insert=(0, pos.y + 20)))

    def _prepareRange(self):
        """
        """
        # Step 1. Calculate scale
        self._x_min = 0.0
        self._x_max = 0.0
        #
        for group in self.__graph.groups:
            for line in group.lines:
                for interval in line.intervals:
                    self._x_max = max(self._x_max, interval.end)
        #
        self.__log.debug("Range: start = {start!r}, end = {end!r}".format(start=self._x_min, end=self._x_max))
        # Step 2. Calculate row number
        group_count = len(self.__graph.groups)
        line_count = 0
        #
        for group in self.__graph.groups:
            for line in group.lines:
                line_count += 1
        #
        height = self.__height - (30 * group_count)
        line_hight = height / line_count
        for group in self.__graph.groups:
            for line in group.lines:
                line.height = line_hight
     
    def _calculateLineX(self, ct):
        width = self.__width - (self.__padding_left + self.__padding_right)
        result = width * ct / self._x_max
        return result

    def _renderLineInterval(self, svg, line, pos, line_height):
        line_padding_top = 0.25 * line_height
        line_height = line_height
        line_padding_bottom = 0.25 * line_height
        #
        pos_x_start = self._calculateLineX(line.start)
        pos_x_end = self._calculateLineX(line.end)
        #
        size_x = pos_x_end - pos_x_start
        #
        svg.add(svgwrite.shapes.Rect(insert=(self.__padding_left + pos_x_start, pos.y + line_padding_top), size=(size_x, line_height-(line_padding_top+line_padding_bottom)), fill=line.color))

    def _renderLine(self, svg, line, pos):
        line_height = line.height
        # Step 1. Render line intervals
        for interval in line.intervals:
            self._renderLineInterval(svg, interval, pos, line_height)
        # Step 2. Render line title
        self._renderLineTitle(svg, line, pos)
        # Step 3. Make position
        pos.y += line_height

    def _renderGroup(self, svg, group, pos):
        # Step 1. Draw title rectangle
        self._renderGroupTitle(svg, group, pos)
        for line in group.lines:
            self._renderLine(svg, line, pos)

    def _renderGroups(self, svg):
        """ Render group
        """
        pos = Point(x=0, y=0)
        for group in self.__graph.groups:
            self._renderGroup(svg, group, pos)

    def _prepareCanvas(self, svg):
        # Step 1. Draw grid
        
        step_width = (self.__width - self.__padding_left) / 10
        for i in xrange(1, 11):
            svg.add(svgwrite.shapes.Line(start=(self.__padding_left + step_width * i, 0), end=(self.__padding_left + step_width * i, self.__height), stroke="#C0C0C0",
                                         style="shape-rendering: crispEdges"))  # Verticale line
        # Step 2. Draw values
        # Step 3. Draw coord's
        svg.add(svgwrite.shapes.Line(start=(self.__padding_left, 0), end=(self.__padding_left, self.__height), stroke="#666666",
                                         style="shape-rendering: crispEdges"))            # Y-Axes
        svg.add(svgwrite.shapes.Line(start=(self.__padding_left, self.__height), end=(self.__padding_left + (self.__width - self.__padding_left), self.__height), stroke="#666666",
                                         style="shape-rendering: crispEdges"))            # X-Axes

    def render(self, filename=None):
        """ Render
        """
        svg = svgwrite.Drawing(filename=filename)
        #
        self._prepareRange()
        self._prepareCanvas(svg)
        self._renderGroups(svg)
        #
        if filename is not None:
            svg.save()
        else:
            return svg.tostring()
