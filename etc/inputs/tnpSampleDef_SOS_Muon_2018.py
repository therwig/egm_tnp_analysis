from libPython.tnpClassUtils import tnpSample

eosSOSMuon2018 = "/eos/cms/store/user/evourlio/SOS_TnP_Muon_191101/2018/"

SOS_Muon_2018 = {
    "DY"   : tnpSample("DY"     , eosSOSMuon2018 + "DYJetsToLL_M50_LO/DYJetsToLL_M50_LO.root"                             , isMC = True, nEvts =  -1 ),
    "data" : tnpSample("data"   , eosSOSMuon2018 + "SingleMuon_Run2018_1June2019/SingleMuon_Run2018*_1June2019.root"      , lumi = 59.7 ),
}
