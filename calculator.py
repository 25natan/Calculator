import tkinter as tk

#font for all the buttons and label text
my_font = ("Arial", 20)

#clean all previous calculations
def clean(result):
    result["text"] = ""
    
#calculate operation on two numbers
#the result will be float if one of them are float
def calc(result):
    eq = result["text"].split()
    if len(eq) != 3:
        return
    x = float(eq[0])
    y = float(eq[2])
    z = op_dict[eq[1]](x, y)
    if z == int(z):
        result["text"] = str(int(z))
    else:
        result["text"] = str(z)
    
#add digit function
#if there is a result on it will delete it and start new calculation
def add_dig(dig, result):
    result["text"] += dig

#add point function
#add point to number only if there are digit(s) before it
#and ther is not point yet
def add_point(result):
    if result["text"] == "" or result["text"][-1] == " ":
        return
    eq = result["text"].split()
    if len(eq) == 1 and "." in eq[0] or len(eq) == 3 and "." in eq[2]:
        return
    result["text"] += "."
    
#add operator function
#add operator only if there is number or if its minus sign
#if there is some calculation on then it willlbe calculated and the new
#operation will be performed on the result of it
def add_op(op, result):
    if op != "-" and (result["text"] == "" or result["text"][-1] == "." or result["text"][-1] == " "):
        return
    if result["text"] != "" and result["text"][-1] == ".":
        return
    calc(result)
    if op == "-" and (result["text"] == "" or result["text"][-1] == " "):
        result["text"] += "-"
    else:
        result["text"] += f" {op} "   

#buttons-functions dictionary
btn_dict = {}

#operator-functions dictionary
op_dict = {"+": lambda x,y: x+y,
        "-": lambda x,y: x-y,
        "/": lambda x,y: x/y,
        "*": lambda x,y: x*y}

#create window
window = tk.Tk()
window.rowconfigure([0, 1, 2, 3, 4], weight=1)
window.columnconfigure([0, 1, 2, 3], weight=1)

#create label
result = tk.Label(master=window, text="", borderwidth=5, bg="#b3fffb", relief="sunken", font = my_font, padx=15, pady=15)
result.grid(row=0, column=0, columnspan=4, sticky="nsew")

#create number buttons 1,2,3,...9
for i in range(9):
    btn_dict[str(i+1)] = add_dig
    btn = tk.Button(master=window, text=str(i+1), borderwidth=5, bg="#b3fffb", font = my_font, padx=15, pady=15)
    btn.grid(row=i//3+1, column=i%3, sticky="nsew")
    btn.configure(command=lambda button=btn: btn_dict[button["text"]](button["text"], result))
#add 0 button
btn_dict["0"] = add_dig
btn = tk.Button(master=window, text="0", borderwidth=5, bg="#b3fffb", font = my_font, padx=15, pady=15)
btn.grid(row=4, column=0, sticky="nsew", columnspan=2)
btn.configure(command=lambda button=btn: btn_dict[button["text"]](button["text"], result))

#create point button
btn_dict["."] = add_point
btn = tk.Button(master=window, text=".", borderwidth=5, bg="#b3fffb", font = my_font, padx=15, pady=15)
btn.grid(row=4, column=2, sticky="nsew")
btn.configure(command=lambda button=btn: btn_dict[button["text"]](result))

#create operations buttons and locate them on the operations frame
for i, op in enumerate("+-/*", 1):
    btn_dict[op] = add_op
    btn = tk.Button(master=window, text=op, borderwidth=5, bg="#b3fffb", font = my_font, padx=15, pady=15)
    btn.grid(row=i, column=3, sticky="nsew")
    btn.configure(command=lambda button=btn: btn_dict[button["text"]](button["text"], result))

#create clean button
btn_dict["clean"] = clean
btn = tk.Button(master=window, text="clean", borderwidth=5, bg="#b3fffb", font = my_font, padx=15, pady=15)
btn.grid(row=5, column=3, sticky="nsew")
btn.configure(command=lambda button=btn: btn_dict[button["text"]](result))

#create equale button
btn_dict["="] = calc
btn = tk.Button(master=window, text="=", borderwidth=5, bg="#b3fffb", font = my_font, padx=15, pady=15)
btn.grid(row=5, column=0, sticky="nsew", columnspan=3)
btn.configure(command=lambda button=btn: btn_dict[button["text"]](result))

window.mainloop()