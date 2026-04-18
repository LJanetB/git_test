
# function to shorten items in a list to 5 characters if they are longer than 5 characters
def main():
    items = ["kettle", "rapper", "stove"]

    for i, item in enumerate(items):
        if len(item) > 5:
            items[i] = item[:5]

    print(items)


main()