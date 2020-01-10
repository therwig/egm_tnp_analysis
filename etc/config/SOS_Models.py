#
# simple class to define fit models
# function should contain at least sigPass/sigFail PDFs
#
class Model(object):
    def __init__(self):
        self.func=[]
        self.params={}
    def GetParams(self):
        return ["{}{}".format(x,list(self.params[x])) for x in self.params]
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
            "Voigtian::sigPass1(x, meanP1, widthP1, sigmaP1)",
            "Voigtian::sigFail1(x, meanF1, widthF1, sigmaF1)",
            "Voigtian::sigPass2(x, meanP2, widthP2, sigmaP2)",
            "Voigtian::sigFail2(x, meanF2, widthF2, sigmaF2)",
            "SUM::sigPass(vFracPass[0.8,0,1]*sigPass1, sigPass2)",
            "SUM::sigFail(vFracFail[0.8,0,1]*sigFail1, sigFail2)"
        ]
        self.params={
            "meanP1":(90,80,100), "widthP1":(2.5,2.0,3.0), "sigmaP1":(1.0,0.5,2.5),
            "meanF1":(90,80,100), "widthF1":(2.5,2.0,3.0), "sigmaF1":(1.0,0.5,2.5),
            "meanP2":(90,80,100), "widthP2":(2.5,2.0,3.0), "sigmaP2":(1.0,0.5,2.5),
            "meanF2":(90,80,100), "widthF2":(2.5,2.0,3.0), "sigmaF2":(1.0,0.5,2.5),
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
