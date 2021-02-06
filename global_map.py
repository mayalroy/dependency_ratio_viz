import numpy as mp
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import json
from bokeh.io import output_notebook, show, output_file, export_png
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer

sns.set(style="whitegrid", palette="pastel", color_codes=True)

shp_path = "/Users/mayaroy/Google Drive/Data/natural_earth_countries/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp"

f, ax1 = plt.subplots(figsize=(10, 6))

countries = gpd.read_file(shp_path)[['ADMIN', 'ADM0_A3', 'geometry']]

countries.columns = ['country', 'country_code', 'geometry']

ratio_data_path = "/Users/mayaroy/Google Drive/Data/Elder Care/WB_old_age_dependency/API_SP.POP.DPND.OL_DS2_en_csv_v2_1929275.csv"

ratio_data = pd.read_csv(ratio_data_path, skiprows=4)


ratio_data.drop(columns=['Indicator Name', 'Indicator Code'])

merged_data = countries.merge(ratio_data, left_on = 'country_code', right_on = 'Country Code')

#Handling missing values
#Replace NaN values to string 'No data'
merged_data.fillna('No data, inplace = True')

merged_json = json.loads(merged_data.to_json())
json_data=json.dumps(merged_json)

geosource = GeoJSONDataSource(geojson = json_data)

palette = brewer['YlGnBu'][8]
palette = palette[::-1]


#Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 30, nan_color = '#d9d9d9')

#Define custom tick labels for color bar.
tick_labels = {'0': '0%', '5': '5%', '10':'10%', '15':'15%', '20':'20%', '25':'25%', '30':'>30%'}

#Create color bar. 
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
border_line_color=None,location = (0,0), orientation = 'horizontal', major_label_overrides = tick_labels)


#Create figure object.
p = figure(title = 'Age dependency ratio, old (% of working-age population)', plot_height = 600 , plot_width = 950, toolbar_location = None)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

#Add patch renderer to figure. 
p.patches('xs','ys', source = geosource,fill_color = {'field' :'2016', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)

#Specify figure layout.
p.add_layout(color_bar, 'below')

export_png(p, filename="/Users/mayaroy/Documents/dependency_ratio_viz/output/global_2016.png")


