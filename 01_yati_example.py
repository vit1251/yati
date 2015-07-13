#!/usr/bin/python

import sys
import random
sys.path.append("src")
import yati


class Application(object):
    def run(self):
        g = yati.Graph(size=(800, 600))
        gg1 = g.createGroup(name="Suite 1")
        gg1l1 = gg1.createLine(name="AR_0001")
        gg1l1.registerInterval(start=0.0, end=2.5, color=yati.Color.GRAY)
        gg1l1.registerInterval(start=2.5, end=5.0, color=yati.Color.RED)
        gg1l1.registerInterval(start=5.0, end=7.5, color=yati.Color.GREEN)
        gg1l1.registerInterval(start=7.5, end=10.0, color=yati.Color.YELLOW)
        #
        gg1l2 = gg1.createLine(name="AR_0002")
        #
        gg1l2.registerInterval(start=2.5, end=5.0, color=yati.Color.parse(yati.Color.GREEN).createDark(50))
        gg1l2.registerInterval(start=5.0, end=7.5, color=yati.Color.parse(yati.Color.GREEN).createLight(50))
        #
        gg2 = g.createGroup(name="Suite 2")
        #
        for i in range(10):
            gg2l1 = gg2.createLine(name="AR_{num:04d}".format(num=i+10))
            color = random.choice([yati.Color.GREEN, yati.Color.YELLOW, yati.Color.GRAY, yati.Color.ORANGE, yati.Color.RED])
            start = random.choice([0.5, 1.5, 2.5, 3.5, 4.5])
            end = start + random.choice([0.5, 1.5, 2.5, 3.5, 4.5])
            gg2l1.registerInterval(start=start, end=end, color=color)
        #
        gr = yati.GraphRender(graph=g, padding=(0,0,0,100))
        gr.render(filename="1.svg")


if __name__ == "__main__":
    app = Application()
    app.run()
