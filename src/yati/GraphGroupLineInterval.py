#

from Color import Color


class GraphGroupLineInterval(object):
    def __init__(self, start, end, color=Color.GRAY, text=None, owner=None):
        self.owner = owner
        #
        self.start = start
        self.end = end
        self.color = color
        #
        self.text = text
