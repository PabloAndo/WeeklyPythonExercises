# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import defaultdict


Person = namedtuple('Person', ['first', 'last'])


class TableFull(Exception):
    pass


class GuestList():
    # GuestList is a list with each element being
    # a Person (numedtuple) and a table number(int)

    max_at_table = 10

    def __init__(self):
        self.tables_and_guests = defaultdict(list)

    def assign(self, person, new_table_number):
        # Check that there is space
        if len(self.tables_and_guests[new_table_number]) == self.max_at_table:
            raise TableFull("No room at the table!")

        # Look through existing tables; remove if the person is there
        for table_number, guests in self.tables_and_guests.items():
            if person in guests:
                guests.remove(person)
                break
        # add the person to the new table
        self.tables_and_guests[new_table_number].append(person)

    def __len__(self):
        return sum([len(one_table) for one_table in
                    self.tables_and_guests.values()])

    def table(self, table_number):
        return self.tables_and_guests[table_number]

    def unassigned(self):
        return self.table(None)

    def free_space(self):
        return {table_number: self.max_at_table - len(guests)
                for table_number, guests in
                self.tables_and_guests.items() if table_number}

    def guests(self):

        guests_dict = {one_guest: table_number
                       for table_number, guests_at_table in
                       self.tables_and_guests.items()
                       for one_guest in guests_at_table}

        return sorted(guests_dict.keys(),
                      key=lambda g: (guests_dict[g] or -1, g.last, g.first))

    def __repr__(self):
        output = ''
        for table_number, guests_at_table in sorted(
                self.tables_and_guests.items(), key=lambda t: t[0] or -1):
            output += '{0}\n'.format(table_number)

            for one_guest in sorted(guests_at_table,
                                    key=lambda t: t[::-1]):
                output += '\t{0}, {1}\n'.format(one_guest.last,
                                                one_guest.first)
        return output


if __name__ == "__main__":

    # Person = namedtuple('Person', ['first', 'last'])

    gl = GuestList()

    gl.assign(Person('Waylon', 'Dalton'), 1)
    gl.assign(Person('Justine', 'Henderson'), 1)
    gl.assign(Person('Abdullah', 'Lang'), 3)
    gl.assign(Person('Marcus', 'Cruz'), 1)
    gl.assign(Person('Thalia', 'Cobb'), 2)
    gl.assign(Person('Mathias', 'Little'), 2)
    gl.assign(Person('Eddie', 'Randolph'), None)
    gl.assign(Person('Angela', 'Walker'), 2)
    gl.assign(Person('Lia', 'Shelton'), 3)
    gl.assign(Person('Hadassah', 'Hartman'), None)
    gl.assign(Person('Joanna', 'Shaffer'), 3)
    gl.assign(Person('Jonathon', 'Sheppard'), 2)

    p = Person('Joanna', 'Shaffer')
    gl.assign(p, 3)

    # print(len(gl))
    # 1print(gl.table(2))
    # print(gl.unassigned())
    # print(gl.free_space())
    print(gl.guests())
