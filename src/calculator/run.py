import sys

USAGE = f"usage: python {sys.argv[0]} DD MM YYYY, DD MM YYYY"

class CommandLine:
    def __init__(self, argv):
        self.daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Check the number of arguments from standard input
        if len(argv) != 7:
            self.warning()

        # Validate Year
        if (not self.yearCheck(argv[3]) or not self.yearCheck(argv[6])):
            print("invalid year")
            self.warning()
        self.year1 = int(argv[3][0:4])
        self.year2 = int(argv[6])

        # Validate Month
        if (not self.monthCheck(argv[2]) or not self.monthCheck(argv[5])):
            print("invalid month")
            self.warning()
        self.month1 = int(argv[2])
        self.month2 = int(argv[5])

        # Validate Day
        if (not self.dayCheck(argv[1], self.month1, self.year1) or not self.dayCheck(argv[4], self.month2, self.year2)):
            print("invalid day")
            self.warning()
        self.day1 = int(argv[1])
        self.day2 = int(argv[4])

        # isEarliest Flag
        self.isEarliest = self.isEarliestDay(argv)
        if (not self.isEarliest):
            self.year1 = int(argv[6])
            self.year2 = int(argv[3][0:4])
            self.month1 = int(argv[5])
            self.month2 = int(argv[2])
            self.day1 = int(argv[4])
            self.day2 = int(argv[1])

        self.response = self.formatResponse(argv)

    # Print error message
    def warning(self):
        print("error: Invalid input format")
        raise SystemExit(USAGE)

    def yearCheck(self, year):
        # 1. Type check: year has to be a four-digit integer
        # Handle case like "1990,"
        if (len(year) == 5):
            if (not year[0:4].isdigit()):
                return False
            else:
                return True
        # Handle regular cases like "2008"
        if (len(year) != 4):
            return False
        if (not year.isdigit()):
            return False
        return True

    def monthCheck(self, month):
        # 1. Type check: month has to be a two-digit integer
        if (len(month) != 2):
            return False
        if (not month.isdigit()):
            return False
        # 2. Value check
        if (int(month) < 1 or int(month) > 12):
            return False
        return True

    def dayCheck(self, day, month, year):
        # 1. Type check: day has to be a two-digit integer
        if (len(day) != 2):
            return False
        if (not day.isdigit()):
            return False
        # 2. Value check
        dayInDigit = int(day)
        if (dayInDigit < 1): return False
        # Special case: leap year
        if (month == 2):
            if (isLeapYear(int(year))):
                if (dayInDigit > 29):
                    return False
                else:
                    return True
        # General cases
        if (dayInDigit > self.daysOfMonths[month]):
            return False
        return True

    # Check whether Date1 is earlier than Date2
    def isEarliestDay(self, argv):
        # Compare with year
        if (int(argv[3][0:4]) > int(argv[6])):
            return False
        elif (int(argv[3][0:4]) == int(argv[6])):
            # Same year -> compare with month
            if (int(argv[2]) > int(argv[5])):
                return False
            elif (int(argv[2]) == int(argv[5])):
                # Same month -> compare with day
                if (int(argv[1]) > int(argv[4])):
                    return False
        return True

    # Generate formated string for output
    def formatResponse(self, argv):
        response = ""
        if (self.isEarliest):
            for i in range(1, 6):
                response += argv[i]
                response += " "
            response += argv[6]
        else:
            for i in range(4, 6):
                response += argv[i]
                response += " "
            response += argv[6] + ", "
            for i in range(1, 3):
                response += argv[i]
                response += " "
            response += argv[3][0:4]
        return response

# Check if it is a leap year
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# Calculate how many days have passed this year
def daysElapsed(day, month, year):
    daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if (month > 2 and isLeapYear(year)): days += 1
    for i in range(1, month):
        days += daysOfMonths[i]
    return days + day

# Calculate numbers of days between two dates
def daysInBetween(input):
    d1 = input.day1
    d2 = input.day2
    m1 = input.month1
    m2 = input.month2
    y1 = input.year1
    y2 = input.year2

    if (y1 == y2):
        return daysElapsed(d2, m2, y2) - daysElapsed(d1, m1, y1)
    else:
        date1Elapsed = daysElapsed(d1, m1, y1)
        date2Elapsed = daysElapsed(d2, m2, y2)
        remainDaysInY1 = 366 - date1Elapsed if isLeapYear(y1) else 365 - date1Elapsed

        dayDifference = 0
        for i in range(1, (y2 - y1)):
            year = y1 + i
            dayDifference += 366 if isLeapYear(year) else 365

    return remainDaysInY1 + dayDifference + date2Elapsed

def main():
    user_input = CommandLine(sys.argv)
    result = daysInBetween(user_input)
    answer = "{}, {}"\
        .format(user_input.response, result)
    print(answer)

if __name__=="__main__":
    main()