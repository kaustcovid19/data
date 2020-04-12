**Dataset Name**:   RedditCommentsCovidTotals
**Source**:  Reddit (via pushshift.io API)

**Frequency:** Daily

**Source Code:** RedditCommentsCovidSubredds/pysrc/extfeed-Pushshift.py

**Objectives:** *Analyze “comments” and “submissions” in top 100 subreddits that mentioned covid-19 in and 
quantify the occurrence of string “covid”.*

**Dataset file format:** CSV

**Fields:**

|Field| Description|
|--|--|
|CovidCommentsTotal| Total number of **comments** mentioning word "covid" in top-100 subreddits |
|TotalComments|Total number of **comments** in top-100 subreddits|
|CovidPct|100*(CovidCommentsTotal/TotalComments) [%]|


