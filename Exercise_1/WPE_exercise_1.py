# WPE exercise 1

# two functions (collect_places and display_places)
# neither takes arguments, work with global variable visits

# user prompted for city, country
# if no comma -> error message, ask again
# empty response -> questioning ends

visits = {}  # python dictionary


def collect_places():
    """
    Prompts user for city/country combinations and stores them in a dictionary.
    Input values _must_ contain a comma or an exception is raised.
    """
    while True:
        global visits
        answer = input("Tell me where you went: ")
        if answer == "":
            break
        elif "," not in answer:
            print("That's not a legal city, country combination.")
        else:
            comma = answer.find(",")
            city = answer[:comma].lstrip().capitalize()
            country = answer[comma + 1:].lstrip()
            if country in visits.keys():
                visits[country].append(city)
            else:
                visits[country] = []
                visits[country].append(city)


def display_places():
    """
    Display cities, grouped by country and with the number of visits if
    they've been visited more than once.
    """
    print("You visited:")
    for country in visits.keys():
        print(country)
        for city in set(visits[country]):
            count = visits[country].count(city)
            if count == 1:
                print("   " + city)
            else:
                print("   " + city + " (" + str(count) + ")")


def main():
    collect_places()
    display_places()


if __name__ == '__main__':
    main()
