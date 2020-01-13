#
# simple class to define fit models
# function should contain at least sigPass/sigFail PDFs
#
class ModelSet(object):
    def __init__(self):
        self.models_data = []
        self.models_mc   = []
    def __init__(self, n, mtype):
        self.models_data = [mtype() for i in range(n)]
        self.models_mc   = [mtype() for i in range(n)]
    def __init__(self, n, mod_sig, mod_bkg):
        self.models_data = []
        self.models_mc   = []
        for i in range(n):
            self.models_data.append(mod_sig())
            self.models_data[-1].AddModel(mod_bkg())
            self.models_mc.append(mod_sig())
            self.models_mc[-1].AddModel(mod_bkg())
    def __init__(self, n, mod_sig_data, mod_bkg_data, mod_sig_mc, mod_bkg_mc):
        self.models_data = []
        self.models_mc   = []
        for i in range(n):
            self.models_data.append(mod_sig_data())
            self.models_data[-1].AddModel(mod_bkg_data())
            self.models_mc.append(mod_sig_mc())
            self.models_mc[-1].AddModel(mod_bkg_mc())
    def UpdateDataModel(self,i,mod_s,mod_b):
        self.models_data[i] = mod_s
        self.models_data[i].AddModel( mod_b )
    def UpdateMCModel(self,i,mod_s,mod_b):
        self.models_mc[i] = mod_s
        self.models_mc[i].AddModel( mod_b )
    def GetData(self,i):
        return self.models_data[i]
    def GetMC(self,i):
        return self.models_mc[i]
    def AddModelSet(self,ms): #e.g. for composing s+b models
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
        self.fit_range=() #to reduce failed fit range
    def GetParams(self):
        return ["{}{}".format(x,list(self.params[x])) for x in self.params]
    def GetFunc(self): return self.func
    def SetFitRange(self,a,b): 
        self.fit_range=(a,b)
    def GetFitRange(self): 
        return self.fit_range
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
        super(Gaussian,self).__init__()
        self.func=[
            "Gaussian::sigPass(x,SPmean,SPsigma)",
            "Gaussian::sigFail(x,SFmean,SFsigma)",
        ]
        self.params={
            "SPmean":(90,80,100),"SPsigma":(0.9,0.5,5.0),
            "SFmean":(90,80,100),"SFsigma":(0.9,0.5,5.0),
        }
class DoubleGaussian(Model):
    def __init__(self):
        super(DoubleGaussian,self).__init__()
        self.func=[
            "Gaussian::sigPass1(x,SPmean1,SPsigma1)",
            "Gaussian::sigFail1(x,SFmean1,SFsigma1)",
            "Gaussian::sigPass2(x,SPmean2,SPsigma2)",
            "Gaussian::sigFail2(x,SFmean2,SFsigma2)",
            "SUM::sigPass(vFracPass[0.8,0.3,1]*sigPass1, sigPass2)",
            "SUM::sigFail(vFracFail[0.8,0.3,1]*sigFail1, sigFail2)"
        ]
        self.params={
            "SPmean1":(90,80,100),"SPsigma1":(0.9,0.5,5.0),
            "SFmean1":(90,80,100),"SFsigma1":(0.9,0.5,5.0),
            "SPmean2":(90,80,100),"SPsigma2":(0.9,0.5,5.0),
            "SFmean2":(90,80,100),"SFsigma2":(0.9,0.5,5.0),
        }

class Voigt(Model):
    def __init__(self):
        super(Voigt,self).__init__()
        self.func=[
            "Voigtian::sigPass(x, SPmean, SPwidth, SPsigma)",
            "Voigtian::sigFail(x, SFmean, SPwidth, SFsigma)",
        ]
        self.params={
            "SPmean":(90,80,100), "SPsigma":(1.0,0.5,2.5), "SPwidth":(2.5,2.0,3.0),
            "SFmean":(90,80,100), "SFsigma":(1.0,0.5,2.5),
        }
class DoubleVoigt(Model):
    def __init__(self):
        super(DoubleVoigt,self).__init__()
        self.func=[
            "Voigtian::sigPass1(x, SPmean1, SPwidth, SPsigma1)",
            "Voigtian::sigFail1(x, SFmean1, SPwidth, SFsigma1)",
            "Voigtian::sigPass2(x, SPmean2, SPwidth, prod::Psigma2(SPsigma1, SPsigmaRatio))",
            "Voigtian::sigFail2(x, SFmean2, SPwidth, prod::Fsigma2(SFsigma1, SFsigmaRatio))",
            "SUM::sigPass(vFracPass[0.8,0,1]*sigPass1, sigPass2)",
            "SUM::sigFail(vFracFail[0.8,0,1]*sigFail1, sigFail2)"
        ]
        self.params={
            "SPmean1":(90,80,100), "SPsigma1":(1.0,0.5,2.5), "SPwidth":(2.5,2.0,3.0),
            "SFmean1":(90,80,100), "SFsigma1":(1.0,0.5,2.5),
            "SPmean2":(90,80,100), "SPsigmaRatio":(4,1.5,10),
            "SFmean2":(90,80,100), "SFsigmaRatio":(4,1.5,10),
        }
# class DoubleVoigt2(Model):
#     def __init__(self):
#         super(Model,self).__init__()
#         self.func=[
#             "Voigtian::sigPass1(x, meanP1, widthP1, sigmaP1)",
#             "Voigtian::sigFail1(x, meanF1, widthF1, sigmaF1)",
#             "Voigtian::sigPass2(x, meanP2, widthP2, prod::sigmaP2(sigmaP1, sigmaPRatio))",
#             "Voigtian::sigFail2(x, meanF2, widthF2, prod::sigmaF2(sigmaF1, sigmaFRatio))",
#             "SUM::sigPass(vFracPass[0.8,0,1]*sigPass1, sigPass2)",
#             "SUM::sigFail(vFracFail[0.8,0,1]*sigFail1, sigFail2)"
#         ]
#         self.params={
#             "meanP1":(90,80,100), "widthP1":(2.5,2.0,3.0), "sigmaP1":(1.0,0.5,2.5),
#             "meanF1":(90,80,100), "widthF1":(2.5,2.0,3.0), "sigmaF1":(1.0,0.5,2.5),
#             "meanP2":(90,80,100), "widthP2":(2.5,2.0,3.0), "sigmaPRatio":(4,1.5,10),
#             "meanF2":(90,80,100), "widthF2":(2.5,2.0,3.0), "sigmaFRatio":(4,1.5,10),
#         }

#############################################################
########## Background models
#############################################################
class CMSShape(Model):
    def __init__(self):
        super(CMSShape,self).__init__()
        self.func=[
            "RooCMSShape::bkgPass(x, BPacms, BPbeta, BPgamma, BPpeak)",
            "RooCMSShape::bkgFail(x, BFacms, BFbeta, BFgamma, BFpeak)",
        ]
        self.params={
            "BPacms":(60.,50.,80.),"BPbeta":(0.05,0.01,0.08),"BPgamma":(0.1, -2, 2),"BPpeak":(90.0,),
            "BFacms":(60.,50.,80.),"BFbeta":(0.05,0.01,0.08),"BFgamma":(0.1, -2, 2),"BFpeak":(90.0,),
        }

class Exponential(Model):
    def __init__(self):
        super(Exponential,self).__init__()
        self.func=[
            "RooExponential::bkgPass(x, BPa0)",
            "RooExponential::bkgFail(x, BFa0)",
        ]
        self.params={
            "BPa0":(0,-5,5),
            "BFa0":(0,-5,5),
        }

class ExponentialN(Model):
    '''Exp of an n-dim polynomial '''
    def __init__(self,n):
        super(ExponentialN,self).__init__()
        self.n=n
        self.func=[
            "RooExponentialN::bkgPass(x,{"+",".join(["BPa{}".format(i) for i in range(n)])+"},1)",
            "RooExponentialN::bkgFail(x,{"+",".join(["BFa{}".format(i) for i in range(n)])+"},1)"
        ]
        self.params={}
        for i in range(n):
            self.params["BPa{}".format(i)] = (0,-5,5)
            self.params["BFa{}".format(i)] = (0,-5,5)
        print(self.func)

class BernsteinN(Model):
    '''Exp of an n-dim polynomial '''
    def __init__(self,n):
        super(BernsteinN,self).__init__()
        self.n=n
        self.func=[
            "RooBernstein::bkgPass(x,{"+",".join(["BPa{}".format(i) for i in range(n)])+"})",
            "RooBernstein::bkgFail(x,{"+",".join(["BFa{}".format(i) for i in range(n)])+"})"
        ]
        self.params={}
        for i in range(n):
            self.params["BPa{}".format(i)] = (0.5,0,1)
            self.params["BFa{}".format(i)] = (0.5,0,1)
