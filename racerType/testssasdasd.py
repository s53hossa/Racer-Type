def get_day_of_week(month, day, year):
    # Adjust month and year according to Zeller's algorithm
    if month < 3:
        month += 12
        year -= 1
    
    K = year % 100
    J = year // 100
    
    # Zeller's Congruence formula
    f = day + 13*(month + 1)//5 + K + K//4 + J//4 + 5*J
    day_of_week = f % 7
    
    # Mapping Zeller's output to day names
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    return days[day_of_week]

# Take input from the user
date_str = input("Enter the date (month day year): ")
month, day, year = map(int, date_str.split())

# Get the day of the week
day_of_week = get_day_of_week(month, day, year)

# Output the result
print(f"The date {date_str} is a {day_of_week}.")