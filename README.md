This program takes in a list of portfolios (composed of stock symbol names and 
their corresponding count) as input and prints out the list of
portfolios, sorted in descending order of overall portfolio value.

To run this program, type in the following at command prompt:

python portfolio_tracker.py portfolio.txt

where portfolio_tracker.py is the source code which you just downloaded
and portfolio.txt is the file where YOU, the user, get to specify the 
list of portfolios.

Here's the format you need to follow while you enter: 

[('GOOG', 50), ('MS', 10)]                       # individual portfolio 1
[('GOOG', 100), ('AMZN', 90), ('MS', 80)]        # individual portfolio 2
[('SGI', 100), ('GOOG', 50), ('MS', 10)]         # individual portfolio 3

where 'GOOG', 'MS', 'AMZN' are *valid* stock symbols and numbers like '50', '10',
'100' are corresponding count values. 

The program will query the current stock value from the Yahoo servers for each 
valid stock symbol, and use that to determine the overall value for each of the 
individual portfolios you input in the file.

For the input above, the output would be: 

$ python portfolio_tracker.py portfolio.txt
[('GOOG', 50), ('MS', 10)]
[('GOOG', 100), ('AMZN', 90), ('MS', 80)]
[('SGI', 100), ('GOOG', 50), ('MS', 10)]
