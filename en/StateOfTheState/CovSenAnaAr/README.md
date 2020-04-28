{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## This file is for dataset explanation written by Somayah Albaradei.\n",
    "Here we provide the output file for arabic tweets sentimental analysis results. Each file corresponds to the sentimental analysis results of a spesific day. The file name 'CovSenAna-YYYYMMDD.csv', where YYYY represents year with 4 digits, MM represents month with 2 digits and DD represnts day with 2 digits.\n",
    "Dataset structure as follows:\n",
    "- Each file has 3 columns and 11 rows.\n",
    "- The first column 'Category' represents the types of sentiments, 'Rate' represents the percentages for each category and 'HotWords' represents the top hot words in each category.\n",
    "- Each row contains one Category type , the percentage of tweets corsponding to this type and the top hot words.\n",
    "- The column 'Category' has 11 different types including \"anger\", \"anticipation\", \"disgust\", \"fear\", \"confident\", \"empathetic\", \"optimism\", \"pessimism\", \"sadness\", \"surprise\", \"trust\".\n",
    "- The column 'Rate' has valuse range from 0 to 1; however ,as we study multilabels, it sums up to more than one!\n",
    "- The column 'HotWords' is in the tuple formate, i.e., (word, word frequency). Here we provide the top 10 hot words in each category.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
