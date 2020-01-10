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
import etc.config.SOS_Models as tnpModels

# tnpModelNom = tnpModels.DoubleVoigt()
# tnpModelNom.AddModel( tnpModels.CMSShape() )

# tnpModelAltSig = tnpModels.DoubleGaussian()
# tnpModelAltSig.AddModel( tnpModels.CMSShape() )

# tnpModelAltBkg = tnpModels.DoubleVoigt()
# tnpModelAltBkg.AddModel( tnpModels.Exponential() )


tnpModelNom = tnpModels.DoubleVoigt()
tnpModelNom.AddModel( tnpModels.CMSShape() )

tnpModelAltSig = tnpModels.DoubleGaussian()
tnpModelAltSig.AddModel( tnpModels.CMSShape() )

tnpModelAltBkg = tnpModels.DoubleVoigt()
#tnpModelAltBkg.AddModel( tnpModels.Exponential() )
tnpModelAltBkg.AddModel( tnpModels.ExponentialN(2) )


# tnpParNomFit = [
#     "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
#     "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#     "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
#     "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
# ]

# tnpParDoublePeakNomFit = [
#      "meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     "meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#     "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

#     ##################### MC #####################
#     # bin00
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[95,90,100]", "width[3.0]", "sigmaF1[4.0,2.0,4.5]", "meanF2[75,74,85]", "sigmaFRatio[9,7.5,10]",
#     # bin01
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,3.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin02
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.8]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,90,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[60,50,75]", "sigmaFRatio[8,7.5,10]",
#     # bin03
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin04
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[6,4.5,10]",
#     # bin05
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.7]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin16
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin18
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin19
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",

#     ##################### DATA #####################
#     # bin00
#     #"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[60,55,75]", "sigmaPRatio[8,5.5,10]",
#     #"meanF1[90,88,92]", "width[2.0]", "sigmaF1[2.0]", "meanF2[90,85,95]", "sigmaFRatio[5,1.0,20.0]",
#     #"acmsF[50]","betaF[0.01]","gammaF[0.056]","peakF[90.0]",
#     # bin01
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[75,70,80]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,88,92]", "width[3.0]", "sigmaF1[1.0,0.5,4.3]", "meanF2[90,20,100]", "sigmaFRatio[4,0.5,10]",
#     #"acmsF[57.0]","betaF[0.60]","gammaF[0.017]","peakF[90.0]",
#     # bin02
#     #"meanP1[90,88,92]", "width[2.0]", "sigmaP1[1.7,1.5,2.5]", "meanP2[70,60,80]", "sigmaPRatio[5,1.0,20.0]",
#     #"meanF1[90,88,92]", "width[2.0]", "sigmaF1[1.8,1.7,3.5]", "meanF2[90,88,92]", "sigmaFRatio[5,1.0,7.0]",
#     #"acmsF[50]","betaF[0.01]","gammaF[0.051]","peakF[90.0]",
#     # bin03
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[60,20,75]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[75,60,80]", "sigmaFRatio[3,1.5,5.5]",
#     #"acmsF[50]","betaF[0.010]","gammaF[0.034]","peakF[90.0]",
#     # bin04
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[60,20,75]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,3.5,5]",
#     # bin05
#     #"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,3.5,10]",
#     #"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin06
#     #"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,3.8,10]",
#     #"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin07
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,3.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",


#     ####################### MC #####################
#     ### bin00
#     ###"meanP1[95,88,100]", "width[1.5]", "sigmaP1[1.0,0.5,2.5]", "meanP2[65,60,70]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[1.5]", "sigmaF1[1.0,0.5,2.9]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin01
#     ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,3.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin03
#     ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,3.5]", "meanP2[90,60,70]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin04
#     ###"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,3.5,10]",
#     ###"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,50,100]", "sigmaFRatio[4,3.5,10]",
#     ### bin06
#     ###"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,1.8]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin10
#     ###"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,2.0]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin11
#     ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,1.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.0]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin12
#     ###"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,2.0]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin13
#     ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin14
#     ###"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,1.7]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin15
#     ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,110]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,110]", "sigmaFRatio[4,1.5,10]",
#     ### bin16
#     ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.3]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.3]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin17
#     ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.1]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin18
#     ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     ### bin19
#     ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
# ]

# tnpParAltSigFit = [
#     "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
#     "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
#     "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#     "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

#     ##################### MC #####################
#     # bin10
#     #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.1]","sosP[1,0.5,5.0]",
#     #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[1.2]","sosF[1,0.5,5.0]",
#     # bin11
#     #"meanP[-0.0,-5.0,5.0]","sigmaP[1.5]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.9]","sosP[1,0.5,5.0]",
#     #"meanF[-0.0,-5.0,5.0]","sigmaF[1.6]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.0]","sosF[1,0.5,5.0]",
#     # bin13
#     #"meanP[-0.2,-5.0,-0.1]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[2.3,2.0,2.4]","sosP[1,0.5,5.0]",
#     #"meanF[-0.2,-5.0,-0.1]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.3,2.0,2.4]","sosF[1,0.5,5.0]",
#     # bin15
#     #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.5,0.5,2.7]","sosP[1,0.5,5.0]",
#     #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.0,0.5,2.7]","sosF[1,0.5,5.0]",
#     # bin16
#     #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
#     #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[1.6]","sosF[1,0.5,5.0]",
#     # bin17
#     #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
#     #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.3,2.0,2.5]","sosF[1,0.5,5.0]",
#     # bin18
#     #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
#     #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[1.5]","sosF[1,0.5,5.0]",
# ]

# tnpParDoublePeakAltSigFit = [
#     "meanP1[90,80,100]","sigmaP1[0.9,0.5,5.0]","meanP2[90,20,110]","sigmaP2[0.9,0.5,5.0]",
#     "meanF1[90,80,100]","sigmaF1[0.9,0.5,5.0]","meanF2[90,20,110]","sigmaF2[0.9,0.5,5.0]",
#     "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#     "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

#     # bin01
#     #"meanP1[90,88,92]","sigmaP1[0.9,0.5,5.0]","meanP2[75,70,85]","sigmaP2[0.9,0.5,7.0]",
#     #"meanF1[90,88,92]","sigmaF1[0.9,0.5,5.0]","meanF2[75,60,80]","sigmaF2[3.9,2.5,7.0]",
#     #"acmsP[65.]","betaP[0.01]","gammaP[0.040]","peakP[90.0]",
#     #"acmsF[53.0]","betaF[0.50]","gammaF[0.016]","peakF[90.0]",
#     # bin03
#     #"meanF1[90,80,100]","sigmaF1[0.9,0.5,5.0]","meanF2[90,20,110]","sigmaF2[3.9,2.5,5.0]",
#     #"acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#     #"acmsF[75.]","betaF[0.01]","gammaF[0.039]","peakF[90.0]",
#     # bin06
#     #"meanP1[90,80,100]","sigmaP1[0.9,0.5,2.8]","meanP2[65,60,75]","sigmaP2[0.9,0.5,19.0]",
#     #"meanF1[90,80,100]","sigmaF1[0.9,0.5,3.0]","meanF2[65,60,75]","sigmaF2[9.9,4.5,10.0]",
#     #"acmsF[75.]","betaF[0.01]","gammaF[0.027]","peakF[90.0]",
#     # bin07
#     #"meanP1[90,80,100]","sigmaP1[0.9,0.5,3.5]","meanP2[65,60,75]","sigmaP2[0.9,0.5,15.0]",
#     #"meanF1[90,80,100]","sigmaF1[0.9,0.5,5.0]","meanF2[65,60,80]","sigmaF2[0.9,0.5,11.0]",
#     #"acmsP[55]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#     #"acmsF[50]","betaF[0.016]","gammaF[0.034]","peakF[90.0]",
# ]
     
# tnpParAltBkgFit = [
#     "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
#     "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#     "alphaP[0.,-5.,5.]",
#     "alphaF[0.,-5.,5.]",
# ]
     
# tnpParDoublePeakAltBkgFit = [
#     #"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     "alphaP[0.,-5.,5.]",
#     "alphaF[0.,-5.,5.]",

#     # bin00
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.9]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin01
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[75,70,80]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,88,92]", "width[3.0]", "sigmaF1[1.0,0.5,4.3]", "meanF2[90,20,100]", "sigmaFRatio[4,0.5,10]",
#     #"alphaF[-0.016]",
#     # bin02
#     #"meanP1[90,88,92]", "width[2.0]", "sigmaP1[1.7,1.5,2.3]", "meanP2[70,60,80]", "sigmaPRatio[5,1.0,20.0]",
#     #"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin03
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[60,20,75]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[70,20,100]", "sigmaFRatio[3,1.5,5]",
#     #"alphaF[-0.029]",
#     # bin04
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.8]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[6,2.5,10]",
#     # bin05
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin06
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.8]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin07
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin14
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin16
#     #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.1]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
#     # bin17
#     "meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
#     "meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
# ]
