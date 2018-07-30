import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 

app = dash.Dash()

app.layout = html.Div(
	[html.H1('My First Dash App.'),

	dcc.Markdown('''
		Dash is a Python framework for building analytical web applications.
		'''),

	dcc.Graph(
		id = 'graph',
		figure = {
		'data':[
		go.Bar(x=[1,2,3,4], y=[4,3,2,1])
        ] 
	   }
	)

])

if __name__ == '__main__':
	app.run_server()
	