# Neutron Interferometry:
### Intro
This repository contains some projects on neutron interferometry. Neutron interferometry is basically interferometry with neutrons. Interferometry, in most cases, involves the coherence splitting of a wave and it interferences with another operation. In neutrons the interferometer is made from single crystals. The most common geometry is the three-blade geometry shown below. There are other geometries including the four and five-blade neutron interferometers. A review of interferometry including these geometries can be found in the article [Neutron interferometry at the NIST](https://www.hindawi.com/journals/ahep/2015/687480/). Interferometry with neutrons is unique in that


1.  It involves the coherent splitting a a single particle wave
2.  Only single particle interference is observe
3.  The neutron has spin and can be polarize to add another degree freedom 
4.  It can be used to verify some clauses of foundations as well as probe materials

[![Picture of an NI](https://github.com/jnsofini/Neutron-interferometry/blob/master/ThinBlade.png)]

A lot of developement has lead to the discovery of subspaces encoded in a neutron interferometer in which information is shielded from vibrational noise, commonly referred to as decoherence-free subspace. Some of these work can be found in this [arXiv article](https://arxiv.org/pdf/1704.03589.pdf) and references there in. Another facilinating work is that of controlling the  `spin-orbit` of a neutron wavepacket. This has lead to advancement with potenrial to probe properties of materials including skipemions. 

Below is a cartoon of the propagation of a wave through a neutron interferometer.

[![Animation of NI](https://vimeo.com/82315901)]

## Project folder
In this folders are programs to simulate the propagation of a wave via a neutron interferometer. The wave is modelled in a similar to a quantum walk. An incident wave progate through a lattice and spreads into a multiray limited only by the spatial coherence of the neutron wavepacket.
The prohects included in this folders are
* Simulation of beam profiles
* Noise effect in an NI


The effect of noise can be modelled as shown in the work bublsied paper available on at the at
[University of Waterloo Repository](https://uwspace.uwaterloo.ca/bitstream/handle/10012/13801/1.4996866.pdf?sequence=1&isAllowed=y)

The effect of noise can be modelled as follow 
(![Noise Modelling in a NI](http://inspirehep.net/record/1591360/files/YNoiseD_multiple.png)). 
