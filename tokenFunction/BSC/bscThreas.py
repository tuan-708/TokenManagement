import time
import requests
import threading
from tokenFunction.Toke import Token
import main

listTokenBSC = []


class BSC_Threads(threading.Thread):
    timeSuccess = 0

    def __init__(self, listLock, listOutLock, listProfile, LenDataFrame, progressBar):
        super().__init__()
        self._list_lock = listLock
        self._listOutLock = listOutLock
        self._listProfiles = listProfile
        self._lenDataFrame = LenDataFrame
        self._processBar = progressBar

    def run(self):
        while True:
            self._list_lock.acquire()
            try:
                profileInfo = next(self._listProfiles)
                BSC_Threads.timeSuccess += 1
                self._processBar.setValue((BSC_Threads.timeSuccess / self._lenDataFrame) * 100)
            except StopIteration:
                return
            finally:
                # release the Lock, so other thread can gain the Lock to access list_num
                self._list_lock.release()

            addressbalance = "https://deep-index.moralis.io/api/v2/" + profileInfo.get('Metamask Address') + "/balance?chain=bsc"
            headers = {
                'x-api-key': "hmVyhuxc1Vzcsq0MvkSeUSfYzhhHyjrqExFkXwwDrc0vzW5RaGA10l9I5EQgeawy"
            }

            try:
                response = requests.request("GET", addressbalance, headers=headers)
                responseBNB = response.json()
            except Exception:
                time.sleep(3)
                response = requests.request("GET", addressbalance, headers=headers)
                responseBNB = response.json()
            balence = int(responseBNB['balance'])
            if balence > 0:
                balenceBNB = {'Address': profileInfo.get('Metamask Address'), 'name': 'BNB', 'balance': str("{:7.4f}".format(int(responseBNB['balance']) / 1000000000000000000)),
                          'token_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'Key': profileInfo.get('Metamask Key')}
            else:
                balenceBNB = {'Address': profileInfo.get('Metamask Address'), 'name': 'BNB',
                              'balance': str("0"),
                              'token_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'Key': profileInfo.get('Metamask Key')}

            print(balenceBNB)
            self._listOutLock.acquire()
            listTokenBSC.append(balenceBNB)
            self._listOutLock.release()
            time.sleep(3)

            erc20balance = "https://deep-index.moralis.io/api/v2/" + profileInfo.get('Metamask Address') + "/erc20?chain=bsc"

            headers = {
                'x-api-key': "hmVyhuxc1Vzcsq0MvkSeUSfYzhhHyjrqExFkXwwDrc0vzW5RaGA10l9I5EQgeawy"
            }

            response = requests.request("GET", erc20balance, headers=headers)
            responseToken = response.json()

            for i in range(len(responseToken)):
                self._listOutLock.acquire()
                try:
                    tokens = {'Address': profileInfo.get('Metamask Address'), 'name': responseToken[i]['name'],
                              'balance': str("{:7.4f}".format(int(responseToken[i]['balance']) / 1000000000000000000)),
                              'token_address': responseToken[i]['token_address'], 'Key': profileInfo.get('Metamask Key')}
                    listTokenBSC.append(tokens)
                except Exception:
                    pass
                self._listOutLock.release()








