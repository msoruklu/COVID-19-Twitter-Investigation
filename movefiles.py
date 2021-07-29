import os
from os import path
import shutil

src = "./COVID-19-TweetIDs"
dst = "./final_data"

months = ["2020-03","2020-07","2020-10","2021-03","2021-06"]
days = ["07","14","21","28"] #take days 7th,14th,21st and  28th from each month
hours = ["15"] #take tweets posted between 15:00 and 16:00 for each day

sources = []
for month in months: 
  for day in days:
    for hour in hours:
      source = "./{}/coronavirus-tweet-id-{}-{}-{}.txt".format(month,month,day,hour)
      sources.append(source)


for f in sources:
    shutil.copy(f, dst)

#also add 1 day from 2020 January since it starts from 21st of Junuary, take 25t of that month
shutil.copy("./2020-01/coronavirus-tweet-id-2020-01-25-15.txt", dst)
