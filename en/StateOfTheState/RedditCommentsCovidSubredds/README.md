**Dataset Name**: _RedditCommentsCovidSubredds_

**Source**:  Reddit (via pushshift.io API)

**Frequency:** Daily

**Source Code:** RedditCommentsCovidSubredds/pysrc/extfeed-Pushshift.py

**Objectives:** *Analyze “comments” and “submissions” in top 100 subreddits that mentioned covid-19 in and quantify the occurrence of string “covid”.*

**Dataset file format:** CSV

**Fields:**

|Field| Description|
|--|--|
| SubredditName | Name of the subreddit |
| SubredditCovidComments | Number of comments mentioning word "covid" in that subreddit |
|SubredditTotalComments|Total number of comments in that subreddit|
|CovidPct|100*(SubredditCovidComments/SubredditTotalComments ) [%]|


