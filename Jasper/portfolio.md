
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
<p align="center">Figuur 1: De RPA3, een reserve patrouillevaartuig van Port of Rotterdam bevestigd met 6 camera's en een stereoscopische setup. Het vaartuig wordt af en toe nog ingezet op normale patrouilles waarbij er data verzameld kan worden.</p>    

## Courses  
Voor deze minor heb ik al een stuk data-analyse uitgevoerd bij mijn bachelor technische natuurkunde. Deze kennis heb ik mede dankzij datacamp ruim uitgebreid. Ik heb de volgende courses in datacamp voltooid:  
  
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Completed_Courses_datacamp.png"></p>  
<p align="center">Figuur 2: Voltooide datacamp courses. Naast deze courses zijn er nog losse chapters gevolgd volgens het curricilum</p>      

Alle voorgeschreven datacamp courses en chapters zijn uitgevoerd. Dit geldt ook voor Coursera zoals te zien is in de volgende figuur:  
  
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Completed_Courses_coursera.png"></p>  
<p align="center">Figuur 3: Voltooide weken van het de Stanford Univeristy machine learning course. Volgens curriculum zijn week 1 tm 3 en 6 voltooid.</p>      
  
  
## Domain Knowledge  
Op het gebied van smart shipping zijn velen partijen bezig. Ook volledig autonoom varen worden actief stappen in gezet. Echter denken wij dat wij nieuwe openbare kennis op het gebied van kadeherkenning leveren. Soortgelijke datasets zijn makkelijk te vinden op YouTube en andere deelplatformen, de toepassing denken wij echter uniek te zijn Domeinkennis is opgedaan dankzij de samenwerking met Port of Rotterdam en CGI. Zo hebben we een Smart Shipping Event bijgewoond van rijkswaterstaat en naast het zelf presenteren op de innovation expo daar ook veel kennis op kunnen doen. Daarnaast kan voor een referentie voor domeinkennis van machine learning gekeken worden naar het behaalde cijfer voor het tentamen (7,6).   



## Predictive models  
  
Conceptueel heb ik meegedacht met de eerste versies van de 'pixel walker'. Dit script schiet lijnen uit die RGB waardes vergelijkt met betrekking van de Euclidian Distance. Daarnaast heb ik ook bijgedragen aan wiskunde concepten die nodig zijn om het script te schrijven zoals cirkelgeometrie. Zo is de startvorm tot versie 8 van de pixel walker een ellips gevormd naar de boot geweest. Hierbij wordt de volgende vergelijking gebruikt:



Waarbij a en b coëfficiënten zijn naar eigen keuze om de vorm van de ellips te bepalen.
  
  
<img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Complexe_vorm_startpunten.png" width="700" >
Figuur 4: De code die gebruikt wordt om startpunten om de boot te laten starten. Dit wordt gedaan door een ovale vorm toe te passen die geconfigureerd kan worden door 2 constanten: 'X_COEFF', 'Y_COEFF'. Startpunten worden op een constant aantal graden van elkaar verwijderd. Ook worden de richtingscoëfficienten berekend voor de uitschietende pixel walkers.      
  
  
  
[pixel_walker_v5](pixel_walker_v5.py)  


<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/pixel_walker_v5_schuim_probleem.png">  </p>
<p align="center">Figuur 9: Links: Een weergave van een frame waar de kade gedetecteerd wordt door 'pixel_walker_v5' waar de meeste punten correct de kade identificeren. Het water in deze frame bevat weinig schuim. Rechts: Een weergave van een frame waar de kade gedetecteerd wordt door 'pixel_walker_v5' waar de meeste punten niet correct de kade identificeren. Het water in deze frame bevat veel schuim. De pixel walker identificeert het schuim als kade.</p>
    
  
## Data collection  
Alle kale data is aangeleverd door Port of Rotterdam. 
  
## Data preparation  

In [pixel_walker_v6](pixel_walker_v6.py) heb ik meerdere functies geschreven om de gevonden punten zoals bedoeld in versie 5 van de pixel walker te filteren om de accuracy te verhogen. Ook is dit de eerste versie van het algoritme waar een lijnfit gemaakt wordt om de kade te benaderen. De functie 'kadefit' past lineaire regressie toe middels Scipy om deze lijn te creëeren. De functie distance_line2point creëert een array aan afstanden tot de gefitte lijn om te gebruiken in de functie 'clean_outliers'. Clean_outliers verwijderd alle gevonden punten die niet binnen een afstand van een X aantal keer de standaardafwijking in de afstanden tot de lijn vallen. Dit zorgt ervoor dat punten die niet de algemene trend volgen verwijderd worden. Het script houdt dan een array met gefilterde punten over waar vervolgens opnieuw een lineaire fit aan gegeven wordt.    

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/pixel_walker_v6_clean_outliers_en_kadefit.png"></p>   
<p align="center">Figuur 5: Een weergave de output van 'pixel_walker_v6': Gevonden punten, gefilterde punten, startpunten en lijnfits. Oranje ovaal naast de boot zijn de startpunten waaruit de pixel walkers worden verstuurd. Blauw en rood zijn de gevonden punten zoals 'pixel_walker_v5' zou doen. Rood zijn de punten die de functie 'clean_outliers' verwijdert in 'pixel_walker_v6' waardoor blauw de overgeleven punten worden. Te zien is dat voornamelijk foute punten gefilter worden. Er blijven nog een aantal blauwe punten over die fout zijn op het schuim. De paarse lijn geeft aan welke lijn 'pixel_walker_v5'had aangegeven. De oranje lijn is de verbeterde lijnfit volgens 'pixel_walker_v6'. Door te kijken naar de paarse en oranje lijn kan een duidelijke verbetering gezien worden van de pixel walker.</p>    


De functie 'distance_line2point' berekent voor een array aan punten de korste afstand tot een lijn voor ieder punt volgens de volgende vergelijking:

##Vergelijking figuur

Waarin x= ;......

<img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_distance_line2point.png" width="700">  
Figuur 6: De functie 'distance_line2point'. Deze functie maakt een array van de korste afstanden tussen een array van punten en een lijn.


<img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_clean_outliers.png" width="700">   
Figuur 7: De functie 'clean_outliers'. Deze functie gebruikt de gevonden punten, de gecreërde lineaire fit bij deze punten en de intercept van deze fit. De functie gebruikt 'distance_line2point' om een array te creëeren met afstanden van elk punt tot de lijn. Vervolgens creëert de return variabele 'cleaned_points' door alle punten die verder dan CLEAN_STD_COEFF keer de standaardafwijking in de afstanden van lijn tot punten te verwijderen. 'CLEAN_STD_COEFF' is dus een voorgedifiniëerde variabele die bepaalt hoeveel keer de standaardafwijking wordt gebruikt als maximum afstand tot de lijn.  


<img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_kadefit.png" width="700">  
Figuur 8: De functie 'kadefit'. Deze functie gebruikt de gevonden punten gebruikt de library 'scipy' om een lineaire fit te creëeren. Vervolgens plot deze functie de fit zelf. 


[pixel_walker_v8](pixel_walker_v8.py) past en extra filterfunctie toe genaamd 'clean_loaners' die een parameter stelt voor de maximale afstand tussen opeenvolgende punten. Als punten verder uit elkaar liggen dan deze parameter worden deze verwijderd.  

Het is belangrijk om op te merken dat deze manier van filtering en lijnfitten later uitgebreid is door Job en dat dit dus op een andere manier terug te vinden is in de nieuwste versie van het algoritme.  
 
 
  
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/pixel_walker_v8_clean_loaners.png"></p>   
<p align="center"> Figuur 11: De output van 'pixel_walker_v8'. Op een frame worden de startpunten, gevonden punten, en gefilterde punten geplot. Ook wordt de lineaire fit door de functie 'kadefit' geplot. Oranje punten: Startpunten van pixel walker. Roze punten: Gevonden punten gefilterd door de functie 'clean_outliers'. Rode punten: Gevonden punten gefilterd door de functie 'clean_loaners'. Blauwe punten: Overgebleven gevonden punten na filtering. Oranje lijn: Lineaire fit aan de kade door de functie 'kadefit'. </p>
    
   


<img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/functie_clean_loaners.png" width="580">  
Figuur 10: De functie 'clean_loaners'. Deze functie creëert een array met de afstand tussen opeenvolgende punten in de array van gevonden punten. Opeenvolgende punten die verder uit elkaar liggen dan de voorgedefinieerde variabele 'MAX_DISTANCE_TO_NEIGHBOURS' worden verwijderd. 




  
## Data Visualization  
De kale data is uiteraard al visueel. Om echter de gevonden punten te laten zien worden deze geplot over de frame. De output van het pixel walker algoritme is echter wel zelf gecreëerd. Zoals in versie 8 van de pixel walker in figuur 11 te zien is wordt zowel de startpunten, gevonden punten en gefilterde punten gevisualiseerd om zo een indruk te geven wat er gebeurt. Dit wordt gebruikt om te analyseren of de gecreëerde functies correct werken en zo deze te kunnen testen op verschillende frames en situaties. Om de outputs van het pixel walker algoritme te plotten en visualiseren wordt voornamelijk matplotlib gebruikt tot versie 8 van de pixel walker. In het volgende hoofdstuk 'Evualation and diagnostics' beschrijf ik ook een zelfgeschreven script die het hyperparameteren visualiseert door de verschillende f1-scores per gekozen parameters te plotten.
   
  
## Evaluation and diagnostics  
  
Voor het hyperparameteren heb ik een script geschreven dat uit alle losse confusion matrices f1 scores berekent zodat hiermee de beste hyperparameters gevonden kunnen worden. Deze confusion matrices worden bepaald op basis van de door ons gelabelde data te vergelijken met wat het algoritme als uitkomst geeft. Elke pixel wordt los vergeleken. Het script extract de data uit [hyperparameter.csv](hyperparameter.csv)  
   
[hyperparameter_evaluation](hyperparameter_evaluation.py)  

Het script plot alle f1 scores bij de bijbehorende parameters. Zo kan de meest effectieve waarde gevonden worden. De volgende figuur is een voorbeeld uit de paper.


<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/hyperparameter.png">   
<p align="center">Figuur 12: Linksboven: filter parameter om schuim uit het water te filteren. Rechtsboven: treshold parameter om randen te detecteren. Linksonder: onder coëfficiënt voor Canny edge detection. Rechtsonder: boven coëfficiënt voor Canny edge detection.</p>


## Hier moet een hyperparameter script figuur met beschrijving  
Figuur 13: Het script 'hyperparameter_evaluation.py'. In de code wordt 'hyperparamter.csv' geïmporteerd en een statistics function uitgevoerd op de data om er vervolgens de f1 score per iedere waarde voor te berekenen. Voor iedere parameter wordt zijn eigen plot gecreëerd. Voor de paper zijn sommige plots later nog gecombineerd.  
  
  
  
## Communication  
Ik heb de leiding genomen over het schrijven van de paper. Hierbij heb ik mijn projectgenoten uitgelegd hoe een paper over het algemeen uit ziet en hoe je dit schrijft. Naast het schrijven van de paper heb ik ook veel aangestuurd in het voorafgaande literatuuronderzoek. Daarnaast heb ik zowel als mijn projectgenoten een aantal presentaties gegeven tijdens de retrospectives:  
  
[Week 1](Presentation_week_1.pptx)  

In week 1 heb ik gepresenteerd vanwege mijn onderzoek in afstandsherkenning met stereoscopische camera's. Het onderzoek heeft aangetoond dat met het verschil van pixel-afstand op een figuur en de eigenschappen van de lens de afstand berekend kan worden. Deze techniek is uiteindelijk niet gebruikt omdat de stereoscopische camera's op de boot stuk waren tijdens de minor.

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Onderzoek_stereoscopische_camera's.png"></p>  
<p align="center">Figuur 12: Slide uit de presentatie van week 1. De figuur aan de linkerzijde is een schematische weergave van de verschillende variabelen in gebruik en zichtvelden van de camera's. Rechtsboven is de ZED te zien, een stereoscopische camera die vergelijkbare proefen kan opleveren als de stereoscopische camera's die op de RPA3 bevestigd zijn. Vergelijking 1, 2 en 3 beschrijven de afstand tot een object met gebruik van de cameraeigenschappen en verschil in pixellocatie.</p> 


[Week 7](Presentation_week_7.pptx)  

In week 7 heb ik gepresenteerd naar aanleiding van onder andere de nieuwe filtering beschreven in data prepration bij [pixel_walker_v6](pixel_walker_v6.py), de functie clean_outliers. Daarnaast heb ik het gehad over de opzet van de paper gezien ik daar leiding in heb genomen.

[Week 8](Presentation_week_8.pptx)  

Week heb ik gepresenteerd naar aanleiding van het onderzoek in horizon detectie wat veel overeenkomsten heeft met kadeherkenning. 

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/Onderzoek_horizon_detection.png"></p>  
<p align="center">Figuur 13: Een slide uit de presentatie van week 8. De slide bevat 2 figuren waarop horizon detectie toegepast wordt. De titel van het bijpassende onderzoek en auteurs worden weergeven boven deze figuren.</p>


Daarnaast heb ik een nieuwe methode gepresenteerd om de lijnfit aan de kade ook niet volledig rechte kade's te kunnen fitten, bijvoorbeeld een kade met een pier. Deze methode heb ik bedacht en 'r_value splitting' genoemd. Deze methode is uiteindelijk niet geïmplenteerd omdat bij de tijd dat deze bijna af was er een betere methode gevonden was. De methode kijkt naar de R ^2, een waarde die beschrijft hoe goed een lineare fit past. Er wordt een treshold gezet voor de gemiddelde R ^2 waarde waar aan voldaan moet worden. Dit houdt in dat van alle gefitte lijnen een R ^2 waarde wordt gecreëerd waarvan het gemiddelde wordt genomen. Als de eerste lineaire fit niet voldoet aan de treshold wordt de lijn gesplitst en worden opnieuw deze stappen ondernomen. Dit gaat door in een loop totdat de treshold behaald is.

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jasper/images/r_value_lijnfit.png"></p>  
<p align="center">Figuur 14: Slide uit de presentatie van week 8. Een schematische flowchart wordt weergaven om een zelfbedacht concept 'r-value filtering' uit te leggen. Daarnaast wordt een frame weergaven waar een kadefit op wordt toegepast wat laat zien dat de lineaire fit inadequaat de kade kan representeren.</p>


[Week 16](Presentation_week_16.pptx)

Week 16 heb ik vanwege mijn grote invloed op de paper gepresentaard waar ik het heb gehad over onze voortgang.