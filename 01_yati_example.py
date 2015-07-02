#!/usr/bin/python

import sys
sys.path.append("src")
import yati


class Application(object):
    def run(self):
        g = yati.Graph()
        gg1 = g.createGroup(name="Group 1")
        gg1l1 = gg1.createLine(name="Line 1.1")
        gg1l1.registerInterval(start=0.5, end=2.5, color=yati.Color.RED)
        gg1l1.registerInterval(start=2.5, end=3.5, color=yati.Color.GREEN)
        #
        gg1l2 = gg1.createLine(name="Line 1.2")
        #
        gg1l2.registerInterval(start=1.5, end=2.5, color=yati.Color.ORANGE)
        gg1l2.registerInterval(start=3.5, end=4.5, color=yati.Color.YELLOW)
        #
        gg2 = g.createGroup(name="Group 2")
        #
        gg2l1 = gg2.createLine(name="Line 2.1")
        gg2l1.registerInterval(start=1.5, end=4.5, color=yati.Color.GREEN)
        #
        gr = yati.GraphRender(graph=g)
        gr.render(filename="1.svg")


if __name__ == "__main__":
    app = Application()
    app.run()
