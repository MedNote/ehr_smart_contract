from brownie import Faucet, accounts

def main():
    account = accounts.load('alex')
    Faucet.deploy({'from': account})