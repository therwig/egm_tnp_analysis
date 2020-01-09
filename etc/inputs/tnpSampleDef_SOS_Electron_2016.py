from libPython.tnpClassUtils import tnpSample

eosSOSElectron2016 = "/eos/cms/store/user/evourlio/SOS_TnP_Electron_191209/2016/"

SOS_Electron_2016 = {
    "DY"   : tnpSample("DY"     , eosSOSElectron2016 + "DYJetsToLL_M50_LO/DYJetsToLL_M50_LO.root"                                   , isMC = True, nEvts =  -1 ),
    "data" : tnpSample("data"   , eosSOSElectron2016 + "SingleElectron_Run2016_1June2019/SingleElectron_Run2016*_1June2019.root"    , lumi = 35.9 ),
}
