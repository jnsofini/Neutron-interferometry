# Neutron Interferometry:
### Intro
This repository contains some projects on neutron interferometry. Neutron interferometry is interferometry with neutrons. Interferometry, in most cases, involves the coherence splitting of a wave and its interferences with another operation. In neutrons, the interferometer is fabricated from single crystals. The most common geometry is the three-blade geometry shown below. There are other geometries, including the four and five-blade neutron interferometers. A review of interferometry including these geometries can be found in the article [Neutron interferometry at the NIST](https://www.hindawi.com/journals/ahep/2015/687480/). Interferometry with neutrons is unique in that


1.  It involves the coherent splitting a single particle wave
2.  Only single particle interference is observed
3.  The neutron has a spin and can be polarized to add another degree freedom 
4.  It can be used to verify some clauses of foundations as well as probe materials

[![Picture of a NI](https://github.com/jnsofini/Neutron-interferometry/blob/master/ThinBlade.png)]

Much development has lead to the discovery of subspaces encoded in a neutron interferometer in which information is shielded from vibrational noise, commonly referred to as decoherence-free subspace. Some of these work can be found in this [arXiv article](https://arxiv.org/pdf/1704.03589.pdf) and references therein. Another interesting work is that of controlling the  `spin-orbit` of a neutron wavepacket. These advancement has led to research progress with potential to probe properties of materials, including skyrmions. 

Below is a cartoon of the propagation of a wave through a neutron interferometer.[Animation of NI](https://vimeo.com/82315901). The signal is chacterized by the value of the contrast. The contrast is defined by the normalized intensity (Imax-Imin)/(Imax+Imin). Below is s typical figure.


## Project folder
In these folders are programmed to simulate the propagation of a wave via a neutron interferometer. The wave is modelled in a similar to a quantum walk. An incident wave propagates through a lattice and spreads into a multi-ray limited only by the spatial coherence of the neutron wavepacket.
The projects included in these folders are
* Simulation of beam profiles
* Noise effect in a NI



The effect of noise can be modelled as shown in work published paper available on at the at
[University of Waterloo Repository](https://uwspace.uwaterloo.ca/bitstream/handle/10012/13801/1.4996866.pdf?sequence=1&isAllowed=y)

The effect of noise can be modelled as following 
(![Noise Modelling in a NI](http://inspirehep.net/record/1591360/files/YNoiseD_multiple.png)). 
