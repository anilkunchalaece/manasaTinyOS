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
if __name__ == '__main__':
    ps = ((30,0), (21, 15), (8,30),(6,45),
            (4,60),(0,75),(-2,90),(-12,110),(-14,150),(-17,300),
            (-29,450),(-37,800),(-42,1000))
    table = InterpolatedArray(ps)

    weightMatrix = [
                    [0,9,-10,7],
                    [9,0,0,5],
                    [-10,0,0,0],
                    [-7,0,0,0]
                  ]
    print len(weightMatrix)
    for listIndex in range(0, len(weightMatrix)) :
        for i in range(0,len(weightMatrix[listIndex])) :
              #print weightMatrix[listIndex][i]
              weightMatrix[listIndex][i] = table[weightMatrix[listIndex][i]]
    g = Graph(4)
    g.graph = weightMatrix
    g.dijkstra(0)  
    #print weightMatrix
    