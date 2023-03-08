# 2095022 # EMAD ABBASI
# QUARTERS, NICKLES, DIMES AND PENNIES

def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100
# remainder from 100 gives us dollars
    num_quarters = user_total // 25
    user_total %= 25
# remainder from 25 from that 100 gives us quarters
    num_dimes = user_total // 10
    user_total %= 10
# and so on and so forth
    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input())

    if input_val <= 0:
        print('no change')
    else:
        num_dollars, num_quarters, num_dimes, num_nickles, num_pennies = exact_change(input_val)

        if num_dollars > 0:
            if num_dollars == 1:
                print('1 dollar')
            else:
                print(num_dollars, 'dollars')

        if num_quarters > 0:
            if num_quarters == 1:
                print('1 quarter')
            else:
                print(num_quarters, 'quarters')
# implementing singular/plural in case we get just one dime instead of many dimes
        if num_dimes > 0:
            if num_dimes == 1:
                print('1 dime')
            else:
                print(num_dimes, 'dimes')

        if num_nickles > 0:
            if num_nickles == 1:
                print('1 nickel')
            else:
                print(num_nickles, 'nickles')

        if num_pennies > 0:
            if num_pennies == 1:
                print('1 penny')
            else:
                print(num_pennies, 'pennies')


