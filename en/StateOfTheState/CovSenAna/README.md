#This file is for dataset explanation written by Qiang Yang.
1. Each file corresponds to the sentimental analysis results of each day. And it is named as the CovSenAna-YYYYMMDD.csv where YYYYMMDD represents year with 4 digitals, month with 2 digitals and day with 2 digitals.

2. Dataset structure is shown as follows:
1) Each dataset has 3 columns and 11 rows. 
2) For the columns, 'Category' means the types of sentiments, 'Rate' means the what percentages are for each type and 'HotWords' means what hot words are for each type. 
3) For the rows, each of them means the name of the Category, the percentage of the current category and the hot words it owns.
4) For the field 'Category', it has 11 different sentiments including "anger", "anticipation", "disgust", "fear", "confident", "empathetic", "optimism", "pessimism", "sadness", "surprise", "trust".
5) For the field 'Rate', it ranges from 0 to 1.
6) For the field 'HotWords', it is in the tuple formate, i.e., (word, word frequency). Here we provide the top 20 hot words in its corresponding category.