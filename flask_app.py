from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown, input_data1=select, input_data2=freeform,
                           output="Thats good to hear! Come back soon %s." % name)

#create a dictionary that maps variables to the input values
#create functions for things like volume or area
#output includes the answer
#if there is an invalid value then the program should return an error
#