#

import svgwrite


class Position(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class GraphRender(object):
    def __init__(self, graph):
        self.graph = graph

    def _renderGroupTitle(self, svg, group, pos):
        """ Render group title
        """
        group_name = group.name
        #
        svg.add(svgwrite.shapes.Rect(insert=(pos.x, pos.y + 0), size=( 500, 30 ), fill="#F6F5F3"))
        svg.add(svgwrite.text.Text(group_name, insert=(pos.x + 0, pos.y + 20)))
        #
        pos.y += 30

    def _renderLineTitle(self, svg, line, pos):
        pass

    def _prepareRange(self):
        #
        self._x_min = 0.0
        self._x_max = 0.0
        #
        for group in self.graph.groups:
            for line in group.lines:
                for interval in line.intervals:
                    self._x_max = max(self._x_max, interval.end)
        #
        print("Range: start = {start!r}, end = {end!r}".format(start=self._x_min, end=self._x_max))

    def _calculateLineX(self, ct):
        size_x = 500
        #
        result = size_x * ct / self._x_max
        #
        return result

    def _renderLineInterval(self, svg, line, pos):
        #
        pos_x_start = self._calculateLineX(line.start)
        pos_x_end = self._calculateLineX(line.end)
        #
        size_x = pos_x_end - pos_x_start
        #
        svg.add(svgwrite.shapes.Rect(insert=( pos.x + pos_x_start, pos.y + 10 ), size=( size_x, 20 ), fill=line.color))

    def _renderLine(self, svg, line, pos):
        # Step 1. Render line title
        self._renderLineTitle(svg, line, pos)
        # Step 2. Render line intervals
        for interval in line.intervals:
            self._renderLineInterval(svg, interval, pos)
        # Step 3. Make position
        pos.y += 20

    def _renderGroup(self, svg, group, pos):
        # Step 1. Draw title rectangle
        self._renderGroupTitle(svg, group, pos)
        #
        for line in group.lines:
            pos.y += 5  # Line padding-top
            self._renderLine(svg, line, pos)
            pos.y += 5  # Line padding-bottom

    def _renderGroups(self, svg):
        """ Render group
        """
        pos = Position(x=0, y=0)
        for group in self.graph.groups:
            pos.y += 5      # Group padding-top
            self._renderGroup(svg, group, pos)
            pos.y += 5      # Group padding-bottom

    def _prepareCanvas(self, svg, size):
        # Step 1. Draw coord's
        #svg.add(svgwrite.shapes.Line(start=(10, 10), end=(50, 50), stroke="#006600" ))
        #svg.add(svgwrite.shapes.Line(start=(10, 10), end=(50, 50), stroke="#006600" ))

        # Step 2. Draw values

        # Step 3. Draw grid
        for i in xrange(50):
            svg.add(svgwrite.shapes.Line(start=( 0, 10 * i ), end=( 500, 10 * i ), stroke="#C0C0C0", shapeRendering="crispEdges", style="shape-rendering: crispEdges" ))  # Horizontile line
            svg.add(svgwrite.shapes.Line(start=( 10 * i, 0 ), end=( 10 * i, 500 ), stroke="#C0C0C0", style="shape-rendering: crispEdges" ))  # Verticale line
        

    def render(self, filename=None):
        """ Render
        """
        size = (500, 500)
        svg = svgwrite.Drawing(filename=filename, size=size)
        #
        self._prepareRange()
        self._prepareCanvas(svg, size)
        self._renderGroups(svg)
        #
        if filename is not None:
            svg.save()
        else:
            return svg.tostring()
