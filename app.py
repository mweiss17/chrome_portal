import mintapi
import os
import json
import datetime
from pprint import pprint
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from database import db_session

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Result

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/minty")
def minty():
    # get my most recent result
    result = Result.query.order_by(Result.created_date).first()
    print(result.created_date - datetime.datetime.utcnow() )
    if result and result.created_date - datetime.datetime.utcnow() < datetime.timedelta(83600):
        # if the most recent result is within the last day, return it
        transactions = result.transactions
        budgets = result.budgets
        return json.dumps({"transactions": transactions, "budget": budgets})
    else:
        # should be done in an RQ job
        try:
            mint = mintapi.Mint(os.environ.get('MINT_EMAIL'), os.environ.get('MINT_PASSWORD'))
        except:
            pass
        budgets = mint.get_budgets()
        transactions = json.loads(mint.get_transactions().to_json())
        try:
            result = Result(budgets=budgets, transactions=transactions)
            db.session.add(result)
            db.session.commit()
        except:
            pass
        return json.dumps(budgets)

@app.route("/money")
def money():
    return json.dumps({"transactions": [1, 2, 3]})

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run()

