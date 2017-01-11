import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('apitext.txt', 'r').read()

##df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
##print(df.head())


def state_list():
    fiddy_states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
    return fiddy_states[0][1][1:]
#this is a list:
#print(fiddy_states)

#this is a data frame:
#print(fiddy_states[0])

#this is a column:
#print(fiddy_states[0][1])


def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()
    
    

    for abbv in states:
        #print("FMAC/HPI_"+str(abbv))
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df[abbv] = (df[abbv]-df[abbv][0])/df[abbv]*100
    
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, lsuffix=abbv)

    print(main_df.tail())

    pickle_out = open('fiddy_states2.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

grab_initial_state_data()

##pickle_in = open('fiddy_states.pickle', 'rb')
##HPI_data = pickle.load(pickle_in)
#print(HPI_data)
##
##HPI_data.to_pickle('pickle.pickle')
##HPI_data2 = pd.read_pickle('pickle.pickle')
##print(HPI_data2)

##HPI_data = pd.read_pickle('fiddy_states2.pickle')
##
##HPI_data.plot()
##plt.legend().remove()
##plt.show()







