from calculator.run import CommandLine, days_elapsed, days_in_between, is_leap_year


def test_command_line():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert user_input.day1 == 1


def test_year_check():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert user_input.year_check("1989,")
    assert not user_input.year_check("123d,")
    assert not user_input.year_check("123d")
    assert user_input.year_check("2000")
    assert not user_input.year_check("123")


def test_month_check():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert not user_input.month_check("-1")
    assert not user_input.month_check("13")
    assert not user_input.month_check("00")
    assert not user_input.month_check("8")
    assert not user_input.month_check("dd")
    assert not user_input.month_check("123")
    assert user_input.month_check("08")


def test_day_check():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    assert not user_input.day_check("1", 2, 2008)
    assert not user_input.day_check("dd", 2, 2008)
    assert not user_input.day_check("00", 2, 2008)
    assert not user_input.day_check("-1", 2, 2008)
    assert not user_input.day_check("30", 2, 2008)
    assert not user_input.day_check("29", 2, 1900)
    assert not user_input.day_check("31", 6, 2008)
    assert user_input.day_check("31", 8, 2008)


def test_is_earliest_day():
    argv = ["run.py", "01", "03", "1990,", "29", "02", "2008"]
    user_input = CommandLine(argv)
    test1 = ["run.py", "01", "03", "1990,", "01", "03", "1990"]
    test2 = ["run.py", "01", "03", "1995,", "01", "03", "1990"]
    test3 = ["run.py", "01", "08", "1990,", "01", "03", "1990"]
    test4 = ["run.py", "07", "08", "1990,", "06", "08", "1990"]
    assert user_input.is_earliest_day(test1)
    assert not user_input.is_earliest_day(test2)
    assert not user_input.is_earliest_day(test3)
    assert not user_input.is_earliest_day(test4)


def test_format_response():
    test1 = ["run.py", "01", "03", "1990,", "10", "10", "1995"]
    test2 = ["run.py", "10", "10", "1995,", "01", "03", "1990"]
    user_input1 = CommandLine(test1)
    user_input2 = CommandLine(test2)
    assert user_input1.format_response(test1) == "01 03 1990, 10 10 1995"
    assert user_input2.format_response(test2) == "01 03 1990, 10 10 1995"


def test_is_leap_year():
    assert not is_leap_year(1995)
    assert not is_leap_year(1900)
    assert is_leap_year(2000)
    assert is_leap_year(2004)


def test_days_elapsed():
    assert days_elapsed(3, 3, 2008) == 63
    assert days_elapsed(14, 2, 2008) == 45
    assert days_elapsed(25, 10, 2005) == 298


def test_days_in_between():
    argv1 = ["run.py", "14", "02", "2008,", "03", "09", "2008"]
    argv2 = ["run.py", "14", "02", "1957,", "03", "09", "2008"]
    argv3 = ["run.py", "31", "12", "2010,", "01", "01", "1900"]
    user_input1 = CommandLine(argv1)
    user_input2 = CommandLine(argv2)
    user_input3 = CommandLine(argv3)
    assert days_in_between(user_input1) == 202
    assert days_in_between(user_input2) == 18829
    assert days_in_between(user_input3) == 40541
