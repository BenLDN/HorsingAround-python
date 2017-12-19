from blockchain import statistics
from blockchain import blockexplorer

stats = statistics.get()



print("Estimated trn volume in USD: "+str(round(stats.estimated_transaction_volume_usd,0)))
print("Number of trn: "+str(round(stats.number_of_transactions,0)))
print("Average trn size: "+str(round(stats.estimated_transaction_volume_usd/stats.number_of_transactions,0)))
print("")
print("Trade volume in BTC: "+str(round(stats.trade_volume_btc,0)))
print("Market price in USD: "+str(round(stats.market_price_usd,0)))

latest_block = blockexplorer.get_latest_block()

l_block = blockexplorer.get_block(latest_block.hash)

print("Transactions in the latest block: "+str(l_block.n_tx))
