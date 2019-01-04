Versie: 04-01-2019

# Persoonlijke portfolio
Persoonlijke portfolio voor de minor Applied Data Science 2018/2019 op de Haagse Hogeschool.  

|  | |
| ---: | :--- |
|Student:| <b>Michiel van Soest</b>|
|Studentnummer:| <b>15080803</b>|
|Groep:| <b>KB-74 Shipping</b>|
|Opdrachtgever:| <b>Port of Rotterdam</b>|
|Begeleider:| <b>Hugo Benne</b>|

# Leeswijzer
In dit portfolio is te lezen wat ik gedaan en behaald heb binnen dit SHIP project. Er is geprobeerd een zo duidelijk mogelijke weergave te geven van de denkwijze, hoe beslissingen tot stand zijn gekomen, en wat er proecies is behaald.
De hoofdstukken zijn verdeeld over de verscheidene velden van Applied Data science, om gemakkelijk een beeld te krijgen wat er binnen elk gebied is gedaan.

# Inhoudsopgave

|Hoofdstuk        | 
|------             |
|[Shipping "Floating Lab"](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#shipping-floating-lab)|  
|[Courses](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#courses)| 
|[Domain Knowledge](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#domain-knowledge)| 
|[Predictive models](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#predictive-models)| 
|[Data preperation](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#data-preparation)| 
|[Data visialization](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#data-visualization)| 
|[Data collection](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#data-collection)| 
|[Evaluation](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#evaluation)| 
|[Diagnostics of the learning process](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#diagnostics-of-the-learning-process)| 
|[Communication](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#communication-presentations-summaries-paper-)| 

### Notebooks
|Notebooks        | 
|------             |
|[frame_checker](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/frame_checker.ipynb)| 
|[picture_processing](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/picture_processing.ipynb)| 
|[wall_labeler](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/wall_labeler.ipynb)| 
|[pixel_walker_V2.1](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/pixel_walker_V2.1.ipynb)|
|[pixel_walker_V5](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/pixel_walker_V5.ipynb)|
|[video_extraction](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/video_extraction.ipynb)|
|[object_detection_V_1](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/object_detection_V1.ipynb)|  
|[grijswaarden_of_rgb](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/grijswaarden_of_rgb.ipynb)|  

# Shipping "Floating Lab"
### Keuze SHIP
Mijn keuze voor het project SHIP is gebaseerd op onderstaande redenen:
- SHIP sprak erg tot de verbeelding door de huidige technologische voortgang op het gebied van autonome producten. Ik wilde dan ook graag in de voorhoede staan van deze ontwikkelingen.
- Om ervaring op te doen in en het leren van programmeren met python.
- Ervaring op doen in het gebied van objectherkenning en machine learning

### Floating Lab 
Floating Lab is een samenwerkingsverband van verscheidene partijen, zoals Port of Rotterdam (PoR), CGI en de Haagse Hogeschool (HHS). PoR biedt de RPA3 (boot uitgerust met camera's en overige sensoren) ter beschikking aan de andere partijen om algoritmen en software te ontwikkelen om autonoom varen mogelijk te maken.  

Wij (Groep SHIP) werken namens de HHS aan beeldherkenning van verscheidene dingen zoals: land/water en objectherkenning.  

### RPA3
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/rpa3.jpg"> </p>

# Courses
Om bovenstaande algoritmen en software te kunnen ontwikkelen heb ik voor zover mogelijk de nodige kennis opgedaan met Datacamp en Coursera. Op onderstaande afbeeldingen is te zien welke courses ik precies heb afgerond. Daarnaast heb ik nog vele youtube videos bekeken met betrekking tot neurale netwerken, filtermogelijkheiden (zoals bv. Gausian Blur) en andere manieren om water/ objecten te herkennnen.  

<b>Datacamp</b>
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/datacamp_michiel.png"> </p>  
<b>Coursera</b>
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/coursera_michiel.png"> </p>

# Domain Knowledge
Voorafgaand aan dit project had ik zeer beperkte programeer ervaring. Deze kennis heb ik aangescherpt a.d.h.v. de aangeboden [Courses](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#courses) en youtube videos. Daarnaast hebben we het SMASH (Smart shipping) event bezocht om kennis op te doen omtrent de veranderende kennis en regelgeving omtrent smart shipping.
De overige opgedane theoretische kennis is behaald door het lezen van verscheidene papers over detectie van onder andere de horizon, randen, richting van randen etc. De bronnen hiervan zijn te vinden in ons paper.

Bovenstaande activiteiten hebben geholpen om de nodige features te onderscheiden en te analyseren om ons algoritme te laten werken.

# Predictive Models
In eerste instantie bestond ons project grotendels uit twee subprojecten; Objectherkenning en land/water herkenning.
Het land/water herkennings algoritme is op conceptueel niveau bedacht door Martin, de uitwerking en de nodige berekeningen zijn vervolgens als groep uitgewerkt.

Als eerste was het de taak om uit te zoeken wat een effectieve manier was om de grens tussen water en land te vinden. In onderstaand notebook gecreerd door mijzelf en Martin is te zien waarom besloten is voor RGB i.p.v. grijswaarden, ondanks dat grijswaarden uiteindelijk minder zwaar zijn voor de cpu. Ook is onderaan het notebook te zien dat we zijn gaan experimenteren met de Euclidian distance, ik had bedacht dat dit wel een effectieve manier kon zijn om het verschil in wardes te berekenen.  
[grijswaarden_of_rgb](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/grijswaarden_of_rgb.ipynb)

Na bovenstaand onderzoek heb ik samen met Jelte en Job het onderstaand notebook gemaakt. Hier in is te zien hoe we de Euclidian distance werkelijk toepassen om de scheidingen tussen water, land en boot te bepalen. (de data was op dit moment nog niet tot onze beschikking, om deze reden is een willekeurig plaatje gebruikt)  
[pixel_walker_V2.1](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/pixel_walker_V2.1.ipynb)

Nadat we de data hebben ontvangen is het idee ontstaan van de "pixel_walker". Het algoritme neemt de gemiddelde waarde van de groene lijn en schiet vervolgens een zogenaamde "pixel walkers" over de afbeelding af richting de andere kant van de afbeelding. Van elke stap/iteratie die de walker neemt, wordt de rgb waarde toegevoegd aan het huidige gemiddelde van die betreffende walker. zodra deze rgb waarde echter teveel afwijkt van het al bestaande gemiddelde, wordt een puntje geplot.   
[pixel_walker_V5](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/pixel_walker_V5.ipynb)
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/pixel_walker_v5.PNG"> </p> 

De hieropvolgende stappen van dit algoritme zijn grotendeels door Job uitgewerkt gezien hij onze ideen met zijn programeerkennis het beste tot uitwerking kon brengen. Er is vervolgens vooral gewerkt in pair-programming.

Aan de objectherkenningskant heb ik zelf veel moeite gedaan om de gekozen objectdetectiemethode YOLO (na onderzoek gebleken meest effectieve methode voor objectherkenning op dat moment) te begrijpen. In onderstaand Notebook is te zien hoe we onze verkegen data door het algoritme konden halen. Het aanpassen van YOLO bleek echter niet binnen mijn programeerkennis te liggen. Daarnaast was het splitsen van het huidig gebruikte model niet mogelijk, en zou het compleet zelf trainen ervan niet binnen de scope liggen van ons project.  

Later is ook Keras uitgewerkt, hoewel dit beter aanpasbaar was, was dit wel zwaarder en te langzaam voor live processing.  
[object_detection_V_1](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/object_detection_V1.ipynb)
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/object_detection.png"> </p> 
# Data preparation
De data die we in eerste instantie ontvangen hebben, bestaat uit een .avi videobestand met de output van een van de voorwaards gerichte camera's(camera 3).  
Om de data te kunnen gebruiken hebben we als eerste elk frame in de video met gebruik van opencv geëxporteerd als png. hiervan hebben we 250 willekeurige frames met een script gekozen en hernoemd tot frame 1 t/m 250 (het originele framenummer en welke daaraan gekoppeld is, is opgeslagen in een .json bestand).

We hebben gekozen om het water te labelen d.m.v. een mask met zwart en witte pixels. We hebben expliciet niet gekozen voor het labelen van objecten, gezien de al bestaande modellen omtrent objectdetectie (vb. Yolov3) niet  zomaar kunnen worden gesplit, en er niet genoeg data beschikbaar was gesteld om de beschikbare modellen te trainen.  

Om deze data te labelen heb ik samen met Martin een "framechecker" gemaakt. Deze vergelijkt de automatisch gelabelde data (gelabeld door ons bestaande algoritme voorland/water herkenning) met de bijpassende frame, door deze over elkaar heen te leggen.  
[Frame checker notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/frame_checker.ipynb)  
Door gebruik te maken van deze framechecker kan de goed gelabelde data gesplitst worden van de juist gelabelde data.  

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/frame_checker.png"> </p> 

De verkeerd gelabelde data kon daarna correct gelabeld worden met een tooltje dat lijkt op de hiervoor getoonde Frame Checker. Dit tooltje gebrukt net zoals voorgaande frame_checker code uit de de [app](https://github.com/KB-74/portfolio/tree/master/Michiel/Notebooks/app) grotendeels gecreerd door Job. Om deze reden kan deze ook alleen gerund worden als deze kan worden aangeroepen. Door op het plaatje te klikken werden er puntjes gecreërd waarvan de locatie wordt opgeslagen in een .json bestand.  
[Wall labeler notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/wall_labeler.ipynb)  
Halverwege is echter gekozen om Photoshop te gebruiken gezien de magnet-lasso tool hier beter geschikt voor is.


De 250 gelabelde frames waren naar ons inzicht echter niet genoeg. Om deze reden, en om verschillende situaties na te bootsen welke niet in onze dataset voorkomen, hebben we verschillende aanpassingen gedaan op de frames. Hoe dit gedaan is, is te zien in de picture processing notebook.  
[Picture Processing notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/picture_processing.ipynb)

<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/picture_processing.PNG"> </p> 

Aanpassingen die uitgevoerd zijn, zijn:  

|  | |
| :--- | :--- |
|brightness| [0.3,1.4]|        # [0.4,0.5,0.6,0.7,0.8,0.9,1.1,1.2,1.3,1.4]
|contrast| [0.3,1.4]|        # [0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.3,1.4]
|sharpness| [5.0,20.0]|        # [5.0, 10.0, 15.0, 20.0]
|color| [0.0,10.0]|            # [0.0, 3.0, 6.0, 10.0]
|mirrored image| [1]|

Bijbehorende masks worden in deze notebook ook automatisch met bijbehorend framenummer meegekopieerd/ aangepast.

# Data Visualization
link video?
`picture processing notebook`
`frame checker`
`wall labeler`

# Data collection
De data die we nodig hadden bestaat uit videomateriaal van verscheidene camera's op de RPA3. Helaas was na analyse van deze beelden duidelijk dat alleen de beelden van camera 3 bruikbaar waren. De overige camera's, waaronder de stereoscopische camera's, waren door onder andere trillingen en de verkeerde instellingen van zeer slechte kwaliteit. Dit heeft ook grotendeels ons onderzoek naar afstandsherkening gehinderd en stopgezet.   

Om de beelden te kunnen gebruiken voor herkenning, hebben we elk frame omgezet naar een aparte afbeelding. Zie onderstaand notebook:
[video_extraction](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/video_extraction.ipynb)
Deze notebook bewerkt indien aangezet, ook de frames door de Fisheye lens te corrigeren. Dit gedeelte is door Job beschreven.


Omdat de verkregen afbeeldingen slechts op één moment gefilmd zijn, bestaat de kans dat ons algoritme slechts getraind wordt op zeer specifieke omstandigheden. Om deze reden is het eerder beschreven [Picture Processing notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/picture_processing.ipynb) gebruikt om het algoritme te verbeteren aan de hand van aanpassing van de afbeeldingen.  
Wat dit inhoud en doet is te lezen in [Data preperation](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#data-preparation), of in de notebook zelf.  

# Evaluation


`frame checker`
`dat ding dat trainde en bekeek wat t beste is`
`filmpjes`

# Diagnostics of the learning process
`verhaaltje?`

# Communication (presentations, summaries, paper, ...)

##Scrum 
Voor dit project is met de SCRUM methode gewerkt. Hierbij is besloten dit op een fysiek bord te doen. Met de project aanpak methode van scrum focussen we ons vooral op een werkend product en niet zozeer op documentatie. Bij het scrum proces staan 4 regels centraal:  
- Individu en interactie staat boven het proces en de tools.  
- Working- product over uitgebreide documentatie.  
- Samenwerken met klanten over onderhandelingscontracten.  
- Verandering van een voorafgesteld plan.  

Daarnaast hebben we naar een aantal tussentijdige deadlines toe gewerkt. Zo hebben we tijdens de expo dag van de innovatiebeurs in Rotterdam ons toenmalige product getoond.
## presentaties 
`TODO: presentaties in algemene map als pdf bijvoegen`
`uitzoeken welke presentaties ik heb gedaan, linkjes bijvoegen naar betreffende presentatie`  
* [Week 3](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_3.pptx), Gepresenteerd door ... en Michiel.
* [Week 4](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_4.pptx), Gepresenteerd door ... en Michiel.
* [Week 5](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_5.pptx), Gepresenteerd door ... en Michiel.
* [Week 6](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_6.pptx), Gepresenteerd door ... en Michiel.
* [Week 12](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_12.pptx), Gepresenteerd door ... en Michiel.
* [Week 13](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_13.pptx), Gepresenteerd door Job en Michiel.
* [Week 14](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_14.pptx), Gepresenteerd door Job en Michiel.
* [Week 15](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_15.pptx), Gepresenteerd door Job en Michiel.
* [Week 16](https://github.com/KB-74/portfolio/blob/master/Presentaties/Presentation_Sprint_16.pptx), Gepresenteerd door Michiel.

