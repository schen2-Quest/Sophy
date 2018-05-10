def total(a=5, *numbers, **phone_book):
    print("a", a)
    for single_item in numbers:
        print("single_item", single_item)
    for first_part, second_part in phone_book.items():
        print(first_part, second_part)


def a(**x): print(x)


print(total(10, 1, 2, 3, jack=4566, inge=45611))
a(x=1, y=2, c=6)
