let balance = 0;
const result_div = document.querySelector(".result")
const bitcoin_div = document.querySelector("#bitcoin")
const solana_div = document.querySelector("#solana")
const ethereum_div = document.querySelector("#ethereum")

bitcoin_div.addEventListener("click", function() {
    console.log("You have chosen Bitcoin")
})

solana_div.addEventListener("click", function() {
    console.log("You have chosen Solana")
})

ethereum_div.addEventListener("click", function() {
    console.log("You have chosen Ethereum")
})