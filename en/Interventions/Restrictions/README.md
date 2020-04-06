Each day download OxCGRT_Download_latest_data.xlsx file with the interventions from https://www.bsg.ox.ac.uk/sites/default/files/OxCGRT_Download_latest_data.xlsx

Then execute code.R that process the intervention and population data and create files that will be read to create the visualizations in the dashboard

**population.csv**

Static data I need to do calculations. Do not show this in the dashboard
  
Population data that has been downloaded from https://population.un.org/wup/Download/
File 18: Annual Total Population at Mid-Year by region, subregion and country, 1950-2050 (thousands) (accessed 1 April, 2020) (2020 data projected from 2018 data)

**countrycodes.csv**

Static data I need to do calculations. Do not show this in the dashboard

Numeric and alpha codes for each of the countries that has been downloaded from https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv


**Restrictions-YYYYMMDD.csv**

Created daily
  
For each country and day, interventions that are in place

Documentation is here: https://www.bsg.ox.ac.uk/sites/default/files/2020-03/BSG-WP-2020-031-v3.0.pdf


- Date: yyyy-mm-dd
- CountryCode: ISO3 code country
- CountryName: name country
- S1_School closing: Record closings of schools and universities
- S1_IsGeneral:
- S2_Workplace closing: Record closings of workplaces
- S2_IsGeneral:
- S3_Cancel public events: Record cancelling public events
- S3_IsGeneral:
- S4_Close public transport: Record closing of public transport
- S4_IsGeneral
- S6_Restrictions on internal movement: Record restrictions on internal movement
- S6_IsGeneral:
- S7_International travel controls: Record restrictions on international travel. coding is 0 - No measures, 1 - Screening, 2 - Quarantine on high-risk regions, 3 - Ban on high-risk regions
- StringencyIndex: Government Response Stringency Index


Coding for S1_School closing, S2_Workplace closing, S3_Cancel public events, S4_Close public transport, S6_Restrictions on internal movement is
0 - No measures, 1 - recommend closing, 2 - require closing
Coding for S1_IsGeneral, S2_IsGeneral, S3_IsGeneral, S4_IsGeneral, S6_IsGeneral is
0 - Targeted, 1- General
Missing values are NA

StringencyIndex: For each ordinal policy response measure S1-S7, we create a score by taking the ordinal value and adding one if the policy is general rather than targeted, if applicable. This creates a score between 0 and 2 and for S5, and 0 and 3 for the other six responses. We then rescale each of these by their maximum value to create a score between 0 and 100, with a missing value contributing 0.
Importantly, the Stringency Index should not be interpreted as a measure of the appropriateness or effectiveness of a government’s response. It does not provide information on how well policies are enforced, nor does it capture demographic or cultural characteristics that may affect the spread of COVID-10. Its value is instead to allow for efficient cross-national comparisons of government interventions.

