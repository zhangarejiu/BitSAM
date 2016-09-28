import sys
import matplotlib.pyplot as plt

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
for line in sys.stdin:
    line = line.strip().split(",")
    HuobiSP = float(line[0].split(":")[1])
    OkcoinSP = float(line[1].split(":")[1])
    if(flag ==0):
        
        HuobiSell.append(HuobiSP)
        HuobiSavg+=HuobiSP
        OkcoinBuy.append(OkcoinSP)
        OkcoinBavg+=OkcoinSP
        Hs_Ob_cover_avg+=(HuobiSP-OkcoinSP)
        Hs_Ob_cover.append(HuobiSP-OkcoinSP)
        flag = 1
        X1.append(i)
        i+=1

    else:
        HuobiBuy.append(HuobiSP)
        HuobiBavg+=HuobiSP
        OkcoinSell.append(OkcoinSP)
        OkcoinSavg+=HuobiSP
        Hb_Os_cover_avg+=(HuobiSP-OkcoinSP)
        Hb_Os_cover.append(HuobiSP-OkcoinSP)
        flag = 0
        X2.append(j)
        j+=1
Hs_Ob_cover_avg /= len(Hs_Ob_cover)
Hb_Os_cover_avg /= len(Hb_Os_cover)
HuobiSavg /= len(HuobiSell)
HuobiBavg /= len(HuobiBuy)
OkcoinSavg /= len(OkcoinSell)
OkcoinBavg /= len(OkcoinBuy)
PlotDemo2(X1,HuobiSell,OkcoinBuy,"avg_price","Huobi","Okcoin")
#PlotDemo(X1,Hs_Ob_cover,"Hs_Ob_cover")
#for x in rang(0,len(HuobiSell)):


