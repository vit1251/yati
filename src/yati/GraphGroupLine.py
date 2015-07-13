#

from GraphGroupLineInterval import GraphGroupLineInterval


class GraphGroupLine(object):
    def __init__(self, name, owner=None, height=10):
        self.owner = owner
        self.name = name
        #
        self.height = height
        #
        self.intervals = []

    def registerInterval(self, start, end, color):
        interval = GraphGroupLineInterval(owner=self, start=start, end=end, color=color)
        self.intervals.append(interval)
        return interval
