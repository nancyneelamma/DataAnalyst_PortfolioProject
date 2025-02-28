#Importing necessary libraries 

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fetching the Url

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

print(page)


#Retriving the data from that webbsite page and parsing it in html format

soup = BeautifulSoup(page.text, 'html')
print(soup)


# Retriving the data for the first table on the website, also the table is in list format

table_name= soup.find_all('table')[0]
print(table_name)


#So the table header i.e., column names are in th tag

table_title = table_name.find_all('th')
print(table_title)


# Remove the th tags and convert them into text format using list comprehenssion

text_table_title = [titles.text.strip() for titles in table_title]
print(text_table_title)


# Adding these table headers into the Data Frame

data=pd.DataFrame(columns=text_table_title)
data


# Retrive the all the records

column_data = table_name.find_all('tr')
print(column_data)

# To retrive data individually we need to iterate

for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_records=[row_records.text.strip() for row_records in row_data]
    print(individual_records)
    #Find the length of the entire data present and then allocate it individually
    data_length = len(data)
    data.loc[data_length]=individual_records


# Then add the data to the csv file and save it in local machine

data.to_csv(r'C:\Users\Nancy\Desktop\del\DataAnalyst_ProjectPortfolio\Python\Companies_Revenue.csv',index=False)






