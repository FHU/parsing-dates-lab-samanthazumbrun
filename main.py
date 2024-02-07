num_mon = 0
def parse_month(month):
    month = month[:3].lower()
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

    return months[month]


def parse_date(date):
    month = str(date[0]) 
    day = str(date[1][:2]).strip(',')
    year= date[2]
    num_month = str(parse_month(month))
    if len(num_month)==1:
        num_month = f"0{num_month}"
    if len(day)==1:
        day = f"0{day}"
    return(f"{num_month}/{day}/{str(year)}")
     
if __name__ == '__main__':
    date = input().split()
    print(parse_date(date))