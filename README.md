# ticker-watcher

Gather_Data_1.0.py uses an online API for looking up live cryptocurrency costs. In this example, the link to the API to view the price of ETH or Etherium is:

  https://api.cryptowat.ch/markets/gdax/ethusd/price

Once pulled, the output is saved to a dictionary as shown below. Per the API documentation (https://cryptowat.ch/docs/api), the result variable points to two dictionary terms: "result" and "allowance" as shown below:

{"result":{"price":862.13},"allowance":{"cost":991451,"remaining":7999008549}}

Restructured for readability, the same output looks like this:
- {
  - "result":{"price":862.13},
  - "allowance":{"cost":991451,"remaining":7999008549}
- }
  
The result term points to another dictionary consisting only of the variable "price" which contains the live updated information which will be used.

The second dictinoary term "allowance" provides data on the time taken to access and obtain the price information.  Each client is allowed 8000000000 nanoseconds or 8 seconds of access per hour.  This means that the frequency of pulling the data during the stream is dictated by the "cost" variable defined by the "allowance" term.
