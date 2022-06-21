from web3 import Web3
from eth_account import Account
import pandas as pd
listWallet = []


def walletMetamask(numbers, progressBar):
    for i in range(int(numbers)):
        Account.enable_unaudited_hdwallet_features()
        acct, mnemonic = Account.create_with_mnemonic("", 12, "english", "m/44'/60'/0'/0/0")
        wallet = {"STT": str(i), "Metamask SeePhrase": mnemonic, "Metamask Address": acct.address,
                  "Metamask Key": Web3.toHex(acct.key)}
        listWallet.append(wallet)
        progressBar.setValue(((i+1)/int(numbers))*100)
    df = pd.DataFrame.from_dict(listWallet)
    df.to_excel(f"createWallet\Data.xlsx", index=False)

