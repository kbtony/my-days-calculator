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
        # if(self.isEarliest): print("early")
        # else: print("not early")

    # print error message
    def warning(self):
        print("error: Invalid input format")
        raise SystemExit(USAGE)

    def yearCheck(self, year):
        # handle case like "1990,"
        if (len(year) == 5):
            if (not year[0:4].isdigit()):
                return False
            else:
                return True
        # handle regular case like "2008"
        if (len(year) != 4):
            return False
        if (not year.isdigit()):
            return False
        return True

    def monthCheck(self, month):
        if (len(month) != 2):
            return False
        if (not month.isdigit()):
            return False
        if (int(month) < 1 or int(month) > 12):
            return False
        return True

    def dayCheck(self, day, month, year):
        # 1. type check: day has to be a two-digit integer
        if (len(day) != 2):
            return False
        if (not day.isdigit()):
            return False
        # 2. value check
        dayInDigit = int(day)
        if (dayInDigit < 1): return False
        # special case: leap year
        if (month == 2):
            if (isLeapYear(int(year))):
                if (dayInDigit > 29):
                    return False
                else:
                    return True
        # general cases
        if (dayInDigit > self.daysOfMonths[month]):
            return False
        return True

    def isEarliestDay(self, argv):
        # compare with year
        if (int(argv[3][0:4]) > int(argv[6])):
            return False
        elif (int(argv[3][0:4]) == int(argv[6])):
            # if same year, compare with month
            if (int(argv[2]) > int(argv[5])):
                return False
            elif (int(argv[2]) == int(argv[5])):
                # if same month, compare with day
                if (int(argv[1]) > int(argv[4])):
                    return False
        return True

def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def daysElapsed(day, month, year):
    daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if (month > 2 and isLeapYear(year)): days += 1
    for i in range(1, month):
        days += daysOfMonths[i]
    return days + day

# date1 is earlier than date2
def daysInBetween(d1, m1, y1, d2, m2, y2):
    if (y1 == y2):
        return daysElapsed(d2, m2, y2) - daysElapsed(d1, m1, y1)
    else:
        dayDifference = 0
        date1Elapsed = daysElapsed(d1, m1, y1)
        date2Elapsed = daysElapsed(d2, m2, y2)

        if (isLeapYear(y1)):
            remainDaysInY1 = 366 - date1Elapsed
        else:
            remainDaysInY1 = 365 - date1Elapsed
        dayDifference = remainDaysInY1

        for i in range(0, (y2 - y1 - 1)):
            year = y1 + i
            if (isLeapYear(year)):
                dayDifference += 366
            else:
                dayDifference += 365
        dayDifference += date2Elapsed
    return dayDifference



def main():
    user_input = CommandLine(sys.argv)

    print(user_input.day2)
    print("hello")

if __name__=="__main__":
    main()