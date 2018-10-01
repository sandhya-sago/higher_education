import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

def get_questionaire():

    '''The questionaire html
    MUST DO: use the same id as the column name in data, data_processing assumes that same
    id is used'''
    questionaire = []
    ids = []

    questionaire.append(html.H4("Section A. Education"))

    # Question 1
    id = "Q1_HS"
    question = html.H6("1. People can get a High School diploma in a variety of ways, such as \
    graduating from High School or by getting a \
    GED or other equivalent. Do \
    you have a High School diploma?")
    questionaire.append(question)
    options = dcc.Checklist(
        id = id,
        options=[
            {'label':"No", 'value': '1'},
            {'label':"Yes, graduated from High School", 'value' :'2'},
            {'label': "Yes, GED or other equivalent", "value":'3'}
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 2
    id = "Q2_COL_CREDIT"
    question = html.H6("2. Have you earned any college credit or completed a college degree?")
    questionaire.append(question)
    options = dcc.Checklist(
        id = id,
        options=[
            {'label':"No", 'value': '1'},
            {'label':"Yes, some college, but less than one year of college credit", 'value' :'2'},
            {'label': "Yes, one or more years of college credit, no degree", "value":'3'},
            {'label': "Yes, completed a degree", "value":'4'}
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 3
    question = html.H6("3. Which of the following degrees have you completed?")
    questionaire.append(question)
    id ="Q3_Q3_A_R"
    options = dcc.Checklist(
        id = id,
        options=[
            {'label':"Associate's degree (For example, AA, AS)", 'value':'2'}
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    id ="Q3_Q3_B_R"
    options = dcc.Checklist(
        id = id,
        options=[
            {'label':"Bachelor's degree (for example, BA, BS)", 'value':'2'}
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id ="Q3_Q3_C_R"
    options = dcc.Checklist(
        id = id,
        options=[
            {'label':"Master's degree (for example, BA, BS)", 'value':'2'}
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id ="Q3_Q3_D_R"
    options = dcc.Checklist(
        id = id,
        options=[
            {'label':"Professional degree (for example, MD, DDS, DVM, LLB, JD)", 'value':'2'}
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id ="Q3_Q3_E_R"
    options = dcc.Checklist(
        id = id,
        options=[
            {'label':"Doctorate degree (for example, PhD, EdD)", 'value':'2'}
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 4
    question = html.H6("4. Which one of the following best describes the field of study for the highest level of school you have completed")
    questionaire.append(question)
    id = "Q4_HIGHEST_EDU_FOS"
    options = dcc.Checklist(
        id = id,
        options = [
            {'label':'General studies, no major, or undeclared','value':'1'},
            {'label':'Accounting, finance, insurance, or real estate','value':'2'},
            {'label':'Administrative support','value':'3'},
            {'label':'Agriculture','value':'4'},
            {'label':'Audio, broadcasting, multimedia, or graphic technologies','value':'5'},
            {'label':'Business management, administration, or marketing','value':'6'},
            {'label':'Communications or journalism','value':'7'},
            {'label':'Computer science or Information Technology','value':'8'},
            {'label':'Transportation','value':'9'},
            {'label':'Cosmetology','value':'10'},
            {'label':'Education','value':'11'},
            {'label':'Engineering or Architecture','value':'12'},
            {'label':'English language or literature','value':'13'},
            {'label':'Fine arts or music','value':'14'},
            {'label':'Healthcare','value':'15'},
            {'label':'Law enforcement, security or firefighting','value':'16'},
            {'label':'Law or legal studies','value':'17'},
            {'label':'Liberal arts','value':'18'},
            {'label':'Psychology','value':'19'},
            {'label':'Religious vocations or theology','value':'20'},
            {'label':'Science or mathematics','value':'21'},
            {'label':'Social or human services or public administration','value':'22'},
            {'label':'Social sciences, Political science, Economics or History','value':'23'},
            {'label':'Library Information Science','value':'25'},
            {'label':'Culinary Arts, Hospitality, Hotel Restaurant, Food Service','value':'26'},
            {'label':'Other','value':'24'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 9
    questionaire.append(html.H4("Section B. Certifications and Licenses"))
    question = html.H6("9. A professional certification or license shows you are qualified to perform a specific \
    job.  Do you have a currently active professional certification or a state or industry license?")
    questionaire.append(question)
    id = "Q9_CERT_LIC"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'No','value':'1'},
            {'label':'Yes','value':'2'}
        ],
        values = []
    )
    questionaire.append(options)
    ids.append(id)

    # Question 45
    questionaire.append(html.H4("Section F. Background"))
    question = html.H6("45. Are you male or female?")
    questionaire.append(question)
    id = "Q45_GENDER"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'Male','value':'1'},
            {'label':'Female','value':'2'},
            {'label':'Other','value':'3'},

        ],
        values=[]
    )

    questionaire.append(options)
    ids.append(id)

    # Question 46
    question = html.H6("46. What is your current marital status?")
    questionaire.append(question)
    id = "Q46_MARITAL_STATUS"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'Now married','value':'1'},
            {'label':'Widowed','value':'2'},
            {'label':'Divorced','value':'3'},
            {'label':'Separated','value':'4'},
            {'label':'Never married','value':'5'},
            {'label':'NA','value':'-3'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 47
    question = html.H6("47. How old are you?")
    questionaire.append(question)
    id = "Q47_AGE"
    checkboxes = [{'label': str(i), 'value' : str(i)} for i in range(18,65)]
    options = dcc.Checklist(
        id=id,
        options = checkboxes,
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 48
    question = html.H6("48. Are you of Hispanic, Latino or Spanish origin?")
    questionaire.append(question)
    id = "Q48_HISPANIC"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'No','value':'1'},
            {'label':'Yes','value':'2'},
            {'label':'NA','value':'-3'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 49
    question = html.H6("49. What is your race?")
    questionaire.append(question)
    id = "Q49_RACE_01"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'White','value':'1'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id = "Q49_RACE_02"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'Black or African American','value':'1'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id = "Q49_RACE_03"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'American Indian or Alaska Native','value':'1'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id = "Q49_RACE_04"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'Asian','value':'1'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id = "Q49_RACE_05"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'Native Hawaiian or Other Pacific Islander','value':'1'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id = "Q49_RACE_06"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'Other','value':'1'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    id = "Q49_RACE_07"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'Multiple','value':'1'},
        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)

    # Question 51
    question = html.H6("51. What is your citizenship status?")
    questionaire.append(question)
    id = "Q51_CITIZENSHIP"
    options = dcc.Checklist(
        id=id,
        options = [
            {'label':'U.S. citizen since birth','value':'1'},
            {'label':'Naturalized U.S. citizen','value':'2'},
            {'label':'Non-U.S. citizen','value':'3'},

        ],
        values=[]
    )
    questionaire.append(options)
    ids.append(id)
    
    return questionaire, ids