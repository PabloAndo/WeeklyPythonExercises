# WPE exercise 1

# two functions (collect_places and display_places)
# neither takes arguments, work with global variable visits

# user prompted for city, country
# if no comma -> error message, ask again
# empty response -> questioning ends
#!/python

from collections import defaultdict, Counter

# BONUS: fuzzy logic when entering countries and cities
try:
    from fuzzywuzzy import fuzz
    FUZZY_ENABLED = True
    print("")
except ImportError as e:
    FUZZY_ENABLED = False
from typing import Dict, List, Generator, Tuple

# For each country, we store a city with number of visits
visits = defaultdict(Counter)  # type: Dict[str, Counter]


def fuzzy_search(to_record: str, storage: dict) -> str:
    """\
    Search a string among the keys of dictionary with fuzzy logic
    Return one of the key if ratio is between 80 and 100
    Otherwise, return "to_record"
    """
    for k in storage:
        if to_record == k:
            return k

        ratio = fuzz.ratio(to_record, k)
        if 80 <= ratio <= 100:
            print(
                f"NOTE: small typo, used {k!r} instead of {to_record!r} [{ratio}]"
            )
            return k

    return to_record


def iter_collect() -> Generator[Tuple[str, str], None, None]:
    """Collect "city, country" by using iterator"""
    input_descr = "Tell me where you went: "
    input_error = "That's not a legal city, country combination"
    city_country = input(input_descr)
    while city_country.strip() != "":
        # We need exactly 1 comma to have a valid answer
        if city_country.count(",") != 1:
            print(input_error)
        else:
            city, country = (e.strip() for e in city_country.split(","))
            yield city, country
        city_country = input(input_descr)


def collect_places() -> None:
    """Collect the visited countries and cities"""
    global visits
    visits.clear()
    for city, country in iter_collect():
        if FUZZY_ENABLED:
            country = fuzzy_search(country, visits)
            city = fuzzy_search(city, visits[country])
        visits[country].update([city])


# def collect_places_OLD(reset=True) -> None:
#     """Collect the visited countries and cities"""
#     global visits
#     if reset:
#         visits.clear()
#     input_descr = "Tell me where you went: "
#     input_error = "That's not a legal city, country combination"
#     city_country = input(input_descr)

#     if city_country.strip() == "":
#         return
#     elif city_country.count(",") != 1:
#         print(input_error)
#     else:
#         city, country = (e.strip() for e in city_country.split(","))
#         # Just for fun, we will add some fuzzy logic with Levenshtein algorithm
#         if FUZZY_ENABLED:
#             country = fuzzy_search(country, visits)
#             city = fuzzy_search(city, visits[country])
#         visits[country].update([city])  # type: ignore # we can update a single list
#     collect_places_OLD(reset=False)


def display_places():
    """Print statistics"""
    print("You visited:")
    for country, cities in sorted(visits.items()):
        print(country)
        for city, nb_visits in sorted(cities.items()):
            details = f" ({nb_visits})" if nb_visits > 1 else ""
            print(f"\t{city}{details}")


if __name__ == "__main__":
    collect_places()
    display_places()