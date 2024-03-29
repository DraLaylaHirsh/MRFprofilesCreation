Requirements
============

.. _instructions:

Instructions
------------

The created profiles are build circularly and linearly, and they can be use to search matches in different databases, 
to do so, pftools is used (fortran source code).

To install pftools you can go to `GitHub Pftools3 <https://github.com/sib-swiss/pftools3/>`_, and follow the installation process or you can use the command:

.. code-block:: InstallPftools

    $sudo apt-get install pftools
    
    
To obtain a more acurate score for the profiles we use autoscaling over the builded profiles. The autoscaling software can be downloaded `here <https://github.com/sib-swiss/pftools3/>`_.You will need to edit the autoscaling.pl file and modify the $dbpath with the complete path of the scaling folder is.
For example, if the downloaded folder is in /home/mypc/Documents/ you will have to modify the $dbpath library inside this perl file to:
   
.. code-block:: SetPath

   $dbpath="/home/mypc/Documents/scaling/";

There are also some python scripts created to verify the profiles results, and verify if all the sequences used in the profile were 
retrieve, so you will also need python.

To install python you can do simply:

.. code-block:: InstallPython

    $ sudo apt-get install python
    
Finally, to create the initial profiles we use clusters and structural alignments and its corresponding sequence alignments. 
To do so we use Mustang.

.. code-block:: InstallMustang
    
    $ sudo apt-get install mustang
    

