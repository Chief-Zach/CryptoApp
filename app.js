let balance = 0;
let mode = "a"
const result_div = document.querySelector(".result")
const bitcoin_div = document.querySelector("#bitcoin")
const solana_div = document.querySelector("#solana")
const ethereum_div = document.querySelector("#ethereum")
const searchInput = document.querySelector("#input")
const submit_div = document.querySelector(".submit")
const form = document.getElementById("submit-form")

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
        fetch(link)
            .then(response => {
                END = response.json()
            })
            .catch(() => {
            })

        END = END["last"];
        return Number.parseFloat(END);
    }

    convertMain() {
        let convert;
        convert = this.coinQuantity * this.conversionRate();
        return "$" + convert.toString();
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
    fetch(linkAddr)
        .then(response => {
            wei = response.json()
        })
        .catch(() => {
            wei = 0
        })

    wei = wei["balance"];
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
    fetch(url, {
        method: "POST",
        headers: headers,
        body: JSON.stringify(result)
    }).then(res => {
        return res.json();
});
}

function solana(addr) {
    let SolConvert, lamports, r, totalSol;
    r = solanaPost(addr);
    lamports = r["result"]["value"];
    totalSol = lamports / Math.pow(10, 9);
    console.log(totalSol);
    SolConvert = new Convert(totalSol, "SOL", "USD");
    return SolConvert.convertMain();
}

bitcoin_div.addEventListener("click", function() {
    mode = "bitcoin"
    console.log(`Mode has been set to ${mode}`)
})

solana_div.addEventListener("click", function() {
    mode = "solana"
    console.log(`Mode has been set to ${mode}`)
})

ethereum_div.addEventListener("click", function() {
    mode = "ethereum"
    console.log(`Mode has been set to ${mode}`)
})

function getData(form) {
    const formData = new FormData(form);
    console.log(Object.fromEntries(formData));
}

form.addEventListener("submit", function(e) {
    e.preventDefault(); // prevents page from reloading/sending data to server
    getData(e.target);
});

