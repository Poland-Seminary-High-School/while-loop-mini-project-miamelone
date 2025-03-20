prompt = "\nEnter your favorite desserts."
prompt += "\nEnter 'quit' when you are finished. "


while ture:
    desserts = input(prompt)
    if desserts == "quit":
        break
    else:
        print(f"My favorite desserts are (brownies, cookies, and cake)!")