import pandas as pd
import math
import numpy as py
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import brewer   
from bokeh.models import Span, LinearColorMapper, ColumnDataSource, NumeralTickFormatter
dealer = pd.read_csv('F:\Python\Test\Demo.csv')
output_file('chart.htm')
p = figure(plot_width=1000, plot_height=700, title='Change in YOY Performance')
p.xaxis.axis_label = 'Change in Vehicle Sales'
p.yaxis.axis_label = 'Change in Contracts'
dealer['Good'] = (dealer['Change'] - dealer['VSC']).pow(2) / 2
dealer['Good'] = dealer['Good'].pow(1/2) * py.sign(dealer['Change'] - dealer['VSC'])
dealer['Units'] = dealer['Units'].pow(1/2)/500
print(dealer)
color_mapper = LinearColorMapper(palette='RdYlGn11') 
data_source = ColumnDataSource(dealer)
p.circle('Change', 'VSC', source=data_source, radius='Units', fill_alpha=0.6, color = {'field': 'Good', 'transform': color_mapper})
p.text(dealer['Change'], dealer['VSC'], dealer['Dealer'], text_color = 'black', text_font_size = '9pt', text_align='center', text_font_style='bold') 
vline=Span(location=0, dimension='height', line_color='black')
hline=Span(location=0, dimension='width', line_color='black')
p.renderers.extend([vline, hline])
p.xaxis.formatter=NumeralTickFormatter(format='0.%') 
p.yaxis.formatter=NumeralTickFormatter(format='0.%') 
p.title.align = 'center'
show(p)
