#!/bin/sh
#!/bin/sh
#This script will allow you to create the msf file, the profile linearly, run the autoscale
# and then create a new profile and run the verification against the results

ruta="/home/lhirsh/Downloads/UpdateRepeatsDB/"
NAME=$1 #alignIV7
echo $NAME

pfw N=2000 $NAME".msf"  > "pfw"$NAME.msf
pfmake -1 "pfw"$NAME".msf" "blosum45.cmp" > $NAME".prf"
pfsearch -f $NAME".prf" $ruta"pdb_seqres.txt" > "output_ali_"$NAME
/home/lhirsh/Documents/scaling/autoscaling.pl $NAME".prf" > "new"$NAME".prf"
pfsearch -f "new"$NAME".prf" $ruta"pdb_seqres.txt" > "outputnew_ali_"$NAME
python3 Verifyresults.py "output_ali_"$NAME "outputnew_ali_"$NAME "/home/lhirsh/Documents/otras_Linear/" $NAME 
