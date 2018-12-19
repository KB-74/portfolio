# WEEK 1
In dit hoofdstuk staat samengevat wat ik tijdens de eerste week van dit project heb gedaan.
#####27-08-2018 t/m 31-08-2018 (Sprint 1)

## Minorkeuze: Applied data science
Tijdens mijn stage heb ik kennis mogen maken met het programmeren. Het beheersen van een programmeer taal
zie ik als een vaardigheid waarbij je complexe problemen kan oplossen met beperkte middelen in een beperkte tijd.
Tijdens mijn opleiding (werktuigbouwkunde) komt dit niet aan de orde, daarom heb ik gekozen voor een minor in de
richting van programmeren.

De minor Applied Data Science lijkt me een uitdagende manier om zelf te leren programmeren en daarnaast kennis 
op te doen van programmeren in een groep.

## Projectkeuze: SHIP
Aan het begin van week 1 werden we genoodzaakt een keuze te maken uit een zes tal verschillende projecten. Het project
Waar mijn voorkeur naar uit gaat was het project autonomous shipping. Dit leek mij erg uitdagend om de volgende redenen:
- Meest passend bij mijn studie (werktuigbouwkunde).
- Mijn intresse in scheepsvaart
- Opdracht waarbij er veel contact is met de project owner [Port of Rotterdam](https://www.portofrotterdam.com/nl)
- Samenwerking met consultant [CGI](https://www.cginederland.nl/)


## Werkwijze
De eerste week van deze minor bestond uit het kennis maken en beslissen van het project (benoemd in projectkeuze parograaf) waarin je je het komende half jaar 
gaat verdiepen. Daarnaast werd er veel toelichting geven over de verschillende tools, deadlines en verplichtingen van de minor.

### Tools
Voor het project hebben we als groep een aantal verschillende tools en programma's nodig. 
Deze tools helpen ons met onderdelen zoals communicatie of het vervaardigen van een product. De volgende programma's
en of tools hebben we daarom geinstalleerd:

####Benodigdheiden

- [GitHub](https://github.com/kb-74) (publieke groep)
- [GitHub](https://github.com/jobvink/wall_detection) (prive groep)
- [GitHub](https://github.com/JelteMolenaar)(persoonlijk)
- [Google group](ship2018@googlegroups.com)
- [Scrumwise](https://www.scrumwise.com/scrum/#/backlog/project/kb74-2018-autonomous-shipping/)
- [ShareLatex](https://www.sharelatex.com/) 

####Ontwikkeling

- [DataCamp](https://www.datacamp.com/)
- [Coursera](https://www.coursera.org/learn/machine-learning/home/welcome)

####Installatie

- [PyCharm](https://www.jetbrains.com/pycharm/)
- [MATLAB](https://www.mathworks.com/)


### Scrum
Met de project aanpak methode van scrum focussen we ons op een daadwerkelijk werkend product en minder op documentatie.
Het bijhouden en schrijven van documentatie kost vaak veel tijd in projecten en gaat ten kosten van de kwaliteit en kwantiteit
van het eindproduct. De Scrum aanpak komt oorspronkelijk uit de ICT-sector, en past goed bij het project wat we op dit 
moment uitvoeren. Bij het scrum proces staan 4 regels centraal:
1. Individu en interactie staat boven het proces en de tools. 
2. Working product over uitgebreide documentatie.
3. Samenwerken met klanten over onderhandelingscontracten.
4. Verandering van een voorafgesteld plan.


## Ontwikkeling
Elke week (in het begin) wordt er vanuit de minor verwacht dat er bepaalde zelfstudie wordt gedaan. 
Hieronder staan de eerste onderdelen die behaalt zijn in week 1. 

### Datacamp
De volgende courses en chapters heb ik succesvol afgerond deze week:
- Intro to Python for Data Science

# WEEK 2
Tijdens de tweede week stond het kennis maken met het ondwerp centraal. Dit hebben we als groep gedaan 
door een aantal meetings tijdens de week te houden. 

#####03-09-2018 t/m 07-09-2018 (sprint 2) 

## Sprintplanning | 03-09-2018
Dit was de eerste meeting die we als groep hadden. Aangezien ik tijdens mijn werk veel scrummeetings facaliteer 
(sprintplanning en retrospectief) heb ik de rol als Scrum-master opgepakt. Hierbij voelde ik de verantwoordelijkheid 
om de groep te begeleiden naar een stabiel systeem op de lange termijn. Tijdens de sprintplanning kwamen de volgende doelen naar voren:
- Opstellen van plan van aanpak (opstellen van doelen) 

## Kick-off meeting / Smash event | 04-09-2018
De kick-off van het project vondt plaatst in het hoofdkantoor van port of rotterdam. Hierbij waren Port of Rotterdam, CGI 
en wij aanwezig. Tijdens deze meeting werd er kennis gemaakt met de partijen die betrokken zijn bij het project.
Na afloop zijn we met de groep naar het SMASH smart shipping event in Amsterdam geweest. Hier zijn we helemaal 
bijgepraat op het onderwerp van smart shipping.


## Projectmeeting CGI |  06-09-2018
Na de kickoff bij port of rotterdam was er een meeting bij CGI. Tijdens deze meeting kregen wij een 
uitleg over machine learning. Daarna zijn we verder gegaan met het maken van het algorithme.


## Ontwikkeling
Deze week was er minder tijd voor het zelfstandig studeren. Desalniettemin zijn de volgende dingen behaalt:

### Datacamp
De volgende courses en chapters heb ik succesvol afgerond deze week:
- Intermediate Python for Data Science
- Customizing plots
- Introduction and flat files

# WEEK 3

#####10-09-2018 t/m 17-09-2018 (sprint 2) 
##Sprintplanning | 10-09-2018
Tijdens de sprintplanning hebben we een aantal doelen opgesteld. Deze doelen waren als volgt:
- Maken van rand/water detectie algorithme
- Herkennen van objecten
- Behalen van courses en chapters op Datacamp

##Verantwoordelijkheiden
Tijdens deze sprint hebben we de groep verdeelt in een object herkenning en een land/water herkenning groep
Ik zat bij de groep zich focusten op het herkennen van land/water.

###Rand Herekening
Deze sprint heb ik mij gefocust op het herkennen van randen en het bewerken van afbeeldingen. Hiervoor moest ik
eerst een afbeelding inladen in Python. Daarna was het mogelijk om een edge-detection filter toe te passen op de foto.
Dit werkte redelijk maar had als groot nadeel dat ook de golven en de weerspiegeling in het water gezien werd als rand. 
Op dit moment gaan we niet verder met edge-detection omdat het te veel false positives geeft. <br/>
Naast edge detection heb ik ook gekenen naar het bewerken van de foto's. Met het bewerken van de foto's
wordt bedoelt: het veranderen van Brightness, contrast, contour en het uitknippen van een bepaalt
gedeelte van de foto. De combinatie van het verhogen van de Brightness en het edge-dection filter was possitief. Hierdoor werden
minder false positives ontdekt. [pixel_walker_edge_detection_v3](https://github.com/jobvink/wall_detection/blob/master/pixel_walker_edge_detection_v3.py)

##Ontwikkeling
Zoals voorgaande weken heb ik ook deze week ook gewerkt aan het vergroten van van
mijn eigen vaardigheiden in Python (met Datacamp), daarnaast ben ik begonnen
aan de machine learning course van Standford.

###Datacamp
De volgende courses en chapters heb ik succesvol afgerond deze week:
- Writing your own functions
- Data ingestion & inspection
- Exploratory data analysis

###Coursera
In week 3 ben ik begonnen aan de machine learning course 
van Standford University. Deze course heb ik half
afgerond. Dit bevatten de volgende onderdelen:
- Introduction to machine learning (+review)
- Linear Regression with One Variable
    - Model and Cost Function
    - Parameter Learning
    
####Feedback

Waarom heb je die beeldbewerking nodig bij edge detection?
 Leg dit uit. Nice dat je uitlegt wat je allemaal hebt gedaan in datacamp en coursera.
 
# WEEK 4
 
#####17-09-2018 t/m 21-09-2018 (sprint4)

## Sprintplanning
Tijdens de sprintplannning hebben we verschillende goals gedefinieerd voor
het succesvol behalen van de sprint. De goals waren als volgt:
- Caliberen van de camera's (verwijderen van fisheye)
- Object specifieke modellen inladen bij de object herkenning
- Persoonlijk portfolio aanvullen
- Kant herkennen op foto bij wall detection algorithme. 
###Verantwoordelijkheid
Tijdens deze sprint lag mijn verantwoorelijkheid bij het herkennen van de randen.

###Rand Herkenning
Vorige week heb ik gekenen naar het bewerken van de foto's (toevoegen van filters). deze week heb ik geprobeerd om
de edge-detection te combineren met de al bestaande pixel walker software. Dit is hier te zien: [pixel_walker_edge_detection_v4](https://github.com/jobvink/wall_detection/blob/master/pixel_walker_edge_detection_v4.py)

##Retrospective 
tijdens de retrospective kwamen een aantal punten naar voren die we als groep kunnen gebruiken om beter 
te presteren of te worden:
- Meer comminucatie met CGI.
- Sprintplanning meer te focussen op wat we willen bereiken.
- Productiever proberen te werken.

##Ontwikkeling
Net zoals voorgaande weken heb ik de volgende ontwikkelingen mee gemaakt:

### Datacamp
De volgende courses en chapters heb ik succesvol afgerond deze week:
- Python Data Science Toolbox (Part 2)
- Plotting 2D arrays
- Statistical plots with Seaborn

### Coursera
In week 4 heb ik gewerkt aan de machine learning course 
van Standford University week 1. Deze course heb ik half
afgerond. Dit bevatten de volgende onderdelen:
- linear Algebra Review
    - Linear Algebra 
    - Matrices and Vectors
    - Matrix multiplication
    - Inverse and transpose Matrices

# WEEK 5

#####24-09-2018 t/m 28-09-2018 (sprint3)

##Sprintplanning
Tijdens de sprintplannning hebben we verschillende goals gedefinieerd voor
het succesvol behalen van de sprint. De goals waren als volgt:
- Kaliberen van de camera's (verwijderen van fisheye vervorming)
- Object specifieke modellen inladen bij de object herkenning
- Persoonlijk portfolio aanvullen
- Kant herkennen op foto bij wall detection algorithme

### Verantwoordelijkheiden
Tijdens deze sprint heb ik me met name gefocust op het onderzoek naar HSV. 

### Onderzoek RGB HSV.
Op dit moment wordt bij ons algorithm gekene naar de kleur van elke pixel. Deze kleur wordt in een RGB waarde opgeslagen.
Naar aanleiding van de feedback van de demo van de week ervoor hebben we gekenen naar een andere manier van het opslaan van de
waarde van de kleur van een pixel. Hieruit bleek dat het handig is om HSV kleuren te gebruiken omdat hierbij minder variabelen
zijn die van invloed zijn voor het weergeven van een kleur. Uiteindelijk is het me nog niet gelukt om dit 
in te voegen in de code
[Onderzoek Detectiemethode kleuren](bijlage/Detectiemethode%20kleuren.pdf)

## Retrospective
Tijdens de retrospective hebben we de volgende punten besproken:
- Hoe zorgen we dat iedereen elkaars code blijft begrijpen
- Zorgen dat we allemaal op dezelfde dag aanwezig (of afwezig) zijn.

## Ontwikkeling
Zoals voorgaande weken heb ik ook deze week ook gewerkt aan het vergroten van van
mijn eigen vaardigheiden in Python (met Datacamp), daarnaast ben ik verder gegaan aan de machine learning course van Standford.

### Datacamp
Deze week heb ik de volgende chapters succesvol afgerond:
- Cleaning Data in Python

### Coursera
In week 5 heb ik gewerkt aan de machine learning course 
van Standford University week 2. Tijdens de tweede week van de course werd er ingegaan op het implementeren 
van de vorafgaande onderdelen in MATLAB/Octave. Ik heb tijdens deze week
de volgende onderdelen geleerd:
- InstallereAn MATLAB en Ocatave
- Multivariate Linear Regression
- Computing Parameters Analytically
- Submitting Programming Assignments
- Octave/Mathlab Tutorial
    - [Programming Assignment (ex1)](https://github.com/JelteMolenaar/machine_learning_standford_university/tree/master/ex1_(week2))
    

####Feedback
Leg bij de sprint planning (in elke week) uit waarom we deze goals hebben gekozen. De link bij onderzoek RGB/HSV werkt nog niet. Leg bij de retrospective uit (elke week) hoe we dit gaan verbeteren en waarom dit problemen zijn.

#Week 6

#####01-10-2018 t/m 05-10-2018 (sprint4)

##Sprintplanning | 01-10-2018
Net zoals voorgaande weken faciliteerde ik de sprintplanning. Tijdens deze sprintplanning 
(sprint 4) hebben we als groep 4 verschillende doelen opgesteld die tijdens deze sprint 
behaald gaan worden. 
1. Onderzoek doen naar het gebruik van een filter om schittering uit het water te halen
2. Bijwerken van portfolio t/m week 6 -> gebruik makend van peer feedback op vrijdag
3. Opstellen van het onderzoeks hoofdstuk in de 
4. Voorbereiding op Innovation Expo Day 2018.

###Verantwoordelijkheiden
Net zoals voorgaande weken facaliteerde ik de sprintplanning. Mijn verantwoordelijkheid
tijdens deze sprint is:
1. Voorbereiden van Innovation Expo Day 2018 [presentatie](bijlage/presentation_innovation_expo_day.pdf)
2. Opstellen van Detectie methode hoofdstuk van het paper. [paper](link)

###Innovation Expo Day | 04-10-2018
De Expo dag was de eerste grote deadline voor het project Smart Shipping. Bij dit event waren veel bedrijven aanwezig 
uit verschillende sectoren. Als groep moesten we laten zien wat we tot nu toe bereikt hebben en waar we in de toekomst
naar toe willen. [Port of Rotterdam](https://www.portofrotterdam.com/nl/nieuws-en-persberichten/havenbedrijf-rotterdam-beproeft-autonoom-varen-met-drijvend-laboratorium)

##Backlog refinement | 05-10-2018
Na het behalen van de innovatie dag deadline (4 okt) was het noodzakelijk om te kijken wat we in de toekomst willen bereiken.
Hiervoor heb ik een backlog refinement meeting georganiseerd. Met deze meeting geeft iedereen evenveel input
en worden er uiteindelijk doelen bepaalt. De demo die we uiteindelijk willen geven is een scherm met daarop een kaart
waar het schip wel of niet kan varen. 

##Ontwikkeling
Zoals elke week heb ik ook gewerkt aan het ontwikkelen van mijn kennis in python en op het gebied van data science.

### DataCamp
De volgende courses en chapters heb ik succesvol afgerond deze week:
- Statistical Thinking in Python (Part 1)
- Supervised Learning with scikit-learn

### Coursera
In week 6 heb ik de derde week van Coursera afgerond
  - Classification and Representation
  - Logistic Regression model
  - Multiclass Classification
  - Solving the Problem of Overfitting
  - Review
    - [Programming Assignment (ex1) python version]()
    - [Programming Assignment (ex2)](https://github.com/JelteMolenaar/machine_learning_standford_university/tree/master/ex2_(week3))
    
####Feedback
Links werken nog niet.


#Week 7

#####08-10-2018 t/m 12-10-2018 (sprint 4)

##Sprintplanning


### Coursera
In week 7 ben ik begonnen aan de vierde wek van coursera. hierbij heb ik de volgende onderdelen afgemaakt:
 - Motivations
 - Neural networks 