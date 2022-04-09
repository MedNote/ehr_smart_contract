from brownie import EHR, accounts

def main():
    account = accounts.load('alex')
    EHR.deploy({'from': account})