#ifndef ROO_EXPONENTIALN
#define ROO_EXPONENTIALN

#include <vector>

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooListProxy.h"
#include "RooAbsReal.h"
#include "TMath.h"
#include "RooMath.h"


/* class RooRealVar;
class RooArgList ;
*/
 
 class RooExponentialN : public RooAbsPdf {
 public:
   RooExponentialN() {};
   RooExponentialN(const char *name, const char *title,
                   RooAbsReal& x, const RooArgList& coefList, Int_t lowestOrder=1) ;
 
   RooExponentialN(const RooExponentialN& other, const char* name);
   inline virtual TObject* clone(const char* newname) const { return new RooExponentialN(*this,newname); }
   inline ~RooExponentialN() {}
   Double_t evaluate() const ;
   
   ClassDef(RooExponentialN,2);
 
 protected:
 
   RooRealProxy _x ;
   RooListProxy _coefList ;
   Int_t _lowestOrder ;

   mutable std::vector<Double_t> _wksp; //! do not persist
   
 };
#endif

// roo polynomial 
 
// class RooExponentialN : public RooAbsPdf {
//  public:
// 
//     RooExponentialN() ;
//     RooExponentialN(const char* name, const char* title, RooAbsReal& x) ;
//     RooExponentialN(const char *name, const char *title,
//                   RooAbsReal& _x, const RooArgList& _coefList, Int_t lowestOrder=1) ;
// 
//     RooExponentialN(const RooExponentialN& other, const char* name = 0);
//     virtual TObject* clone(const char* newname) const { return new RooExponentialN(*this, newname); }
//     virtual ~RooExponentialN() ;
// 
//     Int_t getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName=0) const ;
//     Double_t analyticalIntegral(Int_t code, const char* rangeName=0) const ;
// 
//  protected:
// 
//     RooRealProxy _x;
//     RooListProxy _coefList ;
//     Int_t _lowestOrder ;
// 
//     mutable std::vector<Double_t> _wksp; //! do not persist
// 
//     /// Evaluation
//     Double_t evaluate() const;
//     RooSpan<double> evaluateBatch(std::size_t begin, std::size_t batchSize) const;
// 
// 
//     ClassDef(RooExponentialN,1) // Polynomial PDF
//         };
