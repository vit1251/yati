#

from GraphGroup import GraphGroup


class Graph(object):
    def __init__(self, name=None, size=(500, 500)):
        self.__name = name
        self.__width, self.__height = size
        #
        self.groups = []

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__width, self.__height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def createGroup(self, name):
        group = GraphGroup(owner=self, name=name)
        self.groups.append(group)
        return group
