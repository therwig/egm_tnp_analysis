#
# simple class to define fit models
# function should contain at least sigPass/sigFail PDFs
#
class ModelSet(object):
    def __init__(self):
        self.models_data = []
        self.models_mc   = []
    def __init__(self,mtype,n):
        self.models_data = [mtype() for i in range(n)]
        self.models_mc   = [mtype() for i in range(n)]
    def GetData(self,i):
        if i>=len(self.models_data):
            print("Model out of bounds")
            return None
        return self.models_data[i]
    def GetMC(self,i):
        if i>=len(self.models_mc):
            print("Model out of bounds")
            return None
        return self.models_data[i]
    def AddModelSet(self,ms):
        if (len(ms.models_data) != len(self.models_data)) \
           or (len(ms.models_mc) != len(self.models_mc)):
            print("Model set dimensions don't match")
            return
        for i in range(len(ms.models_mc)):
            self.models_data[i].AddModel(ms.models_data[i])
            self.models_mc[i].AddModel(ms.models_mc[i])

class Model(object):
    def __init__(self):
        self.func=[]
        self.params={}
        self.guess={}
    def GetParams(self):
        print('yoo',self.params)
        return ["{}{}".format(x,list(self.params[x])) for x in self.params]
        # print ["{}({})".format(x,",".join(str(self.params[x]))) for x in self.params]
        # return ["{}({})".format(x,",".join(str(self.params[x]))) for x in self.params]
    def GetFunc(self): return self.func
    def AddModel(self,m):
        add_func = m.func
        add_params = m.params
        for p in m.params:
            if p in self.params:
                self.params[p+"b"]=m.params[p]
                for l in add_func:
                    l = l.replace(p,p+"b")
            else:
                self.params[p]=m.params[p]
        for f in add_func:
            self.func.append(f)
    def UpdateParams(self,d):
        for x in d: 
            if hasattr(d[x], '__iter__'):
                self.params[x]=d[x]
            else:
                self.params[x]=(d[x],)
        
#############################################################
########## Signal models
#############################################################
class Gaussian(Model):
    def __init__(self):
        super(Model,self).__init__()
        self.func=[
            "Gaussian::sigPass(x,meanP,sigmaP)",
            "Gaussian::sigFail(x,meanF,sigmaF)",
        ]
        self.params={
            "meanP":(90,80,100),"sigmaP":(0.9,0.5,5.0),
            "meanF":(90,80,100),"sigmaF":(0.9,0.5,5.0),
        }
class DoubleGaussian(Model):
    def __init__(self):
        super(Model,self).__init__()
        self.func=[
            "Gaussian::sigPass1(x,meanP1,sigmaP1)",
            "Gaussian::sigFail1(x,meanF1,sigmaF1)",
            "Gaussian::sigPass2(x,meanP2,sigmaP2)",
            "Gaussian::sigFail2(x,meanF2,sigmaF2)",
            "SUM::sigPass(vFracPass[0.8,0.3,1]*sigPass1, sigPass2)",
            "SUM::sigFail(vFracFail[0.8,0.3,1]*sigFail1, sigFail2)"
        ]
        self.params={
            "meanP1":(90,80,100),"sigmaP1":(0.9,0.5,5.0),
            "meanF1":(90,80,100),"sigmaF1":(0.9,0.5,5.0),
            "meanP2":(90,80,100),"sigmaP2":(0.9,0.5,5.0),
            "meanF2":(90,80,100),"sigmaF2":(0.9,0.5,5.0),
        }

class Voigt(Model):
    def __init__(self):
        super(Model,self).__init__()
        self.func=[
            "Voigtian::sigPass(x, meanP, widthP, sigmaP)",
            "Voigtian::sigFail(x, meanF, widthF, sigmaF)",
        ]
        self.params={
            "meanP":(90,80,100), "widthP":(2.5,2.0,3.0), "sigmaP":(1.0,0.5,2.5),
            "meanF":(90,80,100), "widthF":(2.5,2.0,3.0), "sigmaF":(1.0,0.5,2.5),
        }
class DoubleVoigt(Model):
    def __init__(self):
        super(Model,self).__init__()
        self.func=[
            "Voigtian::sigPass1(x, meanP1, width, sigmaP1)",
            "Voigtian::sigFail1(x, meanF1, width, sigmaF1)",
            "Voigtian::sigPass2(x, meanP2, width, prod::sigmaP2(sigmaP1, sigmaPRatio))",
            "Voigtian::sigFail2(x, meanF2, width, prod::sigmaF2(sigmaF1, sigmaFRatio))",
            "SUM::sigPass(vFracPass[0.8,0,1]*sigPass1, sigPass2)",
            "SUM::sigFail(vFracFail[0.8,0,1]*sigFail1, sigFail2)"
        ]
        self.params={
            "meanP1":(90,80,100), "sigmaP1":(1.0,0.5,2.5), "width":(2.5,2.0,3.0),
            "meanF1":(90,80,100), "sigmaF1":(1.0,0.5,2.5),
            "meanP2":(90,80,100), "sigmaPRatio":(4,1.5,10),
            "meanF2":(90,80,100), "sigmaFRatio":(4,1.5,10),
        }
class DoubleVoigt2(Model):
    def __init__(self):
        super(Model,self).__init__()
        self.func=[
            "Voigtian::sigPass1(x, meanP1, widthP1, sigmaP1)",
            "Voigtian::sigFail1(x, meanF1, widthF1, sigmaF1)",
            "Voigtian::sigPass2(x, meanP2, widthP2, prod::sigmaP2(sigmaP1, sigmaPRatio))",
            "Voigtian::sigFail2(x, meanF2, widthF2, prod::sigmaF2(sigmaF1, sigmaFRatio))",
            "SUM::sigPass(vFracPass[0.8,0,1]*sigPass1, sigPass2)",
            "SUM::sigFail(vFracFail[0.8,0,1]*sigFail1, sigFail2)"
        ]
        self.params={
            "meanP1":(90,80,100), "widthP1":(2.5,2.0,3.0), "sigmaP1":(1.0,0.5,2.5),
            "meanF1":(90,80,100), "widthF1":(2.5,2.0,3.0), "sigmaF1":(1.0,0.5,2.5),
            "meanP2":(90,80,100), "widthP2":(2.5,2.0,3.0), "sigmaPRatio":(4,1.5,10),
            "meanF2":(90,80,100), "widthF2":(2.5,2.0,3.0), "sigmaFRatio":(4,1.5,10),
        }

#############################################################
########## Background models
#############################################################
class CMSShape(Model):
    def __init__(self):
        super(Model,self).__init__()
        self.func=[
            "RooCMSShape::bkgPass(x, acmsP, betaP, gammaP, peakP)",
            "RooCMSShape::bkgFail(x, acmsF, betaF, gammaF, peakF)",
        ]
        self.params={
            "acmsP":(60.,50.,80.),"betaP":(0.05,0.01,0.08),"gammaP":(0.1, -2, 2),"peakP":(90.0,),
            "acmsF":(60.,50.,80.),"betaF":(0.05,0.01,0.08),"gammaF":(0.1, -2, 2),"peakF":(90.0,),
        }

class Exponential(Model):
    def __init__(self):
        super(Model,self).__init__()
        self.func=[
            "RooExponential::bkgPass(x, a0P)",
            "RooExponential::bkgFail(x, a0F)",
        ]
        self.params={
            "a0P":(0,-5,5),
            "a0F":(0,-5,5),
        }

class ExponentialN(Model):
    '''Exp of an n-dim polynomial '''
    def __init__(self,n):
        super(Model,self).__init__()
        self.n=n
        self.func=[
            "RooExponentialN::bkgPass(x,{"+",".join(["a{}P".format(i) for i in range(n)])+"},1)",
            "RooExponentialN::bkgFail(x,{"+",".join(["a{}F".format(i) for i in range(n)])+"},1)"
        ]
        self.params={}
        for i in range(n):
            self.params["a{}P".format(i)] = (0,-5,5)
            self.params["a{}F".format(i)] = (0,-5,5)
        print(self.func)
