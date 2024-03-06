def e_vogal(letra):
    match letra.lower():
        case "a" | "e" | "i" | "o" | "u":
            return "É vogal"
        case _:
            return "É consoante"
print(e_vogal("b"))


