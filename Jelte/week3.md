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
Op dit moment gaan we niet verder met edge-detection omdat het te veel False Positief geeft. <br/>
Naast edge detection heb ik ook gekenen naar het bewerken van de foto's. Met het bewerken van de foto's
wordt bedoelt: het veranderen van Brightness, contrast, contour en het uitknippen van een bepaalt
gedeelte van de foto. De combinatie van het verhogen van de Brightness en het edge-dection filter was possitief. Hierdoor werden
minder False Positiefs ontdekt. [pixel_walker_edge_detection_v3](https://github.com/jobvink/wall_detection/blob/master/pixel_walker_edge_detection_v3.py)

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