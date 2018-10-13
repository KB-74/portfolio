# WEEK 3

## Aanpak

Er heeft een nieuwe sprint planning plaatsgevonden omdat de opdracht duidelijke gedefinieerd was. Daarbij is de aanpak van de opdracht opnieuw besproken.

De aanpak besproken in week 2 bij CGI is aangepast. Samen met Port of Rotterdam is besloten dat er eerst wordt gefocust is op objectherkenning en land/water herkenning. Daarbij is gericht op de deadline van 4 oktober waarbij een demo moet worden gegeven op het Innovation Expo. Daarna willen we kijken wat het volgende aandachtspunt mag zijn. Dat bijvoorbeeld ook verder werken aan objectherkenning zijn.

In week 3 wordt gefocust op het onderzoeken in objectherkenning. Daarbij heeft iedereen TensorFlow geïnstalleerd, wat een grote hoeveelheid tijd heeft gekost.

Er is geprobeerd druk te leggen op Port of Rotterdam om te data te krijgen om zo snel mogelijk aan de gang te gaan met echte beelden. 

Om de voortgang in het project zo efficiënt mogelijk te houden hebben we samen besloten dat Job de structuur van de code opzet en de leiding neemt in het onderhouden hiervan. Ook hebben we besloten dat ik de structuur en vorm van de paper onder leiding zal nemen. Hierbij bouw ik structureel het verslag op zodat er makkelijk en concreet geschreven kan worden.

##Objectherkenning
Er is besloten om te starten met TensorFlow, een library die al werkende objectdetectie heeft. Het plan is om deze te tweaken en dan toe te passen op onze eigen data. Het is gelukt bij iedereen TensorFlow werkend te krijgen en deze uit te voeren. Echter moet er nog veel getweaked worden.

##Kade herkenning 
Er zijn eerste stappen gezetin het schrijven van code waarbij de eerste 'pixel_walker' is ontstaan. Deze schiet een aantal lijnen over de frame heen die zoekt naar een verschil in kleur. Als dit gevonden wordt wordt dit punt opgeslagen. Zo ontstaat er een array aan punten die de kade aan zouden moeten geven. 

Zelf heb ik mij hierbij ingezet om de start locatie van de lijnen op de juiste plek om de boot te fitten en een lijn te trekken door de gevonden punten. Zo kan de kade worden aangegeven met een lijn wat dus overzichtelijker is.

##Zelfontplooiing
Doormiddel van datacamp is kennis opgedaan over flat files en het aanpassen van plots. Daarnaast is de eerste stap gezet in machine learning d.m.v. de Stanford Universtiy course op Coursera en college van dhr. Vuurens.
