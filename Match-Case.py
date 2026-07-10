num = 3
match num:
    case 1:
        print("1")
    case 2 | 3:
        print("2 or 3")
    case _:
        print("Other")