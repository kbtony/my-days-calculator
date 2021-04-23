from calculator.run import CommandLine, daysElapsed, daysInBetween, isLeapYear


def test_command_line():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert user_input.day1 == 1


def test_year_check():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert user_input.yearCheck("1989,")
    assert not user_input.yearCheck("123d,")
    assert not user_input.yearCheck("123d")
    assert user_input.yearCheck("2000")
    assert not user_input.yearCheck("123")


def test_month_check():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert not user_input.monthCheck("-1")
    assert not user_input.monthCheck("13")
    assert not user_input.monthCheck("00")
    assert not user_input.monthCheck("8")
    assert not user_input.monthCheck("dd")
    assert not user_input.monthCheck("123")
    assert user_input.monthCheck("08")


def test_day_check():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert not user_input.dayCheck("1", 2, 2008)
    assert not user_input.dayCheck("dd", 2, 2008)
    assert not user_input.dayCheck("00", 2, 2008)
    assert not user_input.dayCheck("-1", 2, 2008)
    assert not user_input.dayCheck("30", 2, 2008)
    assert not user_input.dayCheck("29", 2, 1900)
    assert not user_input.dayCheck("31", 6, 2008)
    assert user_input.dayCheck("31", 8, 2008)


def test_is_earliest_day():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    test1 = ["run.py", "01", "03", "1990,", "01", "03", "1990"]
    test2 = ["run.py", "01", "03", "1995,", "01", "03", "1990"]
    test3 = ["run.py", "01", "08", "1990,", "01", "03", "1990"]
    test4 = ["run.py", "07", "08", "1990,", "06", "08", "1990"]
    assert user_input.isEarliestDay(test1)
    assert not user_input.isEarliestDay(test2)
    assert not user_input.isEarliestDay(test3)
    assert not user_input.isEarliestDay(test4)


def test_format_response():
    test1 = ["run.py", "01", "03", "1990,", "10", "10", "1995"]
    test2 = ["run.py", "10", "10", "1995,", "01", "03", "1990"]
    user_input1 = CommandLine(test1)
    user_input2 = CommandLine(test2)
    assert user_input1.formatResponse(test1) == "01 03 1990, 10 10 1995"
    assert user_input2.formatResponse(test2) == "01 03 1990, 10 10 1995"


def test_is_leap_year():
    assert not isLeapYear(1995)
    assert not isLeapYear(1900)
    assert isLeapYear(2000)
    assert isLeapYear(2004)


def test_days_elapsed():
    assert daysElapsed(3, 3, 2008) == 63
    assert daysElapsed(14, 2, 2008) == 45
    assert daysElapsed(25, 10, 2005) == 298


def test_days_in_between():
    argv1 = ["run.py", "14", "02", "2008,", "03", "09", "2008"]
    argv2 = ["run.py", "14", "02", "1957,", "03", "09", "2008"]
    argv3 = ["run.py", "31", "12", "2010,", "01", "01", "1900"]
    user_input1 = CommandLine(argv1)
    user_input2 = CommandLine(argv2)
    user_input3 = CommandLine(argv3)
    assert daysInBetween(user_input1) == 202
    assert daysInBetween(user_input2) == 18829
    assert daysInBetween(user_input3) == 40541

