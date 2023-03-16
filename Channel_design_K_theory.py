#program that gets inputs and outputs a typical Upper Bari doab region channel geometry
#Step 1: inputs required: 1. Discharge Q (m*3/s); 2. Bed slope S; 3. Soil median particle d size or d65
#Step 2: Trial 1: intialize
# d = 2 m, side slope = 0.5 i.e., for every 1 m drop, there's a 0.5 m horizontal distance; manning's coefficient n=d^(1/6)/25.6 or d65^(1/6)/24
#Step 3: Calculation
#critical velocity vcr=0.55*d^0.64
#Area A = Q/vcr
#Bottom breadth b = (A-z(d^2))/d
#Perimeter P = b+(2*d*(1+(z^2))^(1/2))
#Hydraulic radius R = A/P
#Chezy's constant C = ((1/n)+23+(0.00155/S))/(1+((n/(R^(1/2)))*(23+(0.00155/S))))
#Mean velocity vmean=C*((R*S)^(1/2))
#Step 4: Check if vmean == vcr, then proceed to step 5. Else, d=d+0.05, go to step 3
#step 5: Print Bottom breadth = B, channel depth = d
print('Channel design data')

#Q=float(input('1. Discharge required in cusec = '))
#bedslope=float(input('2. Bed slope of channel (vertical/horizontal) = '))
#d=float(input('1. median particle size of channel bed = '))
Q=round(float(input("Design discharge in cumecs = ")),3)
bedslopeinput=round(float(input("Bed slope = 1 in ")),3)
d=round(float(input("median bed particle size = ")),4)
bedslope=1/bedslopeinput
depth=1
area=0
sideslope=0.5
n=round((d**(1/6))/25.6, 3)
vmean=0
C=float(0)
count=1
vcr=round(float(0.55*(depth**0.64)),3)
while vcr!=vmean:
    vcr=round(0.55*(depth**0.64), 3)
    area=round(float(Q)/vcr,3)
    bottombreadth=round((area-(sideslope*(depth**2)))/depth, 3)
    wettedP=round(bottombreadth+(2*depth*(1+(sideslope**2))**(1/2)),3)
    R=round(area/wettedP,3) #R=hydraulic radius
    C = round(((1/n)+23+(0.00155/bedslope))/(1+((n/(R**(1/2)))*(23+(0.00155/bedslope)))),3) #Chezy's constant
    vmean=round(C*((R*bedslope)**(0.5)), 3)
    count=count+1
    depth=round(depth+0.001,3)
depth = round(depth - 0.001,3)
print("\nResults: design geometry of the channel according to Kennedy's regime conditions\n")
print("critical velocity =", vcr)
print("mean velocity =",vmean)
print("channel depth =",depth)
print("channel bottom width =",bottombreadth)
