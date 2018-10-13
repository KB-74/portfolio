#WEEK 5
In deze week is door mij veel gewerkt aan de code en daarmee ook voortgang gemaakt op het gebied van filtering.

##Aanpak
Tijdens de sprintplannning in week 4 hebben we verschillende goals gedefinieerd voor het succesvol behalen van de sprint. De goals waren als volgt:

- De vervorming dankzij de lens verwijderen uit de beelden
- Object specifieke modellen inladen bij de object herkenning
- Persoonlijk portfolio aanvullen
- Kant herkennen op foto bij wall detection algorithme.

##Meeting
Om de vervorming uit de beelden te halen is gevraagd aan Port of Rotterdam of zij beelden kunnen leveren voor de kalibratie. Er is eerder een kalibratiebord langs de camera's gehaald om de vervorming op te meten door CaptainAI. Deze beelden hebben wij daar vervolgens voor gebruikt.

#Oplossing outliers probleem
Er zijn verscheidene methodes bedacht om outliers te verwijderen, de een beter dan de andere:
- STD-Filtering: 'Standaardeviatie-filtering'. Dit is hetzelfde algorithme dat in week 4 is toegelicht. Hierbij wordt er gekeken naar de variatie in de punten ten opzichte van een lineaire fit. Als de afstand tot deze fit groter is dan een x aantal keer de standaarddeviatie wordt dit punt verwijderd. Met de nieuwe array aan punten wordt opnieuwe gefit en dit is de nieuwe kantlijn.
- Hoek-filtering: Hierbij wordt gekeken naar de hoek binnen het driedimensionale HSV of RGB velden ten opzichte van een vast punt binnen deze velden. Het vast punt is dan bijvoorbeeld wit omdat dit de kleur van het schuim is.
- Afstand-filtering: Vergelijkbaar met de STD-filtering methode wordt hierbij gekeken naar fit van de gevonden punten binnen het RGB of HSV veld waarbij er een fit wordt gemaakt binnen dit veld. Ook hierbij wordt gekeken naar de afstand tot deze lijn. Als dit te groot is wordt het punt verwijderd.

###Toepassing
- STD-filtering: Uit tests is gebleken dat STD-filtering zeer toepasbaar is en ook zeer goed werkt. De grootste outliers worden hiermee verwijderd wat een stuk betere dataset creëerd.
- Hoek-filtering: Na visualisatie van waar de gevonden punten liggen binnen een HSV of RGB veld blijkt dat deze niet als een klomp samen liggen zoals gedacht maar ongeveer op een lijn. Dat maakt deze methode niet toepasbaar omdat dit veel true positives zou verwijderen.
- Afstand-filtering: Hiermee is nog weinig getest en dit is daarom nog een mogelijkheid die openstaat. Wel is duidelijk dat de toepassing van dit filter erg moeilijk is om te maken.

## Retrospective
Uit de retrospective is gebleken dat: 
- Het belangrijk is om elkaars code te blijven begrijpen. Daarmee is de afspraak gemaakt om na de daily stand-up een moment te hebben voor code-presentatie voor als er iets nieuws it toegevoegd.
- Dat we op dezelfde dagen aanwezig zijn. Er werken veel uit onze groep en dat betekent dat veel één dag per week afwezig zijn. Het plan is om deze afwezigheid dan zoveel mogelijk op dinsdag te plannen.

#Zelfontplooiing

Verdere stappen zijn gemaakt in Datacamp volgens planning. Coursera is niet aan verder gewerkt i.v.m. de grote hoeveelheid werk aan de code.