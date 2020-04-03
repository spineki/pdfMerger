import subprocess
import os

# SI TU VEUX MODIFIER UN TRUC, C EST SEULEMENT LE NOM DU FICHIER FINAL, VARIABLE DOCFINAL
# NE TOUCHE A RIEN D AUTRE!!
#-------------------------------------------------------------------------------------------------
doc_final = "sortie.pdf" # nom document final, le changer si nécessaire
# ------------------------------------------------------------------------------------------------

template = """ gswin64 -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile={0}"""

path = input("entre le dossier contenant le pdf (il seront fusionnés par ordre alphabétique):")

liste_doc_a_fusionner = os.listdir(path)
liste_doc_a_fusionner = [os.path.join(path,doc) for doc in liste_doc_a_fusionner if len(doc)>4 and doc[-3:] == "pdf"]
liste_doc_a_fusionner = sorted(liste_doc_a_fusionner)
print("\n\n\n" , "*" * 20,"\n",  "fichier trouvés, fusionnés dans cet ordre:")
for doc in liste_doc_a_fusionner:
	print(doc)


doc_final = os.path.join(path, doc_final)

script = template.format(doc_final)

for doc in liste_doc_a_fusionner:
	script += " " + doc 
print("\n\n\n" , "*" * 20,"\n")
print("c'est parti mon kiki")
# print("execution du script ", script)

p = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

if p.stdout is not None:
	for line in p.stdout.readlines():
		print (line)

if p.stderr is not None:
	for line in p.stderr.readlines():
		print(line)

retval = p.wait()





input("tape sur 'entrer' pour sortir")
