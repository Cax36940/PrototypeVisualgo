import tkinter as tk

root_window = tk.Tk()

root_window.geometry("1280x720")
root_window.title("Visualgo")

line_number = 0

variables = {}


class LinkedList:
    def __init__(self, name):
        self.name = name
        self.head = None
        variables[name] = {"type" : "linked_list", "data" : [], "show" : True}

    def append(self, data):
        variables[self.name]["data"].append(data)

    def remove(self, data):
        if data in variables[self.name]["data"]:
            variables[self.name]["data"].remove(data)

    def draw(self):
        x = 20  # Initial x-coordinate for the first node
        y = 20  # Initial y-coordinate
        for data in variables[self.name]["data"]:
            # Draw the rectangle for the data
            data_rect = canvas.create_rectangle(x, y, x + 100, y + 50, outline="black", fill="lightblue")
            data_rect = canvas.create_rectangle(x, y + 50, x + 100, y + 70, outline="black", fill="lightblue")
            # Draw the text on top of the rectangle
            canvas.create_text(x + 50, y + 25, text=str(data), font=("Arial", 12))
            # Draw an arrow to the next node (if not the last node)
            if (x-20)/150 < len(variables[self.name]["data"]) - 1:
                canvas.create_line(x + 50, y + 70, x + 50, y + 80)
                canvas.create_line(x + 50, y + 80, x + 125, y + 80)
                canvas.create_line(x + 125, y + 80, x + 125, y + 25)
                canvas.create_line(x + 125, y + 25, x + 150 , y + 25, arrow=tk.LAST)
            # Move to the next position for the next node
            x += 150  # Move to the next x-coordinate


def prev_step():

    global line_number

    if line_number > 1:
        line_number -= 1
        color_line()

def next_step():

    global line_number

    if line_number < len(textbox.get(1.0,"end").split("\n"))-1:
        line_number += 1
        color_line()
        s = textbox.get(str(line_number)+".0",str(line_number)+".end")
        exe(s)
        draw()
        canvas.update_idletasks()  # Ensure the canvas is updated before getting its size
        canvas.config(scrollregion=canvas.bbox("all"))


def exe(line):
    p = ""
    if "=" in line:
        if "LinkedList()":
            line = line.replace("LinkedList()","LinkedList('" + line.split(" ")[0].split("=")[0] + "')")
            exec(line,globals())
        p = line.split("=")
    else:
        exec(line,globals())

def draw():
    canvas.delete("all")
    for v in variables:
        if variables[v]["show"]:
            exec(v+".draw()")

def color_line():
    global line_number
    textbox.tag_delete("current_line")
    textbox.tag_add('current_line', str(line_number)+'.0', str(line_number+1)+'.0')
    textbox.tag_configure('current_line', background="grey")


textbox = tk.Text(root_window, borderwidth=5, font=("Arial", 10), wrap = "none") # height = number of lines of font
textbox.insert(1.0, "a = LinkedList()\na.append(5)\na.append(11)\na.append(7)\na.remove(11)\na.append(8)\n")
textbox.grid(column=0, row=0, columnspan=10, rowspan=17, sticky="nsew")


canvas = tk.Canvas(root_window, background="white")
canvas.grid(column=10, row=0, columnspan=10, rowspan=17, sticky="nsew")


x_scrollbar = tk.Scrollbar(root_window, orient=tk.HORIZONTAL, command=canvas.xview)
x_scrollbar.grid(column=10, row=17, columnspan=10, sticky="ew")

canvas.config(xscrollcommand=x_scrollbar.set)


button_prev = tk.Button(root_window, command=prev_step, font=("Arial", 12), text="prev")
button_prev.grid(column=1, row=18, sticky="ew")

button_next = tk.Button(root_window, command=next_step, font=("Arial", 12), text="next")
button_next.grid(column=2, row=18, sticky="ew")


for i in range(20):
    root_window.rowconfigure(i, weight=1)
    root_window.columnconfigure(i, weight=1)


root_window.mainloop()






