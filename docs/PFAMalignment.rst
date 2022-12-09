Obtain a Pfam SEED as Sequence Alignment
========================================

Instead of executing Steps 1, 2 and 3 of the :doc:`CreationProcess`  you can obtain the sequence alignment from PFAM in InterPro.
To do so, go into https://www.ebi.ac.uk/interpro/. you can search the family you want, for example TPR, in the search by text area (second tab).
TPRsearch.png

.. image:: /images/TPRsearch.png

Identify from the Source Database column the PFAM entry or entries in this case the first you will see is PF20169 

https://www.ebi.ac.uk/interpro/entry/pfam/PF20269/

Click alignment as shown in image

.. image:: /images/alignmentlink.png

then click on the menu and choose SEED

.. image:: /images/menu.png

.. image:: /images/seed.png

Then click on the download button that is up right, the downloaded file name would be PF20269.alignement.seed.gz inside this compress file you will find a SEED.ann file.
You need to extract the initial file, then use belvu to open it and save it as msf with the correct name, like PF20269.msf.
After this you are able to continue with the process of creating the profiles :doc:`CreationProcess` :ref:`Profile creation`.

If you do not have belvu installed, just type 

.. code-block::  Install Belvu 

  sudo apt-get install belvu

