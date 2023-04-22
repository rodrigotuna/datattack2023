import holidays

# Define a holiday set for Brazil in 2022
us_holidays = holidays.Portugal(years=[2016,2017,2018,2019,2020])
br_holidays = holidays.CountryHoliday('BR', years=2022) 

# Check if a given date is a holiday
if '2022-01-01' in br_holidays:
    print('New Year\'s Day is a holiday in Brazil')
else:
    print('New Year\'s Day is not a holiday in Brazil')
