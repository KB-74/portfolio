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

|Beoordeling        |Link           | Afgerond | 
|------             |:------| ---- |
|Introductie        | [Introduction](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#introduction)             | ✓ | 
|Domein Knoledge    | [Domein kennis](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#domein-kennis)           | |
|Predictive Models  | [Predictive Models](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#predictive-models)   | |
|Data Preparation   |  | | 
|Data Visualization | [Visualization](https://github.com/KB-74/portfolio/blob/master/Jelte/protfolio.md#Data-Visualization) | | 
|Data collection    | |
|Evaluation         | | 
|Diagnostics of the learning process | |
|Communication (presentations, summaries, paper, ...)
> Hoofdstuk en Beordelings indeling portfolio

___
## Introductie

### Opdracht omschrijving

 `Beschrijving van de opdracht toevoegen`
 
 
<p align="left"> <img src="https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/bootje.gif" width="480" height="270" /> </p>

> RPA 3, Smart Ship van Port Of Rotterdam. 

### Projectkeuze: SHIPPING
Aan het begin van week 1 werden we genoodzaakt een keuze te maken uit een zes tal verschillende projecten. Het project
Waar mijn voorkeur naar uit gaat was het project autonomous shipping. Dit leek mij erg uitdagend om de volgende redenen:
- Meest passend bij mijn studie (werktuigbouwkunde).
- Mijn interesses in scheepvaart
- Opdracht waarbij er veel contact is met de project owner [Port of Rotterdam](https://www.portofrotterdam.com/nl)
- Samenwerking met consultant [CGI](https://www.cginederland.nl/)

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

## Domein kennis
Voorafgaand aan het de minor had ik geen ervaring met programmeren. Om mee te kunnen met het programmeerniveau van de 
minor was het noodzakelijk om hiermee aan de slag te gaan. Naast de colleges heb ik verschillende courses gevolgd op 
Coursera en Datacamp, dit is hieronder verder uitgewerkt. 
  
### DataCamp
met behulp van datacamp heb ik mijn domein kennis op het gebied van programmeren met python vergroot. 
In figuur 1 staat een screenshot van alle courses die ik in de eerste weken van de minor heb gevolgd. 


<p align="left"> <img src="https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/datacamp_courses.jpg" 
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

<p align="left"> <img src="https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/coursera_courses.JPG" 
 width="480" height="270"</p>

> Screenshot afgeronden courses Coursera (10-11-2018)

### colleges


###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___
## Predictive Models

### Neuraal Netwerk
Voor het begrijpen en helpen bij het opstellen van het Neuraal netwerk heb ik een aantal papers gelezen, deze papers staan
in de bijlage. Helaas was mijn programmeerervaring en vaardigheid nog niet op het niveau om daadwerkelijk een Neural
Netwerk te kunnen trainen. [Samenvatting](https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/aantekeningen_nn_colleges.pdf)   


### Algoritme
Voor het maken van een algorithme dat een scheiding kan herkennen tussen water en land is het noodzakelijk om mogelijke 
oplossingen eerst te testen. Een van de oplossingen was het kijken naar het verschil in kleur. De aannamen hierbij was: 
is het mogelijk om een kade te herkennen door te kijken naar het kleurverschil tussen het water en de kade. Hieraan heb 
ik samen met Michiel en Job gewerkt. [pixel_walker_v1](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/pixel_walker_V1.ipynb)  


Na de basis te hebben gelegt met programmeren in datacamp was het programmeren met andere de tweede stap. Dit was ook het
geen dat ik het meest heb geleerd aan het samen schrijven van dit stuk code 

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___


## Data preparation
De data die we van POR gekregen hadden bestond uit een video gefilmd met de camera's op de RPA. Nadat deze beelden geknipt 
en geundistored waren waren ze nog steeds niet geschikt voor het neuraal network. Hiervoor moest de data eerst gelabeld worden. 
Lees hierover meer in hoofdstuk [Data Collection](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#data-collection).

Voor het maken van een neuraal netwerk was er onvoldoende data. Hiervoor heb ik samen met Michiel het picture_processing 
script geschreven. Met dit script was het mogelijk om de afbeeldingen te bewerken met betrekking op helderheid, scherpte
, kleur, contrast en spiegelen. Dit om de verschillende senarios met bijvoorbeeld meer en minder licht na te botsen. 
Het script is te vinden onder [picture_processing](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/picture_processing_4.ipynb)



###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

## Data Visualization
grafiek plotten
picture_processing visualization pictures

Tijdens het maken van het picture processing was het moeilijk om te zien of het bewerkte frame en overlay daadwerkelijk
bij elkaar paste. Daarom is er een deel visualisatie toegevoegd dat zorgt voor het inzichtelijk maken van de frame en overlay.
[picture_processing](https://github.com/KB-74/portfolio/blob/master/Jelte/notebooks/picture_processing_4.ipynb) 

Wat heb ik hiervan geleerd: debug 

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___



___
## Data collection
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

## Evaluation and Diagnostics
In het algoritme wordt gekenen naar de kleur van elke pixel. Deze kleur wordt in een RGB waarde opgeslagen. Naar 
aanleiding van de feedback van de demo hebben we gekenen naar een andere manier van het opslaan van de waarde van de 
kleur van een pixel. Hieruit bleek dat het handig is om HSV kleuren te gebruiken omdat hierbij minder variabelen
zijn die van invloed zijn voor het weergeven van een kleur. Uiteindelijk is het me nog niet gelukt om dit 
in te voegen in de code. In de pdf in de link is globaal opgeschreven op welke manier kleuren opgeslagen kunnen worden
[Detectiemethode kleuren](bijlage/Detectiemethode%20kleuren.pdf).

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

## Communication (presentations, summaries, papers, ...)

### Samenvattingen
Voor het studeren van het tentamen heb ik gebruik gemaakt van samenvatting. Deze samenvattingen zijn gemaakt op basis 
de informatie die gegeven werd tijdens de coursera courses, en aangevuld met lessstof uit de colleges.  
[samenvatting colleges](https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/samenvatting_tentamen.pdf){:targer="_blank"}
[samenvatting presentaties](https://github.com/KB-74/portfolio/blob/master/Jelte/bijlage/samenvatting_presentaties.pdf)

### Scrum
Met de project aanpak methode van scrum focussen we ons op een daadwerkelijk werkend product en minder op documentatie.
Het bijhouden en schrijven van documentatie kost vaak veel tijd in projecten en gaat ten kosten van de kwaliteit en kwantiteit
van het eindproduct. De Scrum aanpak komt oorspronkelijk uit de ICT-sector, en past goed bij het project wat we op dit 
moment uitvoeren. Bij het scrum proces staan 4 regels centraal:
1. Individu en interactie staat boven het proces en de tools. 
2. Working product over uitgebreide documentatie.
3. Samenwerken met klanten over onderhandelingscontracten.
4. Verandering van een voorafgesteld plan.


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

<p align="left"> <img src="link-adress" width="480" height="270"</p>

###### Terug naar: [Inhoudsopgaven](https://github.com/KB-74/portfolio/blob/master/Jelte/portfolio.md#inhoudsopgave)
___

