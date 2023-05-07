import math

def main():
    option = take_input()
    if option == 'n':
        s = get_number_of_monthly_payments()
    elif option == 'a':
        s = get_annuity_pma()
    else:
        s = get_loan_principal()
    print(s)


def take_input():
    print('''What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal: ''')
    print()
    s = input()
    return s

def get_annuity_pma():
    lp = int(input('Enter the loan principal: '))
    nop = int(input('Enter the number of periods: '))
    li = float(input('Enter the loan interest: '))
    i = float(li / 1200)
    mp = math.ceil(lp * (i * math.pow(1 + i, nop)) / (math.pow(1 + i, nop) - 1))
    return f'Your monthly payment = {mp}!'

def get_loan_principal():
    ap = float(input('Enter the annuity payment: '))
    nop = int(input('Enter the number of periods: '))
    li = float(input('Enter the loan interest: '))
    i = float(li / 1200)
    lp = ap / ((i * math.pow(1 + i, nop)) / (math.pow(1 + i, nop) - 1))
    return f'Your loan principal = {round(lp)}!'


def get_number_of_monthly_payments():
    lp = int(input('Enter the loan principal: '))
    mp = int(input('Enter the monthly payment: '))
    li = float(input('Enter the loan interest: '))
    i = float(li / 1200)
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
        return f'It will take {months} {text_months} to repay this loan!'
    elif months == 0:
        return f'It will take {years} {text_years} to repay this loan!'
    else:
        return f'It will take {years} {text_years} and {months} {text_months} to repay this loan!'


if __name__ == "__main__":
    main()
