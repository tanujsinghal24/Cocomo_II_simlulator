def type(i):
    if i=='organic':
        a=2.4
        b=1.05
        c=2.5
        d=0.38
    elif i=='semi detached':
        a=3.0
        b=1.12
        c=2.5
        d=0.35
    else:
        a=3.6
        b=1.20
        c=2.5
        d=0.32
    return a,b,c,d
def calc(elf,ilf,eo,ei,eiq,project):
    if project=='simple':
        ilf,elf,ei,eo,eiq=ilf*7,elf*5,ei*3,eo*5,eiq*3
    elif project=='average':
        ilf,elf,ei,eo,eiq=ilf*10,elf*7,ei*4,eo*5,eiq*4
    else :
        ilf,elf,ei,eo,eiq=ilf*15,elf*10,ei*6,eo*7,eiq*6
        print(ilf+elf+ei+eo+eiq)
        return float(ilf+elf+ei+eo+eiq)

def eaf(pri_list):
    cost_drivers={}
    priority={'VERY LOW':0,'LOW':1,'NOMINAL':2,'HIGH':3,'VERY HIGH':4}
    cost_drivers['Required Software Reliability']=[0.75,0.88,1.00,1.15,1.40]
    cost_drivers['Size of Application Database']=[-1,0.94,1.00,1.08,1.16]
    cost_drivers['Complexity of The Product']=[0.70,0.85,1.00,1.15,1.30]
    cost_drivers['Runtime Performance Constraints']=[-1,-1,1.00,1.11,1.30]
    cost_drivers['Memory Constraints']=[-1,-1,1.00,1.06,1.21]
    cost_drivers['Volatility of the virtual machine environment']=[-1,0.87,1.00,1.15,1.30]
    cost_drivers['Required turnabout time']=[-1,0.94,1.00,1.07,1.15]
    cost_drivers['Analyst capability']=[1.46,1.19,1.00,0.86,0.71]
    cost_drivers['Applications experience']=[1.29,1.13,1.00,0.91,0.82]
    cost_drivers['Software engineer capability']=[1.42,1.17,1.00,0.86,0.70]
    cost_drivers['Virtual machine experience']=[1.21,1.10,1.00,0.90,-1]
    cost_drivers['Programming language experience']=[1.14,1.07,1.00,0.95,-1]
    cost_drivers['Application of software engineering methods']=[1.24,1.10,1.00,0.91,0.82]
    cost_drivers['Use of software tools']=[1.24,1.10,1.00,0.91,0.83]
    cost_drivers['Required development schedule']=[1.23,1.08,1.00,1.04,1.10]
    cnt=0
    pri=[]
    for i in cost_drivers.keys():
        pri.append(float(cost_drivers[i][priority[pri_list[cnt]]]))
        cnt+=1
    return pri
