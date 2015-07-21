from bs4 import BeautifulSoup
from sys import argv
import requests
import itertools
import re
import sys


def get_list(filename):
    """
    This function extracts a list of porfolios from a file and populates an
    empty dictionary with the extracted list.

    When fully populated the dictionary would look like:

    {0: [('GOOG', 50), ('MS', 10)], 1: [('GOOG', 100), ('AMZN', 90),
    ('MS', 80)], 2: [('SGI', 100), ('GOOG', 50), ('MS', 10)]}
    """
    port_d = {}

    fileobject = open(filename)
    lines = fileobject.readlines()
    lines = map(lambda s: s.strip(), lines)

    for i, line in enumerate(lines):
        port_d[i] = eval(line)

    for key, list_of_symbols_and_count in port_d.items():
        port_d[key] = [((symbol.replace(' ', '').upper()), abs(count))
         for symbol, count in list_of_symbols_and_count if count != 0]

    return port_d
    fileobject.close()


def get_value(symbol):
    """
    This function will fetch the current stock value from the
    Yahoo server when it receives a valid symbol name.
    If the symbol is invalid, the program halts.
    """
    url = 'http://in.finance.yahoo.com/q?s=' + symbol
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)

    err = str(soup.find('div', {'class': 'error'}))
    if 'There are no results' in err:
        print symbol, """is invalid. No corresponding stock name
    exists for this symbol."""
        print "Computation cannot proceed."
        print "Program Ended"
        sys.exit()

    else:
        value = str(soup.find('span', {'class': 'time_rtq_ticker'})).replace(",", "")
        v = re.findall('[0-9]+\.[0-9]+', value)
        v = ''.join(v)
        return float(v)


def compute_overallvalue(port_dict):
    """
    This function computes the overall value for each portofolio and replaces
    the index of each portfolio with their corresponding overall value. The
    results are returned in a dictionary form.
    """

    for k in port_dict.keys():
        overall_value = 0

        for symbol, count in port_dict[k]:
            overall_value = overall_value + (get_value(symbol) * count)

        port_dict[overall_value] = port_dict[k]
        del port_dict[k]
    return port_dict


def sort_descending_order(list_of_portfolios):
    """
    This function takes in a dict, sorts it based on the indices and prints
    out the list of portfolios in the manner described in the problem
    specification.
    """
    for k in sorted(list_of_portfolios, reverse=True):
        for x, y in list_of_portfolios[k]:
            print "{0} - {1} ".format(x.replace(' ', ''), y),
        print


if __name__ == '__main__':

    script, filename = argv
    list_of_portfolios = compute_overallvalue(get_list(filename))
    sort_descending_order(list_of_portfolios)
