#!/usr/bin/env python3

__author__ = "Michael Danko"
__version__ = "0.1.0"
__license__ = "MIT"

import json
from ethjsonrpc import ParityEthJsonRpc
import csv

rpc = ParityEthJsonRpc('127.0.0.1', 8545)

# Created in block 5934492
# 0x719ea19781af64a5f3997fc2b93368d1fe643066

def findContractCreationBlock(contract):

  # shortcut since we already know block creation date
  return(5934492)

  latestBlock = rpc.eth_blockNumber()

  for i in range(latestBlock, 0, -1):
    data = rpc.eth_getBlockByNumber(i, True)
    for j in range(0, len(data["transactions"]), 1):
      if data["transactions"][j]["creates"] == contract:
        return(int(data["number"], 16))

#-----------------------------------

def findContractCalls(startBlock, contract):
  with open('chain_data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "Block Number", "Transaction Hash", "Transaction Index", "From", "Value", "Gas Price", "Gas Used", "Function Called"])
    latestBlock = rpc.eth_blockNumber()
    for i in range(startBlock, latestBlock, 1):
      data = rpc.eth_getBlockByNumber(i, True)
      for j in range(0, len(data["transactions"]), 1):
        if data["transactions"][j]["to"] == contract:
          receipt = rpc.eth_getTransactionReceipt(data["transactions"][j]['hash'])
          gasPrice = int(data["transactions"][j]["gasPrice"], 16)
          gasUsed = int(receipt['gasUsed'], 16) 

          writer.writerow([int(data["timestamp"], 16),
          int(data['number'], 16),
          data['transactions'][j]['hash'],
          int(data['transactions'][j]['transactionIndex'], 16),
          data["transactions"][j]["from"],
          int(data["transactions"][j]["value"], 16),
          gasPrice, 
          gasUsed,
          (gasPrice * gasUsed),
          data['transactions'][j]['raw'][:6]])


def main():
  contractToTrack = '0x719ea19781af64a5f3997fc2b93368d1fe643066'
  creationBlock = findContractCreationBlock(contractToTrack)
  findContractCalls(creationBlock, contractToTrack) 

if __name__ == "__main__":
    main()
