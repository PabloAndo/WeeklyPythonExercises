# Exercise 6 - WPE

# Given a list of dictionaries, in which each dict represents a person.
# Three key-value pairs:
#   - name
#   - age
#   - hobbies
# 4 methods should be created.

from collections import Counter


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
    output = 0
    i = 0
    try:
        for dc in people:

            if dc['age'] > maxage:
                continue
            else:
                output = output + dc['age']
                i += 1
        output = output/i

    except ZeroDivisionError as e:
        print('Incorrect age. Try with a high number')

    return output


def all_hobbies(people):
    output = set()
    for dc in people:
        for hobbie in dc['hobbies']:
            output.add(hobbie)
    print(output)
    return output


def hobby_counter(people):
    cnt = Counter()
    for dc in people:
        for hobbie in dc['hobbies']:
            cnt[hobbie] += 1
    print(cnt)
    return cnt


def n_most_common(people, n):
    cnt = hobby_counter(people)

    output = [elem[0] for elem in cnt.most_common(n)]

    print(cnt.most_common(n))
    print(output)
    return output


if __name__ == '__main__':

    # average_age_under(all_people, 25)
    # all_hobies(all_people)
    # hobby_counter(all_people)
    n_most_common(all_people, 2)
