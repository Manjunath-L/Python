from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Types", ["Electric","Water","Fire"])
table.align = "r"
print(table)