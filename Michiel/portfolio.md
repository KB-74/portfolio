Versie: 16-12-2018
`!!weghalen!!!:`  

`Darknet/ Yolo/ keras?`

`Additional portfolio requirements:`

`Include your Friday presentations  ``
Add screenshots of the online courses you have finished (DataCamp, Coursera, etc)  
Link to the Python Notebooks you have finished (you can dump them to PDF)  
List the tickets from the Scrum backlog that you worked on, linked to deliverables, own experiments, etc.  
Add any other assignment you feel is evidence of your abilities`

# Persoonlijke portfolio
Persoonlijke portfolio voor de minor Applied Data Science op de Haagse Hogeschool.  

|  | |
| ---: | :--- |
|Student:| <b>Michiel van Soest</b>|
|Studentnummer:| <b>15080803</b>|
|Groep:| <b>KB-74 Shipping</b>|
|Opdrachtgever:| <b>Port of Rotterdam</b>|

# Inhoudsopgave


* [Shipping "Floating Lab"](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#shipping-floating-lab)  
* [Courses](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#courses) 
* [Domain Knowledge](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#domain-knowledge) 
* [Predictive models](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#predictive-models) 
* [Data preperation](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#data-preparation) 
* [Data visialization](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#data-visualization) 
* [Data collection](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#data-collection) 
* [Evaluation](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#evaluation) 
* [Diagnostics of the learning process](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#diagnostics-of-the-learning-process) 
* [Communication](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#communication-presentations-summaries-paper-) 

### Notebooks
* [frame_checker](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/frame_checker.ipynb) 
* [picture_processing](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/picture_processing.ipynb) 
* [wall_labeler](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/wall_labeler.ipynb) 
* [pixel_walker_V2.1](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/pixel_walker_V2.1.ipynb)
* [video_extraction](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/video_extraction.ipynb)   
- object detection () uitleg erbij van eerst yolo, maar code geven van keras (wel door job grotendeels gedaan dit nieuwe) 

`linkjes naar elke paragraaf en notebook`
___
# Shipping "Floating Lab"
`TODO: Introductie project SHIP schrijven.`  
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
Voorafgaand aan dit project had ik zeer beperkte programeer ervaring. Deze kennis heb ik aangescherpt a.d.h.v. de aangeboden [Courses](https://github.com/KB-74/portfolio/blob/master/Michiel/portfolio.md#courses). en youtube videos.  
Daarnaast hebben we het SMASH (Smart shipping) event bezocht om kennis op te doen omtrent de veranderende kennis en regelgeving omtrent smart shipping.

Bovenstaande activiteiten hebben geholpen om de nodige features te onderscheiden en te analyseren om ons algoritme te laten werken.

# Predictive Models
Moeilijk om te doen gezien het live dtectie betreft
object detectie niet precies genoeg om voorspelling uit te voeren
doortrekken regressielijn is voorspelling kade?

`?? ons huidige algoritme beschijven?`

# Data preparation
De data die we in eerste instantie ontvangen hebben, bestaat uit een .avi videobestand met de output van een van de voorwaards gerichte camera's(camera 3).  
Om de data te kunnen gebruiken hebben we als eerste elk frame in de video met gebruik van opencv geëxporteerd als png. hiervan hebben we 250 willekeurige frames met een script gekozen en hernoemd tot frame 1 t/m 250 (het originele framenummer en welke daaraan gekoppeld is, is opgeslagen in een .json bestand).

We hebben gekozen om het water te labelen d.m.v. een mask met zwart en witte pixels. We hebben expliciet niet gekozen voor het labelen van objecten, gezien de al bestaande modellen omtrent objectdetectie (vb. Yolov3) niet  zomaar kunnen worden gesplit, en er niet genoeg data beschikbaar was gesteld om de beschikbare modellen te trainen.  

Om deze data te labelen heb ik een "framechecker" gemaakt. Deze vergelijkt de automatisch gelabelde data (gelabeld door ons bestaande algoritme voorland/water herkenning) met de bijpassende frame, door deze over elkaar heen te leggen.  
[Frame checker notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/frame_checker.ipynb)  
Door gebruik te maken van deze framechecker kan de goed gelabelde data gesplitst worden van de juist gelabelde data.  

`plaatje bijvoegen`

De verkeerd gelabelde data kon daarna correct gelabeld worden met een tooltje dat lijkt op de hiervoor getoonde Frame Checker.  
[Wall labeler notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/wall_labeler.ipynb)  
Halverwege is echter gekozen om Photoshop te gebruikenm gezien de magnet-lasso tool hier beter geschikt voor is.

`plaatje bijvoegen`

De 250 gelabelde frames waren naar ons inzicht echter niet genoeg. Om deze reden, en om verschillende situaties na te bootsen welke niet in onze dataset voorkomen, hebben we verschillende aanpassingen gedaan op de frames. Hoe dit gedaan is, is te zien in de picture processing notebook.  
[Picture Processing notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/picture_processing.ipynb)

`plaatje bijvoegen van de presentatie nog`

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

