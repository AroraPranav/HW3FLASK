from flask import Flask
myobj = Flask(__name__)

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route("/")
def home():
    
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
