import calendar
from datetime import datetime

class FourHundredYearsCalendar:
    def __init__(self, start_year=2000, end_year=2399):
        self.start_year = start_year
        self.end_year = end_year

    def is_leap_year(self, year):
        """Check if a given year is a leap year."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_day_of_week(self, year, month, day):
        """Return the day of the week for a given date."""
        try:
            date = datetime(year, month, day)
            return date.strftime("%A")
        except ValueError:
            return "Invalid date"

    def generate_month_calendar(self, year, month):
        """Generate a text-based calendar for a given month and year."""
        if year < self.start_year or year > self.end_year:
            return f"Year {year} is out of range ({self.start_year}-{self.end_year})"
        try:
            cal = calendar.monthcalendar(year, month)
            month_name = calendar.month_name[month]
            output = f"{month_name} {year}\nMo Tu We Th Fr Sa Su\n"
            for week in cal:
                for day in week:
                    output += f"{day:2d} " if day != 0 else "   "
                output += "\n"
            return output
        except ValueError:
            return "Invalid month or year"

    def count_leap_years(self):
        """Count leap years in the 400-year range."""
        return sum(1 for year in range(self.start_year, self.end_year + 1) if self.is_leap_year(year))

def main():
    cal = FourHundredYearsCalendar()
    while True:
        print("\n400 Years Calendar (2000-2399)")
        print("1. Check day of the week")
        print("2. Display month calendar")
        print("3. Count leap years")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            try:
                year = int(input("Enter year (2000-2399): "))
                month = int(input("Enter month (1-12): "))
                day = int(input("Enter day (1-31): "))
                print(f"Day: {cal.get_day_of_week(year, month, day)}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == "2":
            try:
                year = int(input("Enter year (2000-2399): "))
                month = int(input("Enter month (1-12): "))
                print(cal.generate_month_calendar(year, month))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == "3":
            print(f"Number of leap years: {cal.count_leap_years()}")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()