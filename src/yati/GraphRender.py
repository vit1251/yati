#

import svgwrite


class GraphRender(object):
    def __init__(self, graph):
        self.graph = graph

    def render(self, filename):
        svg = svgwrite.Drawing(filename=filename, size=("800px", "600px"))
        svg.add(svg.line(start=(0, 0), end=(50, 50), style="fill: none; stroke: 1px" ))
        svg.add(svg.text("Hello World", insert=(210, 110)))
        print(svg.tostring())
        svg.save()
