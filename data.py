import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
df=pd.read_csv("StudentsPerformance.csv")

data=df["reading score"].to_list()

mean=sum(data)/len(data)


median=statistics.median(data)


mode=statistics.mode(data)


print("mean,median and mode is {},{} and {}".format(mean,median,mode))


standardDivision=statistics.stdev(data)


first_standard_division_start,first_standard_division_end=mean-standardDivision,mean+standardDivision 
second_standard_division_start,second_standard_division_end=mean-(2*standardDivision),mean+(2*standardDivision)
third_standard_division_start,third_standard_division_end=mean-(3*standardDivision),mean+(3*standardDivision)\


list_within_1standardDivisision=[result for result in data if result>first_standard_division_start and result<first_standard_division_end]
list_within_2standardDivisision=[result for result in data if result>second_standard_division_start and result< second_standard_division_end]
list_within_3standardDivisision=[result for result in data if result>third_standard_division_start and result<third_standard_division_end]

print("{} % of data for height within 1 standard division".format(len( list_within_1standardDivisision)*100.0/len(data)))
print("{} % of data for height within 2 standard division".format(len(list_within_2standardDivisision)*100.0/len(data)))
print("{} % of data for height within 3 standard division".format(len(list_within_3standardDivisision)*100.0/len(data)))
