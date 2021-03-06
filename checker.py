import json
import requests
from web3 import Web3

i = 0
TokenAddress = "0xa5496935A247fA81B1462E553ad139d2FD0af795"

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
url_eth = "https://api.bscscan.com/api"

contract_address = web3.toChecksumAddress(TokenAddress)
API_ENDPOINT = url_eth + "?module=contract&action=getabi&address="+str(contract_address)

r = requests.get(url=API_ENDPOINT)
response = r.json()
abi = json.loads(response["result"])
contract = web3.eth.contract(address=contract_address, abi=abi)

for i in range(0,12):
        MyAddresses = open('input.txt', 'r').read().splitlines()
        MyAddress = Web3.toChecksumAddress(MyAddresses[i])

        address = web3.toChecksumAddress(MyAddress)
        balance=contract.functions.balanceOf(MyAddress).call()
        if web3.fromWei(balance, "ether") != 0:
            print(MyAddress)
            print(web3.fromWei(balance, "ether"))
