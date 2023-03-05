import requests
import bs4
import json

def scan_warframe(item_name):
    item_name = item_name.lower()
    item_name = str(item_name).replace(" ","_")

    API_template = f"https://api.warframe.market/v1/items/{item_name}/orders"

    src = requests.get(API_template).content
    src = str(src).strip()




    with open("output.json","w") as data_file:
        # Formats the src code to be in json format by removing a few extra
        data_file.write(src[2:-1])
        data_file.close()

    with open("output.json") as order_data:
        exported_data = json.load(order_data)
        order_data.close()

    found_data = exported_data['payload']['orders']

    total_price = 0
    order_count = 0
    prices = []

    for order in found_data:
        
        if order["order_type"] =="buy":
            order_count+=1
            found_price = order['platinum']
            prices.append(found_price)

            total_price += found_price
            prices.sort()

    average_price = total_price/order_count
    lowest_price = prices[0]
    highest_price = prices[-1]
    print(f'Average: {average_price}\nTotal Orders: {order_count}\nLowest Price: {lowest_price}\nHighest Price: {highest_price}')

while True:
    item_name = input("Please enter name of item: ")
    if item_name.lower() == 'exit':
        print("Terminating Warframe bot")
        break
    else:
        try:
            scan_warframe(item_name)
        except:
            print("Item not found, please try again")
    print("\n\n\n")
