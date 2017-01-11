import quandl
import pandas as pd

api_key = open('apitext.txt', 'r').read()

##df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
##print(df.head())

fiddy_states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')

#this is a list:
#print(fiddy_states)

#this is a data frame:
#print(fiddy_states[0])

#this is a column:
#print(fiddy_states[0][1])

for abbv in fiddy_states[0][1][1:]:
    #print("FMAC/HPI_"+str(abbv))
    query = "FMAC/HPI_"+str(abbv)
    df = Quandl.get(query, authtoken=api_key)
