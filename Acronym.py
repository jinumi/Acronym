# Designed and Developed by Muhammad Umair Yaqub.
# Made in P A K I S T A N

import tkinter as tk

# Define function to generate acronym
def get_acronym():
    # Get the input term from the user
    term = entry.get()
    # Generate the acronym by taking the first letter of each word in the term
    acronym = ''.join(word[0] for word in term.upper().split())
    # Update the result label with the generated acronym
    result.config(text="" + acronym)

# Create the main window
window = tk.Tk()
window.title("Acronym")
window.iconbitmap("logo.ico")
window.resizable(False, False)
window.geometry("400x400")

# Define fonts for the labels, entry, and button
title_font = ("Cascadia Code", 30, "normal")
label_font = ("Cascadia Code", 20, "bold")
entry_font = ('Cascadia Code', 20, 'bold')
button_font = ("Cascadia Code", 15, "bold")

# Create title label and place it in the window
title = tk.Label(window, text="A C R O N Y M", font=title_font,
                 justify='center', fg='orange')
title.place(relx=0.5, rely=0.1, anchor='n')

# Create term label and entry box and place them in the window
label = tk.Label(window, text="Term:", font=label_font,
                 justify='left', fg='grey')
label.place(relx=0.3, rely=0.4, anchor='e')
entry = tk.Entry(window, font=entry_font,
                 width=20, fg="orange", bg="grey", bd=0, justify=tk.LEFT)
entry.place(relx=0.5, rely=0.5, anchor="center")

# Create acronym label and result label and place them in the window
label = tk.Label(window, text="Acronym:", font=label_font,
                 fg='grey')
label.place(relx=0.42, rely=0.6, anchor='e')


# Create button and place it in the window
button = tk.Button(text="Create", font=button_font, fg="white", activebackground="grey", activeforeground="orange", bg="grey", bd=0,
                   cursor="hand2", command=get_acronym)
button.place(relx=0.5, rely=0.9, anchor='s')

# Create result label and place them in the window
result = tk.Label(window, text="", font=label_font,
                  justify='center', fg='orange')
result.place(relx=0.54, rely=0.7, anchor='e')

# Run the main event loop for the window
window.mainloop()