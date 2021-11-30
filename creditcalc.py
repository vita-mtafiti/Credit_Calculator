
import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"], help="type of payment: 'annuity' or 'diff' (differentiated)")

parser.add_argument("--payment", type=float, help="monthly payment amount")

parser.add_argument("--periods", type=int, help="number of months needed to repay the loan")

parser.add_argument("--interest", type=float)

parser.add_argument("--principal", type=float)

args = parser.parse_args()

loan_parameters = [args.type, args.payment, args.periods, args.interest, args.principal]
values_parameters = [args.payment, args.periods, args.interest, args.principal]

if args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters - type is not given")
    exit()

if args.payment and args.type == "diff":
    print("Incorrect parameters - diff & payment")
    exit()

if not args.interest:
    print("Incorrect parameters - interest value is not given")
    exit()
else:
    interest = float(args.interest / (12 * 100))


for i in values_parameters:
    if i is not None:
        if i < 0:
            print("Incorrect parameters - negative value")
            exit()

#if args.payment < 0 or args.periods < 0 or args.interest < 0 or args.principal < 0:


def differentiated_payments():
        m = 1
        dp_result = 0
        while m < (args.periods + 1):
            brackets = args.principal - ((args.principal * (m - 1)) / args.periods)
            dp = math.ceil((args.principal / args.periods) + interest * brackets)
            # math.ceil(args.principal / args.periods + (interest * (args.principal - (args.principal * m - 1) / args.periods)))
            print(f"Month {m}: payment is {dp}")
            dp_result += dp
            m += 1
        result = math.ceil(dp_result - args.principal)
        print(f"Overpayment = {result}")


def annuity_monthly_payment_amount():
    numerator = interest * (math.pow((1 + interest), args.periods))
    denominator = math.pow((1 + interest), args.periods) - 1
    annuity_payment = args.principal * (numerator / denominator)
    # annuity_payment = args.principal * ((interest * pow((1 + interest), args.periods)) / (pow((1 + interest), args.periods) - 1))
    print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
    result = math.ceil((math.ceil(annuity_payment) * args.periods) - args.principal)
    print(f"Overpayment = {result}")


def loan_principal():
    loan_principal_result = args.payment / ((interest * pow((1 + interest), args.periods)) / (pow((1 + interest), args.periods) - 1))
    print(f"Your loan principal = {math.ceil(loan_principal_result)}!")
    result = math.ceil(args.payment * args.periods - loan_principal_result)
    print(f"Overpayment = {result}")


def number_of_monthly_payments():
    x = args.payment / (args.payment - interest * args.principal)
    log_result = math.log(x, 1 + interest)
    number_of_months = math.ceil(log_result)
    if number_of_months < 12:
        print(f"It will take {number_of_months} months to repay this loan!")
    else:
        whole = int(number_of_months / 12)
        remainder = math.ceil(int(number_of_months % 12))
        if remainder == 1:
            print(f"It will take {whole} years and 1 month to repay this loan!")
        elif remainder == 0:
            print(f"It will take {whole} years to repay this loan!")
        else:
            print(f"It will take {whole} years and {remainder} months to repay this loan!")
    result = math.ceil(args.payment * number_of_months - args.principal)
    print(f"Overpayment = {result}")


# if len(loan_parameters) < 4 or len(loan_parameters) >= 5:
#     print("Incorrect parameters - 4 paramenters needed")
#     exit()
# elif len(loan_parameters) == 4:

arg_values = []

for i in loan_parameters:
    if i is not None:
        arg_values.append(i)


if len(arg_values) < 4 or len(arg_values) >= 5:
    print("Incorrect parameters - 4 paramenters needed")
    exit()
elif len(arg_values) == 4:
    if args.type == "diff" and args.principal and args.periods and args.interest:
        differentiated_payments()
    elif args.type == "annuity" and args.principal and args.periods and args.interest:
        annuity_monthly_payment_amount()
    elif args.type == "annuity" and args.payment and args.periods and args.interest:
        loan_principal()
    elif args.type == "annuity" and args.principal and args.payment and args.interest:
        number_of_monthly_payments()

