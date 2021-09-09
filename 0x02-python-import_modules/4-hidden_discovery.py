#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_names = dir(hidden_4)
    for i in range(0, len(all_names)):
        if "__" != all_names[i][:2]:
            print(all_names[i])
