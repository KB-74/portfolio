# Week 3

## Aanpak

In deze week hebben we een nieuwe sprindplanning plaatsgevonden. Samen met CGI hebben we besrpoken dat we eerste naar 
object herkenning en het detecteren van water en land op de camera beelden.

## Detectie land en water

In deze week hebben we een idee uitgewerkt voor een algoritme dat water en land zou kunnen onderschijden.
Dit idee hebben we gepitched aan een van de [specialisten van cgi](https://www.linkedin.com/in/jelmer-blok-67482936/?originalSubdomain=nl).
Er werdt positief gereageerd op het concept en vanuit daar zijn we met het analyseren van de beelden. Hiervoor heb ik 2 scripts geschreven
- [RGB waardes uit een afbeelding](job/resoucres/images/Average_Pixel_Value_of_Sample_Image.png), dit script maakt een plot van de individuele rood, groen en blauwe waardes in een afbeelding.
- [Euclidean distance tussen pixel waardes](job/resoucres/images/Euclidean_distance_to_baseline.png), dit script kijkt naar de euclidean distance tussen een bepaalde pixel waarde en de voorafgekozen baseline.

## code structuur

Een goede basis van een code structuur kan er voor zorgen dat de code kwaliteit enorm toeneemt. Het is dus in mijn optiek erg belangrijk om daar vroeg over na te denken. Dat begint bij een project structuur. Na wat expirimenteren ben ik tot de volgende structuur gekomen:
```
/ data
 -- / img
 -- / video
 -- / csv
 enz..
/ model
 -- model_dir (specific to each model)
/ docs
/ tests
/ package (specific to each package)
app.py
```

#Feedback
mis de beschrijving bij codestrutuur. Waarom is dit goed voor jou of waarom is dit goed voor de groep?