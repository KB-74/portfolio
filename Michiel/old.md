# Week 1

## Projectkeuze SHIP:

Mijn keuze voor het project SHIP is gebaseerd op onderstaande redenen:
- SHIP sprak erg tot de verbeelding door de huidige technologische voortgang op het gebied van autonome producten.
- Om ervaring op te doen in en het leren van programmeren met python.
- Ervaring op doen in het gebied van objectherkenning en machine learning

## Aanpak
Hoewel het onderwerp was gepresenteerd, was er over de opdracht nog weinig duidelijk. De doelstelling voor de eerste week was dan ook om de opdracht duidelijk te krijgen.

Er is besloten één contactpersoon aan te stellen voor communicatie tussen onze groep (SHIP) en de andere stakeholders; CGI en Port of Rotterdam.

Daarnaast is een Plan van Aanpak opgesteld en een opdracht gedefinieerd om richting aan ons project te geven.

## Tools en opzet
Er is besloten gebruik te maken van onderstaande tools:
1. Pycharm
2. Anaconda
3. Python 3.6
4. Github
5. Onedrive
6. Scrumwise
7. Sharelatex
8. Googlegroup (email en kalender)
9. Zed (stereocamera)

## Onderzoek project:

Om onszelf en de groep op de hoogte te krijgen van de huidige mogelijkheden, is er vooral onderzoek uitgevoerd naar de technieken die beschikbaar zijn voor objectherkenning en afstandsbepaling aan de hand van stereocameras.
De gevonden onderzoeken zijn doorgenomen en de belangrijke punten medegedeeld aan de groep.

- objectherkenning:
Tensorflow biedt verregaande mogelijkheden voor objectherkenning.

- Afstandbepaling
Door de beelden van de stereocameras te vergelijken kan de afstand van objecten worden bepaald aan de hand van het verschil in het aantal pixels dat de beelden van elkaar afwijken.

## Scrum
Ik was zelf compleet onbekend met de SCRUM-methode. Om deze reden heb ik mij ingelezen in scrum in de aanloop naar de workshop. Dankzij de workshop is het concept en de aanpak van Scrum duidelijk geworden.

Q & A

Mijn vraag betrof het verschil tussen een projectleider en een Scrum master.

Het verschil zit hem in de verantwoordelijkheden. Zo heeft een Scrum master slechts een deel van de verantwoordelijkheden van een projectleider.

Agilemanifesto
SCRUM opereert via dezelfde waarden als het Agilemanifesto. Door openheid wederzijds respect en de focus op een sprint, ook als de doelen veranderen, betekend dat de waarden van het Agilemanifesto en SCRUM overeenkomen.
	
## DataCamp:
De Assignments pagina had ik nog niet gezien. Ik heb de course van week 1 wel doorgenomen, maar een paar opdrachten overgeslagen i.v.m. bestaande kennis.


# Week 2

## Aanpak
Er is deze week een kick-off meeting gepland met de huidige stakeholders om onze opdracht te definiëren. Daarnaast is er ook op dinsdag een SMASH-event om in contact te komen met anderen die zich bezighouden met smart shipping, en voor donderdag een meeting bij CGI om de teams beter te leren kennen.

Gezien het feit dat we op maandag nog geen concrete informatie hadden omtrent de opdracht, is de sprint planning ingevuld op basis van de in week 1 opgestelde doelstellingen.

## Kick-off meeting (dinsdag ochtend)
De eerste meeting met alle stakeholders van 'floating lab' heeft plaatsgevonden bij port of Rotterdam.

De gegeven presentatie heeft inzicht geboden over het 'floating lab' en de rol die wij hierbinnen kunnen spelen.
De werkwijze en mogelijkheden tot communicatie zijn vastgesteld en vastgelegd. De bedoeling is dat er 'Agile' wordt gewerkt.
 
De opdracht zelf is niet gedefinieerd. Port of Rotterdam geeft echter aan dat dat ze verschillende mogelijkheden zien en dat we er zelf over na mogen denken.

Op basis van deze meeting hebben we een lijst opgesteld ingedeeld op basis van prioriteit, met mogelijke deelprojecten.


## SMASH event (dinsdag middag)
SMASH (Smart shipping event) was een event georganiseerd georganiseerd door Rijkswaterstaat. 
Het doel van SMASH was om alle gaande projecten die te maken hebben met 'smart shipping' in kaart te brengen en de verschillende partijen te introduceren aan de deelnemers. Hiermee wil Rijkswaterstaat zogenaamde acties opzetten om de voortgang in Smart Shipping in Nederland te versnellen. 

Hoewel dit event zelf voor ons als studenten, weinig toegevoerde waarde boodt, weten we wel wat er mogelijk is, en wat er al wordt uitgevoerd.

## Projectmeeting CGI (donderdag)
Bij de meeting bij CGI zijn onze plannen besproken en goedgekeurd.

Onze plannen:
- Alle beschikbare data van floating lab verzamelen en ordenen en opschonen. 
- Objectherkenning uitwerken en testen.
- combineren radar en map voor wederzijdse verificatie

## Onderzoek
Tensorflow (objectherkenning):
- Cuda geinstalleerd
- Cudnn geinstalleerd
- OpenCV geinstalleerd

Het eerste object is succesvol herkend op basis van reeds bestaande weights.
Tensorflow herkent succesvol mijn schoen.



## Datacamp
deadlines behaald.

## Feedback
Leg 'floating lab' en 'agile' uit als je het tussen haakjes zet.

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

# Week 6

## Aanpak
Deze sprint zal qua doelstellingen anders worden ingedeeld dan voorgaande weken.
Zo is deze sprint gefocust op het verslag en ons portfolio. De verscheidene bestandsdelen van ons onderzoek zijn verdeeld. Ik zal een stuk schrijven over objectherkenning.

## Innovation Expo (donderdag)
De Innovation Expo op 4 oktober was niet alleen een moment om onze voortgang te laten zien, het was ook een deadline omdat we bepaalde demo's moesten kunnen tonen.
Dankzij de expodag hebben we vele bedrijven kunnen spreken die input konden leveren op ons project. Zo kunnen we in de nabije toekomst rekenen op samenwerking met verscheidene partijen zoals Captain AI.

Meer info over ons project en de innovation expo is te vinden op de site van 
[Port of Rotterdam](https://www.portofrotterdam.com/nl/nieuws-en-persberichten/havenbedrijf-rotterdam-beproeft-autonoom-varen-met-drijvend-laboratorium)

## Onderzoek
###- Objectherkenning:
Het is duidelijk geworden dat Darknet voor ons een onhandig model is om te blijven gebruiken. Zo lijken low level modificaties moeilijk en blijft het een questie van het oplossen van de ene error die tot een andere leidt.

Keras daarentegen is gemakkelijk werkend gekregen. Met behulp van Job zijn de eerste stappen hierin gezet. Zo is er een demo gerendered die relatief zeer accuraat weergeeft wat wat is.

###- Land-water
Op het gebied van land-water herkenning is weinig voortgang geboekt. Zo heeft het nieuwe uitgedachte waaier model die aan de hand van een heatmap de outliers eruitpakt moeite met het vinden van de kant.

## Datacamp
deadlines behaald, Datacamp is nu afgerond. Mijn kennis van Python heeft dankzij deze course een grote vooruitgang geboekt.

## Andere courses
Coursera: Coursera is ook deze week weer een doorn in het oog. De filmpjes zijn interessant, maar ook zeer langdradig. Net zoals voorgaande weken maak ik mezelf wijs dat ik dit in het weekend even bijwerk.

## Feedback
Wat zijn 'bepaalde' demos? Onder innovation expo

# Week 7

## Aanpak
Deze week zal voornamelijk gefocust worden op ons paper. De opdrachten zijn verdeeld.
Daarnaast zal ik samen met martin een tooltje maken om gemakkelijk de kust te labelen in verscheidene frames.

## Havenbedrijf Rotterdam (donderdag)
Op donderdag zijn we bij het havenbedrijf Rotterdam geweest. We hebben een korte demo gegeven en overlegd over de voortgang van ons project. Havenbedrijf Rotterdam is er goed over te spreken. 

## Onderzoek
###- Objectherkenning:
Geen voortgang

###- Land-water
De opstart voor het tooltje om de kustlijn de labelen gaat gestaag. Ik heb een gemakkelijke module gevonden om input van zowel de muis als het keyboard te monitoren. Het plan is om dit in een csv bestand te zetten en vervolgens met een ander scriptje automatisch d.m.v bepaalde keystrokes te labelen welke coördinaten bij de kust horen.


## Andere courses
Coursera week 2 af
Coursera week 3 vergevorderd

## Feedback
Opzich prima, wel weinig tekst dichtheid