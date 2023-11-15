"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
    Explore the surprising probabilities of the "Birthday Paradox".
    More info at https://en.wikipedia.org/wiki/Birthday_problem
    View this code at https://nostarch.com/big-book-small-python-projects
    Tags: short, math, simulation"""
import datetime, random, calendar

def get_birthdays(num_of_birthdays):
    birthdays = []
    
    for i in range(num_of_birthdays):
        start_of_year = datetime.date(1988, 1, 1)
        
        random_number_of_year = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_year
        birthdays.append(birthday)
    return birthdays

def get_match(birtdays):
    if len(birtdays) == len(set(birtdays)):
        return None
    
    for i, first_birthday in enumerate(birtdays):
        for j, other_birthdays in enumerate(birtdays[i+1:]):
            if first_birthday == other_birthdays:
                return first_birthday

while True:
    print('How many birthdays do you want to create?')
    response = input()
    if response.isdecimal() and (0 < int(response)):
        num_bdays = int(response)
        break
    
birthdays = get_birthdays(num_bdays)

for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = calendar.month_name[birthday.month]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')
        
match = get_match(birthdays)

if match != None:
    month_name = calendar.month_name[birthday.month]
    date_text = f'{month_name} {match.day}'
    print(f'\nMultiple people have birthday on {date_text}')
else:
    print('\nThere are not matching birthdays.')

while True: 
    print('How many runs you want to simulate?')
    response = input()
    if response.isdecimal() and (0 < int(response)):
        simulation_runs = int(response)
        break
    
input('Press Enter to begin...')

simulation_matches = 0
run_cnt = simulation_runs / 5
for i in range(simulation_runs):
    if i % int(run_cnt) == 0:
        print(f'{i} simulation run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birtdays=birthdays) != None:
        simulation_matches += 1

# Display simulation results:
probability = round(simulation_matches / simulation_runs * 100, 2)
print(f'Out of {simulation_runs} simulations of', num_bdays, 'people, there was a')
print('matching birthday in that group', simulation_matches, 'times. This means')
print('that', num_bdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

