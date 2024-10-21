import string

num_corners = int(input("введіть кількість кутів: "))
first_letter = input("введіть першу літеру: ").upper()

alphabet = tuple(string.ascii_uppercase)
first_index = alphabet.index(first_letter)

name_list=()

for i in range(num_corners):
    letter=alphabet[(first_index + i)%len(alphabet)]
    name_list+=(letter,)

print("назва многокутника: ", ''.join(name_list))