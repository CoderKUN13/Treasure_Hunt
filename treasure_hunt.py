
row1 = [" ⬜️ "," ⬜️ "," ⬜️ "]
row2 = [" ⬜️ "," ⬜️ "," ⬜️ "]
row3 = [" ⬜️ "," ⬜️ "," ⬜️ "]
map = [row1, row2, row3]
position = input("Where do you want to put the treasure? ")


letter = position[0].lower()
abc = ['a','b','c']

letter_index = abc.index(letter)
num_index = int(position[1]) - 1

map[num_index][letter_index]= "X" 
print(map)


print(f"{row1}\n{row2}\n{row3}")

