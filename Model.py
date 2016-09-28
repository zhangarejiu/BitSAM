import sys
import matplotlib.pyplot as plt
import numpy
def avg_list(nlist):
    narray=numpy.array(nlist)
    sum1=narray.sum()
    narray2=narray*narray
    sum2=narray2.sum()
    mean=sum1/len(nlist)
    var=sum2/len(nlist)-mean**2
    return mean

def var_list(nlist):
    narray=numpy.array(nlist)
    sum1=narray.sum()
    narray2=narray*narray
    sum2=narray2.sum()
    mean=sum1/len(nlist)
    var=sum2/len(nlist)-mean**2
    return var


def PlotDemo(x1,y1,title):
 fig  = plt.figure()
 ax = fig.add_subplot(1,1,1)
 ax.plot(x1,y1)
 fig.suptitle(title, fontsize = 14, fontweight='bold')
 ax.set_xlabel("x time")
 ax.set_ylabel("y cover")
 plt.show()

def PlotDemo2(x1,y1,y2,title,titleY1,titleY2):
    fig  = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x1,y1)
    ax.plot(x1,y2)
    fig.suptitle(title, fontsize = 14, fontweight='bold')
    ax.set_xlabel("x time")
    ax.set_ylabel("y cover")
    plt.legend((titleY1, titleY2)) 
    plt.grid(True)
    plt.show()
maxDif = 0
minDif = 99999
flag = 0
HuobiSavg = 0
OkcoinSavg = 0
HuobiBavg = 0
OkcoinBavg = 0
Hs_Ob_cover_avg = 0
Hb_Os_cover_avg = 0
Hs_Ob_cover = []
Hb_Os_cover = []
HuobiSell = []
OkcoinSell = []
HuobiBuy = []
OkcoinBuy = []
X1 = []
X2 = []
i = 0
j = 0
CoverHoBAvg = 0
CoverHoBVar = 0
HuobiCheck = 100
OkcoinCheck = 100
HuobiBT = 0.1
OkcoinBT = 0.1
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip().split(",")
        HuobiSP = float(line[0].split(":")[1])
        OkcoinSP = float(line[1].split(":")[1])
        if(flag ==0):
            HuobiSell.append(HuobiSP)
            OkcoinBuy.append(OkcoinSP)
            Hs_Ob_cover.append(HuobiSP-OkcoinSP)
            if len(Hs_Ob_cover)>500:
                temp_list = [Hs_Ob_cover[i] for i in range(len(Hs_Ob_cover)-500,len(Hs_Ob_cover))]
                CoverHoBAvg = avg_list(temp_list)
                CoverHoBVar = var_list(temp_list)
                if(HuobiSP-OkcoinSP<CoverHoBAvg-0.1*CoverHoBVar and
                HuobiBT<OkcoinBT):
                    HuobiBT += 0.03
                    OkcoinBT -= 0.03
                    HuobiCheck -= 0.03*HuobiSP
                    OkcoinCheck += 0.03*OkcoinSP
                    profile = HuobiCheck + OkcoinCheck - 200
                    print "HuobiCheck: " + str(HuobiCheck)
                    print "OkcoinCheck: " + str(OkcoinCheck) 
                    print "CoverHoBAvg: " + str(CoverHoBAvg)
                    print "CoverHoBVar: " + str(CoverHoBVar) 
                    print "HuobiBT: " + str(HuobiBT)
                    print "OkcoinBT: " + str(OkcoinBT)
                    print "H to O: "+ str(profile)
            flag = 1
            X1.append(i)
            i+=1

        else:
            HuobiBuy.append(HuobiSP)
            OkcoinSell.append(OkcoinSP)
            Hb_Os_cover.append(HuobiSP-OkcoinSP)
            if len(Hs_Ob_cover)>500:
                temp_list = [Hb_Os_cover[i] for i in range(len(Hb_Os_cover)-500,len(Hb_Os_cover))]
                CoverHoBAvg = avg_list(temp_list)
                CoverHoBVar = var_list(temp_list)
                if(HuobiSP-OkcoinSP>CoverHoBAvg+0.1*CoverHoBVar and
                HuobiBT>=OkcoinBT):
                    HuobiBT -= 0.03
                    OkcoinBT += 0.03
                    HuobiCheck += 0.03*HuobiSP
                    OkcoinCheck -= 0.03*OkcoinSP
                    profile = HuobiCheck + OkcoinCheck - 200
                    print "HuobiCheck: " + str(HuobiCheck)
                    print "OkcoinCheck: " + str(OkcoinCheck) 
                    print "CoverHoBAvg: " + str(CoverHoBAvg)
                    print "CoverHoBVar: " + str(CoverHoBVar) 
                    print "HuobiBT: " + str(HuobiBT)
                    print "OkcoinBT: " + str(OkcoinBT)
                    print "O to H: "+ str(profile)
            flag = 0
            X2.append(j)
            j+=1

