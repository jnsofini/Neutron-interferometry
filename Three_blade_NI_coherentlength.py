#Calulate the intensity as a function of phase flag with a mismatch m on the 3rd blade.

#import and use functions from QWfunction module
import numpy as np
from qfunctions import *

#-----------------------------------------------------------------------------------
def InterationPhase3Blade(nofplane,Ope,m=0):
    
    '''
    Phasearray input return wavefuntion &intensities, m=0 is the default value of
    the mismatch on the third blade
    '''
    Phase=np.linspace(0,2*np.pi,100); #Phase flag array to loop through  
    Phaselength=len(Phase);
    SumOBeam=np.zeros(Phaselength);
    SumHBeam=np.zeros(Phaselength);
              
    for k in range(Phaselength):
        psiOut=ThreeBladeNI(nofplane,Phase[k],Ope,m);
        psiOBeam=psiOut[0];
        psiHBeam=psiOut[1];
        IntensityNodesO=AbsF(psiOBeam);
        IntensityNodesH=AbsF(psiHBeam);
        SumOBeam[k]=NodeSum(IntensityNodesO);
        SumHBeam[k]=NodeSum(IntensityNodesH);  
                                             
    return SumOBeam,SumHBeam,Phase  
#-----------------------------------------------------------------------------------
def ThreeBladeNI(nodes,phase,Had,m,FT=1,FR=1):#returns O & H beams in non vector forms!
          
    FT=FT*np.exp(1j*phase);
    FR=FR*np.exp(-1j*phase);
    n=nodes;  
    
    psi0=np.array([[1],[0]]); #initial state  
    '''
    phis = 0;p1=np.sqrt(p);p2=np.sqrt(1-p);
    Had=np.matrix([[p1,np.exp(1j*phis)*p2],[np.exp(-1j*phis)*p2,-p1]]);
    #Operator of the plane '''

    
    #%%%%%%%%%%%%%
    #First blade%
    #%%%%%%%%%%%%
    
    psiRT=BladeF(Had,n,psi0);
    psiT=FT*psiRT[1]; #selecting the reflected beam and adding phase
    psiR=FR*psiRT[0]; #selecting the transmited beam

    #%%%%%%%%%%%%%%%
    #Second blades%
    #%%%%%%%%%%%%%%%
    
    psiT2=BladeF(Had,n,psiT);
    #psiTT=psiT2[1];
    psiTR=psiT2[0];
 
    psiR2=BladeF(Had,n,psiR);
    #psiRT=psiR2[0];
    psiRR=psiR2[1];
    
    #%%%%%%%%%%%%%%%
    #Third blades%
    #%%%%%%%%%%%%%%%
    
    
    if m == 0:
        psi3in=psiRR+psiTR; #input to the third blade
    else:        
        Psioffset=np.zeros((2,m));
        psi3in1=np.concatenate((Psioffset,psiTR),axis=1);
        psi3in2=np.concatenate((psiRR,Psioffset),axis=1);
        psi3in=psi3in1+psi3in2; #input to the third blade
            
    psi3F=BladeF(Had,n+0,psi3in);  #+ m denote how much thicker the 3rd blade it
    psiHBeam= psi3F[0];
    psiOBeam= psi3F[1];
    
    return psiOBeam, psiHBeam
#------------------------------------------------------------------------------------  

def Plot2G(xdata,data1,data2=None):#Plotting two curves
    fig = plt.figure();
    plt.plot(xdata,data1,'b',linewidth=0.5,marker='o',label='O')
    plt.plot(xdata,data2,'k',linewidth=0.5,marker='v',label='H')
    plt.ylabel('Integrated Intensity',fontsize=25)
    plt.xlabel('Phase[rads]',fontsize=25)
    pylab.legend(loc='upper right')
    
    pylab.xticks(np.arange(0,6.5,2),fontsize=24)
    pylab.yticks(np.arange(0,1.01,.25),fontsize=24)
    pylab.legend(loc='upper right',fontsize=21)
    pylab.tight_layout()
    
    return fig
#------------------------------------------------------------------------------------  

def Contrast(Nvals,nofplane,Had):#contrast of O-beam
    
    Nplanelength=len(Nvals);
    Contrast0=np.zeros(Nplanelength);
    
    for k in range(Nplanelength):
        
        data1 = InterationPhase3Blade(nofplane,Had,Nvals[k]);
        min_I0 = np.amin(data1[0]);
        max_I0 = np.amax(data1[0]);
        contr0 = (max_I0-min_I0)/(max_I0+min_I0);
        Contrast0[k]=contr0;
    
    fig = plt.figure();
    plt.plot(Nvals,Contrast0,'b',linewidth=0.5,marker='o',label='Contrast')
    plt.ylabel('Contrast',fontsize=25)
    plt.xlabel('Offset',fontsize=25)
        
    pylab.xticks(fontsize=24)
    pylab.yticks(np.arange(0,1.01,.25),fontsize=24)
    pylab.legend(loc='upper right',fontsize=21)
    pylab.tight_layout()
    
    return fig
#------------------------------------------------------------------------------------  

        


def main():
    
    #===========================================================================
    
    #Cide block for Intensity O and H intensity with phase flag rotation:    
    #--->Begins Here!-----------------------------------------------------------
 
    nofplane=22;    #number of planes considered (Goodvalue=78)
   # planeoffset=0; #offset number

    '''
    Good form to use:
    #q=17*np.pi/(36)
    pa1=1*np.pi/2; #or 64
    ph1=np.exp(1j*pa1);
    ph2=np.exp(-1j*pa1);
    q=1*np.pi/(64)        #Reasonable values q=pi/64, pa1=pi/64
    Had=np.matrix([[ph1*np.cos(q),np.sin(q)],[-np.sin(q),ph2*np.cos(q)]])    
    
    '''
    
    #q=17*np.pi/(36)
    pa1=1*np.pi;
    ph1=np.exp(1j*pa1);
    ph2=np.exp(-1j*pa1);
    q=1*np.pi/(64)        #Reasonable values q=pi/64, pa1=pi/64
    Had=np.matrix([[np.cos(q),ph1*np.sin(q)],[-ph2*np.sin(q),np.cos(q)]])  
    
    #this is for whole interferometer
    ttt=InterationPhase3Blade(nofplane,Had);
    phase_angle=ttt[2]
    ObeamI=ttt[0]/(ttt[0]+ttt[1]);
    HbeamI=ttt[1]/(ttt[0]+ttt[1]);
    gtt=Plot2G(phase_angle,ObeamI,HbeamI);
    #gtt2=PlotG(Phase,HbeamI);
    gtt.show()
    #gtt2.show()
      
    #--->Endss Here!------------------------------------------------------------ 
    
        #Code block for o-contrast vs offset:    
    #--->Begins Here!-----------------------------------------------------------
    
    poffsetvals=np.arange(0,67,1)
    
    gtt2 = Contrast(poffsetvals,nofplane,Had);
   
    gtt2.show()
      
    #--->Endss Here!------------------------------------------------------------ 
    #===========================================================================
    
if __name__ == "__main__":
    main()  
