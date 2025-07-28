from flask import Flask
import psycopg2



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Sulman Haque in 3308!'


# DB conneciton
#postgresql://lab10_sqldb_user:uYGGisS9uXJhSDr5uX0zuNOmWZohhoZv@dpg-d240d7qdbo4c738a4hrg-a/lab10_sqldb


@app.route('/db_test')
def test_db():
    conn = psycopg2.connect("postgresql://lab10_sqldb_user:uYGGisS9uXJhSDr5uX0zuNOmWZohhoZv@dpg-d240d7qdbo4c738a4hrg-a/lab10_sqldb")
    conn.close
    return "Database Connection Successful"