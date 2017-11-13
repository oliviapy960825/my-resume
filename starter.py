from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')

@app.route('/home')
def return_home():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('home.html')

@app.route('/course')
def show_all_courses():
    courses = [
        'MISY350',
        'CISC181',
        'CISC250'
    ]
    # return "<h2>this is the page for all users</h2>"
    return render_template('course.html',courses=courses)


@app.route('/about')
def about_start():
    # return "hello " + name
    # return "Hello %s, this is %s" % (name, 'administrator')
    return render_template('about.html')



# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
