#

def muldiv(number, numerator, denominator):
    return number * numerator / denominator


class Color(object):
    GRAY    = "#CCCCCC"
    YELLOW  = "#FFE97F"
    RED     = "#FF3D33"
    GREEN   = "#53C614"
    ORANGE  = "#FF973D"

    def __init__(self, r, g, b):
        self.__r = r
        self.__g = g
        self.__b = b

    @staticmethod
    def parse(value):
        result = None
        if value.startswith("#"):
            r_h = value[1:3]
            g_h = value[3:5]
            b_h = value[5:7]
            #
            #print r_h,  g_h, b_h
            #
            r = int(r_h, 16)
            g = int(g_h, 16)
            b = int(b_h, 16)
            #
            result = Color(r, g, b)
        else:
            raise ValueError("Invalid color value")
        #
        return result

    def createDark(self, percent):
        """
        :param percent: percent of darknest 0..100
        """
        r = self.__r - muldiv(self.__r, percent, 100)
        g = self.__g - muldiv(self.__g, percent, 100)
        b = self.__b - muldiv(self.__b, percent, 100)
        #
        return Color(r, g, b)

    def darker(self, percent):
        """
        :param percent: percent of darknest 0..100
        """
        self.__r = self.__r - muldiv(self.__r, percent, 100)
        self.__g = self.__g - muldiv(self.__g, percent, 100)
        self.__b = self.__b - muldiv(self.__b, percent, 100)

    def createLight(self, percent):
        r = self.__r + muldiv(255 - self.__r, percent, 100)
        g = self.__g + muldiv(255 - self.__g, percent, 100)
        b = self.__b + muldiv(255 - self.__b, percent, 100)
        #
        return Color(r, g, b)

    def lighter(self, percent):
        """
        :param percent: percent of darknest 0..100
        """
        self.__r = self.__r + muldiv(255 - self.__r, percent, 100)
        self.__g = self.__g + muldiv(255 - self.__g, percent, 100)
        self.__b = self.__b + muldiv(255 - self.__b, percent, 100)

    def __str__(self):
        return "#{r:02X}{g:02X}{b:02X}".format(r=self.__r, g=self.__g, b=self.__b)


if __name__ == "__main__":
    c = Color.parse("#100820")
    print c
    c.lighter(50)
    print c
