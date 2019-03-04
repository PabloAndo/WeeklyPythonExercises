import pickle
import time


fields = ['first_name', 'last_name', 'email']


def checkpickle(cp_stem='people-checkpoint-'):
    people = []

    while True:
        print(people)
        user_choice = input("Enter your choice: ").strip()

        if user_choice == 'q':
            break

        elif user_choice == 'a':
            new_person = {}
            for one_field in fields:
                new_person[one_field] = input(
                    "Enter {}: ".format(one_field)).strip()
            people.append(new_person)

            timestamp = int(time.time())

            pickle.dump(people,
                        open("{}-{}".format(cp_stem, timestamp), 'wb'))

        elif user_choice == 'l':
            for one_person in people:
                print("{last_name}, {first_name}: email {email}".format(
                    **one_person))

        elif user_choice == 'r':
            which_checkpoint = input("Which checkpoint to restore: ").strip()
            people = pickle.load(
                open("{}-{}".format(cp_stem, which_checkpoint), 'rb'))

        else:
            print("No option {}; try again".format(user_choice))


if __name__ == '__main__':
    checkpickle()
