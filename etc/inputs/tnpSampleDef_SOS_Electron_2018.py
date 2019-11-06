from libPython.tnpClassUtils import tnpSample

eosSOSElectron2018 = "/eos/cms/store/user/evourlio/SOS_TnP_Electron_191101/2018/"

SOS_Electron_2018 = {
    "DY"   : tnpSample("DY"     , eosSOSElectron2018 + "DYJetsToLL_M50_LO/DYJetsToLL_M50_LO.root"                   , isMC = True, nEvts =  -1 ),
    "data" : tnpSample("data"   , eosSOSElectron2018 + "EGamma_Run2018_1June2019/EGamma_Run2018*_1June2019.root"    , lumi = 59.7 ),
}
