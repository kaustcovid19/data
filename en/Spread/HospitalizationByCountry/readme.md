HOSPITALIZATION PROJECTIONS (BIOSTATISTICS @ KAUST) 

Method: 

STEP 1. Generate the mean infection, susceptibility and removal rate for each country via the SIR model with country-specific inputs for the range of the infection factor (beta), range of the length of infection period (1/gamma). We developed the SIR simulator which is an  R-shiny app (developed by Marco Pinto, former member of the KAUST Biostatistics group). This app was based on the original python codes and notes on the SIR model by our collaborator Dr. David Ketcheson (Professor in the Applied Mathematics and Computational Science Program at KAUST). 

STEP 2. Using the rates in Step 1, generate the daily infections, susceptible and removal counts and the daily new infections. We are investigating a number of possible simulators for this step. 

In a working report (Ombao et al, KAUST Biostatistics), the procedure is to use the binomial simulator for to generate the observed number of counts (with mean parameter proportional to the mean counts derived from the SIR model). The new infection count for day t is equal to the number of susceptible at day (t-1) who moved into the infection group at day t. 

For this COVID-19 global dashboard, we use the output of the method by colleague Dr. Ketcheson as the observed daily new infection count. The procedure is described here.  


STEP 3. Simulate the number of daily new symptomatics which is in the range of 40-70% of those infected from about 5 days ago. 

STEP 4. From the new symptomatics, simulate the number requiring new daily hospitalization count (new admission) using the table derived by the Imperial College COVID-19 Response Team (source: Lancet paper, Table 3). This table is adjusted to each specific country’s demographics: the country-specific hospitalization rate is derived as a weighted average of the Lancet age-specific rate with weights proportional to the country’s age-specific census count. 

STEP 5. For each newly admitted patient, simulate the total number of days of hospital confinement which is negative binomial with mean within the range of 10-14 days and standard deviation equal to 3 days. NOTE: this range of values will have to be updated as more data becomes available. 

STEP 6. The total number of occupied beds per day is computed. Following 100K simulations, the results for the distribution of count of occupied beds per day is reported: median, 75th percentile and 97.5th percentile. 

COLLABORATORS: 

Faculty: Hernando Ombao (Biostatistics) Joaquin Ortega (Statistics), David Ketcheson (AMCS), 
      Paula Moraga (Statistics) 
Research Staff: Shuhao Jiao (Biostatistics), Fenqing Shao (Biostatistics), Wagner Barreto-Souza 
      (Biostatistics), Cintya Dutta (Biostatistics) 
Students: Matheus Bartolo Guerrero (Biostatistics and Extremes), Anass El Yaagoubi 
      (Biostatistics) and Guillermo Granados-Garcia (Biostatistics) 
Primary Programmers: Matheus Bartolo Guerrero (Biostatistics and Extremes) and Marco Pinto 
      (KAUST Biostatistics and City Univ Oslo).
