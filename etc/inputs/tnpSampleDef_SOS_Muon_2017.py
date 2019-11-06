from libPython.tnpClassUtils import tnpSample

eosSOSMuon2017 = "/eos/cms/store/user/evourlio/SOS_TnP_Muon_191101/2017/"

SOS_Muon_2017 = {
    "DY"   : tnpSample("DY"     , eosSOSMuon2017 + "DYJetsToLL_M50_LO/DYJetsToLL_M50_LO.root"                             , isMC = True, nEvts =  -1 ),
    "data" : tnpSample("data"   , eosSOSMuon2017 + "SingleMuon_Run2017_1June2019/SingleMuon_Run2017*_1June2019.root"      , lumi = 41.5 ),
}
