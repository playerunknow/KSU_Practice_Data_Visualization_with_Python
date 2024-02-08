import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from pywaffle import Waffle
#import seaborn as sns
import folium
import plotly.graph_objects as go
import plotly.express as px


gas = pd.read_csv('gas_prices.csv')

# # LabelConfig for line plot
# plt.figure(figsize=(13, 8))
# plt.title('gas prices in USD', fontdict={'fontweight':'bold', 'fontsize':25}, c='y')
# plt.xlabel('Years', fontdict={'fontsize':20})
# plt.ylabel('Price in Dollars', fontdict={'fontsize':20}, c='g')
#
# # Line plot
# plt.figure(1)
#
# plt.plot(gas.Year, gas.USA, label='USA', lw=7, linestyle='--')
# plt.plot(gas.Year, gas.Canada, label='Canada',)
# plt.plot(gas.Year, gas['South Korea'], label='South Korea')
# plt.plot(gas.Year, gas.UK, label='UK', lw=5)
# plt.plot(gas.Year, gas.Mexico, label='Mexico')
# plt.plot(gas.Year, gas.Japan, label='Japan')
# plt.plot(gas.Year, gas.Italy, label='Italy',)
# plt.plot(gas.Year, gas.Germany, label='Germany')
# plt.plot(gas.Year, gas.France, label='France')
# plt.plot(gas.Year, gas.Australia, label='Australia')
#
# plt.xticks(gas.Year[::2])
#
# plt.legend()
# # plt.show()
#
# # Histogram
#
#
# plt.figure(figsize=(13, 8))
# plt.figure(2)
# plt.title("Histogram of Gas prices in USA", fontdict={'fontweight':'bold', 'fontsize':25})
# plt.xlabel("Years", fontdict={'fontsize':18})
# plt.ylabel('Price in Dollars', fontdict={'fontsize':18}, c="g")
#
# x_digits = gas.Year[::5]
# plt.hist(gas.USA, cumulative=True)
# # plt.show()
#
# # BarCharts
# plt.figure(figsize=(13, 8))
# plt.figure(3)
# plt.title("BarCharts of Gas prices in USA", fontdict={'fontweight':'bold', 'fontsize':25})
# plt.xlabel("Years", fontdict={'fontsize':18})
# plt.ylabel('Price in Dollars', fontdict={'fontsize':18}, c="g")
#
# plt.bar(gas.Year, gas.USA, width=0.2, color='g', align='edge')
# # plt.show()
#
# plt.figure(figsize=(13, 8))
# plt.figure(4)
# plt.title("BarChart of Gas prices in Canada", fontdict={'fontweight':'bold', 'fontsize':25})
# plt.xlabel("Years", fontdict={'fontsize':18})
# plt.ylabel('Price in Dollars', fontdict={'fontsize':18}, c="g")
# plt.bar(gas.Year, gas.Canada, width=0.4, color='r', edgecolor='g', lw=3)
# plt.xticks(gas.Year[::2])
#
# # plt.show()
#
# # Pie
#
#
# # Scatter
# plt.figure(figsize=(13, 8))
# plt.figure(5)
# plt.title("ScatterPlot of Gas prices", fontdict={'fontweight':'bold', 'fontsize':25})
# plt.xlabel("Years", fontdict={'fontsize':18})
# plt.ylabel('Price in Dollars', fontdict={'fontsize':18}, c="g")
#
# plt.scatter(gas.Year, gas.USA, label='USA', marker='*', c='#00f', s=200)
# plt.scatter(gas.Year, gas.Canada, label='Canada', alpha=0.3)
# plt.scatter(gas.Year, gas['South Korea'], label='South Korea')
# plt.scatter(gas.Year, gas.UK, label='UK')
# plt.scatter(gas.Year, gas.Mexico, label='Mexico', alpha=0.7)
# plt.scatter(gas.Year, gas.Japan, label='Japan',)
# plt.scatter(gas.Year, gas.Italy, label='Italy')
# plt.scatter(gas.Year, gas.Germany, label='Germany', alpha=0.9)
# plt.scatter(gas.Year, gas.France, label='France')
# plt.scatter(gas.Year, gas.Australia, label='Australia', alpha=0.6)
#
# plt.legend()
#
# # plt.show()
#
#
# # Multiplot_bar
#
# fig, axs = plt.subplots(2, 2)
#
# axs[0, 0].plot(gas.Year, gas.USA, label='USA', lw=7, linestyle='--')
# axs[0, 0].plot(gas.Year, gas.Canada, label='Canada',)
# axs[0, 0].plot(gas.Year, gas['South Korea'], label='South Korea')
# axs[0, 0].plot(gas.Year, gas.UK, label='UK', lw=5)
# axs[0, 0].plot(gas.Year, gas.Mexico, label='Mexico')
# axs[0, 0].plot(gas.Year, gas.Japan, label='Japan')
# axs[0, 0].plot(gas.Year, gas.Italy, label='Italy',)
# axs[0, 0].plot(gas.Year, gas.Germany, label='Germany')
# axs[0, 0].plot(gas.Year, gas.France, label='France')
# axs[0, 0].plot(gas.Year, gas.Australia, label='Australia')
# axs[0, 0].set_title('First')
#
#
# axs[0, 1].hist(gas.USA, cumulative=True)
# axs[0, 1].set_title('Second')
#
# axs[1, 0].bar(gas.Year, gas.USA, width=0.2, color='g', align='edge')
# axs[1, 0].set_title('Third')
#
#
# axs[1, 1].scatter(gas.Year, gas.USA, label='USA', marker='*', c='#00f', s=200)
# axs[1, 1].set_title('Fourth')
#
# # plt.show()
#
# plt.figure(7)
# ax = plt.axes(projection='3d')
# plt.title("Example of 3D", fontdict={'fontweight':'bold', 'fontsize':25})
# plt.xlabel("X", fontdict={'fontsize':18})
# plt.ylabel('Y', fontdict={'fontsize':18})
#
# x = np.random.random(555)
# y = np.random.random(555)
# z = np.random.random(555)
#
# ax.scatter(x, y, z)
#
# plt.show()

map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
map.save('map.html')
