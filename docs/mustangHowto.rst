How to run Mustang
==================

Mustang superimposes protein structures and as a result you can get not only the structure alignment but also the sequence alignment.

This program needs the structures that are going to be superimposed, their name and the path in where they are allocated.

Create the input file considering that the first line of the file should have the path in where the structures are allocated and it must start with the > symbol the next lines should start with the + symbol and be followed by just the name of the structure files.

So if you want to align the files
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

that are allocated in the folder   /home/mypc/SRUL/  you just need to create a file, we use mus as the file extension in the example, but it could be any, and it should contain the following text:
  
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

You can download the mus file  `here <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/fee5c18e268941d3cec22cf4da90faca4a185fc7/docs/TAL_EFFECTOR.mus>`_, you can download the fragments structures `here <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/SRUL.tar.gz>`_.

To obtain the aligned pdbs and fasta in an output called results you need to execute the following command line:

.. code-block:: runmustang

  /MUSTANG_v3.2.4/bin/mustang-3.2.4 -f example.mus -F fasta -o resultsTAL_EFFECTOR

As a result, if there are no errors, the program will return two files :

`resultsTAL_EFFECTOR.pdb <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/resultsTAL_EFFECTOR.pdb>`_

`resultsTAL_EFFECTOR.afasta <https://github.com/DraLaylaHirsh/MRFprofilesCreation/blob/780e8c5160e553ce8ee3e7b6ca540f47732cbc6e/resultsTAL_EFFECTOR.afasta>`_

To see the resulting pdb you can use pymol and to see the afasta resulting file you can use belvu or seaview.



