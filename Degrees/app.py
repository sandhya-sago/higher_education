import dash 
from flask import (Flask, jsonify, render_template, redirect)
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from  .neas_viz import questionaire
from  .neas_viz import data_processing

server = Flask(__name__)
# Initialize Dash and setup the dashboard
stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css","/static/css/style.css"]
app = dash.Dash(__name__, server=server, url_base_pathname='/neas_viz/', external_stylesheets=stylesheets)

questions, ids = questionaire.get_questionaire()

outputs = [dcc.Graph(id='Q39_EARNINGS'), dcc.Graph(id='Q35_EMPLOYED'),
    dcc.Graph(id='Q36_FULL_TIME'), dcc.Graph(id='Q37_WEEKS_WORKED'),
    dcc.Graph(id='Q38_HOURS_WORKED')]
app.layout = html.Div(children=[
    html.A(html.Button("HOME", className="btn btn-outline-dark btn-lg"), href='/'),
    html.A(html.Button("GRAPHS", className="btn btn-outline-dark btn-lg"), href='../graphs'),
    html.A(html.Button("GEO MAPS", className="btn btn-outline-dark btn-lg"), href='../geomap'),
    html.A(html.Button("DEGREES", className="btn btn-outline-dark btn-lg"), href='../degrees'),
    html.A(html.Button("MACHINE", className="btn btn-outline-dark btn-lg"), href='../new-page'),
    html.A(html.Button("CONCLUSIONS", className="btn btn-outline-dark btn-lg"), href='../conclusions'),
    html.Div([
        html.H1(children=["National Education and Attainment Survey (NEAS)"]), 
        html.P("NORC at the University of Chicago (NORC) conducted the 2017 National Education \
        and Attainment Survey (NEAS), funded by the Lumina Foundation. The purpose of this study \
        was to learn more about education, training experiences, and employment of adults in the \
        United States. "),
        html.P(["More details ", html.A('here', href='http://www.norc.org/Research/Projects/Pages/national-education-and-attainment-survey.aspx')]),
        html.P("This form contains a few of the questions and the choices given, so that the employment \
        status can be visualized. The original question numbers have been retained for easy cross-reference.")
    ], className="bg-warning rounded p-5"),
    html.Div([
        html.Div(questions,className='col-12 col-md-6 p-5'),
        html.Div(outputs,className='col-12 col-md-6 p-5')
    ], className='row')],className='container-fluid')


@server.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@server.route("/graphs")
def graphs():
    """Return the graphs page."""
    return render_template("graphs_page.html")

@server.route("/geomap")
def geomap():
    """Return the geo map page."""
    return render_template("geo-map.html")

@server.route("/degrees")
def degrees():
    """Return the degrees page."""
    return render_template("degrees.html")

@server.route("/new-page")
def new():
    """Return the new page."""
    return render_template("new-page.html")

@server.route("/new-page2")
def new2():
    """Return the other new page."""
    return render_template("new-page2.html")

@server.route("/conclusions")
def conclusions():
    """Return the conclusions page."""
    return render_template("conclusions_page.html")

@server.route("/neas_viz")
def neas_viz():
    return redirect('/neas_viz')

#### Output callbacks
callback_input = [dash.dependencies.Input(component_id=id,component_property= 'values') for id in ids]

#### Callback for Q39_EARNINGS
q39_earnings_ymax = data_processing.get_q39_earnings_ymax()
@app.callback(
    dash.dependencies.Output(component_id='Q39_EARNINGS',component_property='figure'),
    callback_input
    )  
def update_yearly_earnings(*options):
    '''Visualize yearly earnings (responses to Q39_EARNINGS)'''
    data = data_processing.get_responses("Q39_EARNINGS", options, ids)
    total_entries = sum(data)
    trace = go.Bar(
        x = ['No Response', '$0 to $10,000','$10,001 to $20,000','$20,001 to $30,000','$30,001 to $40,000','$40,001 to $50,000','$50,001 to $60,000','$60,001 to $75,000','$75,001 to $150,000','$150,001 or more'],
        y = data,     
    )
    layout = go.Layout(
        title ='Earnings in the last 12 months<br>\
        Total data points = '+str(total_entries),
        yaxis = dict(range=[0,q39_earnings_ymax])
    )    
    return {'data': [trace],'layout':layout}

#### Callback for Q35_EMPLOYED
@app.callback(
    dash.dependencies.Output(component_id='Q35_EMPLOYED',component_property='figure'),
    callback_input
    )  
def update_employment_status(*options):
    '''Visualize employment status(responses to Q35_EMPLOYED)'''
    data = data_processing.get_responses("Q35_EMPLOYED", options, ids)
    total_entries = sum(data)
    trace = go.Bar(
        x = ['No Response', 'No', 'Yes'],
        y = data,     
    )
    layout = go.Layout(
        title ='Last week, were you employed for pay at a job or a business?<br>\
        If you were temporarily absent from a job or business<br>\
        (on vacation, temporarily ill, on maternity leave, etc.), answer "Yes".<br>\
        Total data points = '+str(total_entries),
    )    
    return {'data': [trace],'layout':layout}
    
#### Callback for Q36_FULL_TIME
@app.callback(
    dash.dependencies.Output(component_id='Q36_FULL_TIME',component_property='figure'),
    callback_input
    )  
def update_full_time(*options):
    '''Visualize full time status(responses to Q36_FULL_TIME)'''
    data = data_processing.get_responses("Q36_FULL_TIME", options, ids)
    total_entries = sum(data)
    trace = go.Bar(
        x = ['No Response', 'No', 'Yes'],
        y = data,     
    )
    layout = go.Layout(
        title ='Last week, did you work full time<br> (35 hours or more per week)<br>\
        Total data points = '+str(total_entries),
    )    
    return {'data': [trace],'layout':layout}
    
#### Callback for Q37_WEEKS_WORKED
q37_weeks_ymax = data_processing.get_q37_weeks_ymax()
@app.callback(
    dash.dependencies.Output(component_id='Q37_WEEKS_WORKED',component_property='figure'),
    callback_input
    )  
def update_weeks_worked(*options):
    '''Visualize weeks worked (responses to Q37_WEEKS_WORKED)'''
    data = data_processing.get_responses("Q37_WEEKS_WORKED", options, ids)
    total_entries = sum(data)
    trace = go.Bar(
        x = ['No Response', '51 to 52 weeks', '49 to 49 weeks','41 to 47 weeks', '28 to 39 weeks', 
        '15 to 26 weeks', '2 to 13 weeks', '1 week'],
        y = data,     
    )
    layout = go.Layout(
        title ='During the past 12 months (52 weeks),<br> how many weeks did you work,<br>\
        including paid vacation, paid sick leave, <br>and military service?<br>\
        Total data points = '+str(total_entries),
        yaxis = dict(range=[0,q39_earnings_ymax])
    )    
    return {'data': [trace],'layout':layout}

#### Callback for Q38_HOURS_WORKED
q38_hours_ymax = data_processing.get_q38_hours_ymax()
q38_hours_xrange = data_processing.get_q38_hours_xrange()

@app.callback(
    dash.dependencies.Output(component_id='Q38_HOURS_WORKED',component_property='figure'),
    callback_input
    )  
def update_hours_worked(*options):
    '''Visualize hours worked (responses to Q38_HOURS_WORKED)'''
    ### TODO: Should I do binning in data_processing.py for this column?
    data = data_processing.get_responses("Q38_HOURS_WORKED", options, ids)
    total_entries = sum(data)
    trace = go.Bar(
        x = q38_hours_xrange,
        y = data,     
    )
    layout = go.Layout(
        title ='During the past 12 months, in the weeks you worked,<br>\
        how many hours did you usually work each WEEK?<br>\
        Total data points = '+str(total_entries),
        yaxis = dict(range=[0,q39_earnings_ymax])
    )    
    return {'data': [trace],'layout':layout}

if __name__ == "__main__":
    app.run_server(debug=True)