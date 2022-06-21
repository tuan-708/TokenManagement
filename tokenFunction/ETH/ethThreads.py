import time
import requests
import threading

listTokenETH = []


class ETH_Threads(threading.Thread):
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
                ETH_Threads.timeSuccess += 1
                self._processBar.setValue((ETH_Threads.timeSuccess / self._lenDataFrame) * 100)
            except StopIteration:
                return
            finally:
                # release the Lock, so other thread can gain the Lock to access list_num
                self._list_lock.release()

            addressbalance = "https://deep-index.moralis.io/api/v2/" + profileInfo.get('Metamask Address') + "/balance?chain=eth"
            headers = {
                'x-api-key': "hmVyhuxc1Vzcsq0MvkSeUSfYzhhHyjrqExFkXwwDrc0vzW5RaGA10l9I5EQgeawy"
            }

            try:
                response = requests.request("GET", addressbalance, headers=headers)
                responseETH = response.json()
            except Exception:
                time.sleep(3)
                response = requests.request("GET", addressbalance, headers=headers)
                responseETH = response.json()
            balence = int(responseETH['balance'])
            if balence > 0:
                balenceETH = {'Address': profileInfo.get('Metamask Address'), 'name': 'ETH', 'balance': str("{:7.4f}".format(int(responseETH['balance']) / 1000000000000000000)),
                          'token_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'Key': profileInfo.get('Metamask Key')}
            else:
                balenceETH = {'Address': profileInfo.get('Metamask Address'), 'name': 'ETH',
                              'balance': str("0"),
                              'token_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'Key': profileInfo.get('Metamask Key')}

            print(balenceETH)
            self._listOutLock.acquire()
            listTokenETH.append(balenceETH)
            self._listOutLock.release()
            time.sleep(1)

            erc20balance = "https://deep-index.moralis.io/api/v2/" + profileInfo.get('Metamask Address') + "/erc20?chain=eth"

            headers = {
                'x-api-key': "hmVyhuxc1Vzcsq0MvkSeUSfYzhhHyjrqExFkXwwDrc0vzW5RaGA10l9I5EQgeawy"
            }

            response = requests.request("GET", erc20balance, headers=headers)
            responseToken = response.json()

            for i in range(len(responseToken)):
                self._listOutLock.acquire()
                tokens = {'Address': profileInfo.get('Metamask Address'), 'name': responseToken[i]['name'],
                              'balance': str("{:7.4f}".format(int(responseToken[i]['balance']) / 1000000000000000000)),
                              'token_address': responseToken[i]['token_address'], 'Key': profileInfo.get('Metamask Key')}
                listTokenETH.append(tokens)
                self._listOutLock.release()