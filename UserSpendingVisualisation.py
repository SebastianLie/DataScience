import json
import pandas as pd
import plotly.plotly as py
import cufflinks as cf
import plotly.graph_objs as go

'''
--- PostScript Comments ---

This code uses plotly to visualise user expenditure
and highlight 2 key points:

- How much they spent per month
- On which category of expenditure they spent the most each month

I use a stacked bar chart to do so.

First we read in data, then drop irrelevant columns and filter the cash flows we want,
then drop more irrelelvant columns.

Then we transform data into a form that can be worked on, and then obtain sum of
user expenditure by month and category, and use that
to plot our stacked bar chart.

Detailed comments on what each part of the code does are below.

Useful guides for Pandas:
https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/


__Instructions to other Users__

You need to have a plotly account to run this code.

Once run, it will appear as a project in your files.

To run this code, first use cmd to navigate to directory this code is in

and run:

python
import plotly
plotly.tools.set_credentials_file(username='DemoAccount', api_key='yourkey')

account used here: SebastianLie
api_key used here: 71NfOfHvH86uX8gzZBtH

'''

# Reading in data in the form of json files #

# both users are fictional.

filename = 'responsemary.json'  ## user 1
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

jdf = pd.DataFrame(datastore) # convert to dataframe to manipulate and clean


filename = 'responsejohn.json'  ## user 2
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

mdf = pd.DataFrame(datastore)  # same as above

to_drop = ['accountId',
           'referenceNumber',
           'transactionId']   # irrelevant info

mdf.drop(to_drop,inplace=True,axis=1)
jdf.drop(to_drop, inplace=True, axis=1) # drop irrelevant columns

# Dataframes contain financial inflows and outflows to user's bank account
# thus since we only want to visualise expenditure, we chooose debit

johndebit = jdf[jdf['type'] == 'DEBIT']   # get only expenditure for each user
marydebit = mdf[mdf['type'] == 'DEBIT']

## User 1 Plot ##

johndebit['amount'] = johndebit.amount.astype(float)   # first we transform data from obj to float so it can be added
johndebit['date'] = johndebit.date.astype(str)   # we convert date to string
johndebit['date'] = johndebit['date'].apply(lambda x: x[:7])  # and only use the month and year, going by daily expenditure is messy
johndebit.drop(['type'],inplace=True,axis=1)  # then drop type of cash flow, since is all expenditure

john_tptMonthly = johndebit[johndebit['tag'] == 'TRANSPORT']  # group cash flows into different categories
john_fnbMonthly = johndebit[johndebit['tag'] == 'F&B']
john_xferMonthly = johndebit[johndebit['tag'] == 'TRANSFER']

# now we sum expenditure of each category by month

john_tptMonthly = john_tptMonthly.groupby('date',as_index=False)[['amount']].sum() # special method to make date and amount per month accessible as df
john_fnbMonthly = john_fnbMonthly.groupby('date',as_index=False)[['amount']].sum()
john_xferMonthly = john_xferMonthly.groupby('date',as_index=False)[['amount']].sum()

## Plot begins here ##

# Now we create traces: these are the parts of each bar in the stacked bar chart,
# which contain the amount of money spent on each category per month
# each trace is one layer of the stacked bar chart

trace1 = go.Bar(
    x=john_tptMonthly['date'],
    y=john_tptMonthly['amount'],
    name='Transport'
)
trace2 = go.Bar(
    x=john_fnbMonthly['date'],
    y=john_fnbMonthly['amount'],
    name='F & B'
)
trace3 = go.Bar(
    x=john_xferMonthly['date'],
    y=john_xferMonthly['amount'],
    name='Transfer'
)

data = [trace1, trace2, trace3]  # combining traces
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='User1 Expenditure Visulisation Jan 2018 - Jan 2019') # and plot is done yay!!


marydebit['amount'] = marydebit.amount.astype(float)  # same as above
marydebit['date'] = marydebit.date.astype(str)
marydebit['date'] = marydebit['date'].apply(lambda x: x[:7])
marydebit.drop(['type'],inplace=True,axis=1)

mary_tptMonthly = marydebit[marydebit['tag'] == 'TRANSPORT']  # same as above
mary_fnbMonthly = marydebit[marydebit['tag'] == 'F&B']
mary_xferMonthly = marydebit[marydebit['tag'] == 'TRANSFER']


mary_tptMonthly = mary_tptMonthly.groupby('date',as_index=False)[['amount']].sum()  
mary_fnbMonthly = mary_fnbMonthly.groupby('date',as_index=False)[['amount']].sum()
mary_xferMonthly = mary_xferMonthly.groupby('date',as_index=False)[['amount']].sum()

## next Plot begins here

alttrace1 = go.Bar(
    x=mary_tptMonthly['date'],
    y=mary_tptMonthly['amount'],
    name='Transport'
)
alttrace2 = go.Bar(
    x=mary_fnbMonthly['date'],
    y=mary_fnbMonthly['amount'],
    name='F & B'
)
alttrace3 = go.Bar(
    x=mary_xferMonthly['date'],
    y=mary_xferMonthly['amount'],
    name='Transfer'
)

data = [alttrace1, alttrace2, alttrace3]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='User2 Expenditure Visulisation Jan 2018 - Jan 2019')  # and plot is done yay!!
