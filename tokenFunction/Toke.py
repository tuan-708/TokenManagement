class Token:
    STT = ""
    SeedPhrase = ""
    MetamaskAddress = ""
    MetamaskKey = ""
    PhantomAddress = ""
    PhantomKey = ""

    def setSTT(self, stt):
        self.STT = stt

    def getSTT(self):
        return self.STT

    def setSeedPharse(self, SeedPhrase):
        self.SeedPhrase = SeedPhrase

    def getSeedPharse(self):
        return self.SeedPhrase

    def setMetamaskAddress(self, MetamaskAddress):
        self.MetamaskAddress = MetamaskAddress

    def getMetamaskAddress(self):
        return self.MetamaskAddress

    def setMetamaskKey(self, MetamaskKey):
        self.MetamaskKey = MetamaskKey

    def getMetamaskKey(self):
        return self.MetamaskKey

    def setPhantomAddress(self, PhantomAddress):
        self.PhantomAddress = PhantomAddress

    def getPhantomAddress(self):
        return self.PhantomAddress

    def setPhantomKey(self, PhantomKey):
        self.PhantomKey = PhantomKey

    def getPhantomKey(self):
        return self.PhantomKey
