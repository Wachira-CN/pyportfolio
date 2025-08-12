from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/<string:url_path>')
def url_pth(url_path):
    return render_template(url_path)

@app.route('/')
def root():
    return render_template('index.html') #'Anybody here??'

@app.route('/favicon.ico')
def favicon():
    return 'pythonFI.ico'

def write_to_csv(info_data):
    contact_name = info_data["name"]
    contact_email = info_data["email"]
    contact_message = info_data["message"]
    with open("./pyexercises/webserver/messagesdb.csv", mode='a', newline='') as database_csv:
        dbcsv_writer = csv.writer(database_csv, delimiter= ',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
        # dbcsv_writer.writerow(['Name', 'E-mail', 'Message'])
        dbcsv_writer.writerow([contact_name,contact_email,contact_message])



@app.route('/submit_form', methods=['GET','POST'])
def submit_form():
    if request.method == 'POST':
        contact_info = request.form.to_dict()
        write_to_csv(contact_info)
        # print(contact_info['name'])
        # with open('./pyexercises/webserver/messagesdb.txt',mode='a') as database_file:
        #     # database_file.writelines(contact_info)
        #     database_file.write(contact_info['name'] + ', ' + contact_info['email'] + ', ' + contact_info['message'] + '\n')
        return 'Your message was submitted successfully.'
        #return redirect('\thankyou.html')
    elif request.method == 'GET':
        return  'The GET method was invoked'
    else:
        return f'Not sure about the \'{request.method}\' method that was invoked'

# @app.route('/index.html')
# def home_link():
#     return render_template('index.html')
#
# @app.route('/no-sidebar.html')
# def no_sidebar():
#     return render_template('/no-sidebar.html')
#
# @app.route('/left-sidebar.html')
# def left_sidebar():
#     return render_template('left-sidebar.html')
#
# @app.route('/right-sidebar.html')
# def right_sidebar():
#     return render_template('right-sidebar.html')
#
# @app.route('/blog')
# def blog():
#     return 'Hamna kitu hapa!'
#
# @app.route('/about')
# def about():
#     return 'What about us?'

