import random
from PIL import Image


class Ruido():
    def addruido(self, im, senha):
        a = 0
        for i in senha:
            a += ord(i)
        random.seed(a=a, version=2)
        w = im.size[0]
        h = im.size[1]
        tamanho = w * h

        r = []
        g = []
        b = []
        for i in range(tamanho):
            r.append(int(random.gauss(0, 2)))

        for i in range(tamanho):
            g.append(int(random.gauss(0, 2)))

        for i in range(tamanho):
            b.append(int(random.gauss(0, 2)))
        cont = 0

        for i in range(h):
            for j in range(w):
                p = tuple()
                if im.getpixel((j, i))[0] + r[cont] > 255:
                    r1=im.getpixel((j, i))[0]
                else:
                    r1= im.getpixel((j, i))[0] + r[cont]
                if im.getpixel((j, i))[1] + g[cont] > 255:
                    g1=im.getpixel((j, i))[1]
                else:
                    g1= im.getpixel((j, i))[1] + g[cont]
                if im.getpixel((j, i))[2] + g[cont] > 255:
                    b1 = im.getpixel((j, i))[2]
                else:
                    b1 = im.getpixel((j, i))[2] + g[cont]
                p = (r1, g1, b1)
                im.putpixel((j, i), p)
                cont += 1
            return im

    def rmruido(self, im, senha):
        a = 0
        for i in senha:
            a += ord(i)
        random.seed(a=a, version=2)
        w = im.size[0]
        h = im.size[1]
        tamanho = w * h

        r = []
        g = []
        b = []
        for i in range(tamanho):
            r.append(int(random.gauss(0, 2)))

        for i in range(tamanho):
            g.append(int(random.gauss(0, 2)))

        for i in range(tamanho):
            b.append(int(random.gauss(0, 2)))
        cont = 0

        for i in range(h):
            for j in range(w):
                if im.getpixel((j, i))[0] + r[cont] > 255:
                    r1 = im.getpixel((j, i))[0]
                else:
                    r1 = im.getpixel((j, i))[0] - r[cont]
                if im.getpixel((j, i))[1] + g[cont] > 255:
                    g1 = im.getpixel((j, i))[1]
                else:
                    g1 = im.getpixel((j, i))[1] - g[cont]
                if im.getpixel((j, i))[2] + g[cont] > 255:
                    b1 = im.getpixel((j, i))[2]
                else:
                    b1 = im.getpixel((j, i))[2] - g[cont]
                p = (r1, g1, b1)

                im.putpixel((j, i), p)
                cont += 1
        return im
