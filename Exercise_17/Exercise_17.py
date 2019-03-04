class Cart():

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __format__(self, how):
        if how is 'short':
            item_names = sorted([(item.name) for item in self.items])

            output = ""

            for name in item_names:
                if len(item_names) == 1:
                    output = name
                else:
                    output += f"{name}, "

            return output

        elif how is 'long':
            self.items.sort(key=lambda x: x.name, reverse=False)
            output = ""
            for item in self.items:
                # cost = (item.quantity * item.price)
                # print(cost)
                output += f"    {item.quantity:3} {item.measure:6} "
                output += f"{item.name:10} @ ${item.price:.2f}...$"
                output += f"{item.quantity * item.price:.1f}\n"
            return output


class Item():

    def __init__(self, quantity, measure, name, price):
        self.quantity = quantity
        self.measure = measure
        self.name = name
        self.price = price


if __name__ == "__main__":
    cart = Cart()
    cart.add(Item(1.5, 'kg', 'tomatoes', 5))
    cart.add(Item(2, 'kg', 'cucumbers', 4))
    cart.add(Item(1, 'tube', 'toothpaste', 2))
    cart.add(Item(1, 'box', 'tissues', 4))

    print(f"Your cart contains: {cart:short}")
    print(f"Your cart:\n{cart:long}")
