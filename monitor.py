from visual import *
import time
import numpy as np
import psutil

class test(object):
    def __init__(self):
        print "start"
        self.x = 0
        self.y = 0
        self.z = 1
	self.cpuLoad = 0

        self.obj = sphere(radius=1.0, color=(self.x, self.y, self.z))

    def changeColor(self,x,y,z):
        start = time.ctime()
        #print start
        currentX = self.x
        currentY = self.y
        currentZ = self.z
        print currentX, x, currentY, y, currentZ, z

        #print "xarr"
        xarr = self.gotToValue(currentX, x)
        #print xarr
        #print "yarr"
        yarr = self.gotToValue(currentY, y)
        #print yarr
        #print "zarr"
        zarr = self.gotToValue(currentZ, z)
        #print zarr

        
        for i in range(100):
            rate(50)

            #print xarr[i], yarr[i], zarr[i]
            
            self.obj.color = (xarr[i],yarr[i],zarr[i])
            self.x = xarr[i]
            self.y = yarr[i]
            self.z = zarr[i]

        self.x = x
        self.y = y
        self.z = z
        self.obj.color  = (x,y,z)      


    def gotToValue(self,startVal, endVal):
        arr = np.empty(100)
        #print "gotozero:",startVal, endVal, (startVal - endVal)/100.
        if  startVal ==0 and endVal == 0:
            return np.zeros(100)
	if startVal == 1 and endVal == 1:
	    arr.fill(1)
	    return arr
        if endVal < startVal:
            arr=(np.arange(start = endVal, stop = startVal, step = np.absolute((endVal - startVal)/100.)))
            return np.fliplr([arr])[0]
        else:
            return np.arange(start = startVal, stop = endVal, step = np.absolute((startVal - endVal)/100.))

    def cpuStat(self):
	percs = psutil.cpu_percent(interval=0, percpu=True)
        for cpu_num, perc in enumerate(percs):
            print (" CPU%-2s %5s%%" % (cpu_num,perc))
	print percs, np.sum(percs)/(len(percs)*100)
	self.cpuLoad = np.sum(percs)/(len(percs)*100)
	primary = np.median([percs[0],percs[2]])/100.
	secondary = np.median([percs[1],percs[3]])/100.
	if primary  < 0.25:
	    self.changeColor(0, self.y, 1)  
	if primary >=0.25:
	    self.changeColor(1, self.y, 0)


    def run(self):
	while True:
		self.cpuStat()
		time.sleep(1)

if __name__ == "__main__":
    t = test()
    t.run()
