import  flightline_pb2

def write():
    in_f = open("F_150326_115601.txt", "r")
    flightline = flightline_pb2.Flightline()


    scanline = flightline.scanlines.add()
    for line in in_f:
        x, y, z, i, t, e, a = line.split(' ')
        if e:
            scanline = flightline.scanlines.add()
        point = scanline.points.add()
        point.x = float(x)
        point.y = float(y)
        point.z = float(z)
        point.i = int(i)
        point.t = float(t)
        point.e = bool(e)
        point.a = int(a)

    out_f = open("output.txt", "wb")
    out_f.write(flightline.SerializeToString())
    out_f.close()
    in_f.close()

def read():
    flightline = flightline_pb2.Flightline()
    f = open("output.txt", "rb")
    flightline.ParseFromString(f.read())
    print(flightline.scanlines)
    f.close()

def main():
    # write()
    # read()
    pass
