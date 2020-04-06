Each day download OxCGRT_Download_latest_data.xlsx file with the interventions from https://www.bsg.ox.ac.uk/sites/default/files/OxCGRT_Download_latest_data.xlsx

Then execute code.R that process the intervention and population data and create files that will be read to create the visualizations in the dashboard

**population.csv**

Static data I need to do calculations. Do not show this in the dashboard
  
Population data that has been downloaded from https://population.un.org/wup/Download/
File 18: Annual Total Population at Mid-Year by region, subregion and country, 1950-2050 (thousands) (accessed 1 April, 2020) (2020 data projected from 2018 data)

**countrycodes.csv**

Static data I need to do calculations. Do not show this in the dashboard

Numeric and alpha codes for each of the countries that has been downloaded from https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv


**DateRestrictionInternalMovementTargeted-YYYYMMDD.csv**

Created daily

  
Dates each country put a restriction on internal movement (category targeted applied to part of the country) 

- CountryCode: ISO3 code country
- CountryName: name country
- Date: yyyy-mm-dd

