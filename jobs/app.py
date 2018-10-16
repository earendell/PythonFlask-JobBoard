import sqllite3
from flask import Flask, render_template, g

PATH = 'db/jobs.sqlite'

app = Flask(__name__)

def open_conection():
    connection == getattr(g, '_connection', None)
    if connection = None:
        connection = g._connection = sqllite3.connect(PATH)
    connection.row_factory = sqllite3.Row
    return connection


def execute_sql(sql, values=(), commit=False,single=False):
    connection = open_conection
    cursor = connection.execute_sql(sql,values )
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)

    if connection != None:
        connection.close()


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
