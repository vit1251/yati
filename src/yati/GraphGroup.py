#

from GraphGroupLine import GraphGroupLine


class GraphGroup(object):
    def __init__(self, name, owner=None):
        self.owner = owner
        #
        self.name = name
        self.lines = []

    def createLine(self, name):
        line = GraphGroupLine(owner=self, name=name) 
        self.lines.append(line)
        return line
