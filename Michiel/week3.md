# Week 3

## Aanpak
Na overleg met de groep is besloten om te werken zonder exact gedefinïeerd einddoel omdat het zeer moeilijk is in te schatten wat voor ons mogelijk is in deze 20 weken. We zullen echter wel tussentijdse doelen stellen.

Er is besloten om te beginnen met de data uit de front-facing camera's. We zullen proberen aan de hand van de beelden, de volgende twee dingen live te bepalen:
- De scheiding tussen water en land.
- Objecten herkennen om de boot heen op het water. 

Wanneer deze doelen zijn behaald kunnen er vervolg stappen gezet worden. 
- Ik zal voornamelijk werken aan object detectie. Uiteraard zal dit niet uitsluitend het geval zijn.

## Projectmeeting CGI (donderdag - Eemshaven)
Donderdag zijn we in de Eemshaven geweest om de boot en de camera's te bekijken. Daarnaast zijn we met alle stakeholders in overleg gegaan over de verdere aanpak van dit project.
De nieuwe aanpak is besloten en goedgekeurd. 

Ons concept voor een land/water herkenning algoritme is gepresenteerd aan de stakeholders, zij vonden het een goed idee. 
Daarnaast is een nieuwe stakeholder geintroduceerd; Captain AI. 


## Onderzoek
### Land/water herkenning
Mogelijkheden hoe bepaald kan worden wat land en wat water is, zijn uitgedacht. (zie presentatie week 3)
- Greyscale: kort python script geschreven samen met Martin om het verschil te bepalen tussen pixelgroepen. Differentiatie in waardes is te klein voor betrouwbare herkenning. Detectie op basis van greyscale is niet mogelijk.
- Euclidian distance: Ik heb naar een oplossing gezocht om de rgb waardes te kunnen vergelijken. De uitkomst is de euclidian distance. Op basis van de euclidian distance kan relatief betrouwbaar het verschil tussen water en land worden herkend.
- Het huidige plan voor land/water herkenning voorziet niet in uitschieters op het water i.v.m. bijvoorbeeld flikkeringen. Ik kwam op het idee om overlappende gebieden te bekijken. Doordat de bekeken gebieden overlappen kun je 'false positives' (bv. flikkeringen of kleine objecten) identificeren en uitsluiten.


### Objectherkenning
ik heb verschillende modellen voor objectherkenning op basis van Tensorflow bekeken, Darknet lijkt de beste en snelste oplossing te bieden.
Andere opties die ik heb bekeken:
- Darkflow
- Retinanet
- Darknet

Hoe en wat heb ik beschreven in ons verslag.

## Datacamp
deadlines behaald

## Andere courses
coursera intro uitgevoerd.

## Feedback
uitleggen wat captain AI is.

Welk verslag bedoel je onder het kopje 'objectherkenning'?
