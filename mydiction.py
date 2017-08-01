school_supplies = [ 'scissors', 'pencils', 'laptop', 'paper', 'binder', 'backpack']

del school_supplies[5]



ss_prices = [5.99, 2.99, 1200, 7.99, 2.99]

print('I need to buy ' + school_supplies[0] + ', they will cost me' + str(ss_prices[0]) + '.')

ss_by_price = [
    'scissors': 5.99,
    'pencils': 2.99,
    'laptop': 1200,
    'paper': 7.99,
    'binder':2.99
]

print(ss_by_price['paper'])

del ss_by_price['binder']

if 'Hard boiled eggs' in ss_by_price:
    print "Got Em"
else:
    print('need to add hard boiled eggs to the list')

for item in ss_by_price:
    price = ss_by_price[item]
    print(item + ': $' str(price))

    print('')


city_info = {'new_york': }
