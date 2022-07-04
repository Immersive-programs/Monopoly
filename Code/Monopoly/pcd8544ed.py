import sys
import math
from pcd8544 import PCD8544_FRAMEBUF
class PCD8544_FRAMEBUF_ED(PCD8544_FRAMEBUF):

    def __init__(self, spi, cs, dc, rst=None):
        super().__init__(spi, cs, dc, rst)
        self.__method = 0
        self.__chars = {}
        self.__existchars = ''
        sys.path.insert(1, "chars")

    def circle(self,r,x,y,col,dx = 1,dy = 1):
        for i in range(r*180):
            #i = i+3.14/180
            ax = x + round(math.sin(i)* (r * dx))
            ay = y + round(math.cos(i)* (r * dy))
            self.fbuf.pixel(ax,ay,col)

    def elipse(self,x,y,dx,dy,col):
        bx = dx/2
        by = dy/2
        for i in range((dx+dy)*180):
            ax = round(x+bx + math.sin(i)* bx)
            ay = round(y+by + math.cos(i)* by)
            self.fbuf.pixel(ax,ay,col)

    def getmethod(self):
        return self.__method

    def setmethod(self,m):
        if m > 0 and m < 2:
            self.__method = m

    def includechars(self):
        import os
        for inc in os.listdir('chars'):
            idd = str(inc.replace('.py',''), "utf-8")
            self.__chars[idd] = __import__(idd).char
            self.__existchars += idd
        del os

    def text(self, string, x, y, col):
        ind = 0
        nstring = ''
        if self.__method == 0:
            for u in string.lower():
                if 1040 <= ord(u) <= 1103:
                    try:
                        imp = __import__(u).char
                        imp.draw(self.fbuf,x,y,ind,col)
                        del imp
                        nstring += ' '
                    except:
                        nstring += '?'
                else:
                    nstring += string[ind]
                ind += 1
        elif self.__method == 1:
            for u in string.lower():
                if 1040 <= ord(u) <= 1103:
                    if u in self.__existchars:
                        nstring += ' '
                        self.__chars[u].draw(self.fbuf,x,y,ind,col)
                    else:
                        nstring += '?'
                else:
                    nstring += string[ind]
                ind += 1
        self.fbuf.text(nstring, x, y, col)

