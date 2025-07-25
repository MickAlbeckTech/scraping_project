from bs4 import BeautifulSoup
import requests
import random

def play_again() -> bool:
    """Asks player if they want to play again, returns True or False"""
    response = input("Would you like to play again? (Y/N)")
    return response.upper() == "Y"

list_of_list_of_quotes =[]

page = 1

while True:
    #we want to increment the page number to scrape all the pages so we format the url string with 'page' variable.
    url = f"https://quotes.toscrape.com/page/{page}/"
    #use requests to get url content and parse into Beautifulsoup. Each page has maybe 8 quotes
    q = requests.get(url)
    soup = BeautifulSoup(q.content, "html.parser")
    #get all the quote classes from the 8 or so quotes on the page, these contain quote, author and href for each quote
    #quote_class_soup is a list of all the quote classes
    quote_class_soup = soup.find_all(class_="quote")

    for quote_class in quote_class_soup:

        #extract a list of [quote, author, href] from each quote class on the page
        single_quote = []
        single_quote.append(quote_class.find(class_="text").getText())
        single_quote.append(quote_class.find(class_="author").getText())
        single_quote.append(quote_class.find("a")["href"])


        #add the list of [quote, author, href] to our master list list_of_list_of_quotes. We have a list of lists.
        list_of_list_of_quotes.append(single_quote)

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

#now we have the 100 quotes, make a new loop for the game
while True:
    #choose a random quote from the list of 100 quotes
    quote_info = list_of_list_of_quotes[random.randint(0, 99)]
    print(quote_info)
    quote = quote_info[0]
    author = quote_info[1]
    href = quote_info[2]


    guess_1 = input("Who said this? " + quote + "\n")
    if guess_1 == author:
        print("You win!!!")
    else:
        #scrape birthdate and place using href from quote to go to info page of author
        url = f"https://quotes.toscrape.com{href}/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content,"html.parser" )
        birthdate = soup.find(class_="author-born-date").getText()
        birthplace = soup.find(class_="author-born-location").getText()
        guess_2 = input(f"Incorrect! Here's a hint. The author was born on {birthdate} {birthplace}. Who is it??"  + "\n")

        if guess_2 == author:
            print("You win!!!")

        else:
            guess_3 = input(f"Incorrect! Here's another hint. The author's first name starts with {author[0]}. Who is it??"  + "\n")

            if guess_3 == author:
                print("You win!!!")

            else:
                #get the first letter of the author's last name
                guess_4 = input(f"Incorrect! Here's another hint. The author's last name starts with {author.split(" ")[-1][0]}'. Who is it??"  + "\n")

                if guess_4 == author:
                    print("You win!!!")

                else:
                    print(f"You're out of guesses! The author was {author}!!")
    #ask if player wants to play again
    if not play_again():
        quit()

# TODO: how to move "You win!!" print statement so it's only coded once
# TODO: make some functions to make the code tidier 




