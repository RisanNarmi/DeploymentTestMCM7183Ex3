from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = [html.H3('Hello world! Hope you have a terrible day')]

if __name__ == '__main__':
    app.run(debug=True)
