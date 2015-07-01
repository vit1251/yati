#

from GraphGroup import GraphGroup


class Graph(object):
    def __init__(self, name=None):
        self.name = name
        self.groups = []

    def createGroup(self, name):
        group = GraphGroup(owner=self, name=name)
        self.groups.append(group)
        return group
