from bs4 import BeautifulSoup
import requests

list_of_dicts_of_quotes = []
page = 1

while True:
    #we want to increment the page number to scrape all the pages so we format the url string with 'page' variable.
    url = f"https://quotes.toscrape.com/page/{page}/"
    # use requests to get url content and parse into Beautifulsoup. Each page has maybe 8 quotes
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    #get all the quote classes from the 8 or so quotes on the page, these contain quote, author and href for each quote
    #quote_class_soup is a list of all the quote classes
    quote_class_soup = soup.find_all(class_="quote")

    for quote_class in quote_class_soup:
        #extract a dict with keys: quote, author, href
        single_dict ={"quote" : "", "author" : "", "href" : ""}
        single_dict["quote"] = quote_class.find(class_="text").getText()
        single_dict["author"] = quote_class.find(class_="author").getText()
        single_dict["href"] = quote_class.find("a")["href"]
        # add the dict to our master list list_of_dicts_of_quotes. We have a list of dicts.
        list_of_dicts_of_quotes.append(single_dict)

    # stops the program when there is no 'Next' to click on
    try:
        # look for the text for the 'Next' button on each page
        soup.find(class_="next").getText()
    except AttributeError:
        # when next_test returns None, we get an Attribute Error (None type has no attribute getText())
        print("no more next page")
        break

    #go to next page by changing page number in url
    page += 1


print(list_of_dicts_of_quotes)
print(len(list_of_dicts_of_quotes))


# TODO: how to store the dict as a text file so we don't have to access url each time
# TODO: so this would be 2 different programs - one to make a file of quotes, another to access that file and pick quotes
# TODO: and then how to reload the text file into a dict
# TODO: use pickle or json

# TODO: make some functions to make the code tidier