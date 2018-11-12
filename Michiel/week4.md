# Week 4

## Aanpak
Tijdens de sprintplannning zijn de volgende goals gedefinieerd:
- Kalibreren van de camera's (verwijderen van fisheye)
- Object specifieke modellen inladen bij de object herkenning
- Persoonlijk portfolio aanvullen
- Kant herkennen op foto bij wall detection algoritme. 

 
## Projectmeeting CGI (donderdag)
Zoals de andere weken hebben we een meeting gehad met CGI, hier is onze huidige voortgang besproken. Voor ons als groep had deze helaas weinig toegevoegde waarde gezien CGI geen oplossingen kan bieden voor problemen waar we momenteel tegen aan lopen. Zo lukt het hen ook niet om de Darknet modellen te splitsen.

## Onderzoek
###- Objectherkenning:
Gezien de problemen waar ik tegenaan loop met het compilen en werkend krijgen van Darknet, heb ik Ubuntu geinstalleerd.
Darknet live detectie van webcam werkt (op laptop echter met zogenaamd 'tiny-model' omdat normale weights te zwaar zijn voor mijn GPU), op de server kan ik het helaas niet werkend krijgen. Online worden verschillende oplossingen aangeboden zoals python wrappers, deze lijken echter niet te werken.
Lokaal werkt darknet image detectie echter naar behoren (sommige schepen niet herkend in zeer drukke plaatjes, dit mogelijk door gebruik van het kleine weights model).

Op de server krijg ik Darknet niet werkend op videobeelden. Ik loop tegen problemen aan met OpenCV. Gezien de geprobeerde oplossingen moet er misschien naar een ander model worden gekeken.

###- Land-water
land/ water herkenning uitgedacht (hoe te programeren, euclidian distance, greyscaling onderzocht en besloten dat het 
niet duidelijk genoeg is.)

## Datacamp
deadlines behaald

## Andere courses
coursera week 1 behaald

## Feedback
wat voor model? (Laatste regel objectherkenning)
Land-water potentieel iets beter uitwerken?
