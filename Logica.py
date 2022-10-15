def logicaocult(pix, bitmsg, k, rgb):  # k = 2, 4, 8, 16, 32, 64
    boo = not ((bitmsg == "0" and pix[rgb] % k < k / 2) or (bitmsg == "1" and pix[rgb] % k >= k / 2)
               )
