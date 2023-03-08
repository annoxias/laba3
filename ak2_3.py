slovo=input()
for i in slovo:
    if "ф" in slovo:
        print("Ого!Это редкое слово!")
        break
    elif "Ф" in slovo:
        print("Ого!Это редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово...")
        break