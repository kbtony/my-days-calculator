# My-days-calculator
My-days-calculator will find out how many days are there between two dates.
## Technologies
Project is created with:
* Python 3.9.1

Testing with:
* Pytest 6.2.2
## Launch
Simply execute **run.py** and specify two dates through **standard input**.
The pairs of dates must be in the following format:
```
DD MM YYYY, DD MM YYYY
```
## Sample Outputs
```
$> python3 run.py 03 09 2009, 14 02 1943

14 02 1943, 03 09 2009, 24308
```
## Design and Assumptions
### Design
We put most code into a function or class and call them from main().  
```
def main():
    user_input = CommandLine(sys.argv)
    result = daysInBetween(user_input)
    answer = "{}, {}"\
        .format(user_input.response, result)
    print(answer)
```
First, we validate the information entered by the user and store it in the CommandLine class.

We then calculate the days between two dates by comparing their year, month, and day in order and output the result.
### Assumptions
We do not include the end date in the calculation. Therefore, it is 1 day from 02.09.2009 to 03.09.2009.
