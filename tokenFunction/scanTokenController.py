import threading
from tokenFunction.BSC.bscThreas import BSC_Threads
from tokenFunction.ETH.ethThreads import ETH_Threads
from tokenFunction.SOL.solThreads import SOL_Threads
from tokenFunction.POLYGON.polygonThreads import POLYGON_Threads

from tokenFunction.BSC.bscThreas import listTokenBSC
from tokenFunction.ETH.ethThreads import listTokenETH
from tokenFunction.SOL.solThreads import listTokenSOL
from tokenFunction.POLYGON.polygonThreads import listTokenPOLYGON

from excelFunction import ExcelManager


def scanTokenController(radioButton, listProfiles, LenDataFrame, progressBar):
    numThreads = 4
    if numThreads is None:
        try:
            numThreads = os.cpu_count()
        except AttributeError:
            numThreads = 5

    listLock = threading.Lock()
    listOutLock = threading.Lock()
    threads = []
    if radioButton == "Bsc":
        for i in range(numThreads):
            thread = BSC_Threads(listLock, listOutLock, listProfiles, LenDataFrame, progressBar)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        ExcelManager.saveScanToken(f"excelManagment\Bsc.xlsx", listTokenBSC)

    if radioButton == "Eth":
        for i in range(numThreads):
            thread = ETH_Threads(listLock, listOutLock, listProfiles, LenDataFrame, progressBar)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        ExcelManager.saveScanToken(f"excelManagment\Eth.xlsx", listTokenETH)

    if radioButton == "Sol":
        for i in range(numThreads):
            thread = SOL_Threads(listLock, listOutLock, listProfiles, LenDataFrame, progressBar)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        print(len(listTokenSOL))
        ExcelManager.saveScanToken(f"excelManagment\Sol.xlsx", listTokenSOL)
    if radioButton == "Polygon":
        for i in range(numThreads):
            thread = POLYGON_Threads(listLock, listOutLock, listProfiles, LenDataFrame, progressBar)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        print(len(listTokenPOLYGON))
        ExcelManager.saveScanToken(f"excelManagment\Polygon.xlsx", listTokenPOLYGON)
    print("Hoàn thành")