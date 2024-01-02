count = 0
while (count < 3):  # Change the condition to limit the number of iterations
    game = input("Please enter the scratch id.: ")
    text = input("Please enter the text: ")

    import scratchattach as scratch3

    session = scratch3.login("very-cool-dude1", "usethispassword")
    project = session.connect_project(game)

    project.post_comment(text)

    count += 1  # Update the count variable
