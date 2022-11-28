
Usage
=====
.. _Process:

Process
-------

.. image:: /images/CreationProcess.png
    
    :alt: A description

The steps 1, 2, and 3 are part of an iterative process. 
In this particular case, we use a cluster of the pdb fragments from the SRUL library and evaluate all the cluster units as following:
Using TAL_Effector cluster, it contains the following units:

4cj9A_490_522_reg1
  
2ypfA_301_335_reg1
  
4gg4A_607_640_reg1
  
2ypfA_471_505_reg1
  
4cj9A_457_489_reg1
  
4hpzA_301_334_reg1
  
4cj9A_589_621_reg1
  
4cj9A_688_720_reg1
  
4cj9A_193_225_reg1
  
2ypfA_369_402_reg1
  
4cj9A_424_456_reg1
  
4hpzA_539_573_reg1
  
4gg4A_403_436_reg1
  
4cj9A_325_357_reg1
  
4hpzA_437_470_reg1
  
4cj9A_523_555_reg1
  
2ypfA_811_844_reg1
  
4gg4A_573_606_reg1
  
4gg4A_369_402_reg1
  
4hpzA_403_436_reg1
  
4hpzA_335_368_reg1
  
2ypfA_506_538_reg1
  
4cj9A_622_654_reg1
  
2ypfA_539_572_reg1
  
4cj9A_226_258_reg1

so, the first step is done, then we need to create the .mus file by using the following text, 
assuming that the fragments (or the SRUL folder is in /home/mypc/SRUL/) and saving it with the name TAL_EFFECTOR.mus:

>/home/mypc/SRUL/
  
+4cj9A_490_522_reg1
  
+2ypfA_301_335_reg1
  
+4gg4A_607_640_reg1
  
+2ypfA_471_505_reg1
  
+4cj9A_457_489_reg1
  
+4hpzA_301_334_reg1
  
+4cj9A_589_621_reg1
  
+4cj9A_688_720_reg1
 
+4cj9A_193_225_reg1
  
+2ypfA_369_402_reg1
  
+4cj9A_424_456_reg1
  
+4hpzA_539_573_reg1
  
+4gg4A_403_436_reg1
  
+4cj9A_325_357_reg1
  
+4hpzA_437_470_reg1
 
+4cj9A_523_555_reg1
  
+2ypfA_811_844_reg1
  
+4gg4A_573_606_reg1
  
+4gg4A_369_402_reg1
  
+4hpzA_403_436_reg1
  
+4hpzA_335_368_reg1
  
+2ypfA_506_538_reg1
  
+4cj9A_622_654_reg1
  
+2ypfA_539_572_reg1
  
+4cj9A_226_258_reg1

Finally, the step 3 would be done by running the following command, assuming that the mustang app is in the path 
/home/mypc/MUSTANG_v3.2.4/bin/mustang-3.2.4 and that our two output files (afasta and pdb) will have the name resultsTAL_EFFECTOR but with a different extension.
  
.. code-block:: MustangRun
  
  $/home/mypc/MUSTANG_v3.2.4/bin/mustang-3.2.4 -f TAL_EFFECTOR.mus -F fasta -o resultsTAL_EFFECTOR

At this point we can see the outputs using belvu/seaview and pymol/vmd/chimera and should work on the sequence alignment to create the profile. In this
process we could realiced that some of the units are wrongly alined so we could identify the units, erase then from the mus file, rerun mustang and reevaluate the results.

.. _Mustang Results:

Mustang Results
---------------
The sequence alignment given by mustang and using belvu would be observed as following:

.. image:: /images/MSA.png

The structure alignment given by mustang and using pymol as ribbon would be observed as following:

.. image:: /images/superimpColor.png

The structure alignment given by mustang and using pymol as sticks would be observed as following:

.. image:: /images/superimposition.png

.. _Profile Creation:

Profile creation
----------------

Once we have a sequence alignment that consider as correct, we need to decide if we will use circular or a linear profile. In case you want a circular 
profile just save the alignment as a msf, if you want a linear profile you need to make a copy of the sequence alignment and put them together as many times as needed. 

You can see the example files (this examples are based on the raw results from mustang).  

`Linear msf file <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/TAL_EFFECTORLinear.msf>`_

`Circular msf file <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/TAL_EFFECTOR.msf>`_.

Then you can download the following scripts to create the profiles, search and compare the results.

`Circular script file <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/runCircularProfile.sh>`_.

`Linear script file <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/runLinearProfile.sh>`_.

You will also need to download the python script to be able to compare the results with and without scaling:
`Python script for comparison 
<https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/VerifyresultsAgainstRepeatsDB.py>`_.

To run the scripts you can use one of the following commands:

.. code-block:: RunLinear

  $./runLinearProfile.sh TAL_EFFECTORLinear

 RunCircular

  $./runCircularProfile.sh TAL_EFFECTOR

.. _Linear Results:

Linear Results
---------------

After running the script you will have the following files:

*pfwTAL_EFFECTORLinear.msf

*TAL_EFFECTORLinear.prf

*searchLinearResultsTAL_EFFECTORLinear

*newTAL_EFFECTORLinear.prf

*autoscalingsearchLinearrResultsTAL_EFFECTORLinear


.. code-block::

  The output of the verification tells you:
  The profile retrieve 68 protein chains in the search
  The missing proteins to retrieve are: []
  The scaling profile retrieve 72 protein chains in the search
  The missing proteins to retrieve are: []
  These are the new findings to verify:
  These are the new findings to verify all the details:
  ('26.137', '2ypf_A', 'AVRBS3')
  ('26.695', '3ugm_A', 'TAL effector AvrBs3/PthA')
  ('26.407', '3v6p_A', 'dHax3')
  ('28.563', '4cj9_A', 'BURRH')
  ('26.277', '4gg4_A', 'Hax3')
  ('26.537', '4hpz_A', 'dTale2')
  ('26.063', '6jtq_A', 'TAL effector')
  
In the output you can observe that the profile without the autoscaling retrieves 68 protein chains, and they include the ones used in the profile. Then, considering the autoscaling profile 72 protein chains were retrieved, and again they include the ones used in the profile. Finally a list of the new protein chains found using the autoscaling profiles is shown.

.. _Circular Results:

Circular Results
---------------
After running the script you will have the following files:

*autoscalingsearchCircularResults_TAL_EFFECTORcircular

*newTAL_EFFECTORcircular.prf

*searchCircularResults_TAL_EFFECTORcircular

*TAL_EFFECTORcircular.prf

*pfwTAL_EFFECTORcircular.msf

.. code-block::

  The output of the verification tells you:
  The profile retrieve 104 protein chains in the search
  The missing proteins to retrieve are: []
  The profile retrieve 197 protein chains in the search
  The missing proteins to retrieve are: []
  These are the new findings to verify:
  These are the new findings to verify all the details:
  ('16.885', '2kq5_A', 'Avirulence protein')
  ('115.626', '2ypf_A', 'AVRBS3')
  ('97.466', '3ugm_A', 'TAL effector AvrBs3/PthA')
  ('120.548', '3v6p_A', 'dHax3')
  ('121.765', '4cj9_A', 'BURRH')
  ('9.601', '4d49_A', 'ARMADILLO REPEAT PROTEIN ARM00027')
  ('9.086', '4d4e_A', 'ARMADILLO REPEAT PROTEIN ARM00016')
  ('9.000', '4db6_A', 'Armadillo repeat protein')
  ('9.472', '4db8_A', 'Armadillo-repeat Protein')
  ('121.979', '4gg4_A', 'Hax3')
  ('86.876', '4hpz_A', 'dTale2')
  ('11.547', '4hxt_A', 'De Novo Protein OR329')
  ('10.302', '4pjq_A', 'Pentatricopeptide repeat protein')
  ('10.574', '4plq_A', 'Arm00011')
  ('10.574', '4plr_A', 'Arm00008')
  ('10.574', '4pls_A', 'Arm00010')
  ('17.901', '4rv1_A', 'Engineered Protein OR497')
  ('14.509', '4rzp_A', 'Engineered Protein OR366')
  ('10.688', '4v3o_A', 'YIII_M5_AII')
  ('9.071', '4v3q_A', 'YIII_M4_AII')
  ('12.234', '5aei_A', 'DESIGNED ARMADILLO REPEAT PROTEIN YIIIM5AII')
  ('8.885', '5mfb_A', 'YIII(Dq)4CqI')
  ('12.234', '5mfc_A', 'YIIIM5AII')
  ('12.406', '5mfd_A', "YIIIM''6AII")
  ('9.415', '5mfi_A', 'YIII(Dq.V2)4CqI')
  ('9.601', '5mfk_A', 'YIII(Dq.V1)4CPAF')
  ('13.851', '5mfl_A', '(KR)5_GS10_YIIIM6AII')
  ('13.479', '5mfm_A', 'YIIIM6AII_GS11_(KR)5')
  ('13.479', '5mfm_C', 'Importin subunit alpha')
  ('12.778', '5orm_A', 'cPPR-Telo1')
  ('121.507', '6jtq_A', 'TAL effector')
  ('11.876', '6s9l_A', 'KR4KLSF Lock1')
  ('14.295', '6s9m_A', 'Lock2_KRKRKAKITW')
  ('14.724', '6s9n_A', 'Lock2_KRKRKAKLSF')
  ('14.824', '6s9o_A', 'designed Armadillo repeat protein with internal Lock1 fused to target peptide KRKRKLKFKR')
  ('15.168', '6s9p_A', 'internal Lock2 fused to target peptide KRKAKITWKR')
  ('10.002', '6sa6_A', 'DARPin-Armadillo fusion A5')
  ('13.779', '6sa7_A', 'DARPin-Armadillo fusion C8long83')
  ('14.352', '6sa8_A', 'ring-like DARPin-Armadillo fusion H83_D01')
  ('10.245', '7qnp_AAA', 'ength:240  Designed Armadillo Repeat Protein N(A4)M4C(AII)')
  ('9.286', '7r0r_A', 'Designed Armadillo Repeat Protein N(A4)M4C(AII)')

In the output you can observe that the profile without the autoscaling retrieves 104 protein chains, and they include the ones used in the profile. Then, considering the autoscaling profile 197 protein chains were retrieved, and again they include the ones used in the profile. Finally a list of the new protein chains found using the autoscaling profiles is shown.
