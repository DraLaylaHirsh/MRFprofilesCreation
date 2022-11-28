#!/bin/sh
#!/bin/sh
#This script will allow you to create the msf file, the profile linearly, run the autoscale
# and then create a new profile and run the verification against the results

#path is where you locate the database for the pfsearch
path="/home/mypc/Downloads/"
#NAME is the name of your msffile
NAME=$1 #alignIV7
#OUTPUTPATH is the path were the results will be saved and all the input data will be, this includes the blosum45
OUTPUTPATH="/home/mypc/Documents/"

pfw N=2000 $NAME".msf"  > "pfw"$NAME.msf
pfmake -1 "pfw"$NAME".msf" "blosum45.cmp" > $NAME".prf"
pfsearch -f $NAME".prf" $path"pdb_seqres.txt" > "searchLinearResults"$NAME
/home/lhirsh/Documents/scaling/autoscaling.pl $NAME".prf" > "new"$NAME".prf"
pfsearch -f "new"$NAME".prf" $path"pdb_seqres.txt" > "autoscalingsearchLinearrResults"$NAME
python3 Verifyresults.py "searchLinearResults"$NAME "autoscalingsearchLinearrResults"$NAME $OUTPUTPATH $NAME 
