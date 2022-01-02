# Initialize Libraries Necessary for API and GET pulls
import requests

class Convert:
    def __init__(self, coinQuantity, coin, currency):
        self.coinQuantity = coinQuantity
        self.coin = coin
        self.currency = currency
    def conversionRate (self):
        link = 'https://cex.io/api/ticker/' + self.coin + '/' + self.currency
        r = requests.get(link)
        END = r.json()['last']
        return float(END)

    def convertMain (self):
        convert = self.coinQuantity * self.conversionRate()
        print('$' + str(round((convert), 2)))




class Bitcoin:

    def __init__(self, addr):
        self.addr = addr

    def Pull(self):
        linkAddr = 'https://blockchain.info/q/addressbalance/' + self.addr
        r = requests.get(linkAddr)
        satoshi = r.text
        totalBtc = int(satoshi) / (10**8)
        print(str(totalBtc) + 'BTC')
        BtcConvert = Convert(totalBtc, 'BTC', 'USD')
        BtcConvert.convertMain()

        #totalUSD = round(conversionRate('BTC') * totalBtc, 2)
        #print('$' + str(totalUSD))




class Ethereum:

    def __init__(self, addr):
        self.addr = addr

    def Pull(self):
        linkAddr = 'https://api.blockcypher.com/v1/eth/main/addrs/' + self.addr
        r = requests.get(linkAddr)
        wei = r.json()['balance']
        print(wei)
        totalEth = wei / (10**18)
        print(str(totalEth) + 'ETH')
        EthConvert = Convert(totalEth, 'ETH', 'USD')
        EthConvert.convertMain()


# lead = input("What coin: ")
addrB = Bitcoin('bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh')
addrE = Ethereum('738d145faabb1e00cf5a017588a9c0f998318012')

addrB.Pull()
