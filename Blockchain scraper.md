# Blockchain scraper


Geth and Parity have trace_ debug functions. 

An 'internal transaction' is a value change that happens from executing the contract. These are not always shown as raw 'in/out' transactions.


To truly monitor a contract and not over-index the blockchain, must do:

1. Determine when the contract was created.
2. scan from that point looking for calls to the contract 
3. Monitor and trace all calls to this contract for flows
4. Decode the first 4bits of method call, record this.


Useless Ethereum Token
Creation block: 0x7e668005bae6354cdb11b333cc01e6acc97b8d5873e7192fc7afa3be2232e616

Creator address: 0x00d0fd20924037C2B182d0aA0B139434A0b1A081

Contract Address: 0x27f706edde3aD952EF647Dd67E24e38CD0803DD6


CSV format :
block_timestamp,
block_number,
tx_hash,
index,
from,
value,
tx_fee,
method_name


Pseudo Code:

start_block = 3940814
contract_addr = "0x27f706edde3aD952EF647Dd67E24e38CD0803DD6"

foreach blocknum in 122121...stop_block:
	block = get_Block(blockNum)
	
	foreach tx in block.txns:
		if tx.to == contract_addr:
			receipt = get_receipt(tx.hash)
			
			# todo figure out the method name
			# decoded = decode_method(tx.input)
			
			fee = receipt.gas_consumed * tx.gas_price

			data = (block.timestamp, block.number, tx.hash, tx.index, tx.from, tx.value, fee , decoded )
			
			output.write(data)
	

