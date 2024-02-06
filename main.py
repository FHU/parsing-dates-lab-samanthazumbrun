num_mon = 0
def parse_month(month):
    month=month[:3].lower()
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
extra_zero = 0
day = 0
def parse_date(month, day, year):
    month, day, year = month.strip(","), day.strip(","), year.strip(",")
    month = str(parse_month(month))
    day = str(day)
    if len(month)==1:
        month = f"0{month}"
    if len(day)==1:
        day = f"0{day}"
    
    return(f"{month}/{day}/{str(year)}")     
if __name__ == '__main__':
    date = input().split()
    month = date[0]  
    day = date[1] 
    day=day[:2]
    year= date[2]
    print(parse_date(month,day,year))
#test