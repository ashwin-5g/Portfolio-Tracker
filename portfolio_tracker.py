from bs4 import BeautifulSoup
from sys import argv
import requests
import itertools
import re
import sys


def fetch(filename):
    """
    This function calls the 'get_list' function which returns a set of portfolios 
    in dict type. The dict, then, is passed onto 'compute_overallvalue' as argument
    which returns yet another dict, with overall portfolio values as keys of this 
    dict (and individual portfolios as values of this dict) 
     """

    return compute_overallvalue(get_list(filename))
    

def get_list(filename):
    """
    This function extracts a list of porfolios from a file and populates an
    empty dictionary with the extracted list.

    When fully populated the dictionary would look like:

    {0: [('GOOG', 50), ('MS', 10)], 1: [('GOOG', 100), ('AMZN', 90),
    ('MS', 80)], 2: [('SGI', 100), ('GOOG', 50), ('MS', 10)]}
    """
    portfolios = {}
    
    lines = map(lambda s: s.strip(), open(filename).readlines())     
    # opens portfolio.txt, reads the list of portfolios, removes '\n', and stores
    # the resultant content in lines 
    
    for i, line in enumerate(lines):

        portfolios[i] = eval(line) 
        # eval transforms a piece of str like "[('GOOG', 50), ('MSFT', 100)]" to
        # a list [('GOOG', 50), ('MSFT', 100)]
        

    for key, portfolio in portfolios.items():
        portfolios[key] = [((symbol.replace(' ', '').upper()), abs(count))
         for symbol, count in portfolio if count != 0] 
         #fixes non-standard ways of inputting symbols and meaningless count values in 
         #portfolio.txt

    return portfolios
    
    
def compute_overallvalue(portfolios):
    """
    This function computes the overall value for each portofolio and replaces
    the index of each portfolio with their corresponding overall value. The
    results are returned in a dictionary form.
    """

    for k in portfolios.keys():
        overall_value = 0

        for symbol, count in portfolios[k]:
            overall_value = overall_value + (get_value(symbol) * count)

        portfolios[overall_value] = portfolios[k]
        del portfolios[k]
    return portfolios


def sort_descending_order(portfolios):
    """
    This function takes in a dict, sorts it based on the indices and prints
    out the list of portfolios in the manner described in the problem
    specification.
    """
    for k in sorted(portfolios, reverse=True):
        for x, y in portfolios[k]:
            print "{0} - {1} ".format(x.replace(' ', ''), y),
        print


def get_value(symbol):
    """
    This function will fetch the current stock value from the
    Yahoo server when it receives a valid symbol name.
    If the symbol is invalid, the program halts.
    """
    url = 'http://in.finance.yahoo.com/q?s=' + symbol
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml") 
    # fetches html code that corresponds to 'url'
    #and stores that in 'soup'                      
    print soup

    value = str(soup.find('span', {'class': 'time_rtq_ticker'})).replace(",", "")
    v = re.findall('[0-9]+\.[0-9]+', value)
    v = ''.join(v)
    return float(v) 
    # above four statements help extract symbol value using 
    # 'soup', 'findall', and str-manipulation functions like 'replace' and 'join'


if __name__ == '__main__':

    script, filename = argv
    portfolios = fetch(filename)
    sort_descending_order(portfolios)
