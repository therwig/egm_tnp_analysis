
#include "RooExponentialN.h"

ClassImp(RooExponentialN) 

RooExponentialN::RooExponentialN(const char *name, const char *title, 
                                 RooAbsReal& x, const RooArgList& coefList, Int_t lowestOrder) :
    RooAbsPdf(name,title), 
    _x("x","x",this,x),
    _coefList("coefList","List of coefficients",this),
    _lowestOrder(lowestOrder)
{ 
    RooFIter coefIter = coefList.fwdIterator() ;
    RooAbsArg* coef ;
    while((coef = (RooAbsArg*)coefIter.next())) {
        if (!dynamic_cast<RooAbsReal*>(coef)) {
            coutE(InputArguments) << "RooExponentialN::ctor(" << GetName() << ") ERROR: coefficient " << coef->GetName()
                                  << " is not of type RooAbsReal" << endl ;
        }
        _coefList.add(*coef) ;

    }
}


RooExponentialN::RooExponentialN(const RooExponentialN& other, const char* name):
   RooAbsPdf(other,name),
     _x("x", this, other._x),
     _coefList("coefList",this,other._coefList),
     _lowestOrder(other._lowestOrder) 
 { } 



 Double_t RooExponentialN::evaluate() const 
 { 
     const unsigned sz = _coefList.getSize();
     const int lowestOrder = _lowestOrder;
     if (!sz) return lowestOrder ? 1. : 0.;
     _wksp.clear();
     _wksp.reserve(sz);
     {
         const RooArgSet* nset = _coefList.nset();
         RooFIter it = _coefList.fwdIterator();
         RooAbsReal* c;
         while ((c = (RooAbsReal*) it.next())) _wksp.push_back(c->getVal(nset));
     }
     const Double_t x = _x;
     Double_t retVal = _wksp[sz - 1];
     for (unsigned i = sz - 1; i--; ) retVal = _wksp[i] + x * retVal;
     return TMath::Exp(retVal * std::pow(x, lowestOrder) + (lowestOrder ? 1.0 : 0.0));

 } 
