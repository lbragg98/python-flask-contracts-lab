#!/usr/bin/env python3

from flask import Flask, abort, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.get("/contract/<int:contract_id>")
def get_contract(contract_id):
    for contract in contracts:
        if contract["id"] == contract_id:
            return make_response(contract["contract_information"], 200)
    abort(404)


@app.get("/customer/<string:customer_name>")
def get_customer(customer_name):
    if customer_name in customers:
        return make_response("", 204)
    abort(404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
