"""As part of your community service project, you organize a raffle to raise money for a good cause.  Tickets cost $5 each and you spent $50 on the prizes.  Write a Python function that computes the amount of money you raised. """

def moneyRaised(ticketsBought):
    return "You rasied " + str(5 * ticketsBought - 50) + " dollars!"

print(moneyRaised(240))