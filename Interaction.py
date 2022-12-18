from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests

def postTransaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(receiver.publicKeyString(), amount, type)

    url = 'http://localhost:5001/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)

if __name__ == '__main__':

    sakura = Wallet()
    asuka = Wallet()
    sakura.fromKey('keys/stakerPrivateKey.pem')
    exchange = Wallet()

    #forger: genesis 
    postTransaction(exchange, sakura, 100, 'EXCHANGE')
    postTransaction(exchange, asuka, 100, 'EXCHANGE')
    postTransaction(sakura, sakura, 25, 'STAKE')

    #forger: probably sakura
    postTransaction(sakura, asuka, 10, 'TRANSFER')
    
   