# import necessary libraries
from flask import (Flask, jsonify, render_template)

# create instance of Flask app
app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/graphs")
def graphs():
    """Return the graphs page."""
    return render_template("graphs_page.html")

@app.route("/geomap")
def geomap():
    """Return the geo map page."""
    return render_template("geo-map.html")

@app.route("/degrees")
def degrees():
    """Return the degrees page."""
    return render_template("degrees.html")

@app.route("/new-page")
def new():
    """Return the new page."""
    return render_template("new-page.html")

@app.route("/new-page2")
def new2():
    """Return the other new page."""
    return render_template("new-page2.html")

@app.route("/conclusions")
def conclusions():
    """Return the conclusions page."""
    return render_template("conclusions_page.html")


# @app.route("/apis")
# def home():
#     return (
#         f"<h1>Welcome to Project 2's APIs!</h1>"
#         f"<p>Usage:</p>"
#         f"<p>/api/v1.0/HSGrads</p>"
#         f"<p>/api/v1.0/4YrEnrollPctChange</p>"
#         f"<p>/api/v1.0/Tuition4YearPctChange</p>"
#         f"<p>/api/v1.0/BachelorsDegrees</p>"
    
#     )

# # /api/v1.0/HSGrads
# # Query for the percent change YoY of High School graduates by state for 2009-2015
# # Returns the JSON representation of the dictionary.
# @app.route("/api/v1.0/HSGrads")
# def HS_Grads_by_state():
#     hs_results = list(mongo.db.hs_grad_geo.find({}, {'_id': False}))
#     return jsonify(hs_results)

# # /api/v1.0/4YrEnrollPctChange
# # Query for the percent change YoY enrollment in 4-year universities by state for 2009-2015
# # Returns the JSON representation of the dictionary.
# @app.route("/api/v1.0/4YrEnrollPctChange")
# def Enroll_4yr_by_state():
#     enroll_4yr_results = list(mongo.db.enroll_4year_pct_chg_by_state.find({}, {'_id': False}))
#     return jsonify(enroll_4yr_results)

# # /api/v1.0/BachelorsDegrees
# # Query for the Bachelor's Degrees awarded for 2003-2015
# # Returns the JSON representation of the dictionary.
# @app.route("/api/v1.0/BachelorsDegrees")
# def Bach_degrees_by_year():
#     bach_results = list(mongo.db.bachelors_degrees_by_year.find({}, {'_id': False}))
#     return jsonify(bach_results)

# # /api/v1.0/Tuition4YearPctChange
# # Query for the tuition cost for 4-year institutions by state for 2004-2018
# # Returns the JSON representation of the dictionary.
# @app.route("/api/v1.0/Tuition4YearPctChange")
# def Tuition4Year_by_state():
#     tuition4Year_results = list(mongo.db.tuition_4year_pct_chg_by_state.find({}, {'_id': False}))
#     return jsonify(tuition4Year_results)



if __name__ == "__main__":
    app.run(debug=True)