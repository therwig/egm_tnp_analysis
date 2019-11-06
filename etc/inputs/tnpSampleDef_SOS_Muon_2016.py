from libPython.tnpClassUtils import tnpSample

eosSOSMuon2016 = "/eos/cms/store/user/evourlio/SOS_TnP_Muon_191101/2016/"

SOS_Muon_2016 = {
    "DY"   : tnpSample("DY"     , eosSOSMuon2016 + "DYJetsToLL_M50_LO/DYJetsToLL_M50_LO.root"                             , isMC = True, nEvts =  -1 ),
    "data" : tnpSample("data"   , eosSOSMuon2016 + "SingleMuon_Run2016_1June2019/SingleMuon_Run2016*_1June2019.root"      , lumi = 35.9 ),
}
