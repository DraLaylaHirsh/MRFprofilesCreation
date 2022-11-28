
Usage
=====
.. _Process:

Process
-------

.. image:: /images/CreationProcess.svg



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

.. code-block:: RunCircular

  $./runCircularProfile.sh TAL_EFFECTOR

.. _Linear Results:

Linear Results
---------------

After running the script you will have the following files
*pfwTAL_EFFECTORLinear.msf
*TAL_EFFECTORLinear.prf
*searchLinearResultsTAL_EFFECTORLinear
*newTAL_EFFECTORLinear.prf
*autoscalingsearchLinearrResultsTAL_EFFECTORLinear


.. _Circular Results:

Circular Results
---------------
