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

baseOutDir = "results/SOS_Electron_2017/"


#############################################################
########## samples definition  - preparing the samples
#############################################################
import etc.inputs.tnpSampleDef_SOS_Electron_2017 as tnpSamples
tnpTreeDir = "./Events"

samplesDef = {
    "data"   : tnpSamples.SOS_Electron_2017["data"].clone(),
    "mcNom"  : tnpSamples.SOS_Electron_2017["DY"].clone(),
    "mcAlt"  : tnpSamples.SOS_Electron_2017["DY"].clone(),
    "tagSel" : tnpSamples.SOS_Electron_2017["DY"].clone(),
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
cutBase   = "Tag_pt > 37 && abs(Tag_eta) < 2.5 && Tag_cutBased > 3 && Tag_isGenMatched && Probe_pt > 5.0 && abs(Probe_eta) < 2.5 && Probe_isGenMatched && TnP_trigger && Probe_charge*Tag_charge < 0" # tightNoIsoObject
#cutBase   = "Tag_pt > 37 && abs(Tag_eta) < 2.5 && Tag_cutBased > 3 && Tag_isGenMatched && Probe_pt > 5.0 && abs(Probe_eta) < 2.5 && Probe_isGenMatched && TnP_trigger && Probe_charge*Tag_charge < 0 && " + Probe_isTightNoIso # tightObjectOverTightNoIso

additionalCuts = {}


#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
]

tnpParDoublePeakNomFit = [
    "meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    "meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ##################### MC #####################
    # bin01
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,3.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin02
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin03
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin04
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[6,4.5,10]",
    # bin05
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",

    ##################### DATA #####################
    # bin00
    #"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[60,55,75]", "sigmaPRatio[8,5.5,10]",
    #"meanF1[90,88,92]", "width[2.0]", "sigmaF1[2.0]", "meanF2[90,85,95]", "sigmaFRatio[5,1.0,20.0]",
    #"acmsF[50]","betaF[0.01]","gammaF[0.052]","peakF[90.0]",
    # bin01
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[75,70,80]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,88,92]", "width[3.0]", "sigmaF1[1.0,0.5,4.3]", "meanF2[90,20,100]", "sigmaFRatio[4,0.5,10]",
    #"acmsF[57.0]","betaF[0.60]","gammaF[0.017]","peakF[90.0]",
    # bin02
    #"meanP1[90,88,92]", "width[2.0]", "sigmaP1[1.7,1.5,2.5]", "meanP2[70,60,80]", "sigmaPRatio[5,1.0,20.0]",
    #"meanF1[90,88,92]", "width[2.0]", "sigmaF1[1.8,1.7,3.5]", "meanF2[90,88,92]", "sigmaFRatio[5,1.0,7.0]",
    # bin03
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[60,20,75]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[70,60,80]", "sigmaFRatio[3,1.5,5]",
    # bin04
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[60,20,75]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[6,2.5,10]",
    # bin05
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[65,60,70]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[65,50,70]", "sigmaFRatio[1,0.3,1.5]",
    #"acmsF[48.]","betaF[0.048]","gammaF[0.043]","peakF[90.0]",
    # bin06
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[70,60,70]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    #"acmsF[75.]","betaF[0.01]","gammaF[0.028]","peakF[90.0]",
    # bin07
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[70,60,75]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[70,60,80]", "sigmaFRatio[2,1.5,4]",
    # bin14
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin15
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[3.0,1.5,4.5]", "meanP2[90,20,100]", "sigmaPRatio[8,4.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[3.0,1.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[8,4.5,10]",
    # bin19
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",


    ####################### MC #####################
    ### bin01
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,3.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,3.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin02
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.2]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin03
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,3.3]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,3.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin05
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,3.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,3.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin06
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin07
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.4]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,3.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin08
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,1.9]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.1]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin11
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,3.2]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin14
    ###"meanP1[90,80,100]", "width[2.0]", "sigmaP1[1.0,0.5,1.9]", "meanP2[90,20,110]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.0]", "sigmaF1[1.0,0.5,1.9]", "meanF2[90,20,110]", "sigmaFRatio[4,1.5,10]",
    ### bin15
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,3.5]", "meanP2[90,20,110]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,3.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin16
    ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,1.8]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin17
    ###"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.1]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    ### bin19
    ###"meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    ###"meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ##################### MC #####################
    # bin02
    #"meanP[-0.0,-5.0,5.0]","sigmaP[2.1]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[0.5]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    # bin04
    #"meanP[-0.0,-5.0,5.0]","sigmaP[2.1]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[0.5]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    # bin08
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1.7]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[0.5]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[2.3]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[0.9]","sosF[1,0.5,5.0]",
    # bin10
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1.4]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.4]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[1.4]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[1.5]","sosF[1,0.5,5.0]",
    # bin11
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[1.9]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.2]","sosF[1,0.5,5.0]",
    # bin12
    #"meanP[-0.5,-5.0,0.6]","sigmaP[1.2]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[1.8]","sosP[1,0.5,5.0]",
    #"meanF[-0.5,-5.0,0.7]","sigmaF[1.7]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.0]","sosF[1,0.5,5.0]",
    # bin13
    #"meanP[-0.5,-5.0,5.0]","sigmaP[2.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[2.5]","sosP[1,0.5,5.0]",
    #"meanF[-0.5,-5.0,5.0]","sigmaF[2.4]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.6]","sosF[1,0.5,5.0]",
    # bin14
    #"meanP[-0.5,-5.0,0.6]","sigmaP[1.2,1.5,2.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[2.0]","sosP[1,0.5,5.0]",
    #"meanF[-0.5,-5.0,0.7]","sigmaF[1.7,2.0,2.2]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.2]","sosF[1,0.5,5.0]",
    # bin15
    #"meanP[-0.5,-5.0,0.6]","sigmaP[1.2,1.5,2.0]","alphaP[2.0,1.2,3.5]" ,"nP[3,-5,5]","sigmaP_2[2.5]","sosP[1,0.5,5.0]",
    #"meanF[-0.5,-5.0,0.7]","sigmaF[1.7,2.0,2.2]","alphaF[2.0,1.2,3.5]","nF[3,-5,5]","sigmaF_2[2.7]","sosF[1,0.5,5.0]",
]

tnpParDoublePeakAltSigFit = [
    "meanP1[90,80,100]","sigmaP1[0.9,0.5,5.0]","meanP2[90,20,110]","sigmaP2[0.9,0.5,5.0]",
    "meanF1[90,80,100]","sigmaF1[0.9,0.5,5.0]","meanF2[90,20,110]","sigmaF2[0.9,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    # bin00
    #"meanP1[90,80,100]","sigmaP1[0.9,0.5,3.3]","meanP2[70,60,80]","sigmaP2[0.9,0.5,7.0]",
    #"meanF1[90,80,100]","sigmaF1[0.9,0.5,5.0]","meanF2[90,20,110]","sigmaF2[0.9,0.5,5.0]",
    #"acmsP[50]","betaP[0.08]","gammaP[0.04]","peakP[90.0]",
    # bin01
    #"meanP1[90,88,92]","sigmaP1[0.9,0.5,5.0]","meanP2[75,70,85]","sigmaP2[0.9,0.5,7.0]",
    #"meanF1[90,88,92]","sigmaF1[0.9,0.5,5.0]","meanF2[75,60,80]","sigmaF2[3.9,2.5,7.0]",
    #"acmsP[65.]","betaP[0.01]","gammaP[0.040]","peakP[90.0]",
    #"acmsF[53.0]","betaF[0.50]","gammaF[0.017]","peakF[90.0]",
    # bin06
    #"meanP1[90,80,100]","sigmaP1[0.9,0.5,2.8]","meanP2[65,60,75]","sigmaP2[0.9,0.5,9.0]",
    #"meanF1[90,80,100]","sigmaF1[0.9,0.5,4.5]","meanF2[65,60,75]","sigmaF2[9.9,4.5,15.0]",
    #"acmsF[75.]","betaF[0.01]","gammaF[0.022]","peakF[90.0]",
    # bin07
    #"meanP1[90,80,100]","sigmaP1[0.9,0.5,3.5]","meanP2[65,60,75]","sigmaP2[0.9,0.5,15.0]",
    #"meanF1[90,80,100]","sigmaF1[0.9,0.5,5.0]","meanF2[65,60,80]","sigmaF2[0.9,0.5,11.0]",
    #"acmsP[55]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    #"acmsF[50]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    # bin15
    #"meanP1[90,80,100]","sigmaP1[0.9,0.5,11.0]","meanP2[90,20,120]","sigmaP2[0.9,0.5,15.0]",
    #"meanF1[90,80,100]","sigmaF1[0.9,0.5,16.0]","meanF2[90,20,120]","sigmaF2[0.9,0.5,11.0]",
    # bin17
    #"meanP1[90,80,100]","sigmaP1[0.9,0.5,11.0]","meanP2[90,20,120]","sigmaP2[0.9,0.5,9.0]",
    #"meanF1[90,80,100]","sigmaF1[0.9,0.5,11.0]","meanF2[90,20,120]","sigmaF2[0.9,0.5,9.0]",
]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
]
     
tnpParDoublePeakAltBkgFit = [
    "meanP1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    "meanF1[90,80,100]", "width[2.5,2.0,3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",

    # bin00
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin01
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[75,70,80]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,88,92]", "width[3.0]", "sigmaF1[1.0,0.5,4.3]", "meanF2[90,20,100]", "sigmaFRatio[4,0.5,10]",
    #"alphaF[-0.016]",
    # bin02
    #"meanP1[90,88,92]", "width[2.0]", "sigmaP1[1.7,1.5,2.5]", "meanP2[70,60,80]", "sigmaPRatio[5,1.0,20.0]",
    #"meanF1[90,88,92]", "width[2.0]", "sigmaF1[2.0,1.5,4.0]", "meanF2[90,85,95]", "sigmaFRatio[5,1.0,20.0]",
    #"alphaF[-0.039]",
    # bin03
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,4.5]", "meanP2[60,20,75]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[70,20,100]", "sigmaFRatio[3,1.5,5]",
    #"alphaF[-0.032]",
    # bin04
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[60,20,75]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,4.5]", "meanF2[90,20,100]", "sigmaFRatio[6,2.5,10]",
    #"alphaF[-0.037]",
    # bin08
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.5]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin14
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.3]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin16
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.2]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin18
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,1.1]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
    # bin19
    #"meanP1[90,80,100]", "width[3.0]", "sigmaP1[1.0,0.5,2.0]", "meanP2[90,20,100]", "sigmaPRatio[4,1.5,10]",
    #"meanF1[90,80,100]", "width[3.0]", "sigmaF1[1.0,0.5,2.5]", "meanF2[90,20,100]", "sigmaFRatio[4,1.5,10]",
]
