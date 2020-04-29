## This file is for dataset explanation written by Somayah Albaradei.
Here we provide the output file for arabic tweets sentimental analysis results. Each file corresponds to the sentimental analysis results of a spesific day. The file name 'CovSenAna-YYYYMMDD.csv', where YYYY represents year with 4 digits, MM represents month with 2 digits and DD represnts day with 2 digits.
Dataset structure as follows:
- Each file has 3 columns and 11 rows.
- The first column 'Category' represents the types of sentiments, 'Rate' represents the percentages for each category and 'HotWords' represents the top hot words in each category.
- Each row contains one Category type , the percentage of tweets corsponding to this type and the top hot words.
- The column 'Category' has 11 different types including "anger", "anticipation", "disgust", "fear", "confident", "empathetic", "optimism", "pessimism", "sadness", "surprise", "trust".
- The column 'Rate' has valuse range from 0 to 1; however ,as we study multilabels, it sums up to more than one!
- The column 'HotWords' is in the tuple formate, i.e., (word, word frequency). Here we provide the top 10 hot words in each category.

