import requests

def live_data(url):

    #url='https://worldpopulationreview.com/countries/#popTable'

    header = {
          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
          "X-Requested-With": "XMLHttpRequest"
    }

    data = requests.get(url, headers=header)

    return data


def growth_rate(prev,curr):
    try:
        return round((1-(prev/curr))*100,2)
    except ZeroDivisionError:
        return 0


def population_density(curr,area):
    try:
        return round(curr/area)
    except ZeroDivisionError:
        return 0