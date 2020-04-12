#!/usr/bin/python3

import pycurl
from io import BytesIO 
import time
import json
import pprint
from datetime import datetime
import csv
import datetime
import os



def getJSONFromURL(url):
    b_obj = BytesIO() 
    crl = pycurl.Curl() 
    crl.setopt(crl.URL, url)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform() 
    crl.close()
    return(json.loads(b_obj.getvalue()))

def getAllDocs(url, subreddit_lists):
    k = 0
    i = 0
    n = {}
    all_docs = []
    n['0'] = []

    for subreddit in subreddit_lists:
        if i < 20:
           n[str(k)].append(subreddit)
           i += 1
        else:
           i = 1
           k += 1
           n[str(k)] = []
           n[str(k)].append(subreddit)
    for k in n:
      tj = getJSONFromURL(url + '?q=&after={}&before={}&aggs=subreddit&size=0&subreddit={}'.format(TIME_START, TIME_END, ','.join(n[k])))
      all_docs += tj["aggs"]["subreddit"]
    return(all_docs)


def extractSubredditList(docs_dict):
    subreddit_list = []
    doc_count = 0
    for dic in docs_dict:
        doc_count += dic['doc_count']
        subreddit_list.append(dic['key'])
    return subreddit_list

def getCount(dic_list, key):
    for dic in dic_list:
        if dic['key'] == key:
           return dic['doc_count']
    return 0

def saveDiv(x, y):
    return 0 if y == 0 else x / y

def  getFinalList(all_docs, cov_docs, header):
     f_list = []
     for cor in cov_docs:
         total = getCount(all_docs, cor['key'])
         f_list.append({ header[0]: cor['key'], header[1]: cor['doc_count'], header[2]: total, header[3]: saveDiv(100*cor['doc_count'],total)})
     return f_list


def createCSVFile(filename, header, content):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = header
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, lineterminator=os.linesep)

        writer.writeheader()
        for line in content:
            writer.writerow(line)
        csvfile.close()


# Main
TIME_END = int(time.time())
TIME_START = TIME_END - 3600*24
today = datetime.date.today()
print(TIME_START)
print(TIME_END)

COMM_URL_COVID="https://api.pushshift.io/reddit/search/comment/?q=covid&after={}&before={}&aggs=subreddit&size=0".format(TIME_START, TIME_END)
COMM_URL_CORONA="https://api.pushshift.io/reddit/search/comment/?q=coronavirus&after={}&before={}&aggs=subreddit&size=0".format(TIME_START, TIME_END)
COMM_URL_ALL_DOC_SUBRED = "https://api.pushshift.io/reddit/search/comment/"


comm_json = getJSONFromURL(COMM_URL_COVID)
COMM_FINAL = getFinalList(getAllDocs(COMM_URL_ALL_DOC_SUBRED, extractSubredditList(comm_json["aggs"]["subreddit"])),
                          comm_json["aggs"]["subreddit"], ['SubredditName', 'SubredditCovidComments', 'SubredditTotalComments', 'CovidPct'])


BASEDIR = "/var/www/html/data/en/StateOfTheState/"

DATASET = "RedditCommentsCovidSubredds"
DATASET_FILE = DATASET + "-"
CSV_FILE = BASEDIR + DATASET + "/" + DATASET_FILE +today.strftime('%Y%m%d') + ".csv"
createCSVFile(CSV_FILE, ['SubredditName', 'SubredditCovidComments', 'SubredditTotalComments', 'CovidPct'], COMM_FINAL)

total_doc = searched_doc = subreddits = 0
for jsn in COMM_FINAL:
    total_doc += jsn['SubredditTotalComments']
    searched_doc += jsn['SubredditCovidComments']
    subreddits +=1

DATASET = "RedditCommentsCovidTotals"
DATASET_FILE = DATASET + "-"
CSV_FILE = BASEDIR + DATASET + "/" + DATASET_FILE +today.strftime('%Y%m%d') + ".csv"
createCSVFile(CSV_FILE, ['CovidCommentsTotal', 'TotalComments', 'CovidPct'], [{'CovidCommentsTotal': searched_doc, 'TotalComments': total_doc, 'CovidPct': 100*(searched_doc/total_doc)}] )


SUBM_URL_COVID="https://api.pushshift.io/reddit/search/submission/?q=covid&after={}&before={}&aggs=subreddit&size=0".format(TIME_START, TIME_END)
SUBM_URL_CORONA="https://api.pushshift.io/reddit/search/submission/?q=coronavirus&after={}&before={}&aggs=subreddit&size=0".format(TIME_START, TIME_END)
SUBM_URL_ALL_DOC_SUBRED = "https://api.pushshift.io/reddit/search/submission/"

subm_json = getJSONFromURL(SUBM_URL_COVID)
SUBM_FINAL = getFinalList(getAllDocs(SUBM_URL_ALL_DOC_SUBRED, extractSubredditList(subm_json["aggs"]["subreddit"])),
                          subm_json["aggs"]["subreddit"], ['SubredditName', 'SubredditCovidSubmissions', 'SubredditTotalSubmissions', 'CovidPct'])


DATASET = "RedditSubmissionsCovidSubredds"
DATASET_FILE = DATASET + "-"
CSV_FILE = BASEDIR + DATASET + "/" + DATASET_FILE +today.strftime('%Y%m%d') + ".csv"
createCSVFile(CSV_FILE, ['SubredditName', 'SubredditCovidSubmissions', 'SubredditTotalSubmissions', 'CovidPct'], SUBM_FINAL)

total_doc = searched_doc = subreddits = 0
for jsn in SUBM_FINAL:
    total_doc += jsn['SubredditTotalSubmissions']
    searched_doc += jsn['SubredditCovidSubmissions']
    subreddits +=1

DATASET = "RedditSubmissionsCovidTotals"
DATASET_FILE = DATASET + "-"
CSV_FILE = BASEDIR + DATASET + "/" + DATASET_FILE +today.strftime('%Y%m%d') + ".csv"
createCSVFile(CSV_FILE, ['CovidSubmissionsTotal', 'TotalSubmissions', 'CovidPct'], [{'CovidSubmissionsTotal': searched_doc, 'TotalSubmissions': total_doc, 'CovidPct': 100*(searched_doc/total_doc)}] )


exit(0)


