import  os
def find_winner(bidders_data):
    highest_bid = 0
    winner = ""
    for bidder in bidders_data:
        bidding_prices =bidders_data[bidder]
        if bidding_prices> highest_bid:
            highest_bid =bidders_data[bidder]
            winner = bidder
    print(f"Here is the list of all the bidders:\n{bidders_data}")
    print(f"The winner is {winner} with bid {highest_bid} lakh.")
    print("Thank you")



bidders_data={}

flag = True
while flag:
    name = input("what is your name:")
    bid_price = int(input("what is your bid?:"))
    bidders_data[name] = bid_price
    bid_flag = True
    while bid_flag:
        more_bidders = input("Are there any other bidders? type 'yes' or 'no':").lower()
        if more_bidders == 'no' or more_bidders == 'n':
            flag = False
            find_winner(bidders_data)
        elif more_bidders == 'yes' or more_bidders == 'y':
            bid_flag = False
            os.system('cls')
        else:
            print("invalid input plz enter yes or no")





