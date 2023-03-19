"""
Movie theatre ticketing system - v3
Calculate price
Created by Eleasha Chan
"""


# Component 1 - welcome screen and set up variables
def sell_ticket():
    print("********** Fanfare Movies - ticketing system **********\n")

    adult_tickets = 0
    child_tickets = 0
    student_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

    # Component 2 - get details of sale
    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What kind of ticket do you want? Press: \n"
                            "\t A for Adult \n"
                            "\t C for Child \n"
                            "\t S for Student \n"
                            "\t G if using a Gift Voucher \n"""
                            ">> ").upper()
        ticket = ticket_type
        num_tickets = int(input(f"How many {ticket} tickets do you want: "))

        cost = get_price(ticket_type)

        print(f"You have ordered {num_tickets} {ticket} tickets! \n"
              f"Cost: ${cost:.2f} \n"
              f"Total: ${cost * num_tickets:.2f}")
        ticket_wanted = input("Do you want to order another ticket? Y/N: "
                              "").upper()


# Component 3 - calculate price
def get_price(type_):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type_"":
            return price[1]


# Main routines
sell_ticket()
