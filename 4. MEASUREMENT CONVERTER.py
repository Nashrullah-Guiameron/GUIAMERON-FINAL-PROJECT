print()
print('** MEASUREMENT CONVERTER **')
print()

conversions_availabe = [(1,'km', 'mi'),
                        (2, 'mi', 'km'),
                        (3, 'kg', 'lbs'),
                        (4, 'lbs', 'kg'),
                        (5, 'in', 'ft')
                        ]

print('Conversion Avaiable:')
print()

for conversions_number, from_unit, to_unit in conversions_availabe:
    print(f'{conversions_number}) {from_unit} -> {to_unit}')
    
print()
conversion = input('Enter The number of the conversion to use:')
conversion_index = int(conversion) - 1

conversion_number, from_unit, to_unit = conversions_availabe[conversion_index]
print()
from_value = float(input(f'ENTER {from_unit} -->'))

if conversion_number == 1:
    to_value = from_value * 0.62
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
elif conversion_number == 2:
    to_value = from_value * 1.61
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
elif conversion_number == 3:
    to_value = from_value * 2.22
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
elif conversion_number == 4:
    to_value = from_value * 0.45
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
elif conversion_number == 5:
    to_value = from_value * 0.08
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')



