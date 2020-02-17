# Repeating Decimals To Fractions

This script converts a decimal number  with its infinitely recurring digits and returns the equivalent result in fraction form.
## Set up your virtualenv with Python 3.7

Assuming virtualenv is already installed on your system.  
If using a virtualenvwrapper then set up a virtual environment for this project 
eg.
```
mkvirtualenv -p /usr/bin/python3.7 -a [path to project] [virtualenv name]
```
Otherwise set up your virtual environment as you normally would.  

Once your virtualenv is active, from the project root dir install the necessary dependencies

```
pip3 install -r requirements.txt
```

## Script usage
```bash
python solution.py -h      
usage: solution.py [-h] decimal_fraction

Script takes a decimal in string form with the repeating part in parentheses
and returns the equivalent fraction in string form and in lowest terms.

positional arguments:
  decimal_fraction  decimal value in the form "0.(6)", "3.(36)", etc where the
                    digit(s) in the parentheses represent digits that repeat
                    infinitely

optional arguments:
  -h, --help        show this help message and exit

```

## Run script: convert repeating decimals to fraction
```bash
python solution.py <number_with_repeating_digit>
```
eg.
```bash
python solution.py '1.(1)'
```
produces to the terminal `10/9`

## Run unittests
From the project root ...
```bash 
pytest -v test_solution.py
```
