# create a product and price for three items
product1_name, product1_price = 'CPVC Pipes', 154.89
product2_name, product2_price = 'Column Pipes', 768.56
product3_name, product3_price = 'UPVC Pipes', 956.21

# create a company name and information
company_name = 'Flowkem Pipes Pvt. Limited'
company_address = 'Gandhinagar'
company_city = 'Ahmedabad'

# declare ending message
message = 'Thanks for shopping with us today!'

# create a top border
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name))
print('\t\t{}'.format(company_address))
print('\t\t{}'.format(company_city))

# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
message_print = '\t{}\tRs.{}'
print(message_print.format(product1_name.title(), product1_price))
print(message_print.format(product2_name.title(), product2_price))
print(message_print.format(product3_name.title(), product3_price))

# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = product1_price + product2_price + product3_price
print('\t\t\t${:.2f}'.format(total))

# print a line between sections
print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)