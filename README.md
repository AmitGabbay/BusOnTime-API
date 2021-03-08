
# BusOnTime

#### BusOnTime project is a POC for Israel's public transport performance rating using public data analysis. Using both Scheduled data (Called GTFS) and past real-time GPS locations for buses (Called SIRI), we created the platform for analyzing all trips performance and publishing it to the users via rest API and a web app.

### Try it on https://purple-pond-0a34b4703.azurestaticapps.net/
  
---
## :bus:  Current Available features:

##### At this stage, our analysis is made on the trips departures: Is a scheduled trip departed? If it's late, what is the departure delay in minutes? We can answer those questions
 - Search for a specific line data (all trips in selected days) and watch each trip departure verdict
 
 - View general statistics - which operator tends to late more? Which lines are the best? and worst?
 
 - See departure delays distribution by minutes (i.e. how many trips are late by 2 minutes?)

- Available analyzed data: all trips made on selected 2 days - 2/8/20 and 3/8/20.  Updated data with much more days to select will be added soon.


## :clipboard: Data sources: 

All raw data was taken from [The Public Knowledge Workshop (“HASADNA”)](https://www.hasadna.org.il/en/) In Israel, with the support of [Open-bus team](https://github.com/hasadna/open-bus). Their data is based on the public published data from [Israel's ministry of transportation.](https://www.gov.il/he/departments/general/real_time_information_siri)
  
##  :circus_tent: Technologies:

- Raw data analysis - Python [Pandas](https://pandas.pydata.org/) library and Jupyter notebooks
- API development- Python [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [SQLAlchemy](https://www.sqlalchemy.org/) for database connection and modeling
- Web app: ReactJS
- #### For deployment:
	- API node is hosted on [Heroku dyno](https://www.heroku.com/dynos)
	- The Database is [AzureSQL](https://azure.microsoft.com/en-us/services/azure-sql/) (initially was on local sqlite, and later on postgres)
	- The Web app is deployed with [Azure static web apps service](https://azure.microsoft.com/en-us/services/app-service/static/)

## :floppy_disk: Code

- Data analysis and raw data - please contact me for more details
- API - This Repository
- Web app - Available on [this repo](https://github.com/AmitGabbay/BusOnTime-App/tree/deploy) 


## :construction: Development phases plan
:white_check_mark: Initial plan and design
:white_check_mark: Raw data analysis with pandas
:white_check_mark: API & Web app development
:white_check_mark: Initial deployment on small sample data
:white_check_mark: Database migration from local sqlite to AzureSQL (also tested on PostgresSQL) 

In progress:

:arrows_counterclockwise: Web app UI improvements
:arrows_counterclockwise: Scaling from 2 days to 1 month data

Planned:

:white_circle: Automatic data updating and analyzed data archive
:white_circle: Major UI upgrade and more search and statistics features  