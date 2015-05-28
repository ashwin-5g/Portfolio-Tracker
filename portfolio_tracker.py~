from bs4 import BeautifulSoup
from sys import argv
import requests
import itertools
import re
import sys

portfolio_dict = {}

def extract_symbols_and_count_from_file(filename):

    port_d = {}

    fileobject = open(filename)
    lines = fileobject.readlines()
    lines = map(lambda s: s.strip(), lines)

    for i, line in enumerate(lines):
        port_d[i] = eval(line)

    for key, list_of_symbols_and_count in port_d.items():
        port_d[key] = [((symbol.replace(' ', '').upper()), abs(count)) for symbol, count in list_of_symbols_and_count if count != 0]

        # The above assignment ensures that all letters of symbol are capitalized, inadvertent spaces around letters of symbol removed and sequences containing 'zero' count to be rejected for further processing

    return port_d

    fileobject.close()


def generate_value_from_symbol(symbol):

    url = generate_url_from_symbol(symbol)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)


    err = str(soup.find('div', {'class': 'error'}))
    if 'There are no results' in err:
        print symbol, "is invalid. No corresponding stock name exists for this symbol."
        print "Computation cannot proceed."
        print "Program Ended"
        sys.exit()

    else:

        value = str(soup.find('span', {'class': 'time_rtq_ticker'})).replace(",", "")
        v = re.findall('[0-9]+\.[0-9]+', value)
        v = ''.join(v)

        #print "Symbol: ", symbol
        #print "Stock Value: ", float(v)
        return float(v)


def generate_url_from_symbol(symbol):

    url = 'http://in.finance.yahoo.com/q?s=' + symbol
    return url


def compute_overall_value_for_each_portfolio(port_dict):

    for k in port_dict.keys():
        overall_value = 0

        for symbol, count in port_dict[k]:
            overall_value = overall_value + (generate_value_from_symbol(symbol) * count)

        port_dict[overall_value] = port_dict[k]
        del port_dict[k]

    #print port_dict


def display_portfolios_in_descending_order_of_overall_value(port_dict):

    for k in sorted(port_dict, reverse=True):
        for x, y in port_dict[k]:
            print "{0} - {1} ".format(x.replace(' ', ''), y),
        print


if __name__ == '__main__':

    script, filename = argv

    portfolio_dict = extract_symbols_and_count_from_file(filename)

    compute_overall_value_for_each_portfolio(portfolio_dict)

    display_portfolios_in_descending_order_of_overall_value(portfolio_dict)
