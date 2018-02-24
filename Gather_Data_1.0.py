# https://api.cryptowat.ch/markets/gdax/ethusd/price
# {
#     "result":{"price":862.13},
#     "allowance":{"cost":991451,"remaining":7999008549}
# }

# import collections as col
import urllib3 as ul
import csv
import certifi
import json
import time


def error_check(code):
    switcher = {
        # Server issue
        800: "No response from API",
        801: "Network Problem",
        802: "Unauthenticated requrest",
        803: "Request was rate limited",
        804: "API key lacking necessary privileges",
        805: "API key invalid",
        806: "Invalid nonce",
        807: "Invalid passphrase",
        808: "Timeout",
        809: "Exchange API is unavailable",
        810: "Invalid anonymous session",
        820: "Internal error",
        821: "Unknown error",
        # User isue
        900: "Not enough balance",
        901: "Order ID is invalid",
        902: "Order amount is too small",
        903: "Cannot open position",
        904: "Margin allowance exceeded",
        905: "Insufficient margin",
        906: "Too many open orders",
        907: "Too many open positions",
        908: "Invalid position",
        909: "Invalid arguments",
        910: "Invalid price parameter",
        911: "Invalid amount parameter",
        912: "Price is too precise",
        913: "Order price is too low/high",
        914: "Order size is too low/high"
    }
    return switcher.get(code, "success")


def write_data(response, name):
    data = json.loads(response.data.decode('utf-8'))
    with open(name, 'a', newline='') as file:
        fields = ['price', 'time', 'time remaining']
        writer = csv.DictWriter(file, fieldnames=fields)
        # print(data["result"]["price"])
        # print(data["allowance"]["cost"])
        # print(data["allowance"]["remaining"])
        writer.writerow({'price': data["result"]["price"],
                         'time': data["allowance"]["cost"],
                         'time remaining': data["allowance"]["remaining"]
                         })


def write_header(response, fields, file):
    err = error_check(response.status)
    if err == "success":
        with open(file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()


def switch_state(state):
    if state:
        state = False
    else:
        state = True


def get_state(state):
    if state:
        return "stop"
    return "start"


def update(filename, repeats, sleep):
    for i in range(0, repeats):
        print(str(i) + " out of " + str(repeats))
        r = http.request(
            "GET",
            "https://api.cryptowat.ch/markets/gdax/ethusd/price")
        write_data(r, filename)
        time.sleep(sleep)


# def window(state, window):
#     startend = tk.Button(top,
#                          text=get_state(on),
#                          fg='green',
#                          command=switch_state(on))
#     startend.pack(side=tk.LEFT)
#     quit = tk.Button(top,
#                      text='QUIT',
#                      fg='red',
#                      command=end())
#     quit.pack(side=tk.RIGHT)
#     window.mainloop()


#############
### START ###
#############

# Get data and record
# on = False  # false = off, true = on
filename = "test.csv"
data_points = 500
data_spacing = 1
http = ul.PoolManager(cert_reqs='CERT_REQUIRED',
                      ca_certs=certifi.where()
                      )
fields = ['price',
          'time',
          'time remaining'
          ]
response = http.request(
    "GET",
    "https://api.cryptowat.ch/markets/gdax/ethusd/price"
)
# write_header(response, fields, filename)
print("Gathering data...")
update(filename, data_points, data_spacing)
