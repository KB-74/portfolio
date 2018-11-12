## planning
Aan het begin van de week hadden we weer een sprintplanning, hier hebben we gedetaileerder gekeken naar de weg
die we in wilde slaan voor het maken van een algoritme voor kade herkenning op basis van een convolutional network

We hebben bedacht dat we delen van ons bestaande algoritme konden gebruiken om de gelabelde data te genereren voor het neural network.
We willen alle frames van de 15 minuten film die we hebben door het bestaande algoritme duwen, vervolgens willen we deze checken
en de frames zie niet goed gedetecteerd zijn willen we vervolgens alsnog handmatig labelen.

## labaling tool
Om data te labelen op afbeeldingen hebben we een klein script geschreven waarmee we aan kunnen geven waar de kade zich bevind op
een frame van de camera en waar het water zich bevind.
