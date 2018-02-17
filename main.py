#!/usr/bin/env python3

__author__ = "Michael Danko"
__version__ = "0.1.0"
__license__ = "MIT"

import json
from ethjsonrpc import ParityEthJsonRpc

rpc = ParityEthJsonRpc('127.0.0.1', 8545)

# Created in block 5934492
# 0x719ea19781af64a5f3997fc2b93368d1fe643066

def findContractCreationBlock(contract):
  latestBlock = rpc.eth_blockNumber()
  for i in range(latestBlock, 5934492, -1):
    print("Searching:" + str(i))
    data = rpc.eth_getBlockByNumber(i, True)
    for j in range(0, len(data["transactions"]), 1):
      if data["transactions"][j]["creates"] == contract:
        print(int(data["number"], 16))
  return(data)


def main():
#  print(json.dumps(rpc.eth_getBlockByNumber(5934492, True), indent=4))
  createdBlock = 5934492
  transactionBlock = 5934537
  findContractCreationBlock('0x719ea19781af64a5f3997fc2b93368d1fe643066')
#  print(foundContract)
  data = rpc.eth_getBlockByNumber(transactionBlock, True)
#  for i in range(latestBlock, latestBlock - 1000, -1):
#    data = rpc.eth_getBlockByNumber(i, True)
#    
#  for j in range(0, len(data["transactions"]), 1):
#    #if data["transactions"][j]["creates"]:
#    print(json.dumps(data["transactions"], indent=2))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
