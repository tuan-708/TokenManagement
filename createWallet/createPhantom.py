import pandas as pd
from bip_utils import *
from excelFunction import ExcelManager

listWallet = []


def walletPhantom(progressBar):
    dataFrame = ExcelManager.readFileExcel(f"createWallet\Data.xlsx", "Sheet1")
    listSTT = dataFrame['STT']
    listSeedPhrase = dataFrame['Metamask SeePhrase']
    lendataFrame = len(dataFrame['Metamask SeePhrase'])
    listAddress = dataFrame['Metamask Address']
    listMetamaskKey = dataFrame['Metamask Key']

    for index, item in enumerate(dataFrame["Metamask SeePhrase"]):
        MNEMONIC = item

        seed_bytes = Bip39SeedGenerator(MNEMONIC).Generate("")

        bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)

        bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)

        bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

        wallet = {"STT": listSTT[index], "Metamask SeePhrase": listSeedPhrase[index], "Metamask Address": listAddress[index],
                  "Metamask Key": listMetamaskKey[index], "Phantom Address": bip44_chg_ctx.PublicKey().ToAddress(),
                  "Phantom Key": bip44_chg_ctx.PrivateKey().Raw().ToHex()}
        listWallet.append(wallet)
        progressBar.setValue(((index+1)/lendataFrame)*100)

    df = pd.DataFrame.from_dict(listWallet)
    df.to_excel(f"createWallet\Data.xlsx", index=False)
