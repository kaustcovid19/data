### COVID-19 World-Wide

**Data Sources**

Download files  of COVID-19  (Cases and death) data from  (JHU)

https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series

Then WorldCasesEffectiveR.R  and WorldDeathsEffectiveR.R  process the  data and create .csv files 

**Data/Population_data-2020.csv**

Static data need to do read country code. Do not show this in the dashboard
  
Population data that has been downloaded from https://population.un.org/wup/Download/
File 18: Annual Total Population at Mid-Year by region, subregion and country, 1950-2050 (thousands) (accessed 1 April, 2020) (2020 data projected from 2018 data)


**WorldEffRCases-YYYYMMDD.csv**

Created daily on Cases data World-Wide for each country

- CountryCode: ISO3 code country
- Country: name country
- Date: yyyy-mm-dd
- Rt: Effective reproduction number 

**WorldEffRDeaths-YYYYMMDD.csv**

Created daily on Death data World-Wide for each country

- CountryCode: ISO3 code country
- Country: name country
- Date: yyyy-mm-dd
- Rt: Effective reproduction number 
  
  
  ######################
  ### COVID-19 Data Source US States
  Each day download files of  U.S. State-Level Data
  NewYork Times: https://github.com/nytimes/covid-19-data/blob/master/us-states.csv
  
  Then USCasesEffectiveR.R  and USDeathEffectiveR.R  process the  data and create files 

**USCasesEffR-YYYYMMDD.csv**

Created daily on Cases data for US states for each country

- CountryCode: ISO3 code country
- Country: name country
- Date: yyyy-mm-dd
- Rt: Effective reproduction number 
  

**USDeathsEffR-YYYYMMDD.csv**

Created daily on Death data for US states for each country

- CountryCode: ISO3 code country
- Country: name country
- Date: yyyy-mm-dd
- Rt: Effective reproduction number 


**Analysis**
Daily Caculated effective reproduction number (Rt) based on 5-days sliding window using statistical R  **EpiEstim** package. We used a discrete 
γ distribution with a mean of 4.8 days and a standard deviation of 2.5 for the serial interval distribution. 

Calculated the estimate to each country  world-wide and US-States where the COVID-19 incident has at least a 7-day growth period, and where the cumulative cases/deaths was at least 100.
