from libPython.tnpClassUtils import tnpSample

eosSOSElectron2017 = "/eos/cms/store/user/evourlio/SOS_TnP_Electron_191101/2017/"

SOS_Electron_2017 = {
    "DY"   : tnpSample("DY"     , eosSOSElectron2017 + "DYJetsToLL_M50_LO/DYJetsToLL_M50_LO.root"                                   , isMC = True, nEvts =  -1 ),
    "data" : tnpSample("data"   , eosSOSElectron2017 + "SingleElectron_Run2017_1June2019/SingleElectron_Run2017*_1June2019.root"    , lumi = 41.5 ),
}
