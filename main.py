def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()
print_params()
print_params(6,'строка')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = (False, 'Mir', 34)
values_dict = {'a' : 8, 'b' : True, 'c' : 'Dom'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
