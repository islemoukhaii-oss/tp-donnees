def somme_valeurs(liste): return sum(liste)
def nombre_elements(liste): return len(liste)
def valeur_centrale(liste): return liste[2]
def produit(liste):
    s=1
    for i in range(len(liste)):
        s=s*liste[i]
    return s
        
liste=[4,7,2,9,5]
print("somme=",somme_valeurs(liste))
print("nombre=",nombre_elements(liste))
print("valeur",valeur_centrale(liste))
print ("produit",produit(liste))