import math
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    args = parser.parse_args()

    try:
        i = float(args.interest)
        i = i / 1200
        if i < 0:
            raise TypeError
    except TypeError:
        print("Incorrect parameters")
        sys.exit()
    if args.type != 'diff' and args.type !='annuity':
        print("Incorrect parameters.")

    if args.type =='annuity' and args.payment == None:
        s = get_annuity_pma(args.principal, args.periods, i)
    elif args.type =='annuity' and args.principal == None:
        s = get_loan_principal(args.payment, args.periods, i)
    elif args.type =='annuity' and args.periods == None:
        s = get_number_of_monthly_payments(args.principal, args.payment, i)
    elif args.type =='diff' and args.payment == None:
        s = get_diff_pma(args.principal, args.periods, i)
    print(s)

def get_diff_pma(lp, nop, i):
    try:
        lp = int(lp)
        nop = int(nop)
        sum = 0
        for m in range(1, nop+1):
            mthp = math.ceil( lp / nop + i * (lp -( lp * (m - 1) / nop)) )
            print(f'Month {m}: payment is {mthp}')
            sum = sum + mthp
        return f'\nOverpayment = {sum - lp}'
    except TypeError:
        return f"Incorrect parameters."

def get_annuity_pma(lp, nop, i):
    try:
        lp = int(lp)
        nop = int(nop)
        mp = math.ceil(lp * (i * math.pow(1 + i, nop)) / (math.pow(1 + i, nop) - 1))
        return (f'Your annuity payment = {mp}!\n' +
                f'Overpayment = {int(mp * nop - lp)}')
    except TypeError:
        return f"Incorrect parameters."

def get_loan_principal(ap, nop, i):
    try:
        ap = float(ap)
        nop = int(nop)
        lp = math.floor(ap / ((i * math.pow(1 + i, nop)) / (math.pow(1 + i, nop) - 1)))
        return (f'Your loan principal = {lp}!\n'+
                f'Overpayment = {int(ap * nop - lp)}')
    except TypeError:
        return f"Incorrect parameters."

def get_number_of_monthly_payments(lp, mp, i):
    lp = int(lp)
    mp = int(mp)

    n = math.log(( mp / (mp - i * lp)), 1 + i)
    n = math.ceil(n)
    years = math.floor(n / 12)
    months = n % 12

    if years != 1:
        text_years = 'years'
    else:
        text_years = 'year'
    if months != 1:
        text_months = 'months'
    else:
        text_years = 'month'

    if years == 0:
        s = f'It will take {months} {text_months} to repay this loan!\n'
    elif months == 0:
        s = f'It will take {years} {text_years} to repay this loan!\n'
    else:
        s = f'It will take {years} {text_years} and {months} {text_months} to repay this loan!\n'
    return (s +
            f'Overpayment = {mp * n - lp}')


if __name__ == "__main__":
    main()
