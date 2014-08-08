import math
import numpy
import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm

def plottimestep(x, y, u):
  """Does a surface plot of u as a function of x and y.
  """

  fig = pylab.figure()
  ax = Axes3D(fig, azim=-128, elev=43)
  surf = ax.plot_surface(x, y, u, rstride=1, cstride=1, norm=LogNorm(), cmap = pylab.cm.jet)
  pylab.xlabel("x")
  pylab.ylabel("y")
  pylab.show(block=False)

if __name__ == "__main__":
  # Demonstrates the usage of the plottimestep() function
  xmax = 10.
  ymax = 10.
  nx = 101
  ny = 101
  dx = xmax/(nx-1)
  dy = ymax/(ny-1)

  u = numpy.zeros((nx, ny), dtype=numpy.float64)
  x = numpy.zeros((nx, ny), dtype=numpy.float64)
  y = numpy.zeros((nx, ny), dtype=numpy.float64)

  for i in range(nx):
    for j in range(ny):
      x[i,j] = i*dx
      y[i,j] = j*dy
      u[i,j] = math.exp(-(x[i,j]-xmax/2.)**2 - (y[i,j]-ymax/2.)**2)

  plottimestep(x,y,u)

  cx = 1
  cy = 1
  nTimeSteps = 200
  dt = 0.01
  for t in range(nTimeSteps):
    print "%s %s %s %s" % (t,int(indices[0]),int(indices[1]), numpy.max(u))
    uold = u.copy()
    for i in range(1,nx-1):
      for j in range(1,ny-1):
        u[i][j] = uold[i][j] - cx*dt*(uold[i][j]-uold[i-1][j])/dx - cy*dt*(uold[i][j]-uold[i][j-1])/dy
    indices = numpy.unravel_index(u.argmax(),u.shape);
  plottimestep(x,y,u)