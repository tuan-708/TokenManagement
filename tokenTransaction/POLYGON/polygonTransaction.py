import time
from web3 import Web3


def polygonTransaction(sAccount, sKey, AmountTranfers, gasFee, listAccountRevice, progressBar):
    eth = "https://polygon-rpc.com/"

    web3 = Web3(Web3.HTTPProvider(eth))
    count = 0
    for address in listAccountRevice["Address"]:
        count += 1
        balance = web3.eth.get_balance(sAccount)
        firstBalance = web3.fromWei(balance, "ether")
        print(address+":"+str(firstBalance))

        nonce = web3.eth.getTransactionCount(sAccount)

        tx = {
            'nonce': nonce,
            'to': address,
            'value': web3.toWei(float(AmountTranfers), 'ether'),
            'gas': 21000,
            'gasPrice': web3.toWei(gasFee, 'gwei'),
            'chainId': 137,
        }

        signed_tx = web3.eth.account.sign_transaction(tx, sKey)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
        for i in range(200):
            time.sleep(1)
            balance = web3.eth.get_balance(sAccount)
            lastBalance = web3.fromWei(balance, "ether")
            if firstBalance != lastBalance:
                break
        progressBar.setValue((count / len(listAccountRevice)) * 100)
    print("Hoàn thành")