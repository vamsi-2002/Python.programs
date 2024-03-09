def is_leap_year(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False


def get_month_days(year, month):
  if month in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  elif month in [4, 6, 9, 11]:
    return 30
  elif is_leap_year(year):
    return 29
  else:
    return 28


def print_calendar(year, month):
  days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

  num_days = get_month_days(year, month)

  days = []
  for i in range(1, num_days + 1):
    days.append(i)

  print(f"Calendar for {month}/{year}")
  print("-" * 20)
  for day in days_of_week:
    print(f"{day:3}", end=" ")
  print()

  for i in range(0, len(days), 7):
    for j in range(i, i + 7):
      if j < len(days):
        print(f"{days[j]:3}", end=" ")
      else:
        print("   ", end=" ")
    print()
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print_calendar(year, month)