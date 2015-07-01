#

from GraphGroupLineInterval import GraphGroupLineInterval


class GraphGroupLine(object):
    def __init__(self, name, owner=None):
        self.owner = owner
        self.name = name
        #
        self.intervals = []

    def registerInterval(self, start, end, color):
        interval = GraphGroupLineInterval(owner=self, start=start, end=end, color=color)
        self.intervals.append(interval)
        return interval
