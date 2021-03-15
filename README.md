# BusOnTime 
![BusOnTime](https://i.imgur.com/IRymGE8.jpg)    
    
#### BusOnTime project is a POC for Israel's public transport performance rating using public data analysis. Using both Scheduled data (Called GTFS) and past real-time GPS locations for buses (Called SIRI), we created the platform for analyzing all trips performance and publishing it to the users via rest API and a web app UI.    
 ## Try it on https://purple-pond-0a34b4703.azurestaticapps.net/    
---
 ## :bus:  Current Available features:    
 **At this stage, our analysis is made on the trips departures: Is a scheduled trip departed? If it's late, what is the departure delay in minutes? We can answer those questions**    
- Search for a specific line data (all trips in selected days) and watch each trip departure verdict    
     
 - View general statistics - which operator tends to late more? Which lines are the best? and worst?    
     
 - See departure delays distribution by minutes (i.e. how many trips are late by 2 minutes?)    
    
- Available analyzed data: all trips made on selected 2 days - 2/8/20 and 3/8/20.  Updated data with much more days to select will be added soon.    
    
    
## :clipboard: Data sources:
 All raw data was taken from [The Public Knowledge Workshop (“HASADNA”)](https://www.hasadna.org.il/en/) In Israel, with the support of [Open-bus team](https://github.com/hasadna/open-bus). Their data is based on the public published data from [Israel's ministry of transportation.](https://www.gov.il/he/departments/general/real_time_information_siri)    
      
##  :rocket: Technologies:    
 - Raw data analysis - Python [Pandas](https://pandas.pydata.org/) library and Jupyter notebooks    
- API development- Python [Flask](https://flask.palletsprojects.com/) and [SQLAlchemy](https://www.sqlalchemy.org/) for database connection and modeling    
- Web app (Uses the API): ReactJS    
- #### For deployment:    
 - API node is hosted on [Heroku dyno](https://www.heroku.com/dynos)    
  - The Database is [AzureSQL](https://azure.microsoft.com/en-us/services/azure-sql/) (initially was on local sqlite, and later on postgres)    
  - The Web app is deployed with [Azure static web apps service](https://azure.microsoft.com/en-us/services/app-service/static/)    
    
## :floppy_disk: Code    
 - Data analysis and raw data - please contact me (Amit) for more details    
- API Backend - This Repository    
- Web app UI - Available on [this repo](https://github.com/OrLior/BusOnTime-App/tree/deploy) 
    
    
## :construction: Dev plan:    
 :white_check_mark: Done:    
- Initial plan and design    
- Raw data analysis with pandas    
- API & Web app development    
- Initial deployment on small sample data    
- Database migration from local sqlite to AzureSQL (also tested on PostgresSQL)     
    
:arrows_counterclockwise: In progress:    
- Web app UI improvements    
- Scaling from 2 days to 1 month data    
    
:white_circle: Planned:    
 - Automatic data updating and analyzed data archive    
- Major UI upgrade and more search and statistics features     
    
## :phone: For more information and docs:
 ### Amit Gabbay (Data and API):     
 [![GitHub](https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white) ](https://github.com/AmitGabbay) [      ![Mail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) ](mailto:amit.gabbay1@gmail.com) [![Linkedin](https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white) ](https://linkedin.com/in/amit-gabbay) 
 ### Or Lior (Front end web app):    
 [![GitHub](https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white) ](https://github.com/OrLior) [      ![Mail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) ](mailto:or.lior92@gmail.com ) [![Linkedin](https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/or-lior-7962b519b/)
