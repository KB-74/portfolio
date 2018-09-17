# Week 3

## code structuur

Een goede basis van een code structuur kan er voor zorgen dat de code kwaliteit enorm toeneemt. Het is dus in mijn optiek erg belangrijk om daar vroeg over na te denken. Dat begint bij een project structuur. Na wat expirimenteren ben ik tot de volgende structuur gekomen:
```
/ data
 -- / img
 -- / video
 -- / csv
 enz..
/ model
 -- model_dir (specific to each model)
/ docs
/ tests
/ package (specific to each package)
app.py
```
