
# Persoonlijk portfolio  
Persoonlijke portfolio voor de minor Applied Data Science aan de Haagse Hogeschool.    
  
|                   |                   |  
| ---               | ---               |  
| Naam:             | <b>Jasper Vlaar</b>      |  
| Studentnummer:    | <b>16016149</b>          |  
| Groep:            | <b>KB-74 Shipping</b>    |  
| Begeleider:       | <b>H. Benne</b>          |  
  
## Inhoudsopgave  
|                 |                   |  
|------           |:------            |  
|<b>Hoofdstuk</b>|<b>Code</b>| |[Introductie](#Introductie)               | - |  
|[Courses](#Courses)                       | - |  
|[Domain Knowledge](#Domain-Knowledge)     | - |  
|[Predictive Models](#Predictive-models)   | [pixel_walker_v5](pixel_walker_v5.py)|  
|[Data Collection](#Data-collection)       | -  |  
|[Data Preparation](#Data-preparation)     | [pixel_walker_v6](pixel_walker_v6.py), [pixel_walker_v8](pixel_walker_v8.py)  |  
|[Data Visualization](#Data-Visualization) | - |  
|[Evaluation and Diagnostics](#Evaluation-and-diagnostics)                 | [hyperparameter_evaluation](hyperparameter_evaluation.py) |  
|[Communication](#Communication)           | - |  
  
## Introductie  
Het Floating Lab van Port of Rotterdam biedt een interesant en divers project. Met gebruik van data kunnen veel innoverende projecten op dit Lab uitgevoerd worden. Juist vanwege de diversiteit en mogelijkheid tot innovatie heb ik dit project gekozen. Het heeft ons de mogelijkheid geboden om vaardigheden in zowel programmeren en data science als communicatie en presenteren op te doen.   
  
Wij hebben gekozen om binnen het kader autonoom varen te werken aan kadeherkenning in een maritieme omgeving met gebruik van camera's.  
  
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/RPA3.jpg"></p>  
  
## Courses  
Voor deze minor heb ik al een stuk data-analyse uitgevoerd bij mijn bachelor technische natuurkunde. Deze kennis heb ik mede dankzij datacamp ruim uitgebreid. Ik heb de volgende courses in datacamp voltooid:  
  
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Completed_Courses_datacamp.png"></p>  
  
Alle voorgeschreven datacamp courses en chapters zijn uitgevoerd. Dit geldt ook voor Coursera zoals te zien is in de volgende figuur:  
  
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Completed_Courses_coursera.png"></p>  
  
## Domain Knowledge  
Op het gebied van smart shipping zijn velen partijen bezig. Ook volledig autonoom varen worden actief stappen in gezet. Echter leveren wij nieuwe openbare kennis op het gebied van kadeherkenning. Soortgelijke datasets zijn makkelijk te vinden op YouTube en andere deelplatformen, de toepassing is echter uniek. Domeinkennis is opgedaan dankzij de samenwerking met Port of Rotterdam en CGI. Daarnaast kan voor een referentie voor domeinkennis van machine learning gekeken worden naar het behaalde cijfer voor het tentamen (7,6).   
  
## Predictive models  
  
Conceptueel heb ik meegedacht met de eerste versies van de 'pixel walker'. Dit script schiet lijnen uit die RGB waardes vergelijkt met betrekking van de Euclidian Distance. Daarnaast heb ik ook bijgedragen aan wiskunde concepten die nodig zijn om het script te schrijven zoals cirkelgeometrie.  
  
[pixel_walker_v5](pixel_walker_v5.py)  
  
  
## Data collection  
Alle kale data is aangeleverd door Port of Rotterdam. Er is ook geen extra data collection uitgevoerd.  
  
## Data preparation  

  <p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/complexe_vormen_startpunten.png"></p>   

In [pixel_walker_v6](pixel_walker_v6.py) heb ik meerdere functies geschreven om de gevonden punten zoals bedoeld in versie 5 van de pixel walker te filteren om de accuracy te verhogen. Ook is dit de eerste versie van het algoritme waar een lijnfit gemaakt wordt om de kade te benaderen. De functie 'kadefit' past lineaire regressie toe middels Scipy om deze lijn te creëeren. De functie distance_line2point creëert een array aan afstanden tot de gefitte lijn om te gebruiken in de functie 'clean_outliers'. Clean_outliers verwijderd alle gevonden punten die niet binnen een afstand van een X aantal keer de standaardafwijking in de afstanden tot de lijn vallen. Dit zorgt ervoor dat punten die niet de algemene trend volgen verwijderd worden. Het script houdt dan een array met gefilterde punten over waar vervolgens opnieuw een lineaire fit aan gegeven wordt.   


  <p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_clean_outliers.png"></p>   
    <p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_distance_line2point"></p>   
  <p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_kadefit.png"></p>   
    <p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/pixel_walker_v5_schuim_probleem.png"></p>   
    

[pixel_walker_v8](pixel_walker_v8.py) past en extra filterfunctie toe genaamd 'clean_loaners' die een parameter stelt voor de maximale afstand tussen opeenvolgende punten. Als punten verder uit elkaar liggen dan deze parameter worden deze verwijderd.  

  <p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_clean_loaners.png"></p>   
    <p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/pixel_walker_v8_clean_loaners.png"></p>   
    
Het is belangrijk om op te merken dat deze manier van filtering en lijnfitten later uitgebreid is door Job en dat dit dus op een andere manier terug te vinden is in de nieuwste versie van het algoritme.  
  
  
## Data Visualization  
De kale data is uiteraard al visueel. Om echter de gevonden punten te laten zien worden deze geplot over de frame. Zoals in het vorige hoofdstuk toegelicht wordt hier ook een lijn over de kade gefit om dit te visualiseren.  
  
  
  
  
## Evaluation and diagnostics  
  
Voor het hyperparameteren heb ik een script geschreven dat uit alle losse confusion matrices f1 scores berekent zodat hiermee de beste hyperparameters gevonden kunnen worden. Deze confusion matrices worden bepaald op basis van de door ons gelabelde data te vergelijken met wat het algoritme als uitkomst geeft. Elke pixel wordt los vergeleken.  
  
[hyperparameter_evaluation](hyperparameter_evaluation.py)  
  
  
## Communication  
Ik heb de leiding genomen over het schrijven van de paper. Hierbij heb ik mijn projectgenoten uitgelegd hoe een paper over het algemeen uit ziet en hoe je dit schrijft. Naast het schrijven van de paper heb ik ook veel aangestuurd in het voorafgaande literatuuronderzoek. Daarnaast heb ik zowel als mijn projectgenoten een aantal presentaties gegeven tijdens de retrospectives:  
  
[Week 1](Presentation_week_1.pptx)  

In week 1 heb ik gepresenteerd vanwege mijn onderzoek in afstandsherkenning met stereoscopische camera's. Het onderzoek heeft aangetoond dat met het verschil van pixel-afstand op een figuur en de eigenschappen van de lens de afstand berekend kan worden. Deze techniek is uiteindelijk niet gebruikt omdat de stereoscopische camera's op de boot stuk waren tijdens de minor.

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Onderzoek_stereoscopische_camera's.png"></p>  

[Week 7](Presentation_week_7.pptx)  

In week 7 heb ik gepresenteerd naar aanleiding van onder andere de nieuwe filtering beschreven in data prepration bij [pixel_walker_v6](pixel_walker_v6.py), de functie clean_outliers. Daarnaast heb ik het gehad over de opzet van de paper gezien ik daar leiding in heb genomen.

[Week 8](Presentation_week_8.pptx)  

Week heb ik gepresenteerd naar aanleiding van het onderzoek in horizon detectie wat veel overeenkomsten heeft met kadeherkenning. 

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Onderzoek_horizon_detection.png"></p>  

Daarnaast heb ik een nieuwe methode gepresenteerd om de lijnfit aan de kade ook niet volledig rechte kade's te kunnen fitten, bijvoorbeeld een kade met een pier. Deze methode heb ik bedacht en 'r_value splitting' genoemd. Deze methode is uiteindelijk niet geïmplenteerd omdat bij de tijd dat deze bijna af was er een betere methode gevonden was. De methode kijkt naar de R ^2, een waarde die beschrijft hoe goed een lineare fit past. Er wordt een treshold gezet voor de gemiddelde R ^2 waarde waar aan voldaan moet worden. Dit houdt in dat van alle gefitte lijnen een R ^2 waarde wordt gecreëerd waarvan het gemiddelde wordt genomen. Als de eerste lineaire fit niet voldoet aan de treshold wordt de lijn gesplitst en worden opnieuw deze stappen ondernomen. Dit gaat door in een loop totdat de treshold behaald is.

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/r_value_lijnfit.png"></p>  

[Week 16](Presentation_week_16.pptx)

Week 16 heb ik vanwege mijn grote invloed op de paper gepresentaard waar ik het heb gehad over onze voortgang.