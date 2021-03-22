def print_current_state(inputs, inputs_dict):
    print(f"""{" | ".join(inputs_dict[cell] for cell in inputs[0: 3])}
---------
{" | ".join(inputs_dict[cell] for cell in inputs[3: 6])}
---------
{" | ".join(inputs_dict[cell] for cell in inputs[6:])}""" )

    print("Empty cells are: ")
    print("  ".join(cell for cell in inputs if inputs_dict[cell] == " "))


def choose_cell(inputs_dict):
    global count
    print_current_state(cells, cells_dict)
    while True:
        try:
            chosen_cell = input("Choose a cell: ").upper()
        except:
            print("Please choose a valid and empty cell.")
        else:
            if inputs_dict.get(chosen_cell) == " ":
                if count % 2 == 1:
                    inputs_dict[chosen_cell] = "X"
                else:
                    inputs_dict[chosen_cell] = "O"
                break
            else:
                print("Please choose an empty cell.")


def check_winner(groups, cells_dict):
    global count
    for group in groups:
        group_cells_content = [cells_dict[group[i]] for i in range(3)]
        if len(set(group_cells_content)) == 1 and group_cells_content[0] != " ":
            if count % 2 == 1:
                return "Player 1 won"
            else:
                return "Player 2 won"
    count += 1


cells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
cells_dict = {cell: " " for cell in cells}
triples = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"],
["A1", "B2", "C3"], ["A3", "B2", "C1"]]
count = 1             

while True:
    choose_cell(cells_dict)
    winner = check_winner(triples, cells_dict)
    if winner:
        print_current_state(cells, cells_dict)
        print(winner)
        break
