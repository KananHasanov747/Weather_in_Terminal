#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10

from bs4 import BeautifulSoup as bs
import requests

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

'''def get_weather_data (url): # we have not to use default argument, because the second same argument, which have default value, can accept itself
    while True:
        if args.i:
            url += 'data?ids=' + args.i

        if args.ids:
            url += 'data?ids=' + args.ids


        if args.rd:
            if args.rd == 'raw' or args.rd == 'decoded':
                url += '&format=' + args.rd
            else:
                print ('Error, format can only be "raw" or "decoded"')
                return False

        if args.raw_decoded:
            if args.raw_decoded == 'raw' or args.raw_decoded == 'decoded':
                url += '&format=' + args.raw_decoded
            else:
                print ('Error, format can only be "raw" or "decoded"')
                return False

        if args.m:
            if args.m == 'on' or args.m == 'off':
                url += '&metars=' + args.m
            else:
                print ('Error, metars can only be "on" or "off"')
                return False

        if args.metars:
            if args.metars == 'on' or args.metars == 'off':
                url += '&metars=' + args.metars
            else:
                print ('Error, metars can only be "on" or "off"')
                return False


        html = requests.get (url, headers = HEADERS)
        # create a new soup
        soup = bs (html.text, 'html.parser')

        # store all results on this directory
        for result in soup.find_all ('div', {'id': 'awc_main_content_wrap'}):
            result.find ('div', {'id': 'app_menu'}).decompose () # we delete non-need div
            

        if args.rd == 'raw' or args.raw_decoded == 'raw':
            result = result.text
            result = result.replace ('TEMPO', '\n  TEMPO')
            result = result.replace ('BECMG', '\n  BECMG')
            
            print (result)
            return False

        if args.rd == 'decoded' or args.raw_decoded == 'decoded':
            print ('\n\n' + result.strong.text + '\n')
            
            for td in soup.find_all ('div', {'id': 'awc_main_content_wrap'}):
                td_body = td.find_all ('td')

            i = 0
            while i < len (td_body):
                body = td_body [i].text
                if i % 2 == 0:
                    body = body.replace ('Text:', '\nText:')
                    body = body.replace ('TAF', '\n\nTAF')
                    print (body, end = ' ')
                else:
                    print (body)
                i += 1

        return False
'''        


def optional (url):
    while True:
        if args.i:
            url += 'data?ids=' + args.i

        if args.rd:
            if args.rd == 'raw' or args.rd == 'decoded':
                url += '&format=' + args.rd
            else:
                print ('Error, format can only be "raw" or "decoded"')
                return False

        if args.m:
            if args.m == 'on' or args.m == 'off':
                url += '&metars=' + args.m
            else:
                print ('Error, metars can only be "on" or "off"')
                return False


        html = requests.get (url, headers = HEADERS)
        # create a new soup
        soup = bs (html.text, 'html.parser')

        # store all results on this directory
        for result in soup.find_all ('div', {'id': 'awc_main_content_wrap'}):
            result.find ('div', {'id': 'app_menu'}).decompose () # we delete non-need div

        if args.rd == 'raw':
            result = result.text
            result = result.replace ('TEMPO', '\n  TEMPO')
            result = result.replace ('BECMG', '\n  BECMG')
            result = result.replace ('FM', '\n  FM')

            print (result)
            return False
            
        if args.rd == 'decoded':
            print ('\n\n' + result.strong.text + '\n')
            
            for td in soup.find_all ('div', {'id': 'awc_main_content_wrap'}):
                td_body = td.find_all ('td')
                
            i = 0
            while i < len (td_body):
                body = td_body [i].text
                if i % 2 == 0:
                    body = body.replace ('Text:', '\nText:')
                    body = body.replace ('TAF', '\n\nTAF')
                    print (body, end = ' ')
                else:
                    print (body)
                i += 1

        return False


def positional (url):
    while True:
        if args.ids:
            url += 'data?ids=' + args.ids

        if args.raw_decoded:
            if args.raw_decoded == 'raw' or args.raw_decoded == 'decoded':
                url += '&format=' + args.raw_decoded
            else:
                print ('Error, format can only be "raw" or "decoded"')
                return False

        if args.metars:
            if args.metars == 'on' or args.metars == 'off':
                url += '&metars=' + args.metars
            else:
                print ('Error, metars can only be "on" or "off"')
                return False

        html = requests.get (url, headers = HEADERS)
        # create a new soup
        soup = bs (html.text, 'html.parser')

        # store all results on this directory
        for result in soup.find_all ('div', {'id': 'awc_main_content_wrap'}):
            result.find ('div', {'id': 'app_menu'}).decompose () # we delete non-need div

        if args.raw_decoded == 'raw':
            result = result.text
            result = result.replace ('TEMPO', '\n  TEMPO')
            result = result.replace ('BECMG', '\n  BECMG')
            result = result.replace ('FM', '\n  FM')
            
            print (result)
            return False
            
        if args.raw_decoded == 'decoded':
            print ('\n\n' + result.strong.text + '\n')
            
            for td in soup.find_all ('div', {'id': 'awc_main_content_wrap'}):
                td_body = td.find_all ('td')

            i = 0
            while i < len (td_body):
                body = td_body [i].text
                if i % 2 == 0:
                    body = body.replace ('Text:', '\nText:')
                    body = body.replace ('TAF', '\n\nTAF')
                    print (body, end = ' ')
                else:
                    print (body)
                i += 1
        return False


if __name__ == "__main__":
    URL = "https://aviationweather.gov/taf/"
    import argparse
    parser = argparse.ArgumentParser (description = "Quick Script for Extracting Weather data using Aviation Weather Center. For more information see the manual '$ man weather'") #conflict_handler = 'resolve')

    #parser.add_argument ('ids', type = str)

    parser.add_argument ('-i', type = str, metavar = '', action = 'store', default = '')
    parser.add_argument ('ids', type = str, nargs = '?', metavar = '', action = 'store', default = '')

    parser.add_argument ('-rd', type = str, metavar = '', action = 'store', default = 'raw', help = '')
    parser.add_argument ('raw_decoded', type = str, nargs = '?', metavar = '', action = 'store', default = 'raw')


    parser.add_argument ('-m', type = str, metavar = '', action = 'store', default = 'on', help = 'Include METAR (METeorological Aerodrome Report): "on" or "off"')
    parser.add_argument ('metars', type = str, nargs = '?', metavar = '', action = 'store', default = 'on')

    args = parser.parse_args () # you can write this only after all arguments, not between and beginning

    if args.i and args.rd and args.m:
        optional (URL)

    if args.ids and args.raw_decoded and args.metars:
        positional (URL)
        

    #get_weather_data (URL)
