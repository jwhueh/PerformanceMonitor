from visual import *
import time
import numpy as np
import psutil

class test(object):
    def __init__(self):
        print "start"
        self.red = 0
        self.green = 0
        self.blue = 1
	self.cpuLoad = 0

        self.obj = sphere(radius=1.0, color=(self.red, self.green, self.blue))

    def changeColor(self,x,y,z):
        #start = time.ctime()
        #print "time", start
        currentX = self.red
        currentY = self.green
        currentZ = self.blue
        #print currentX, x, currentY, y, currentZ, z

	xarr = self.gotToValue(currentX, x)
	yarr = self.gotToValue(currentY, y)
	zarr = self.gotToValue(currentZ, z)
        
	#print "xarr"
        #print xarr
        #print "yarr"
        #print yarr
        #print "zarr"
        #print zarr
        
        for i in range(100):
            rate(75)
            #print xarr[i], yarr[i], zarr[i]
            
	    self.obj.color = (xarr[i],yarr[i],zarr[i])
            self.x = xarr[i]
            self.y = yarr[i]
            self.z = zarr[i]

        self.red = x
        self.green = y
        self.blue = z
        self.obj.color  = (x,y,z)      


    def gotToValue(self,startVal, endVal):
        arr = np.empty(100)
        #print "gotozero:",startVal, endVal, (startVal - endVal)/100.
        if  startVal ==0 and endVal == 0:
            return np.zeros(100)
	if startVal == 1 and endVal == 1:
	    arr.fill(1)
	    return arr
	if startVal == endVal:
	    arr.fill(endVal)
	    return arr
        if endVal < startVal:
            arr=(np.arange(start = endVal, stop = startVal, step = np.absolute((endVal - startVal)/100.)))
            return np.fliplr([arr])[0]
        else:
            return np.arange(start = startVal, stop = endVal, step = np.absolute((startVal - endVal)/100.))

    def cpuStat(self):
	percs = psutil.cpu_percent(interval=0, percpu=True)
	#print percs, np.sum(percs)/(len(percs)*100)
	self.cpuLoad = np.sum(percs)/(len(percs)*100)
	if self.cpuLoad  < 0.25:
	    blue = 1
	    red = 0
	    green = 0
	if self.cpuLoad >=0.25 and self.cpuLoad <=.75:
	    green = self.cpuLoad
	    blue = 0
	    red = 0
	if self.cpuLoad >.75:
	    red = self.cpuLoad 
	    blue = 0
	    green = 0
	self.changeColor(red, green, blue)

    def run(self):
	while True:
		self.cpuStat()
		#print self.red, self.green, self.blue
		# implement

if __name__ == "__main__":
    t = test()
    t.run()
