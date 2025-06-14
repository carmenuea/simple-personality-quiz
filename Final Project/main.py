from tkinter import *
from PIL import Image, ImageTk

# Declare global variable 
explorer_percent_text = None
dreamer_percent_text = None

# -------- Window setup -------- 
window = Tk() # make a window
window.geometry("640x360") # change the size of the window 
window.title("Simple Personality Quiz") # change the window title

# ---- Container setup ----
# make container to accomodate all frames
container = Frame(window)
container.pack(fill="both", expand=True)

# ---- Dictionary setup ----
# dictionary to save all of the pages
#"landing": frame link to landing_page,
#"page_1": frame link to page_1
pages = {}

# ---- Background image setup ----
# load and resize image with pillow
bg_image = Image.open("sunset_pastel.jpg")
bg_image = bg_image.resize((640,360))
bg_photo = ImageTk.PhotoImage(bg_image)

# --- Landing page frame ---
landing = Frame(container)
landing.place(relwidth=1, relheight=1)
pages["landing"] = landing

# put the background image on the canvas
canvas = Canvas(landing, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# create text for landing page
canvas.create_text(
    310, 
    80, 
    text="Simple Personality Quiz", 
    font=("AkzidenzGrotesk", 22), 
    anchor="center")

canvas.create_text(
    310, 
    115, 
    text=">> Created by Gaby W <<", 
    font=("Roboto", 11), 
    anchor="center")

canvas.create_text(
    310, 
    160, 
    text=">> Let's find out whether you are more", 
    font=("DM Sans", 13), 
    anchor="center")

canvas.create_text(
    310, 
    185, 
    text="of an explorer or a dreamer at heart", 
    font=("DM Sans", 13), 
    anchor="center")

# make a button to start the the quiz
take_quiz_btn = Button(
    landing, 
    text="TAKE THE QUIZ", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : show_frame("page_1")) 
take_quiz_btn.place(x=310, y=244, anchor="center")

# make a global variable for score
explorer_score = 0
dreamer_score = 0
# make a function for updating the score
def choose_type(type):
    global explorer_score, dreamer_score
    if type == "explorer":
        explorer_score += 1
    elif type == "dreamer":
        dreamer_score += 1
    # temporary code to print score to the terminal
    #print("Explorer:", explorer_score)
    #print("Dreamer:", dreamer_score)

# ------ Page 1 ------
# --- page 1 frame ---
page_1 = Frame(container)
page_1.place(relwidth=1, relheight=1)
pages["page_1"] = page_1

# put the background image on the canvas
canvas = Canvas(page_1, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# create text for question 1
canvas.create_text(
    310, 
    60, 
    text="1) Which fruit do you prefer?", 
    font=("DM Sans", 15), 
    anchor="center")

left_x = 140
top_y = 100
right_x = 260
bottom_y = 220
# make a square to put left image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
apple_image = Image.open("apple.png")
apple_image = apple_image.resize((120,120))
apple_photo = ImageTk.PhotoImage(apple_image)
# add apple image to the screen
canvas.create_image(left_x, top_y, image = apple_photo, anchor="nw")

# make a button for question 1 left option
apple_btn = Button(
    page_1, 
    text="APPLE", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("explorer"), show_frame("page_2")]) 
apple_btn.place(x=200, y=260, anchor="center")

left_x = 350
top_y = 100
right_x = 470
bottom_y = 220
# make a square to put right image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
grape_image = Image.open("grape.png")
grape_image = grape_image.resize((120,120))
grape_photo = ImageTk.PhotoImage(grape_image)
# add grape image to the screen
canvas.create_image(left_x, top_y, image = grape_photo, anchor="nw")

# make a button for question 1 right option
grape_btn = Button(
    page_1, 
    text="GRAPE", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("dreamer"), show_frame("page_2")]) 
grape_btn.place(x=410, y=260, anchor="center")

# ------ Page 2 ------
# --- page 2 frame ---
page_2 = Frame(container)
page_2.place(relwidth=1, relheight=1)
pages["page_2"] = page_2

# put the background image on the canvas
canvas = Canvas(page_2, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# create text for question 2
canvas.create_text(
    310, 
    60, 
    text="2) Pick your favourite treat", 
    font=("DM Sans", 15), 
    anchor="center")

left_x = 140
top_y = 100
right_x = 260
bottom_y = 220
# make a square to put left image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
fries_image = Image.open("fries.png")
fries_image = fries_image.resize((120,120))
fries_photo = ImageTk.PhotoImage(fries_image)
# add french fries image to the screen
canvas.create_image(left_x, top_y, image = fries_photo, anchor="nw")

# make a button for question 2 left option
potato_btn = Button(
    page_2, 
    text="FRENCH FRIES", font=("Glacial Indifference",11), 
    padx=8, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("explorer"), show_frame("page_3")]) 
potato_btn.place(x=200, y=260, anchor="center")

left_x = 350
top_y = 100
right_x = 470
bottom_y = 220
# make a square to put right image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
cupcake_image = Image.open("cupcake.png")
cupcake_image = cupcake_image.resize((120,120))
cupcake_photo = ImageTk.PhotoImage(cupcake_image)
# add cupcake image to the screen
canvas.create_image(left_x, top_y, image = cupcake_photo, anchor="nw")

# make a button for question 2 right option
cupcake_btn = Button(
    page_2, 
    text="CUPCAKE", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("dreamer"), show_frame("page_3")]) 
cupcake_btn.place(x=410, y=260, anchor="center")

# ------ Page 3 ------
# --- page 3 frame ---
page_3 = Frame(container)
page_3.place(relwidth=1, relheight=1)
pages["page_3"] = page_3

# put the background image on the canvas
canvas = Canvas(page_3, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# create text for question 3
canvas.create_text(
    310, 
    60, 
    text="3) When do you feel most alive?", 
    font=("DM Sans", 15), 
    anchor="center")

left_x = 140
top_y = 100
right_x = 260
bottom_y = 220
# make a square to put left image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
day_image = Image.open("day.png")
day_image = day_image.resize((120,120))
day_photo = ImageTk.PhotoImage(day_image)
# add day image to the screen
canvas.create_image(left_x, top_y, image = day_photo, anchor="nw")

# make a button for question 3 left option
day_btn = Button(
    page_3, 
    text="DAY", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("explorer"), show_frame("page_4")]) 
day_btn.place(x=200, y=260, anchor="center")

left_x = 350
top_y = 100
right_x = 470
bottom_y = 220
# make a square to put right image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
night_image = Image.open("night.png")
night_image = night_image.resize((120,120))
night_photo = ImageTk.PhotoImage(night_image)
# add night image to the screen
canvas.create_image(left_x, top_y, image = night_photo, anchor="nw")

# make a button for question 3 right option
night_btn = Button(
    page_3, 
    text="NIGHT", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("dreamer"), show_frame("page_4")]) 
night_btn.place(x=410, y=260, anchor="center")

# ------ Page 4 ------
# --- page 4 frame ---
page_4 = Frame(container)
page_4.place(relwidth=1, relheight=1)
pages["page_4"] = page_4

# put the background image on the canvas
canvas = Canvas(page_4, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# create text for question 4
canvas.create_text(
    310, 
    60, 
    text="4) Which one do you enjoy more?", 
    font=("DM Sans", 15), 
    anchor="center")

left_x = 140
top_y = 100
right_x = 260
bottom_y = 220
# make a square to put left image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
read_image = Image.open("book.png")
read_image = read_image.resize((120,120))
read_photo = ImageTk.PhotoImage(read_image)
# add read image to the screen
canvas.create_image(left_x, top_y, image = read_photo, anchor="nw")

# make a button for question 4 left option
read_btn = Button(
    page_4, 
    text="READ", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("explorer"), show_frame("page_5")]) 
read_btn.place(x=200, y=260, anchor="center")

left_x = 350
top_y = 100
right_x = 470
bottom_y = 220
# make a square to put right image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
write_image = Image.open("pencil.png")
write_image = write_image.resize((120,120))
write_photo = ImageTk.PhotoImage(write_image)
# add write image to the screen
canvas.create_image(left_x, top_y, image = write_photo, anchor="nw")

# make a button for question 4 right option
write_btn = Button(
    page_4, 
    text="WRITE", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("dreamer"), show_frame("page_5")]) 
write_btn.place(x=410, y=260, anchor="center")

# ------ Page 5 ------
# --- page 5 frame ---
page_5 = Frame(container)
page_5.place(relwidth=1, relheight=1)
pages["page_5"] = page_5

# put the background image on the canvas
canvas = Canvas(page_5, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# create text for question 5
canvas.create_text(
    310, 
    60, 
    text="5) Which one do you like more?", 
    font=("DM Sans", 15), 
    anchor="center")

left_x = 140
top_y = 100
right_x = 260
bottom_y = 220
# make a square to put left image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
door_image = Image.open("door.png")
door_image = door_image.resize((120,120))
door_photo = ImageTk.PhotoImage(door_image)
# add door image to the screen
canvas.create_image(left_x, top_y, image = door_photo, anchor="nw")

# make a button for question 5 left option
door_btn = Button(
    page_5, 
    text="DOOR", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("explorer"), update_percentage(), show_frame("page_6")]) 
door_btn.place(x=200, y=260, anchor="center")

left_x = 350
top_y = 100
right_x = 470
bottom_y = 220
# make a square to put right image
canvas.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# load and resize image with pillow
window_image = Image.open("window.png")
window_image = window_image.resize((120,120))
window_photo = ImageTk.PhotoImage(window_image)
# add window image to the screen
canvas.create_image(left_x, top_y, image = window_photo, anchor="nw")

# make a button for question 5 right option
window_btn = Button(
    page_5, 
    text="WINDOW", font=("Glacial Indifference",11), 
    padx=15, #padx to change the length x of the button
    bg="#d1d1d1", # change the background color of the button
    command=lambda : [choose_type("dreamer"), update_percentage(),show_frame("page_6")]) 
window_btn.place(x=410, y=260, anchor="center")

# ------ Page 6 ------
# --- page 6 frame ---
page_6 = Frame(container)
page_6.place(relwidth=1, relheight=1)
pages["page_6"] = page_6

# put the background image on the canvas
canvas_page_6 = Canvas(page_6, highlightthickness=0)
canvas_page_6.pack(fill="both", expand=True)
canvas_page_6.create_image(0, 0, image=bg_photo, anchor="nw")

# create text for result
canvas_page_6.create_text(
    317, 
    60, 
    text="Result", 
    font=("AkzidenzGrotesk", 20), 
    anchor="center")

# explorer text
canvas_page_6.create_text(
    200, 
    120, 
    text="Explorer", 
    font=("Roboto", 11), 
    anchor="center")

left_x = 150
top_y = 135
right_x = 250
bottom_y = 160
# make a square to put explorer score
canvas_page_6.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# Print explorer percentage to the screen
explorer_percent_text = canvas_page_6.create_text(
    200, 
    147.5, 
    text="", 
    font=("Roboto", 11), 
    anchor="center")

# dreamer text
canvas_page_6.create_text(
    440, 
    120, 
    text="Dreamer", 
    font=("Roboto", 11), 
    anchor="center")

left_x = 390
top_y = 135
right_x = 490
bottom_y = 160
# make a square to put dreamer score
canvas_page_6.create_rectangle(
    left_x, top_y, right_x, bottom_y
)

# Print dreamer percentage to the screen
dreamer_percent_text = canvas_page_6.create_text(
    440, 
    147.5, 
    text="", 
    font=("Roboto", 11), 
    anchor="center")

start_x = 145
start_y= 190
end_x = 495
end_y = 190
# make a top line to decor result message section
canvas_page_6.create_line(
    start_x, start_y, end_x, end_y
)

# Add result text to the screen
result_message_text = canvas_page_6.create_text(
    320,
    220,
    text="", 
    font=("Roboto", 12), 
    anchor="center",
    # declare text width, when exceed the width text will wrap to next line automatically
    width=370
)

start_x = 145
start_y= 250
end_x = 495
end_y = 250
# make a bottom line to decor result message section
canvas_page_6.create_line(
    start_x, start_y, end_x, end_y
)

def update_percentage():
    total_questions = 5
    explorer_percent = round((explorer_score / total_questions) * 100)
    dreamer_percent = round((dreamer_score / total_questions) * 100)
    canvas_page_6.itemconfig(explorer_percent_text, text=f"{explorer_percent} %")
    canvas_page_6.itemconfig(dreamer_percent_text, text=f"{dreamer_percent} %")

    # Update result message 
    message = result_message(explorer_percent)
    canvas_page_6.itemconfig(result_message_text, text=message)

    # print the calculated percentages + message to the terminal
    #print()
    #print("--- Score in % ---")
    #print(f"Explorer: {explorer_percent} %")
    #print(f"Dreamer: {dreamer_percent} %")
    #print(message)

def result_message(explorer_percent):
    # Explorer 100% and Dreamer 0% (5 left option, 0 right option)
    if explorer_percent == 100 :
        return "100% Explorer — you're brave enough to step out and always ready to explore the world."
    # Explorer 80% and Dreamer 20% (4 left option, 1 right option)
    elif explorer_percent == 80:
        return "Mostly an Explorer — you love new experiences, while still holding on to what inspires you."
    # Explorer 60% and Dreamer 40% (3 left option, 2 right option)
    elif explorer_percent == 60:
        return "You enjoy exploring things that resonate with your dreams — moving with purpose and passion."
    # Explorer 40% and Dreamer 60% (2 left option, 3 right option)
    elif explorer_percent == 40:
        return "You dream deeply while staying open to exploring what feels right to you."
    # Explorer 20% and Dreamer 80% (1 left option, 4 right option)
    elif explorer_percent == 20:
        return "Mostly a dreamer — you follow your heart and take action when it truly matters."
    # Explorer 0% and Dreamer 100% (0 left option, 5 right option)
    elif explorer_percent == 0:
        return "100% Dreamer — you follow your heart and take action in ways that feel right to you."

# temporary code to print what's inside dictionary to the terminal
#print(pages)

# function to show specific page
def show_frame(name):
    frame = pages[name]
    frame.tkraise()

# first page to show
show_frame("landing")

# make the window looping so it will appear on the screen
window.mainloop()