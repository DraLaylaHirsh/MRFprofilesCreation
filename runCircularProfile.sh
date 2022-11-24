#!/bin/sh
#This script will allow you to create the msf file, the profile circularly using 2000 iterations, run the autoscale
# and then create a new profile and run the verification against the results

#path is where you locate the database for the pfsearch
path="/home/lhirsh/Downloads/UpdateRepeatsDB/"
#NAME is the name of your msffile
NAME=$1 #alignIV7
#OUTPUTPATH is the path were the results will be saved and all the input data will be, this includes the blosum45
OUTPUTPATH="/home/lhirsh/Documents/otras/"

pfw N=2000 $NAME".msf"  > "pfw"$NAME.msf
pfmake -c "pfw"$NAME".msf" "blosum45.cmp" > $NAME".prf"
pfsearch -f $NAME".prf" $ruta"pdb_seqres.txt" > "searchCircularResults_"$NAME
/home/lhirsh/Documents/scaling/autoscaling.pl $NAME".prf" > "new"$NAME".prf"
pfsearch -f "new"$NAME".prf" $path"pdb_seqres.txt" > "autoscalingsearchResults_"$NAME
python3 Verifyresults.py "searchResults_"$NAME "autoscalingsearchCircularResults_"$NAME $OUTPUTPATH $NAME 
