import dog_related_classes

arya = dog_related_classes.Dog('wags her tail')
poe = dog_related_classes.Dog('pees a lot')
daisy = dog_related_classes.Dog('is super big and adorable')

print(arya.value)


the_puppy_brigade = dog_related_classes.LinkedDogs(arya)
the_puppy_brigade.append(poe)
the_puppy_brigade.append(daisy)

#print(the_puppy_brigade)
