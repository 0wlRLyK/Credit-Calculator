import argparse
import sys
from math import ceil, log, floor

def endings(value):
    if value % 12 == 0:
        y = round(value / 12)
        if y != 1:
            return "You need {} years to repay this credit!".format(y)
        return "You need {} year to repay this credit!".format(y)
    else:
        y = round(value / 12)
        m = (value % 12) + 1
        if m != 1:
            if y != 1:
                return "You need {} years and {} months to repay this credit!".format(y, m)
            return "You need {} year and {} months to repay this credit!".format(y, m)
        else:
            if y != 1:
                return "You need {} years and {} month to repay this credit!".format(y, m)
            return "You need {} year and {} month to repay this credit!".format(y, m)


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()


if args.type not in ['diff', 'annuity']:
    print('Incorrect parameters')
elif args.type == 'diff' and args.payment:
    print('Incorrect parameters')
elif not args.interest:
    print('Incorrect parameters')
elif len(sys.argv) < 4:
    print('Incorrect parameters')
else:
    TYPE = args.type
    P = args.principal
    N = args.periods
    INTEREST = args.interest / 100
    I = INTEREST / 12 * 1
    PAYMENT = args.payment


    if TYPE == "diff" and P and N and INTEREST:
        Over = 0
        for num in range(1, N + 1):
            calc = ceil(P / N + I * (P - (P * (num - 1) / N)))
            Over += calc
            print(f"Month {num}: paid out {calc}")
        overpayment = Over - P
        print(f"\nOverpayment = {overpayment}")
    elif TYPE == "annuity" and P and N and INTEREST:
        annuity_payment = ceil(P * (I * pow((1 + I), N) / (pow(1 + I, N) - 1)))
        print(f"Your annuity payment = {annuity_payment}!")
        overpayment = annuity_payment * N - P
        print(f"Overpayment = {overpayment}")
    elif TYPE == "annuity" and PAYMENT and N and INTEREST:
        credit_principal = floor((PAYMENT / ((I * pow(1 + I, N)) / (pow(1 + I, N) - 1))))
        print(f"Your credit principal = {credit_principal}!")
        overpayment = PAYMENT * N - credit_principal
        print(f"Overpayment = {overpayment}")
    elif TYPE == "annuity" and P and PAYMENT and INTEREST:
        repayment = round(log((PAYMENT / (PAYMENT - I * P)), 1 + I))
        print(endings(repayment))
        overpayment = PAYMENT * repayment - P
        print(f"Overpayment = {overpayment}")
    else:
        print('Incorrect parameters')
