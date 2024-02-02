#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    months = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    a = x.strip()[:3].lower()
    num_month = months[a]
    return num_month

extra_zero = 0
month = 0
day = 0
year = 0
def parse_date(day):
    if day > 0 and day < 10:
        day2 = str(day).zfill(extra_zero)
        print(parse_month(month),'/',day2,'/'year)
    else:
        print(parse_month(month),'/',day,'/'year)
        
if __name__ == '__main__':
    date = input().strip(' ')
    month = date[0]
    day = date[1]
    year = date[2]
    parse_date(day)



