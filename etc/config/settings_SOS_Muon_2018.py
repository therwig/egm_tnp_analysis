#############################################################
########## General settings
#############################################################
Probe_isTightNoIso = "Probe_isClean && abs(Probe_ip3d)<0.01 && Probe_sip3d<2"
flags = {
    "looseObject"    : "Probe_isClean",
    "tightNoIsoObject"    : Probe_isTightNoIso,
    "tightObjectOverTightNoIso"    : "Probe_isTight",
    "tightObject"    : "Probe_isTight",
}

baseOutDir = "results/SOS_Muon_2018/"


#############################################################
########## samples definition  - preparing the samples
#############################################################
import etc.inputs.tnpSampleDef_SOS_Muon_2018 as tnpSamples
tnpTreeDir = "./Events"

samplesDef = {
    "data"   : tnpSamples.SOS_Muon_2018["data"].clone(),
    "mcNom"  : tnpSamples.SOS_Muon_2018["DY"].clone(),
    "mcAlt"  : tnpSamples.SOS_Muon_2018["DY"].clone(),
    "tagSel" : tnpSamples.SOS_Muon_2018["DY"].clone(),
}

# Set tree name/directory
samplesDef["data" ].set_tnpTree(tnpTreeDir)
if not samplesDef["mcNom" ] is None: samplesDef["mcNom" ].set_tnpTree(tnpTreeDir)
if not samplesDef["mcAlt" ] is None: samplesDef["mcAlt" ].set_tnpTree(tnpTreeDir)
if not samplesDef["tagSel"] is None: samplesDef["tagSel"].set_tnpTree(tnpTreeDir)

# Set MC truth
if not samplesDef["mcNom" ] is None: samplesDef["mcNom" ].set_mcTruth()
if not samplesDef["mcAlt" ] is None: samplesDef["mcAlt" ].set_mcTruth()
if not samplesDef["tagSel"] is None: samplesDef["tagSel"].set_mcTruth()

# Set PU weight
weightName = "puWeight"
if not samplesDef["mcNom" ] is None: samplesDef["mcNom" ].set_weight(weightName)
if not samplesDef["mcAlt" ] is None: samplesDef["mcAlt" ].set_weight(weightName)
if not samplesDef["tagSel"] is None: samplesDef["tagSel"].set_weight(weightName)


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    { 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0.0, 1.2, 2.4] },
    { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [3.5, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 1000.0] },
]


#############################################################
########## Cuts definition for all samples
#############################################################
cutBase   = "Tag_pt > 29 && abs(Tag_eta) < 2.4 && Tag_tightId && Tag_isGenMatched && Probe_pt > 3.5 && abs(Probe_eta) < 2.4 && Probe_looseId && Probe_isGenMatched && TnP_trigger && Probe_charge*Tag_charge < 0" # tightNoIsoObject
#cutBase   = "Tag_pt > 29 && abs(Tag_eta) < 2.4  && Tag_tightId && Tag_isGenMatched && Probe_pt > 3.5 && abs(Probe_eta) < 2.4 && Probe_looseId && Probe_isGenMatched && TnP_trigger && Probe_charge*Tag_charge < 0 && " + Probe_isTightNoIso # tightObjectOverTightNoIso

additionalCuts = {}


#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
from etc.config.SOS_Models import *
nbins=(len(biningDef[0]['bins'])-1)*(len(biningDef[1]['bins'])-1)

tnpModelsNom    = ModelSet(nbins,DoubleVoigt,CMSShape, DoubleVoigt,CMSShape)
tnpModelsAltSig = ModelSet(nbins,DoubleGaussian,CMSShape,DoubleGaussian,CMSShape)
tnpModelsAltBkg = ModelSet(nbins,DoubleVoigt,Exponential,DoubleVoigt,Exponential)

# Nominal Data (switch to plain exponential bkg for lowest bins)
#tnpModelsNom.GetData(00).UpdateParams({"SFmean1":(90,89,92),"SFmean2":(90,89,92)})
tnpModelsNom.GetData(00).UpdateParams({"SFmean1":(90,89,92),"SFmean2":(90,89,92),"SFsigmaRatio":(1,)})
tnpModelsNom.GetData(01).SetFitRange(70,110)
#tnpModelsNom.GetData(01).UpdateParams({"BFacms":(10,),"BFbeta":(1,),"SFmean1":(90,86,92),"SFmean2":(90,86,92)}) 
tnpModelsNom.GetData(01).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92),"SFsigmaRatio":(1,0.5,2)})
tnpModelsNom.GetData(02).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92),"SFsigmaRatio":(1,0.5,4)})
#tnpModelsNom.GetData(03).UpdateParams({"BFacms":(10,),"BFbeta":(1,), "SFmean1":(90,86,92),"SFmean2":(90,86,92),"SFsigmaRatio":(1,0.5,4)})
tnpModelsNom.GetData(03).UpdateParams({"BFacms":(10,),"BFbeta":(1,), "SFmean1":(90,88,92),"SFmean2":(90,88,92),"SFsigmaRatio":(1,0.5,4)})
tnpModelsNom.GetData(04).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92)})
tnpModelsNom.GetData(05).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92),"SFsigmaRatio":(1,0.5,4)})
tnpModelsNom.GetData(06).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92)})
tnpModelsNom.GetData(07).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92)})

# Alternate Signal -- Data
tnpModelsAltSig.GetData(01).SetFitRange(70,110)
tnpModelsAltSig.GetData(01).UpdateParams({"BFacms":(10,),"BFbeta":(1,),"SFsigma1":(1,0.5,2.5),"SFsigma2":(1,0.5,2.5)})
tnpModelsAltSig.GetData(02).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92),})
tnpModelsAltSig.GetData(03).UpdateParams({"BFacms":(10,),"BFbeta":(1,),"SFsigma1":(1,0.5,3),"SFsigma2":(1,0.5,3),})

# Alternate Background -- Data (exponential doesn't seem to fit well, use bernstein instead )
# the following works, but prefering the bernstein as more of a variation?
# tnpModelsAltBkg.GetData(00).UpdateParams({"SFsigmaRatio":(1,),"SFmean1":(90,),"SFmean2":(90,)})
tnpModelsAltBkg.UpdateDataModel(0, DoubleVoigt(), BernsteinN(5))
tnpModelsAltBkg.GetData(00).UpdateParams({"SFsigmaRatio":(1,),"SFmean1":(90,88,92),"SFmean2":(90,88,92)})
tnpModelsAltBkg.UpdateDataModel(1, DoubleVoigt(), BernsteinN(3))
tnpModelsAltBkg.GetData(01).UpdateParams({"SFsigmaRatio":(1,),"SFmean1":(90,88,92),"SFmean2":(90,88,92)})
tnpModelsAltBkg.UpdateDataModel(2, DoubleVoigt(), BernsteinN(4))
tnpModelsAltBkg.GetData(02).UpdateParams({"SFsigmaRatio":(1,0.5,5),"SFmean1":(90,86,92),"SFmean2":(90,86,92)})
tnpModelsAltBkg.UpdateDataModel(3, DoubleVoigt(), BernsteinN(3))
tnpModelsAltBkg.GetData(3).UpdateParams({"SFsigmaRatio":(1,),"SFmean1":(88,86,92),"SFmean2":(88,86,92)})
tnpModelsAltBkg.UpdateDataModel(4, DoubleVoigt(), BernsteinN(3))
tnpModelsAltBkg.GetData(4).UpdateParams({"SFsigmaRatio":(1,),"SFmean1":(88,86,92),"SFmean2":(88,86,92)})
tnpModelsAltBkg.UpdateDataModel(5, DoubleVoigt(), BernsteinN(3))
tnpModelsAltBkg.GetData(5).UpdateParams({"SFsigmaRatio":(1,),"SFmean1":(88,86,92),"SFmean2":(88,86,92)})
tnpModelsAltBkg.UpdateDataModel(6, DoubleVoigt(), BernsteinN(4))
tnpModelsAltBkg.GetData(06).UpdateParams({"SFmean1":(90,86,92),"SFmean2":(90,86,92)})
tnpModelsAltBkg.UpdateDataModel(7, DoubleVoigt(), BernsteinN(5))
tnpModelsAltBkg.GetData(07).UpdateParams({"SFmean1":(90,88,92),"SFmean2":(90,88,92)})

# Nominal fit with MC
tnpModelsNom.GetMC(00).UpdateParams({"SPmean2":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),})
tnpModelsNom.GetMC(01).UpdateParams({"SPmean2":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),})
tnpModelsNom.GetMC(02).UpdateParams({"SPmean2":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),"SPwidth":(1,0.5,3)})
tnpModelsNom.GetMC(03).UpdateParams({"SPmean2":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),})
tnpModelsNom.GetMC(04).UpdateParams({"SPmean2":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),})
tnpModelsNom.GetMC(05).UpdateParams({"SPmean2":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),})
tnpModelsNom.GetMC(06).UpdateParams({"SPmean1":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),})
tnpModelsNom.GetMC(07).UpdateParams({"SPmean1":(90,20,100),"SFmean2":(90,20,100),"SPsigma1":(1,0.5,5),"SFsigma1":(1,0.5,5),})


#
# The above are all fit with the following 'default' parameters
#
# Double-Voigt defaults
# "SPmean1":(90,80,100), "SPsigma1":(1.0,0.5,2.5), "SPwidth":(2.5,2.0,3.0),
# "SFmean1":(90,80,100), "SFsigma1":(1.0,0.5,2.5),
# "SPmean2":(90,80,100), "SPsigmaRatio":(4,1.5,10),
# "SFmean2":(90,80,100), "SFsigmaRatio":(4,1.5,10),
#
# Double Gaussian
# "SPmean1":(90,80,100),"SPsigma1":(0.9,0.5,5.0),
# "SFmean1":(90,80,100),"SFsigma1":(0.9,0.5,5.0),
# "SPmean2":(90,80,100),"SPsigma2":(0.9,0.5,5.0),
# "SFmean2":(90,80,100),"SFsigma2":(0.9,0.5,5.0),
#
# CMSShape defaults """ RooMath::erfc((alpha - x) * beta) * (x - peak)*gamma """
# "BPacms":(60.,50.,80.),"BPbeta":(0.05,0.01,0.08),"BPgamma":(0.1, -2, 2),"BPpeak":(90.0,),
# "BFacms":(60.,50.,80.),"BFbeta":(0.05,0.01,0.08),"BFgamma":(0.1, -2, 2),"BFpeak":(90.0,),
#
# Exponential
# "BPa0":(0,-5,5),
# "BFa0":(0,-5,5),
#
#  RooBernstein is (0.5,0,1) for all parameters.
