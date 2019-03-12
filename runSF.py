import os
from multiprocessing import Pool

def GetCommand(command, den, tag):
  return command%(den,tag)

def ex(command):
  print 'Executing command: ', command
  os.system(command)

def RunTnP(listOfArguments):
  den, tag = listOfArguments 
  for c in commands: ex(GetCommand(c, den, tag))
  return True

den = ['MID'] #['LID', 'MID', 'MPID', 'TID']
#num = ['passRelIsoL', 'passRelIsoT']
num = ['passMultiIsoL', 'passMultiIsoM', 'passMultiIsoM2017', 'passMultiIsoM2017v2', 'passMiniIsoL', 'passMiniIsoM', 'passMiniIsoT', 'passMiniIsoVT']

listInput = []
for d in den:
  for n in num:
    listInput.append([d,n])
njobs = len(listInput)
print 'List of inputs (%i):\n'%njobs, listInput

commands = [
 'python tnpEGM_fitter.py etc/config/settings_muo_%s.py --flag %s --createBins',
 'python tnpEGM_fitter.py etc/config/settings_muo_%s.py --flag %s --createHists',
 'python tnpEGM_fitter.py etc/config/settings_muo_%s.py --flag %s --doFit',
 'python tnpEGM_fitter.py etc/config/settings_muo_%s.py --flag %s --doFit --mcSig --altSig',
 'python tnpEGM_fitter.py etc/config/settings_muo_%s.py --flag %s --doFit --altSig',
 'python tnpEGM_fitter.py etc/config/settings_muo_%s.py --flag %s --doFit --altBkg',
# 'python tnpEGM_fitter.py etc/config/settings_muo_%s.py --flag %s --sumUp'
]
if njobs == 1:
  print 'Secuential mode...'
  RunTnP(listInput[0])
else: 
  print 'Multiprocess: calculating %i scale factors...'%njobs
  pool = Pool(njobs)
  retlist = pool.map(RunTnP, listInput)
  pool.close()
  pool.join()

#os.system("mv results results_data2017_MPID")
