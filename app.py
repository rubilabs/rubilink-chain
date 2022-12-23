from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import socket
import sys

app = Flask(__name__)

cors = CORS(app)

@app.route("/", methods=["POST"])
def post():
    data = request.get_json()
    data = jsonify(data)
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])
    keyFile = None
    if len(sys.argv) > 4:
        keyFile = sys.argv[4]

    node = Node(ip, port, keyFile)
    node.startP2P()
    node.startAPI(apiPort)