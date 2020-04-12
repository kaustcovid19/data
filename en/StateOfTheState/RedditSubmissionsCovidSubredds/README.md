**Dataset Name**:   RedditSubmissionsCovidSubredds

**Source**:  Reddit (via pushshift.io API)

**Frequency:** Daily

**Source Code:** RedditCommentsCovidSubredds/pysrc/extfeed-Pushshift.py

**Objectives:** *Analyze “comments” and “submissions” in top 100 subreddits that mentioned covid-19 in and 
quantify the occurrence of string “covid”.*

**Dataset file format:** CSV

**Fields:**

|Field| Description|
|--|--|
| SubredditName | Name of the subreddit |
| SubredditCovidSubmissions| Number of **submissions** mentioning word "covid" in that subreddit |
|SubredditTotalSubmissions|Total number of **submissions** in that subreddit|
|CovidPct|100*(SubredditCovidSubmissions/SubredditTotalSubmissions ) [%]|

