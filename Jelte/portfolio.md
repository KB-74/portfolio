# Portfolio Data Science

|                   |                   |
| ---:              | :---              |
| Naam:             | Jelte Molenaar    |
| Studentnummer:    | 15084302          |
| Groep:            | KB-74 Shipping    |
| Datum:            | 14-11-2018        |

## Inleiding
Dit portfolio is tijdens de minor Data science individueel ongesteld en geeft weer wat de bijdragen voor het project was, 
de capaciteiten en datgene dat tijdens de minor geleerd is. 

## Inhoudsopgave
In de tabel hieronder staat waarop het portfolio beoordeelt wordt:

|Beoordeling                |Link           | Afgerond | 
|------                     |:------| ---- |
|Introductie                | [1](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#introduction)                 |  | 
|Domein knowledge           | [2](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#domein-kennis)                | ✓ |
|Predictive Models          | [2](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#predictive-models)            | ✓ |
|Data Preparation           | [4](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#data-preparation)             | ✓ | 
|Data Visualization         | [5](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#Data-Visualization)           | ✓ | 
|Data collection            | [6](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#data-collection)              | ✓ |
|Evaluation and Diagnostics | [7](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#evaluation-and-diagnostics)   | ✓ |
|Communication              | [8](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#communication)                | |
> Hoofdstuk en Beordelings indeling portfolio

___
## 1. Introductie

### Opdracht omschrijving
Hieronder zie je afbeelding van  de RPA3 ofwel bekend als het floatingLab van Port of Rotterdam (POR). Met dit schip biedt
POR de mogelijkheid aan om te experimenten met autonoom varen. Tijdens dit project hebben we de eerste stapjes gezet
richting autonoom varen. De focus lag op het herkennen van de grens tussen land en water. 

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/bootje.gif" width="480" height="270" /> </p>

> RPA 3, Smart Ship van Port Of Rotterdam. 

### persoonlijk leerdoel
Voor deze minor heb ik een persoonlijk leerdoel opgesteld, dit doel hield in dat ik vaardigheid kreeg in het programmeren.
en een basis legde in het werken en aansturen met en in verschillende teams. Tijdens de minor heb ik zeker kunnen werken
aan deze vaardigheid.   

### Projectkeuze: SHIPPING
Aan het begin van week 1 werden we genoodzaakt een keuze te maken uit een zes tal verschillende projecten. Het project
Waar mijn voorkeur naar uit gaat was het project autonomous shipping. Dit leek mij erg uitdagend om de volgende redenen:
- Meest passend bij mijn studie (werktuigbouwkunde).
- Mijn interesses in scheepvaart
- Opdracht waarbij er veel contact is met de project owner [Port of Rotterdam](https://www.portofrotterdam.com/nl)
- Samenwerking met consultant [CGI](https://www.cginederland.nl/)

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

## 2. Domain knowledge
Voorafgaand aan het de minor had ik geen ervaring met programmeren. Om mee te kunnen met het programmeerniveau van de 
minor was het noodzakelijk om hiermee aan de slag te gaan. Naast de colleges heb ik verschillende courses gevolgd op 
Coursera en Datacamp, dit is hieronder verder uitgewerkt. 
  
### DataCamp
met behulp van datacamp heb ik mijn domein kennis op het gebied van programmeren met python vergroot. 
In figuur 1 staat een screenshot van alle courses die ik in de eerste weken van de minor heb gevolgd. 


<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/datacamp_courses.jpg" 
 width="480" height="270"</p>

> Screenshot afgeronden courses Datacamp (08-11-2018)

### Coursera
Om kennis op te doen voor het maken van machine learning ben ik de online courses gevolgd die op coursera beschikbaar 
zijn. Tijdens deze courses bode een introductie in machine learning en de hierbij de behorende statestieken.
Er is ingegaan op Linear en Logistic Regression en regularization. Naast de theorie waren er ook opdrachten waarbij je 
bewust werd gemaakt hoe je dit toepasbaar kan maken in de praktijk. Deze oefeningen werden uitgevoerd in mathlab
en Octave. In de [github](https://github.com/JelteMolenaar/machine_learning_standford_university) staan de uitgewerkte 
oefeningen.

Naast de verplichten coursers heb ik zelf wat extra courses gevolgd waarbij ingegaan werd op Neural networks. De 
bijgehorende opdrachten heb ik overgeslagen en alleen gefocused op de informatie die gegeven werd. Dit omdat we dit 
verderop in het project nodig hebben. [samenvatting](https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/aantekeningen_nn_colleges.pdf)   

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/coursera_courses.JPG" 
 width="480" height="270"</p>

> Screenshot afgeronden courses Coursera (10-11-2018)

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___
## 3. Predictive Models

### Neuraal Netwerk
Voor het begrijpen en helpen bij het opstellen van het Neuraal netwerk heb ik een aantal papers gelezen, deze papers 
staan in de bijlage. Helaas was mijn programmeerervaring en vaardigheid nog niet op het niveau om daadwerkelijk een 
Neural Netwerk te kunnen trainen. [Samenvatting](https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/aantekeningen_nn_colleges.pdf)   


### Algoritme
Voor het maken van een algorithme dat een scheiding kan herkennen tussen water en land is het noodzakelijk om mogelijke 
oplossingen eerst te testen. Hierbij hebben we gekeken naar verschillende oplossing. Inhoudelijk ga ik hier niet op in
omdat dit in de paper beschreven is. een van de aannames die we voor het algorithme moesten testen was: Is het mogelijk 
om een kade te herkennen door te kijken naar het kleurverschil tussen het water en de kade? Hieraan heb ik samen met
Michiel en Job gewerkt. [pixel_walker_v1](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/pixel_walker_V1.ipynb)  
Na de basis te hebben gelegt met programmeren in datacamp was het programmeren met andere de tweede stap. Dit was ook 
het geen dat ik het meest heb geleerd aan het samen schrijven van de pixel walker v1 

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___


## 4. Data preparation
De data die we van POR gekregen hadden bestond uit een video gefilmd met de camera's op de RPA. Nadat deze beelden geknipt 
en geundistored waren waren ze nog steeds niet geschikt voor het neuraal network. Hiervoor moest de data eerst gelabeld worden. 
Lees hierover meer in hoofdstuk [6. Data Collection](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#data-collection).

Voor het maken van een neuraal netwerk was er onvoldoende data. Hiervoor heb ik samen met Michiel het picture_processing 
script geschreven. Met dit script was het mogelijk om de afbeeldingen te bewerken met betrekking op helderheid, scherpte
, kleur, contrast en spiegelen. Dit om de verschillende senarios met bijvoorbeeld meer en minder licht na te botsen. 
Het script is te vinden onder [picture_processing](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/picture_processing_4.ipynb)

Naast het picture_processing script heb ik ook gewerkt aan het undistorden (verwijderen van bolling) van de camera beelden. 
[fisheye_undistord](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/fisheye_undistord.ipynb) Hiervan heb 
ik leren zoeken op internet naar soortgelijke projecten. Vervolgens heb ik dit toegepast op ons project. 

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

## 5. Data Visualization
Tijdens het maken van het picture processing was het moeilijk om te zien of het bewerkte frame en overlay daadwerkelijk
bij elkaar paste. Daarom is er een deel visualisatie toegevoegd dat zorgt voor het inzichtelijk maken van de frame en overlay.
[picture_processing](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/picture_processing_4.ipynb) 
Wat heb ik geleerd heb tijdens het maken van het picture_processing script is hoe je moet debuggen. Na verloop van de tijd
werd de code complexer en was het moeilijk om te zien wat er fout ging. Uiteindelijk heb ik dit opgelost door mezelf af 
te vragen wat de verwachten output moet zijn, en vervolgens stapje voor stapje het probleem op te lossen. Met name de print
statements en een hoop gedult hebben mij geholpen om dit op te lossen. 

In [pixel_walker_v1](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/pixel_walker_V1.ipynb) is ook een deel
data visualizatie te vinden. Dit is onderaan in het script waar de euclidean distance geplot wordt onder de afbeelding.

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___



___
## 6. Data collection
Voor trainen van een neural network is gelabelde data noodzakelijk om het te kunnen trainen. Om deze afbeeldingen te maken
hebben we het geselcteerde data bestand verdeeld in verschillende frames. Vervolgens hebben daarvan 250 random frames
geselecteerd en door het algorithme gehaald. Toen de tijd was het algorithme minder accuraat en had het algorithme een 
lage precision per foto. Voor het neural netwerk mocht er weinig afweiking in de overlay en het orginele frame zitten. 
Dit is opgelost door handmatig de afbeeldingen te labelen in in photoshop. Hier heb ik me op gefocused tijdens twee sprints.
Ik had nog geen ervaring met fotoshop maar tijdens het label van de afbeeldingen heb ik hier veel kennis van opgedaan.  

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/labelen_photoshop.png" width="480" height="270"</p>

> labelen in photoshop. Hierbij is wit het water en is boven het gedeelte te zien waar geen water is. 


###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

## 7. Evaluation and Diagnostics
In het algoritme wordt gekenen naar de kleur van elke pixel. Deze kleur wordt in een RGB waarde opgeslagen. Naar 
aanleiding van de feedback van de demo hebben we gekenen naar een andere manier van het opslaan van de waarde van de 
kleur van een pixel. Hieruit bleek dat het handig is om HSV kleuren te gebruiken omdat hierbij minder variabelen
zijn die van invloed zijn voor het weergeven van een kleur. Uiteindelijk is het me nog niet gelukt om dit 
in te voegen in de code. In de pdf in de link is globaal opgeschreven op welke manier kleuren opgeslagen kunnen worden
[Detectiemethode kleuren](bijlage/Detectiemethode%20kleuren.pdf).

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

## Communication

### Samenvattingen
Voor het studeren van het tentamen heb ik gebruik gemaakt van samenvatting. Deze samenvattingen zijn gemaakt op basis 
de informatie die gegeven werd tijdens de coursera courses, en aangevuld met lessstof uit de colleges.  
[samenvatting colleges](https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/samenvatting_tentamen.pdf){:targer="_blank"}
[samenvatting presentaties](https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/samenvatting_presentaties.pdf)

### Scrum
Tijdens het project gebruikte we de scrum methode aanpak. Hier had ik al veel ervaring in ten opzichte van mijn 
groepsgenoten. Hierbij nam ik de rol als scrummaster op me. Elke week hadden we op maandag een sprintplanning waarin we
met zn alle besloten wat we in de aankomende sprint wouden bereiken. Daarnaast hadden we elke vrijdag een retrospectief.
Tijdens deze meetings kwam naar voren waar we op vast liepen en wat we konden verbeteren. Al deze meetings facaliteerde 
ik.


### Presentaties
Elke week moesten we presentaties geven. 
De presenaties zijn [hier](https://github.com/KB-74/portfolio/blob/master/Presentaties) te vinden.

Naast de presentaties die we op school gegeven hebben, hebben we ook een aantal presentaties extern gegeven. 
Een van de leukste dingen was de [Innovation Expo 2018](https://www.portofrotterdam.com/nl/nieuws-en-persberichten/havenbedrijf-rotterdam-beproeft-autonoom-varen-met-drijvend-laboratorium) 
hier stonden we met een stand van POR, en mochten we andere vertellen over ons project.

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

### Bijlage
[1](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
[2](http://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf)
[3](https://www.degruyter.com/downloadpdf/j/itms.2017.20.issue-1/itms-2017-0002/itms-2017-0002.pdf)
[4](http://cs231n.github.io/convolutional-networks/)

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

#### Contact

- [Student email](15084302student.hhs.nl)


'toevoegen afbeelding in MD'

<p align="center"> <img src="link-adress" width="480" height="270"</p>

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

