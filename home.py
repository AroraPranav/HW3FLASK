from flask import Flask
myobj = Flask(__name__)



@myobj.route("/")
def home():
    name = 'Lisa'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    city=""
    for i in city_names:
        city += f'<li>{i}</li>'

    return f'''
        <html>
        <body>
                <h1>Welcome {name}!</h1><br>
                <a href="www.google.com">notgoogle</a><br>
                <ul>
                    {city}<br>
                </ul>
            </body>
        </html>
    '''
#app.run()
