from flask import Flask ,render_template,request,Response
import func
app = Flask(__name__)
x=0
klocc=0
fp=0
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/i2', methods=['GET','POST'])
def index2():
    # first=request.args.get('first')
    # select = request.form.get('')
    global x
    select = request.form.get('service')
    if select == 'kloc':
        x=1
        return render_template("index2.html",result=select)
    else:
        x=0
        return render_template("fpmodule.html")
@app.route('/i2e', methods=['GET','POST'])
def i2e():
    global klocc
    # first=request.args.get('first')
    elf = int(request.form.get('elf'))
    ilf = int(request.form.get('ilf'))
    eo = int(request.form.get('eo'))
    ei = int(request.form.get('ei'))
    eiq = int(request.form.get('eiq'))
    pl = request.form.get('pl')
    complexity=int(request.form.get('av'))
    project = str(request.form.get('project'))
    project=project.lower()
    print(project)
    if project=='simple':
        ilf,elf,ei,eo,eiq=ilf*7,elf*5,ei*3,eo*5,eiq*3
    elif project=='average':
        ilf,elf,ei,eo,eiq=ilf*10,elf*7,ei*4,eo*5,eiq*4
    else :
        ilf,elf,ei,eo,eiq=ilf*15,elf*10,ei*6,eo*7,eiq*6
        print(ilf+elf+ei+eo+eiq)
    UFP=float(ilf+elf+ei+eo+eiq)
    # UFP=float(func.calc(elf,ilf,eo,ei,eiq,project))
    # ilf,elf,ei,eo,eiq=ilf*7,elf*5,ei*3,eo*5,eiq*3
    ilf,elf,ei,eo,eiq=ilf*10,elf*7,ei*4,eo*5,eiq*4
    print(elf+ilf+eo+ei+eiq)
    DI=14*complexity
    # print(type(func.calc(elf,ilf,eo,ei,eiq,project.lower)))
    TCF=(0.65+(0.01*DI))
    FP=TCF*UFP
    fp=FP
    # lang_fac=lang_fac(pl)
    if pl.lower()=='Java':
        lang_fac=38
    if pl.lower()=='C++':
        lang_fac=53
    else:
        lang_fac=38
    kloc=FP*lang_fac/1000
    klocc=kloc
    select =UFP
    return render_template("index2e.html",result=UFP,fp=fp)
@app.route('/index3', methods=['GET','POST'])
def index3():
    global klocc
    # first=request.args.get('first')
    sloc = str(request.form.get('sloc'))
    print(sloc)
    if sloc!='None':
        kloc=float(sloc)/1000
        klocc=kloc
    cost = float(request.form.get('cost_per_month'))
    project = str(request.form.get('project_type'))
    cost_drivers=['Required Software Reliability','Size of Application Database','Complexity of The Product','Runtime Performance Constraints','Memory Constraints','Volatility of the virtual machine environment','Required turnabout time','Analyst capability','Applications experience','Software engineer capability','Virtual machine experience','Programming language experience','Application of software engineering methods','Use of software tools','Required development schedule']
    EAF=1
    # priority={'VERY LOW':0,'LOW':1,'NOMINAL':2,'HIGH':3,'VERY HIGH':4}
    l=[]
    for i in range(15):
        l.append(request.form.get(cost_drivers[i]))
    eaf=func.eaf(l)
    x=1.0
    for i in eaf:
        x*=i
    EAF=x
    # project=project.lower
    a,b,c,d=func.type(project.lower())
    effort=EAF*a*(klocc)**b
    dev_time=float(EAF)*c*(effort)**d
    cost=dev_time*cost
    print(klocc)
    print(EAF)
    print((klocc)**d)
    print(d)
    return render_template("index3.html",effort=effort,dev_time=dev_time,cost=cost)
    # return result
# @app.route('/fp', methods=['GET','POST'])
# def fp_mod():
#     # first=request.args.get('first')
#     select = request.form.get('cost_per_month')
#     project = request.form.get('project')
#     if project=='organic':
#         result=5000#put needed formula here
#     return render_template("fpmodule.html",result=result)
#     return result
if __name__ == '__main__':
    app.run(debug=True)