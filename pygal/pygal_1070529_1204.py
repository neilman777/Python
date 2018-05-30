
#1070529_1204

# To install, just type as superuser:
# !sudo pip install pygal
#-------------------------------------------------------------------
import pygal

#-------------------------------------------------------------------
#lxml which can improve rendering speed (except on pypy).
#!pip3 install lxml
import lxml

#cairosvg, tinycss, cssselect to render png.
#!pip3 install cairosvg
import cairosvg

#!pip3 install tinycss
import tinycss

#!pip3 install cssselect
import cssselect
#-------------------------------------------------------------------

bar_chart = pygal.Bar() 

#-------------------------------------------------------------------

def date_chart():

# Time
	from datetime import datetime, timedelta
	date_chart = pygal.Line(x_label_rotation=20)
	date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
	 datetime(2013, 1, 2),
	 datetime(2013, 1, 12),
	 datetime(2013, 2, 2),
	 datetime(2013, 2, 22)])
	date_chart.add("bb106", [300, 412, 823, 672])
	date_chart.render()

	bar_chart = pygal.HorizontalStackedBar()
	bar_chart.title = "bb106"
	bar_chart.x_labels = map(str, range(11))
	bar_chart.add('positive', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
	bar_chart.add('negative', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])


	#bar_chart.render()
	bar_chart.render_to_file('555.svg') 
	bar_chart.render_to_png(filename='555555.png')

#if __name__== '__main__':
#	main()

if __name__ == '__main__': 
    date_chart()

#print(bar_chart.render_to_file('555.svg') )	
print(bar_chart.render_to_png(filename='555555.png'))	
bar_chart.render_to_png(filename='10705292007.png')	
	

	
	
	
	
