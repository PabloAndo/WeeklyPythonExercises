# Exercise 6 - WPE

# Given a list of dictionaries, in which each dict represents a person.
# Three key-value pairs:
#   - name
#   - age
#   - hobbies
# 4 methods should be created.

from collections import Counter
import statistics


all_people = [{'name': 'Reuven', 'age': 48, 'hobbies': ['Python', 'cooking', 'reading']},
              {'name': 'Atara', 'age': 17, 'hobbies': [
                  'horses', 'cooking', 'art', 'reading']},
              {'name': 'Shikma', 'age': 15, 'hobbies': [
                  'Python', 'piano', 'cooking', 'reading']},
              {'name': 'Amotz', 'age': 13, 'hobbies': ['biking', 'cooking']}]


def average_age_under(people, maxage=200):
    """ Return the average age of all people, or (optionally)
    all people under a given age.
    """
    try:
        return statistics.mean([person['age'] for person in people if person['age'] < maxage])
    except statistics.StatisticsError:
        return 0


def all_hobbies(people):
    """ Return a set of the different hobbies enjoyed by people in our database.
    """
    return {hobby for p in people for hobby in p['hobbies']}
    """
    output = set()
    for dc in people:
        for hobbie in dc['hobbies']:
            output.add(hobbie)
    print(output)
    return output"""


def hobby_counter(people):
    """ Return a Counter object indicating how many people have each hobby - this is, how many people are interested in Python, how many enjoy cooking, and so forth. 
    """
    return Counter(hobby for dc in people for hobby in set(dc['hobbies']))
    """cnt = Counter()
    for dc in people:
        for hobbie in dc['hobbies']:
            cnt[hobbie] += 1
    print(cnt)
    return cnt"""


def n_most_common(people, n):
    """ Return the n most common hobbies, as a list of strings.
    """
    return [h[0] for h in hobby_counter(people).most_common(n)]
    """
    cnt = hobby_counter(people)

    output = [elem[0] for elem in cnt.most_common(n)]

    print(cnt.most_common(n))
    print(output)
    return output"""


if __name__ == '__main__':

    # average_age_under(all_people, 25)
    # all_hobies(all_people)
    # hobby_counter(all_people)
    n_most_common(all_people, 2)
