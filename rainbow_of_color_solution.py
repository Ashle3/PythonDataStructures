colors = []

colors.append("Red")
colors.append("Orange")
colors.append("Yellow")
colors.append("Green")
colors.append("Blue")
colors.append("Purple")

def print_colors(colors_list):
    #base case
    if len(colors_list) == 0:
        print("There are no more colors to print.")
    else:
        #store the first item we remove into a variable
        removed_first = colors_list.pop(0)
        #print the variable to the screen
        print(removed_first)
        #call the function, by passing in the new colors_list
        #this function will keep calling until it reaches the base case condition above
        print_colors(colors_list)


print_colors(colors)