# Initialize Libraries Necessary for API and GET pulls
import requests
import json

link = ''


class Bitcoin:

    def __init__(self, addr):
        self.addr = addr

    def Pull(self):
        link = 'https://blockchain.info/q/addressbalance/' + self.addr
        r = requests.get(link)
        satoshi = r.text
        totalBtc = int(satoshi) / (10**8)
        print(totalBtc)


class Ethereum:

    def __init__(self, addr):
        self.addr = addr

    def Pull(self):
        link = 'https://api.blockcypher.com/v1/eth/main/addrs/' + self.addr
        r = requests.get(link)
        wei = (r.json()['balance'])
        print(wei)
        totalEth = wei / (10**18)
        print(totalEth)

# lead = input("What coin: ")
addrB = Bitcoin('bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh')
addrE = Ethereum('738d145faabb1e00cf5a017588a9c0f998318012')

addrB.Pull()
