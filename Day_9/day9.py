from art import logo
print(logo)
bids = {}
def finde_highest_bidder(bidding_dect):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dect:
        bid_amount = bidding_dect[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid_amount

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    shude_continue = input("Are there any oter bidder? Type 'yes' or 'no'.\n").lower()
    if shude_continue == "no":
        finde_highest_bidder(bids)
        break
    elif shude_continue == "yes":
        print("\n" * 20)
        
        
        



