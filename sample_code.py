def main():
    items = ["kettle", "rapper", "stove"]

    for i, item in enumerate(items):
        if len(item) > 5:
            items[i] = item[:5]

    print(items)


main()