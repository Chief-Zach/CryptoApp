let balance = 0;
const result_div = document.querySelector(".result")
const bitcoin_div = document.querySelector("#bitcoin")
const solana_div = document.querySelector("#solana")
const ethereum_div = document.querySelector("#ethereum")

let BNBWord, BTCWord, ETHWord, SOLWord;

BTCWord = ["BTC", "btc", "Bitcoin", "bitcoin"];
ETHWord = ["ETH", "eth", "Ethereum", "ethereum"];
SOLWord = ["SOL", "sol", "solana", "Solana"];
BNBWord = ["BNB", "bnb", "Binance", "binance"];

class Convert {
    constructor(coinQuantity, coin, currency) {
        this.coinQuantity = coinQuantity;
        this.coin = coin;
        this.currency = currency;
    }

    conversionRate() {
        let END, link, r;
        link = "https://cex.io/api/ticker/" + this.coin + "/" + this.currency;
        r = requests.get(link);
        END = r.json()["last"];
        return Number.parseFloat(END);
    }

    convertMain() {
        let convert;
        convert = this.coinQuantity * this.conversionRate();
        return "$" + round(convert, 2).toString();
    }

}

function bitcoin(addr) {
    let BtcConvert, linkAddr, satoshi, totalBtc;
    linkAddr = "https://blockchain.info/q/addressbalance/" + addr;
    fetch(linkAddr)
        .then(response => {
            satoshi = response.text()
        })
        .catch(() => {
            satoshi = 0
        })
    totalBtc = Number.parseInt(satoshi) / Math.pow(10, 8);
    console.log(totalBtc.toString() + "BTC");
    BtcConvert = new Convert(totalBtc, "BTC", "USD");
    return BtcConvert.convertMain();
}

function ethereum(addr) {
    let EthConvert, linkAddr, r, totalEth, wei;
    linkAddr = "https://api.blockcypher.com/v1/eth/main/addrs/" + addr;
    r = requests.get(linkAddr);
    wei = r.json()["balance"];
    console.log(wei);
    totalEth = wei / Math.pow(10, 18);
    console.log(totalEth.toString() + "ETH");
    EthConvert = new Convert(totalEth, "ETH", "USD");
    return EthConvert.convertMain();
}

function solanaPost(addr) {
    let headers, r, result, url;
    url = "https://api.mainnet-beta.solana.com";
    headers = {
        "content-type": "application/json"
    };
    result = {
        "jsonrpc": "2.0",
        "method": "getBalance",
        "params": [addr],
        "id": 0
    };
    r = requests.post(url, {
        "data": json.dumps(result),
        "headers": headers
    });
    return r;
}

function solana(addr) {
    let SolConvert, lamports, r, totalSol;
    r = solanaPost(addr);
    lamports = r.json()["result"]["value"];
    totalSol = lamports / Math.pow(10, 9);
    console.log(totalSol);
    SolConvert = new Convert(totalSol, "SOL", "USD");
    return SolConvert.convertMain();
}

function binance(addr) {
    let BnbConvert, linkAddr, part, r, totalBnb;
    linkAddr = "https://dex.binance.org/api/v1/account/" + addr;
    r = requests.get(linkAddr);
    part = r.json()["balance"];
    console.log(part);
    totalBnb = part / Math.pow(10, 18);
    console.log(totalBnb.toString() + "BNB");
    BnbConvert = new Convert(totalBnb, "BNB", "USD");
    BnbConvert.convertMain();
}

bitcoin_div.addEventListener("click", function() {
    console.log("You have chosen Bitcoin")
})

solana_div.addEventListener("click", function() {
    console.log("You have chosen Solana")

})

ethereum_div.addEventListener("click", function() {
    console.log("You have chosen Ethereum")

})