# Week 5

## Aanpak
Tijdens de sprintplannning is duidelijk geworden dat de huidige doelen van de vorige sprint worden behouden.

## Onderzoek
###- Objectherkenning:
Ik heb samen met Martin getracht het huidige model van Darknet aan te passen en lichter te maken door onbelangrijke objecten zoals bananen eruit te halen. Het splitsen hiervan lijkt echter moeilijker dan gedacht. Ook samen met Jelmer van CGI kunnen we er niet uit komen.
Is het dan toch beter om een een alternatief te zoeken?
- Keras, en dan specifiek Keras-Retinanet, lijkt de beste oplossing. Dit model is zeer recent uitgebracht en schijnt sneller te zijn dan Darknet. Daarnaast bevind de api zich dichter bij Tensorflow en is het beter aanpasbaar.

###- Land-water
De herkenning werkt naar behoren. Als de kade echter niet recht is, loopt de regressielijn echter niet netjes meer over de kade. We hebben nagedacht over oplossingen hiervoor. 

## Datacamp
deadlines behaald.

## Andere courses
Coursera: Week 2 nog niet af. 

## Feedback
Prima, misschien iets meer bij land-water