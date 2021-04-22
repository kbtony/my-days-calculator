from calculator.run import CommandLine


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





