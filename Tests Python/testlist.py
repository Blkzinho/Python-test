#==================================================================================================================
# Structure de données
#==================================================================================================================
# Ensemble de donnée ordonée


#Listes
liste_1= [1,2,3,20,35,6,4,78,99,100]
villes= ['Paris','Londres','Bruxelles','Berlin']
liste_2= [liste_1,villes]
liste_3=[]

#Tuples
tuple_1 = (1,2,3,4,5,6) # pas modifiable mais plus rapide

#string ( chaine de caracter )
prenom = 'Fabio' 


#Utilisation indexing
print(villes[0]) #Premier element
print(villes[1]) #Deuxieme element
print(villes[-1]) #Dernier element
print(villes[-2]) #Avant derniere element

#Utilisation slicing
print(liste_1[0:-1:2]) #Liste [ debut:fin:pas]
print(tuple_1[3])


