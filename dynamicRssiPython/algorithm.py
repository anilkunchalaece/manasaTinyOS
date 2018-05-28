class InterpolatedArray(object):

  """An array-like object that provides
  interpolated values between set ps."""

  def __init__(self, ps):
    self.ps = sorted(ps)

  def __getitem__(self, x):
    if x < self.ps[0][0] or x > self.ps[-1][0]:
      raise ValueError
    lower_p, upper_p = self._GetBoundingps(x)
    return self._Interpolate(x, lower_p, upper_p)

  def _GetBoundingps(self, x):
    """Get the lower/upper ps that bound x."""
    lower_p = None
    upper_p = self.ps[0]
    for p  in self.ps[1:]:
      lower_p = upper_p
      upper_p = p
      if x <= upper_p[0]:
        break
    return lower_p, upper_p

  def _Interpolate(self, x, lower_p, upper_p):
    """Interpolate a Y value for x given lower & upper
    bounding ps."""
    slope = (float(upper_p[1] - lower_p[1]) /
             (upper_p[0] - lower_p[0]))
    return lower_p[1] + (slope * (x - lower_p[0]))


from dj import *
from time import sleep
import re
import serial
a=0
d=0
z=0
b=z-a
c=z-d

#cmd = 'java RssiDemo -comm serial@/dev/ttyUSB0:telos'
#cmd = 'python ./output.py'

ser = serial.Serial('/dev/ttyACM0',9600)

if __name__ == '__main__':
    ps = ((30,0), (21, 15), (8,30),(6,45),
            (4,60),(0,75),(-2,90),(-12,110),(-14,150),(-17,300),
            (-29,450),(-37,800),(-42,1000))
    table = InterpolatedArray(ps)

    # weightMatrix = [
    #                 [0,a,0,d],
    #                 [a,0,b,0],
    #                 [0,b,0,0],
    #                 [d,0,c,0]
    #               ]
    #print len(weightMatrix)
    while True:
        user_input = input("please enter y to calculate the shortest path ")
        if user_input == y:
            for i in range(0,6):
                recvData = ser.readline()
                val = re.findall('\d+',recvData)
                if int(val[0]) == 1 :
                    a =  table[int(val[1])]
                    print "received rssi val for node 1"
                elif int(val[0]) == 2:
                    z = table[int(val[1])]  
                    print "received rssi for node 2"               
                elif int(val[0]) == 3:
                    d = table[int(val[1])]
                    print "received rssi for node 3"
                sleep(0.02) #optional delay - we need experiment with it
            b=z-a
            c=z-d
            weightMatrix = [
                        [0,a,0,d],
                        [a,0,b,0],
                        [0,b,0,0],
                        [d,0,c,0]
                      ]
            g = Graph(4)
            g.graph = weightMatrix
            g.dijkstra(0)
        else :
          print "please enter y to calulate the shortest path"  
    #print weightMatrix
    