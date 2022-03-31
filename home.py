from flask import Flask
myobj = Flask(__name__)


name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']


@myobj.route("/")
def home():
    for i in city_names:
        city += f'<li>{i}</li>'

    return f'''
        <html>
        <body>
                <h1>Welcome {name}!</h1>
                <a href={("https://www.google.com/")}>not google</a>
                <ul>
                    {city}<br>
                </ul>
            </body>
        </html>
    '''
#app.run()
