import time
import requests
import threading

listTokenPOLYGON = []


class POLYGON_Threads(threading.Thread):
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
                POLYGON_Threads.timeSuccess += 1
                self._processBar.setValue((POLYGON_Threads.timeSuccess / self._lenDataFrame) * 100)
            except StopIteration:
                return
            finally:
                # release the Lock, so other thread can gain the Lock to access list_num
                self._list_lock.release()

            addressbalance = "https://deep-index.moralis.io/api/v2/" + profileInfo.get('Metamask Address') + "/balance?chain=polygon"
            headers = {
                'x-api-key': "hmVyhuxc1Vzcsq0MvkSeUSfYzhhHyjrqExFkXwwDrc0vzW5RaGA10l9I5EQgeawy"
            }

            try:
                response = requests.request("GET", addressbalance, headers=headers)
                responsePOLYGON = response.json()
            except Exception:
                time.sleep(3)
                response = requests.request("GET", addressbalance, headers=headers)
                responsePOLYGON = response.json()
            balence = int(responsePOLYGON['balance'])
            if balence > 0:
                balencePOLYGON = {'Address': profileInfo.get('Metamask Address'), 'name': 'MATIC', 'balance': str("{:7.4f}".format(int(responsePOLYGON['balance']) / 1000000000000000000)),
                          'token_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'Key': profileInfo.get('Metamask Key')}
            else:
                balencePOLYGON = {'Address': profileInfo.get('Metamask Address'), 'name': 'MATIC',
                              'balance': str("0"),
                              'token_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'Key': profileInfo.get('Metamask Key')}

            print(balencePOLYGON)
            self._listOutLock.acquire()
            listTokenPOLYGON.append(balencePOLYGON)
            self._listOutLock.release()
            time.sleep(2)

            erc20balance = "https://deep-index.moralis.io/api/v2/" + profileInfo.get('Metamask Address') + "/erc20?chain=polygon"

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
                listTokenPOLYGON.append(tokens)
                self._listOutLock.release()