Versie: 12-11-2018

`LET OP
Portfolio moet volgende bevatten (weghalen bij inleverdatum)`
- 1 file (deze)
- courses
- domain knowledge
- voorspel model
- Data preparatie
- Data visualisatie
- Data collectie
- Data evaluatie
- leeproces
- communicatie en presentaties

# Persoonlijke portfolio  
Persoonlijke portfolio voor de minor Applied Data Science op de Haagse Hogeschool.  

Student: Michiel van Soest
Studentnummer: 15080803

## Introductie
`TODO: Introductie project SHIP schrijven.`

## Woordenlijst
`TODO: betere naam dan woordenlijst verzinnen`
`TODO: woorden die specifiek voor SHIP zijn bijvoegen` 

## Courses
Voor deze minor zijn verschillende courses gevolgd om de benodigde kennis op te doen, namelijk:

### DataCamp
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/datacamp_michiel.png"> </p>

`TODO: uitleg waarom deze en wat precies gedaan is`  

### Coursera: Machine Learning by Stanford University
<p align="center"> <img src="https://github.com/KB-74/portfolio/blob/master/Michiel/pictures/coursera_michiel.png"> </p>
Did not do a lot of Coursera yet, am planning on finishing it within 7 days from now (29-10-2018).


## Vrijdagse presentaties 
`TODO: presentaties in algemene map als pdf bijvoegen`
`uitzoeken welke presentaties ik heb gedaan, linkjes bijvoegen naar betreffende presentatie`  
The weekly Opschaler presentations that I contributed to.
* [Week X](Link naar de powerpoint!!), Gepresenteerd door ... en Michiel.


## Python notebooks
`TODO: alle code omzetten naar python notebooks`
`TODO: uitzoeken waaraan en wat ik heb gedaan in welk notebook`
`TODO: comments toevoegen in notebook met uitleg`
`TODO: evt. uitleggen waarom ik bepaalde dingen heb gedaan en hoe`
All notebooks have been commented, apart from lines where the programming is basic Python (for data science). Besides commenting code, i try to document all changes by committing small changes to GitHub. Doing this helped to document the work being done. However, the amount of commits obviously is no estimate of the quality of the work.  

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/github_commits_v2.png"> </p>
  
Quite a lot of notebooks which are relevant for Opschaler have been created. Most started out as smaller notebooks, to learn the programming techniques required for the job. Later on a lot of the smaller notebooks have been combined in larger important notebooks. Important notebooks have been marked with a (!), really important ones are marked with a (!!). These are notebooks that contain main code for Opschaler.  
  
The notebooks that have been made for Opschaler are:
  
* Data preperation  
This is the process of preparing the raw data for analysis, getting the data in easy useable DataFrames. The raw data consists of sensor data per dwelling, smartmeter data per dwelling and KNMI weather data of a station in Rotterdam. The smartmeter dataframes consists of merged electricity and gasmeter frames. Certain datafiles are in nested folders, with each file having a uniqiue name. The file types are both `.csv` and `.xlsx`. 
  * Reading in data 
    * Reading in raw sensor + excel data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Reading%20_in_data/reading_in_raw_sensor%2Bexcel_data.ipynb)
    * Reading in raw smartmeter data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Reading%20_in_data/reading_in_raw_smartmeter_data.ipynb)
    * Reading in raw weather data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Reading%20_in_data/reading_in_raw_weather_data.ipynb)

  * Cleaning & combining data  
    * Combining weather, electricity and gas data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Cleaning_combining_data/Combining%20weather%2C%20electricity%20and%20gas%20data.ipynb)
    * Cleaning house data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Cleaning_combining_data/cleaning_excel_data.ipynb)

  * NaN checker  
    * DataFrame NaN checker: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/NaN_checker/df_NaN_checker.ipynb)
    * Drop NaN streaks above set threshold: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/NaN_checker/drop_nan_streaks_above_threshold.ipynb)

  * Main data preperation notebooks: Reading, cleaning & combining all dwellings
    * (!) Data preperation main notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/data_preperation_main.ipynb)
    * Loading combined smart, gas and weather generalized notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/loading_combining_smart_gas_weather_generalized.ipynb)
    * (!) Creating one DataFrame for all dwellings: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Create%20one%20df%20for%20all%20dwellings.ipynb)

* KNMI  
In these notebooks the 10 minute resolution weather data is processed. This data has been received by mail from the KNMI. The raw data consists of a folder with multiple `.csv` files. There are different file types depending on the measured variables and the year in which the values were measured.  
  * (!) Combining DataFrames: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/1.KNMI_high_resolution_combining_dfs.ipynb)
  * (!) Cleaning DataFrames: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/2.KNMI_high_resolution_cleaning_df.ipynb)
  * Exploratory Data Analysis (EDA): [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/KNMI%20visualization.ipynb)

* (!) EDA  
Notebooks that contain general EDA on the created DataFrames which contain all the combined raw data per dwelling. Plus a table containing usefull information per dwelling has been created. 
  * EDA on dwelling P01S01W8655: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/EDA%20on%20dwelling%20P01S01W8655.ipynb)
  * Raw dwelling information table: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/Raw%20dwelling%20information%20table.ipynb)
  * Reading in all dwellings, plus making correlation matrices: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/reading%20in%20%26%20correlation%20matrices%20on%20processed%20data.ipynb)
  
* PyCharm  
The 'data_preperation_main.py' file used to be the main script to create the prepared dwelling data. Later on Dask has been implemented due to having improved performance because of being able to parallelize tasks on multiple CPU cores.  
  * (!) Data preperation main script: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/reading%20in%20%26%20correlation%20matrices%20on%20processed%20data.ipynb)
  * Data preperation main test notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/pycharm/data_preperation_main_test_notebook.ipynb)
  * EDA on processed data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/pycharm/EDA%20on%20processed%20data.ipynb)
 
* Dask  
Currently (29-10-2018) this is the main notebook for all the data processing done for the Opschaler project. This notebook has implemented most relevant functions from previously listed notebooks in a way so they can be run in parallel with Dask. It basically takes all raw data and saves unprocessed and processed (NaNs taken care off) `.csv` files per dwelling, which can be used for analysis.
  * (!!) Dask data processing: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Dask/Dask%20data%20processing.ipynb)

* Keras  
This folder contains all the notebooks related to deep learning. Note that there are multiple notebooks being very similar to each other. Sometimes the only difference inbetween similar notebooks are changes in settings (nodes, layers and selected dwellings). Most notebooks start off with EDA to check if the correct data is being used, then the model is being created and evaluated.
  * Feedforward
    * All dwellings EDA + machine learning: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/all%20dwellings%20EDA%20%2B%20machine%20learning.ipynb)  
  Notebooks containing feedforward models.  
    * 8655 gasPower, sample rate 1 day: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/8655%20gasPower%201D.ipynb)
    * 8655 gasPower, higher sample rate: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/8655%20gasPower%20higher%20resolution.ipynb)
  * Hyper parameter optimization  
  Notebook that tries out different network architectures and shows all the results. This can be used to evaluate and choose between different architectures and hyperparameters. 
    * Hyperparameter optimization (Only feedforward for now 29-10-2018): [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/Hyperparameter%20optimization.ipynb)
  * LSTM  
  Notebook used to learn how LSTM time series prediction works.
    * (!) 8655 RNN LSTM: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/LSTM/8655%20RNN%20LSTM.ipynb)
  * sequence to sequence  
  Notebook used to learn how sequence to sequence time series prediction works.
    * 8655 seq2seq: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/seq2seq/8655%20seq2seq.ipynb)
    * General seq2seq: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/seq2seq.ipynb)
   * Opschaler LSTM & seq2seq main  
   These notebooks contain the currently (29-10-2018) being used deep learning models. There also is a notebook where the input data shape of LSTM has been analyzed. This has made because it was quite unclear how this actually was done, dispite reading a lot of literature about it.  
     * (!) LSTM data preperation: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/LSTM%20data%20preperation.ipynb)
     * (!!) LSTM & seq2seq for gasPower prediction: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/LSTM.ipynb)
       * Results  
       Pictures of current results. For 'single layer LSTM' a single LSTM input layer of size 35 has been used. The input data is of an hourly sample rate. The previous 5*24 samples have been used as timesteps (also known as look back). The mean of gasPower from all dwelling from `all_dwellings_combined_hour.csv` per datetime value has been taken. Avarage error is the average percentage difference between the predicted and true value. The original images can be downloaded to get view them in high resolution.  
          * Single layer LSTM result with a hourly sample rate: <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/LSTM%20result%20hourly%2029-10-2018.png"> </p>
          * Single layer LSTM result with a daily sample rate: <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/LSTM%20result%20hourly%20resampled%20to%20daily%20by%20sum%2029-10-2018.png"> </p>
          * Sequence 2 sequence with a hourly sample rate: <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/seq2seq%20result%20hourly%2029-10-2018.png"> </p>
          * Sequence 2 sequence with a daile sample rate: still need to create this
   

**Note about shared work:** `PyCharm: Data preperation main script` and `Dask: Dask data processing` contain functions which were made by other group members. Some of these functions (NaN figure for example) have been adapted and changed by me. Besides that, all listed notebooks are made by me.

## Scrum
`TODO: Don't link individual tickets, possibly show a screenshot of each task board.`  
`TODO: Combine these tickets with the notebooks. `  
`TODO: Say that after week 10 we stopped using Scrum due to it not being particulary usefull (in the way it should be used) for our research.`  
The guidelines set up by the minor make it mandatory to use Scrum. We are doing small sprints with a length of 2 weeks. Personally I like to do the most throughout documentation in GitHub with for example commits. However, I did use Scrum to document my time spend on tasks related to the minor.  
* [Sprint 1](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-1/id-84641-11359-18)  
It seems that a lot of Scrum tickets are missing.
  * (3h) Datacamp course 1+2
  * (2h) Visualizing practise data: create practise data for the group, to create visualizations from.
* [Sprint 2](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-2/id-84641-11359-120)  
It seems that a lot of Scrum tickets are missing.
  * (14h) Cleaning data
* [Sprint 3](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-3/id-84641-11359-158)
  * (7.5h) NaN information per dwelling, one large table
  * (33h) Datacamp KB-74 assignments
  * (4h) NaN streak checker function
  * (5h) NaN checker plot function
  * (4h) EDA on dwelling P01S01W8655
  * (3h) Correlation heatmaps of all dwellings
  * (2h) EDA + multi variate regression on all dwellings
  * (8h) Prepare dwelling dataframes (unprocessed)
  * (1h) Combine dataframes (smartmeter, weather)
  * (20h) Prepare dwelling dataframes (processed)
  * (5h) Prepare high resolution weather df
  * (2h) GitHub README: document important notebooks & datalocations
  * (1.5h) Create two files which contain all the 'combined_gas_smart_weather_dfs'
  * (2h) Correctly document my own Scrumwise tasks
  * (8h) Preprocessing data for deep learning
* [Sprint 4](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-4/id-84641-11393-72)  
A lot of time has gone into certain tasks due to searching for literature, reading literature and learning how certain things should be done.
  * (7.5h) NaN information per dwelling, in one large table
  * (8h) Preprocessing data for deep learning
  * (35h) Basic LSTM & seq2seq
  * (35h) Feedforward NNs
  * (8h) Hyperparameter optimazation
  * (18h) Preprocessing for LSTM

## Other
Other contributions to the project / learning progress, worth mentioning.

### GitHub
Introduced the group to GitHub and made some resources that help with the setup and usage of GitHub at the datascience server. It can be clearly seen when project Opschaler has been started, as pointed out by the red arrow below. 

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/github_start_of_opschaler.png"> </p>

* Setup a GitHub environment for the project, plus keep maintaining it: [link](https://github.com/deKeijzer/KB-74-OPSCHALER)  
* Made a README for the project members containing information on how to setup GitHub on the datascience server, plus general important information about the project: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/README.md)  
* Made a GitHub push & pull tutorial: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/GitHub%20push%20%26%20pull%20tutorial.ipynb)  
* Created .bat files to run [jupyter lab](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/jupyterlab.bat), [run notebooks](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/run_notebook.bat) and do [ssh portforwarding](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/ssh%20portforward.bat) for usage at your local computer.
