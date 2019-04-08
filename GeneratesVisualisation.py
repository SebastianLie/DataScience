# Get this figure: fig = py.get_figure("https://plot.ly/~SebastianLie/28/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~SebastianLie/28/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="User Financial Data (Ideasmash)", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~SebastianLie/28/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('SebastianLie', '71NfOfHvH86uX8gzZBtH')
trace1 = {
  "x": ["2018-01", "2018-02", "2018-03", "2018-04", "2018-05", "2018-06", "2018-07", "2018-08", "2018-09", "2018-10", "2018-11", "2018-12", "2019-01"], 
  "y": [207.20000000000002, 166.65999999999997, 285.1499999999999, 182.67, 286.85999999999996, 275.27, 148.17, 262.0, 203.24, 244.10000000000002, 268.28999999999996, 215.17000000000002, 178.65], 
  "name": "Transport", 
  "type": "bar", 
  "uid": "ac49b034-ad34-4326-8b0e-cff8af2b0055", 
  "xsrc": "SebastianLie:29:f4fa91", 
  "ysrc": "SebastianLie:29:9b74f0"
}
trace2 = {
  "x": ["2018-01", "2018-02", "2018-03", "2018-04", "2018-05", "2018-06", "2018-07", "2018-08", "2018-09", "2018-10", "2018-11", "2018-12", "2019-01"], 
  "y": [574.8899999999999, 452.4799999999999, 669.7199999999999, 571.5, 635.87, 626.88, 660.6400000000001, 602.3200000000002, 693.6399999999998, 669.6899999999999, 549.1399999999999, 631.51, 608.45], 
  "name": "F & B", 
  "type": "bar", 
  "uid": "2825b90c-85ae-4b3d-8fbe-c9de139ba462", 
  "xsrc": "SebastianLie:29:f4fa91", 
  "ysrc": "SebastianLie:29:c77542"
}
trace3 = {
  "x": ["2018-01", "2018-03", "2018-04", "2018-06", "2018-07", "2018-08", "2018-10", "2018-11", "2018-12", "2019-01"], 
  "y": [47.41, 105.25999999999999, 151.06, 52.19, 55.63, 46.95, 50.0, 50.86, 189.75, 148.81], 
  "name": "Transfer", 
  "type": "bar", 
  "uid": "a7be0fb4-518c-4223-9059-06a4e368fded", 
  "xsrc": "SebastianLie:29:f804d2", 
  "ysrc": "SebastianLie:29:b94aab"
}
data = Data([trace1, trace2, trace3])
layout = {"barmode": "stack"}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
