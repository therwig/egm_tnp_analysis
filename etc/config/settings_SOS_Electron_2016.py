#############################################################
########## General settings
#############################################################
Probe_isTightNoIso = "Probe_isClean && Probe_isTightEle && abs(Probe_ip3d)<0.01 && Probe_sip3d<2"
flags = {
    "looseObject"    : "Probe_isClean",
    "tightNoIsoObject"    : Probe_isTightNoIso,
    "tightObjectOverTightNoIso"    : "Probe_isTight",
    "tightObject"    : "Probe_isTight",
}

baseOutDir = "results/SOS_Electron_2016/"


#############################################################
########## samples definition  - preparing the samples
#############################################################
import etc.inputs.tnpSampleDef_SOS_Electron_2016 as tnpSamples
tnpTreeDir = "./Events"

samplesDef = {
    "data"   : tnpSamples.SOS_Electron_2016["data"].clone(),
    "mcNom"  : tnpSamples.SOS_Electron_2016["DY"].clone(),
    "mcAlt"  : tnpSamples.SOS_Electron_2016["DY"].clone(),
    "tagSel" : tnpSamples.SOS_Electron_2016["DY"].clone(),
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
    { 'var' : 'abs(Probe_eta)' , 'type': 'float', 'bins': [0.0, 1.5, 2.5] },
    { 'var' : 'Probe_pt' , 'type': 'float', 'bins': [5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 1000.0] },
]


#############################################################
########## Cuts definition for all samples
#############################################################
cutBase   = "Tag_pt > 29 && abs(Tag_eta) < 2.5 && Tag_cutBased > 3 && Tag_isGenMatched && Probe_pt > 5.0 && abs(Probe_eta) < 2.5 && Probe_isGenMatched && TnP_trigger && Probe_charge*Tag_charge < 0" # tightNoIsoObject
#cutBase   = "Tag_pt > 29 && abs(Tag_eta) < 2.5 && Tag_cutBased > 3 && Tag_isGenMatched && Probe_pt > 5.0 && abs(Probe_eta) < 2.5 && Probe_isGenMatched && TnP_trigger && Probe_charge*Tag_charge < 0 && " + Probe_isTightNoIso # tightObjectOverTightNoIso

additionalCuts = {}


#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
#import etc.config.SOS_Models as tnpModels
from etc.config.SOS_Models import *
nbins=(len(biningDef[0]['bins'])-1)*(len(biningDef[1]['bins'])-1)

tnpModelsNom = ModelSet(DoubleVoigt,nbins)
tnpModelsNom.AddModelSet( ModelSet(CMSShape,nbins) )
tnpModelsAltSig = ModelSet(DoubleGaussian,nbins)
tnpModelsAltSig.AddModelSet( ModelSet(CMSShape,nbins) )
tnpModelsAltBkg = ModelSet(DoubleVoigt,nbins)
tnpModelsAltBkg.AddModelSet( ModelSet(Exponential,nbins) )

# tnpModelNom = tnpModels.DoubleVoigt()
# tnpModelNom.AddModel( tnpModels.CMSShape() )
# tnpModelAltSig = tnpModels.DoubleGaussian()
# tnpModelAltSig.AddModel( tnpModels.CMSShape() )
# tnpModelAltBkg = tnpModels.DoubleVoigt()
# tnpModelAltBkg.AddModel( tnpModels.Exponential() )


# tnpModelsNom.GetMC(00).UpdateParams({
#     "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.5), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
#     "meanF1":(95,90,100), "width":(3.0), "sigmaF1":(4.0,2.0,4.5), "meanF2":(75,74,85), "sigmaFRatio":(9,7.5,10),})
tnpModelsNom.GetMC(01).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,3.5), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,4.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsNom.GetMC(02).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.8), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,90,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(60,50,75), "sigmaFRatio":(8,7.5,10),})
tnpModelsNom.GetMC(03).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,4.5), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,4.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsNom.GetMC(04).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.0), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(6,4.5,10),})
tnpModelsNom.GetMC(05).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.7), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,4.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsNom.GetMC(16).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.5), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsNom.GetMC(18).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,1.2), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsNom.GetMC(19).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.0), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})

tnpModelsNom.GetData(00).UpdateParams({
    # "meanP1":(90,80,100), "width":(2.0), "sigmaP1":(1.0,0.5,2.5), "meanP2":(60,55,75), "sigmaPRatio":(8,5.5,10),
    "meanF1":(90,88,92), "width":(2.0), "sigmaF1":(2.0), "meanF2":(90,85,95), "sigmaFRatio":(5,1.0,20.0),
    "acmsF":(50),"betaF":(0.01),"gammaF":(0.056),"peakF":(90.0),
})
tnpModelsNom.GetData(01).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,4.5), "meanP2":(75,70,80), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,88,92), "width":(3.0), "sigmaF1":(1.0,0.5,4.3), "meanF2":(90,20,100), "sigmaFRatio":(4,0.5,10),
    "acmsF":(57.0),"betaF":(0.60),"gammaF":(0.017),"peakF":(90.0),})
tnpModelsNom.GetData(02).UpdateParams({
    "meanP1":(90,88,92), "width":(2.0), "sigmaP1":(1.7,1.5,2.5), "meanP2":(70,60,80), "sigmaPRatio":(5,1.0,20.0),
    "meanF1":(90,88,92), "width":(2.0), "sigmaF1":(1.8,1.7,3.5), "meanF2":(90,88,92), "sigmaFRatio":(5,1.0,7.0),
    "acmsF":(50),"betaF":(0.01),"gammaF":(0.051),"peakF":(90.0),})
tnpModelsNom.GetData(03).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,4.5), "meanP2":(60,20,75), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,4.5), "meanF2":(75,60,80), "sigmaFRatio":(3,1.5,5.5),
    "acmsF":(50),"betaF":(0.010),"gammaF":(0.034),"peakF":(90.0),})
tnpModelsNom.GetData(04).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.0), "meanP2":(60,20,75), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,4.5), "meanF2":(90,20,100), "sigmaFRatio":(4,3.5,5),})
tnpModelsNom.GetData(05).UpdateParams({
    "meanP1":(90,80,100), "width":(2.0), "sigmaP1":(1.0,0.5,2.5), "meanP2":(90,20,100), "sigmaPRatio":(4,3.5,10),
    "meanF1":(90,80,100), "width":(2.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsNom.GetData(06).UpdateParams({
    "meanP1":(90,80,100), "width":(2.5,2.0,3.0), "sigmaP1":(1.0,0.5,2.5), "meanP2":(90,20,100), "sigmaPRatio":(4,3.8,10),
    "meanF1":(90,80,100), "width":(2.5,2.0,3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsNom.GetData(07).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.2), "meanP2":(90,20,100), "sigmaPRatio":(4,3.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})

# alt sig
tnpModelsAltSig.GetData(01).UpdateParams({
    "meanP1":(90,88,92),"sigmaP1":(0.9,0.5,5.0),"meanP2":(75,70,85),"sigmaP2":(0.9,0.5,7.0),
    "meanF1":(90,88,92),"sigmaF1":(0.9,0.5,5.0),"meanF2":(75,60,80),"sigmaF2":(3.9,2.5,7.0),
    "acmsP":(65.),"betaP":(0.01),"gammaP":(0.040),"peakP":(90.0),
    "acmsF":(53.0),"betaF":(0.50),"gammaF":(0.016),"peakF":(90.0),})
tnpModelsAltSig.GetData(03).UpdateParams({
    "meanF1":(90,80,100),"sigmaF1":(0.9,0.5,5.0),"meanF2":(90,20,110),"sigmaF2":(3.9,2.5,5.0),
    "acmsP":(60.,50.,75.),"betaP":(0.04,0.01,0.06),"gammaP":(0.1, 0.005, 1),"peakP":(90.0),
    "acmsF":(75.),"betaF":(0.01),"gammaF":(0.039),"peakF":(90.0),})
tnpModelsAltSig.GetData(06).UpdateParams({
    "meanP1":(90,80,100),"sigmaP1":(0.9,0.5,2.8),"meanP2":(65,60,75),"sigmaP2":(0.9,0.5,19.0),
    "meanF1":(90,80,100),"sigmaF1":(0.9,0.5,3.0),"meanF2":(65,60,75),"sigmaF2":(9.9,4.5,10.0),
    "acmsF":(75.),"betaF":(0.01),"gammaF":(0.027),"peakF":(90.0),})
tnpModelsAltSig.GetData(07).UpdateParams({
    "meanP1":(90,80,100),"sigmaP1":(0.9,0.5,3.5),"meanP2":(65,60,75),"sigmaP2":(0.9,0.5,15.0),
    "meanF1":(90,80,100),"sigmaF1":(0.9,0.5,5.0),"meanF2":(65,60,80),"sigmaF2":(0.9,0.5,11.0),
    "acmsP":(55),"betaP":(0.04,0.01,0.06),"gammaP":(0.1, 0.005, 1),"peakP":(90.0),
    "acmsF":(50),"betaF":(0.016),"gammaF":(0.034),"peakF":(90.0),})

#alt bkg
tnpModelsAltBkg.GetData(00).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,1.9), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsAltBkg.GetData(01).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,4.5), "meanP2":(75,70,80), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,88,92), "width":(3.0), "sigmaF1":(1.0,0.5,4.3), "meanF2":(90,20,100), "sigmaFRatio":(4,0.5,10),
    "alphaF":(-0.016),})
tnpModelsAltBkg.GetData(02).UpdateParams({
    "meanP1":(90,88,92), "width":(2.0), "sigmaP1":(1.7,1.5,2.3), "meanP2":(70,60,80), "sigmaPRatio":(5,1.0,20.0),
    "meanF1":(90,80,100), "width":(2.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsAltBkg.GetData(03).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,4.5), "meanP2":(60,20,75), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,4.5), "meanF2":(70,20,100), "sigmaFRatio":(3,1.5,5),
    "alphaF":(-0.029),})
tnpModelsAltBkg.GetData(04).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,1.8), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,4.5), "meanF2":(90,20,100), "sigmaFRatio":(6,2.5,10),})
tnpModelsAltBkg.GetData(05).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.2), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsAltBkg.GetData(06).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,1.8), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsAltBkg.GetData(07).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.2), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsAltBkg.GetData(14).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.5), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsAltBkg.GetData(16).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,1.1), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
tnpModelsAltBkg.GetData(17).UpdateParams({
    "meanP1":(90,80,100), "width":(3.0), "sigmaP1":(1.0,0.5,2.2), "meanP2":(90,20,100), "sigmaPRatio":(4,1.5,10),
    "meanF1":(90,80,100), "width":(3.0), "sigmaF1":(1.0,0.5,2.5), "meanF2":(90,20,100), "sigmaFRatio":(4,1.5,10),})
