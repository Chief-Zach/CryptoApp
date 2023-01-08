# Initialize Libraries Necessary for API and GET pulls
import datetime
import requests
import json

BTCWord = ['BTC', 'btc', 'Bitcoin', 'bitcoin']
ETHWord = ['ETH', 'eth', 'Ethereum', 'ethereum']
SOLWord = ['SOL', 'sol', 'solana', 'Solana']
BNBWord = ['BNB', 'bnb', 'Binance', 'binance']

""""
class Setup:
    def __init__(self, blank):
        self.blank = blank

    def welcome(self):
        print(datetime.date.today())
        print('Welcome to the Multi-coin Crypto Wallet')
        self.DetCoin()

    def DetCoin(self):
        leadInput = input("To continue please enter the coin you would like to search for: ")
        if leadInput in BTCWord:
            self.InputBTC()
        elif leadInput in ETHWord:
            self.InputETH()
        elif leadInput in SOLWord:
            self.InputSOL()
        elif leadInput in BNBWord:
            print('Binance support is currently under maintenance')
            self.DetCoin()
            # self.InputBNB()

    def InputBTC(self):
        addrB = Bitcoin(input("What is you Bitcoin Public Key: "))
        addrB.Pull()

    def InputETH(self):
        addrE = Ethereum(input("What is you Ethereum Public Key: "))
        addrE.Pull()

    def InputSOL(self):
        addrS = Solana(input("What is you Solana Public Key: "))
        addrS.Pull()

    def InputBNB(self):
        addrBN = Binance(input("What is you Binance Public Key: "))
        addrBN.Pull()

"""


class Convert:
    def __init__(self, coinQuantity, coin, currency):
        self.coinQuantity = coinQuantity
        self.coin = coin
        self.currency = currency

    def conversionRate(self):
        link = 'https://cex.io/api/ticker/' + self.coin + '/' + self.currency
        r = requests.get(link)
        END = r.json()['last']
        return float(END)

    def convertMain(self):
        convert = self.coinQuantity * self.conversionRate()
        return '$' + str(round(convert, 2))


# BITCOIN

def bitcoin(addr):
    linkAddr = 'https://blockchain.info/q/addressbalance/' + addr
    r = requests.get(linkAddr)
    satoshi = r.text
    totalBtc = int(satoshi) / (10 ** 8)
    print(str(totalBtc) + 'BTC')
    BtcConvert = Convert(totalBtc, 'BTC', 'USD')
    return BtcConvert.convertMain()


# ETHEREUM

def ethereum(addr):
    linkAddr = 'https://api.blockcypher.com/v1/eth/main/addrs/' + addr
    r = requests.get(linkAddr)
    wei = r.json()['balance']
    print(wei)
    totalEth = wei / (10 ** 18)
    print(str(totalEth) + 'ETH')
    EthConvert = Convert(totalEth, 'ETH', 'USD')
    return EthConvert.convertMain()


def solanaPost(addr):
    url = 'https://api.mainnet-beta.solana.com'
    headers = {'content-type': 'application/json'}

    result = {
        "jsonrpc": "2.0",
        "method": "getBalance",
        "params": [addr],
        "id": 0,
    }
    r = requests.post(url, data=json.dumps(result), headers=headers)
    return r


def solana(addr):
    r = solanaPost(addr)
    lamports = r.json()['result']['value']
    totalSol = lamports / (10 ** 9)
    print(totalSol)
    SolConvert = Convert(totalSol, 'SOL', 'USD')
    return SolConvert.convertMain()


def binance(self):
    linkAddr = 'https://dex.binance.org/api/v1/account/' + self.addr
    r = requests.get(linkAddr)
    part = r.json()['balance']
    print(part)
    totalBnb = part / (10 ** 18)
    print(str(totalBnb) + 'BNB')
    BnbConvert = Convert(totalBnb, 'BNB', 'USD')
    BnbConvert.convertMain()


def main(argv):
    if argv[0] == "bitcoin":
        return "You have chosen Bitcoin!"
        # return bitcoin(argv[1])
    elif argv[0] == "solana":
        return "You have chosen Bitcoin!"
        # return solana(argv[1])
    elif argv[0] == "ethereum":
        return "You have chosen Bitcoin!"
        # return ethereum(argv[1])
    else:
        return "Error"


if __name__ == '__main__':
    main(sys.argv[1:])
