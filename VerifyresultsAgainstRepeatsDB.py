import os
import argparse
fromprofile=[]

found=[]

newfound=[]
founddesc=[]
parser = argparse.ArgumentParser(description='ReUPred', usage='xxx')
parser.add_argument('input', nargs=1, default='', help='list containin PDB by default/PDBid and chain --one')
parser.add_argument('input2', nargs=1, default='', help='list containin PDB by default/PDBid and chain --one')
parser.add_argument('work', nargs=1, default='', help='work directory where the targetList is')
parser.add_argument('family', nargs=1, default='', help='work directory where the targetList is')
args = parser.parse_args()
directory = vars(args)['work'][0]
inputfile = vars(args)['input'][0]
inputfile2 = vars(args)['input2'][0]
family = vars(args)['family'][0]
with open(directory+inputfile, 'r') as f:
    proteinList = f.read().split("\n")
for line in proteinList:
    if len(line)>0:
            protline=(line[40:60])
            descline=(line[60:])
            desc=line[60+len(descline.split(" ")[0])+2:]
          
            protein=protline.split(" ")[0].split("_")
            if len(protein[0])>0 and len(protein[1])>0:
                proteinName=(protein[0]+protein[1])
                prot=(proteinName).upper()
                if prot not in found:
                    found.append(prot)
                if desc not in founddesc:
                    founddesc.append(desc)
               
newfounddesc=[]
listado={}
with open(directory+inputfile2, 'r') as f:
    proteinList = f.read().split("\n")
for line in proteinList:
    if len(line)>0:
            protline=(line[40:60])
            descline=(line[60:])
            desc=line[60+len(descline.split(" ")[0])+2:]
            values=line.split()
            protein=protline.split(" ")[0].split("_")
            if len(protein[0])>0 and len(protein[1])>0:
                proteinName=(protein[0]+protein[1])
                prot=(proteinName).upper()
                if prot not in newfound:
                    newfound.append(prot)
                if desc not in newfounddesc:
                    newfounddesc.append(desc)
                    listado[desc]=(values[0],values[6],desc)

with open(directory+family+'.msf', 'r') as f:
    proteinList = f.read().split("\n")
for line in proteinList:
            if len(line)>0:
                info=line.split(" ")  
                if len(info)>2 and "Name:"==info[1]:
                    proteinName=(info[2].split("_"))
                    prot=(proteinName[0]).upper()
                    if prot not in fromprofile:
                        fromprofile.append(prot)


count=0
countnew=0
obtained=[]
cpyFromProfile=fromprofile
for prot in found:
    if prot in fromprofile:
        count=count+1
        if prot in cpyFromProfile:
            cpyFromProfile.remove(prot)
    else:
        if prot not in obtained:
            obtained.append(prot)
            countnew=countnew+1


print("The profile retrieve "+str(countnew)+" protein chains in the search")
print("The missing proteins to retrieve are: "+ str(cpyFromProfile))


count=0
countnew=0
obtained=[]
cpyFromProfile=fromprofile
for prot in newfound:
    if prot in fromprofile:
        count=count+1
        if prot in cpyFromProfile:
            cpyFromProfile.remove(prot)
    else:
        if prot not in obtained:
            obtained.append(prot)
            countnew=countnew+1


print("The autoscaled profile retrieve "+str(countnew)+" protein chains in the search")
print("The missing proteins to retrieve are: "+ str(cpyFromProfile))

for desc in founddesc:
    if desc in newfounddesc:
        newfounddesc.remove(desc)

print("These are the new findings to verify all the details:")
for line in listado:
    print(listado[line])


