[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18785174&assignment_repo_type=AssignmentRepo)
# While Loop Mini Project
Upload your finished code here.


#Good start but you are missing some key elements.

desserts = []

while True:
    dessert = input("\nEnter your favorite desserts (type 'done' when you are finished): ")

    if dessert == "done":
        break

    desserts.append(dessert.lower())
    print(f"- {dessert} has been added!")

if desserts:
    print("\nHere is a list of your favorite desserts: ")
    
    for dessert in desserts:
        print(f"~ {dessert.title()}")
else:
    print("/nThere are no desserts in your list.")
