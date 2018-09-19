## Beslissing aanpak SHIP:

Na een grondig overleg op Maandagmorgen is er besloten om niet direct het einddoel van
het project te definiëren, maar in stappen te werken, aangezien het met onze ervaring
niet in te schatten was, wat een realistisch doel is. 

Er is besloten om te beginnen met de camera beelden en de volgende twee dingen live te bepalen:
- De scheiding tussen water en land.
- Objecten herkennen om de boot heen op het water. 

Als dit doel is behaald kunnen er vervolg stappen gezet worden. 
In de groep is er een onderverdeling gemaakt in het werk en iedereen had een eigen taak om uit te voeren
binnen deze scope. 

Port of Rotterdam vroeg ook een agile aanpak waarbij we per doel zouden werken, zodat er 
indien waardevol aanpassingen gemaakt kunnen worden. Aangezien er nog veel informatie ontbrak aan het begin
van het project. 

## Idee algoritme land/water:
Na een tijdje nadenken kreeg ik een idee voor een algoritme om de scheidslijn tussen water en land te bepalen.
Dit idee heb ik besproken met de groep en uiteindelijk hebben we samen een aanpak bepaald.

De camera's zitten vast op de boot, dat betekent dat de boeg altijd op dezelfde plek is in de foto. 
Verder doen we de aanname dat het gebied om de boeg heen altijd water is. Van dit gebied wordt de gemiddelde
pixel waarde genomen. Vervolgens wordt er een algoritme op los gelaten die naar alle kanten berekent of de gemiddelde pixel waarde
hetzelfde blijft of veranderd. Indien de waarde ongeveer hetzelfde blijft, is het water, indien de waarde over een aantal pixels
veranderd, is het geen water, dus land of een object. Om te voorkomen dat boeien als land worden gezien, zal het algoritme altijd even
doorscannen na het vinden van iets dat niet water is. Als de gemiddelde pixel waarde terugkeert naar water, was het een object op het water,
zo niet is het kant. 
    

## Onderzoek algoritme land/water:
Mijn taak was om het onderzoek te starten naar dit algoritme en bestaande concepten te vinden. 
De eerste onderzoeksvraag was op welke manier we de foto zouden analyseren.
Twee voorbeelden hiervan zijn Greyscale en RGB. 

Ik ben begonnen met het gebruiken van Greyscale. Ik heb een random frame gepakt vanuit de data 
en hier gekeken of het zou werken. In het frame op het water lag er een schip en het bleek dat de 
grijswaarde van de zijkant van het schip identiek was aan de grijswaarde van het water. 
Dit werkt, dus niet. Hierna heb ik dezelfde foto geanalyseerd d.m.v. RGB en daar was er wel een duidelijk verschil.

Daar zijn we dus mee verder gegaan. 

## Meeting Port of Rotterdam en CGI:
Ten slotte zijn we op de Donderdag langsgeweest bij de opdrachtgever en hebben we de boot bezocht.
Zeer interessant, we hebben meer informatie verkregen over de mogelijkheden en onze nieuwe aanpak besproken.
Beide partijen waren zeer enthousiast. 

Ik heb het algoritme ook gepresenteerd aan CGI, aangezien hun experts zijn op het gebied van Data Science en hun vonden
het een goed idee. Dat was voor ons ook een belangrijke reden om er mee verder te gaan. 
