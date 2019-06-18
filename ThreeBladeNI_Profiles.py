#Fully functional program. Capable of plotting the probability distrubution for
#each beam inside a three blade NI.

import matplotlib.pyplot as plt
import numpy as np
import pylab

###################Beginning of functions!######################################
def AbsF(psin):
    psif=np.linalg.norm(psin,ord=2,axis=0)**2;
    return psif

def PlotF(data1,data2=None):
    fig = plt.figure();
    plt.plot(data1,'k',linewidth=5,label='O-Beam')
    #ax=fig.add_subplot(221)
    pylab.axis('off')
    #plt.plot(data2,'b',linewidth=2.5,label='H-Beam')
    plt.ylabel('Probability')
    plt.xlabel('Nodes')
    return fig
    
def BladeF(Ope,n,psin):
    
    PsiPad=np.zeros((2,n-1));
    psi=np.concatenate((psin,PsiPad),axis=1);
    Opef=Ope;
    psi=np.matrix(psi)

    for j in range(0, n):
        psi=Opef*psi;
        psi[1]=np.roll(psi[1],1,axis=1);
        
    psiR=np.concatenate((np.zeros((1,np.size(psi[1]))),psi[1]),axis=0);
    psiT=np.concatenate((psi[0],np.zeros((1,np.size(psi[1])))),axis=0);
        
    return psiR, psiT
    
###################End of functions!###########################################

def main():
    #Flags
    FT=1;
    FR=1;
    FTR=1;
    FRR=1;
    FTT=1;
    FRT=1;
    
    N=20000 #%number of planes used
    
    psi0=np.array([[1],[0]]); #initial state

    n=N;   
    pa1=0;
    ph1=np.exp(1j*pa1);
    ph2=np.exp(-1j*pa1);
    q=3*np.pi/(4)
    Had=np.matrix([[ph1*np.cos(q),np.sin(q)],[-np.sin(q),ph2*np.cos(q)]]) 
    #Operator of the plane
    
    #%%%%%%%%%%%%%
    #first blade%
    #%%%%%%%%%%%%
    
    [psiR,psiT]=BladeF(Had,n,psi0);
    
    psiT=FT*psiT; #selecting the reflected beam and adding phase
    psiR=FR*psiR; #selecting the transmited beam
    
    #%%%%%%%%%%%%%%%
    #Second blades%
    #%%%%%%%%%%%%%%%
    
    [psiTR,psiTT]=BladeF(Had,n,psiT);
    
    psiTT=FTT*psiTT; #selecting the reflected beam
    psiTR=FTR*psiTR; #selecting the transmited beam
    
    
    [psiRT,psiRR]=BladeF(Had,n,psiR);
    
    psiRT=FRT*psiRT; #selecting the reflected beam
    psiRR=FRR*psiRR; #selecting the transmited beam
    
    #%%%%%%%%%%%%%%%
    #Third blades%
    #%%%%%%%%%%%%%%%
    
    psiTRX=psiRR+psiTR; #input to the third blade
    
    [psiTRT,psiTRR]=BladeF(Had,n,psiTRX);
  
    #Intensities on each beam
    
    DT=AbsF(psiT);
    DR=AbsF(psiR);
    #DTPhase=np.real();
    #DRPhase=np.real(psi1wf[0]);
    figDT=PlotF(DT); #outputing the R and T
    figDT.show()
    figDR=PlotF(DR); #outputing the  phase of R and T
    figDR.show()
    
    DRR=AbsF(psiRR);
    DTR=AbsF(psiTR);
   
    #fig2B=PlotF2B(DRR,DTR); #outputing the O and H
    #fig2B.show()
    figDRR=PlotF(DRR);
    figDTR=PlotF(DTR);
    figDRR.show()
    figDTR.show()
       
    DTT=AbsF(psiTT);
    DRT=AbsF(psiRT);
    
    figDTT=PlotF(DTT);
    figDRT=PlotF(DRT);
    figDTT.show()
    figDRT.show()
    
    
    D0=AbsF(psiTRT);
    DH=AbsF(psiTRR);
    #figOH=PlotF2(D0,DH); #outputing the O and H
    #figOH.show()
    figD0=PlotF(D0);
    figDH=PlotF(DH);
    figD0.show()                   
    figDH.show()
    #DH=PlotF(DTR);
    #D0=PlotF(DRR);  
    #D0.show()
    #DH.show()
    
       
if __name__ == "__main__":
    main()  