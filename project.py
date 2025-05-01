print()

print('Please provide the following information:')
print()
# Prompt for username and password
first_name = input('First name: ')
print()
last_name = input('Last name: ')
print()
email_address = input('Email address: ')
print()
phone_number = input('Phone number: ')
print()
job_title = input('Job title: ')
print()
id_number = input('ID Number: ')
print()

hair_color = input('Hair: ')
print()
eye_color = input('Eyes: ')
print()
start_month = input('Month: ')
print()
training = input('Enter Yes or No: ')
print()

badge = f'''
The ID card is:
----------------------------------------'''
{last_name}, {first_name}
{email_address}
{phone_number}
{hair_color}, {eye_color}
{start_month}, {training}
{job_title}
{badge}
print()
print('The ID card is:')
print('----------------------------------------')
print(f'{first_name.upper()}, {last_name.capitalize()}')
print(f'{job_title}')
print(f'{id_number}')
print()

print(f'{email_address}')
print(f'{phone_number}')
print()
print(f'Hair: {hair_color.capitalize()}        Eyes: {eye_color.capitalize()}')
print(f'Month: {start_month.capitalize()}      Training: {training.capitalize()}')
print('----------------------------------------')
print()
