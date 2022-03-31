

from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    name = 'Lisa'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    city = ""
    for i in city_names:
        city += f'<li>{i}</li>'

    return f'''
        <html>
        <body>
                <h1>Welcome {name}!</h1>
                <a href={("https://www.google.com/")}>not google</a>
                <ul>
                    {city}
                </ul>
            </body>
        </html>
    '''
#app.run()
