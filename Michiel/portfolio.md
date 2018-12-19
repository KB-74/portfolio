Versie: 16-12-2018
`!!weghalen!!!:`
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
* [Xe](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/Xe.ipynb)
* [Y](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/Y.ipynb)   
`linkjes naar elke paragraaf en notebook`
___
# Shipping "Floating Lab"
`TODO: Introductie project SHIP schrijven.`  
Floating Lab is een samenwerkingsverband van verscheidene partijen, zoals Port of Rotterdam (PoR), CGI en de Haagse Hogeschool (HHS). PoR biedt de RPA3 (boot uitgerust met camera's en overige sensoren) ter beschikking aan de andere partijen om algoritmen en software te ontwikkelen om autonoom varen mogelijk te maken.  

Wij (Groep SHIP) werken namens de HHS aan beeldherkenning van verscheidene dingen zoals: land/water en objectherkenning.  

### RPA3
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/rpa3.jpg"> </p>

# Courses
Om bovenstaande algoritmen en software te kunnen ontwikkelen heb ik voor zover mogelijk de nodige kennis opgedaan met Datacamp en Coursera. Op onderstaande afbeeldingen is te zien welke courses ik precies heb afgerond.  

<b>Datacamp</b>
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/datacamp_michiel.png"> </p>  
<b>Coursera</b>
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/coursera_michiel.png"> </p>

# Domain Knowledge
`Welke features zijn belangrijk bij onze algoritmen?`

# Predictive Models
`?? ons huidige algoritme beschijven?`

# Data preparation
De data die we in eerste instantie ontvangen hebben, bestaat uit een .avi videobestand met de output van een van de voorwaards gerichte camera's(camera 3).  
Om de data te kunnen gebruiken hebben we als eerste elk frame in de video met gebruik van opencv geëxporteerd als png. hiervan hebben we 250 willekeurige frames met een script gekozen en hernoemd tot frame 1 t/m 250 (het originele framenummer en welke daaraan gekoppeld is, is opgeslagen in een .json bestand).

We hebben gekozen om het water te labelen d.m.v. een mask met zwart en witte pixels. We hebben expliciet niet gekozen voor het labelen van objecten, gezien de al bestaande modellen omtrent objectdetectie (vb. Yolov3) niet  zomaar kunnen worden gesplit, en er niet genoeg data beschikbaar was gesteld om de beschikbare modellen te trainen.  

Om deze data te labelen heb ik een "framechecker" gemaakt. Deze vergelijkt de automatisch gelabelde data (gelabeld door ons bestaande algoritme voorland/water herkenning) met de bijpassende frame, door deze over elkaar heen te leggen.  
[Frame checker notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/frame_checker.ipynb)  
Door gebruik te maken van deze framechecker kan de goed gelabelde data gesplitst worden van de juist gelabelde data.  


De verkeerd gelabelde data kon daarna correct gelabeld worden met een tooltje dat lijkt op de hiervoor getoonde Frame Checker.  
[Wall labeler notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/wall_labeler.ipynb)  
Halverwege is echter gekozen om Photoshop te gebruikenm gezien de magnet-lasso tool hier beter geschikt voor is.

De 250 gelabelde frames waren naar ons inzicht echter niet genoeg. Om deze reden, en om verschillende situaties na te bootsen welke niet in onze dataset voorkomen, hebben we verschillende aanpassingen gedaan op de frames. Hoe dit gedaan is, is te zien in de picture processing notebook.  
[Picture Processing notebook](https://github.com/KB-74/portfolio/blob/master/Michiel/Notebooks/picture_processing.ipynb)

Aanpassingen die uitgevoerd zijn, zijn:  

|  | |
| :--- | :--- |
|brightness| [0.3,1.4]|        # [0.4,0.5,0.6,0.7,0.8,0.9,1.1,1.2,1.3,1.4]
|contrast| [0.3,1.4]|        # [0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.3,1.4]
|sharpness| [5.0,20.0]|        # [5.0, 10.0, 15.0, 20.0]
|color| [0.0,10.0]|            # [0.0, 3.0, 6.0, 10.0]
|mirrored image| [1]|

Bijghorende masks worden in deze notebook ook automatisch met bijbehorend framenummer meegekopieerd/ aangepast.
`picture processing notebook`
`frame checker`
`wall labeler`

# Data Visualization
`picture processing notebook`
`frame checker`
`wall labeler`

# Data collection
`video extraction`
`picture processing notebook`

# Evaluation
`picture processing notebook`
`frame checker`
en filmpjes

# Diagnostics of the learning process
`verhaaltje?`

# Communication (presentations, summaries, paper, ...)
## presentaties 
`TODO: presentaties in algemene map als pdf bijvoegen`
`uitzoeken welke presentaties ik heb gedaan, linkjes bijvoegen naar betreffende presentatie`  
* [Week X](Link naar de powerpoint!!), Gepresenteerd door ... en Michiel.
* [Week X](Link naar de powerpoint!!), Gepresenteerd door ... en Michiel.
* [Week X](Link naar de powerpoint!!), Gepresenteerd door ... en Michiel.
* [Week X](Link naar de powerpoint!!), Gepresenteerd door ... en Michiel.


# Kade herkenning


## Evaluation

### precision / recall

#notebooks
`TODO: alle code omzetten naar python notebooks`
`TODO: uitzoeken waaraan en wat ik heb gedaan in welk notebook`
`TODO: comments toevoegen in notebook met uitleg`
`TODO: evt. uitleggen waarom ik bepaalde dingen heb gedaan en hoe`

`Algemeen mapje aanmaken waar alle notebooks komen`
- picture processing
- frame checker
- pixel walker (euclidian distance deel?)
- wall labeler
- video extraction ()deeltje
- object detection () uitleg erbij van eerst yolo, maar code geven van keras (wel door job grotendeels gedaan dit nieuwe) 



