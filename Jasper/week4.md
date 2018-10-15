#WEEK 4
In week 4 is ingezet op de kade detectie uit te breiden en te optimaliseren.

##Aanpak
Tijdens de sprintplannning hebben we verschillende goals gedefinieerd voor het succesvol behalen van de sprint. De goals waren als volgt:

- De vervorming dankzij de lens verwijderen uit de beelden
- Object specifieke modellen inladen bij de object herkenning
- Persoonlijk portfolio aanvullen
- Kant herkennen op foto bij wall detection algoritme.

##Meeting
In deze meeting is de huidige progressie laten zijn waarbij er enkele tips vanuit CGI en CaptainAI zijn gekomen. CaptainAI is een ander bedrijf dat zich ook bezig houdt met het Floating Lab en met een vergelijkbare opdracht vanuit Port of Rotterdam bezig zijn. Zij hebben de tip gegeven om niet TensorFlow maar Yolo (You only see once) te gebruiken. Dit is namelijk sneller en beter geoptimaliseerd. Ook heeft CaptainAI laten zien wat zij gebruikt hebben om de bolling uit de beelden te halen.


##Wall detection algorithme
Er is gebleken dat het ontworpen algorithme moeite heeft met objecten op het water of schuim. Om ervoor te zorgen dat schuim niet wordt herkend als kant. Ik ben hiervoor op een aantal ideeën. Omdat schuim maar zelden wordt herkend kunen we deze beschrijven als 'outliers'. Het idee is om een lijn te fitten aan deze data, een array maken met kortste afstand tot de lijn vanuit elk punt, hier de standaarddeviatie uit halen en dan vervolgens alle punten weg te halen die zich verder van de lijn bevinden dan een x aantal keer de standaarddeviatie. Vervolgens moet er dan weer een nieuwe lijn geplot worden met de nieuwe array. 


##Objectherkenning
In objectherkenning is deze week een kleine maar toch grote stap gezet. Omdat CaptainAI ons heeft aangeraden Yolov3 te gebruiken in plaats van TensorFlow. Dit betekent dat de moeite die in week 3 is gestopt in het installeren van TensorFlow voor niet was. Dit is een punt wat we van te voren in hadden moeten zien. Hieruit blijkt dat vooronderzoekn dermate belangrijk is dat dat uren werk kan schelen.

##Retrospective
Uit de retrospective kwamen de volgende punten:
- Meer communicatie met CGI. Zo kan de kennis die zij bezitten nuttig gebruikt worden.
- De sprintplanning moet meer gefocusd op wat we willen bereiken zodat we zo productiever kunnen werken.

#feedback michiel
spelling
yolov3 was een keuze gemaakt door CGI (jelmer), niet captain ai. daarnaast maakt yolov3 ook gebruik van tensorflow waarbij cuda etc dus wel handig was om te instaleren