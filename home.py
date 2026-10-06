import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My Beautiful Small House")
root.geometry("700x500")

# Create the canvas
canvas = tk.Canvas(root, width=700, height=500, bg="skyblue")
canvas.pack()

# -----------------------------
# SKY
# -----------------------------

# Sun
canvas.create_oval(
    570, 40, 640, 110,
    fill="yellow",
    outline="orange",
    width=3
)

# Clouds
canvas.create_oval(80, 60, 150, 100, fill="white", outline="white")
canvas.create_oval(120, 45, 190, 100, fill="white", outline="white")
canvas.create_oval(160, 60, 220, 100, fill="white", outline="white")

# -----------------------------
# GROUND
# -----------------------------

canvas.create_rectangle(
    0, 350, 700, 500,
    fill="lightgreen",
    outline="lightgreen"
)

# Grass line
canvas.create_line(
    0, 350, 700, 350,
    fill="green",
    width=4
)

# -----------------------------
# HOUSE BODY
# -----------------------------

canvas.create_rectangle(
    220, 190, 500, 370,
    fill="lightyellow",
    outline="brown",
    width=4
)

# -----------------------------
# ROOF
# -----------------------------

canvas.create_polygon(
    180, 190,
    360, 70,
    540, 190,
    fill="firebrick",
    outline="darkred",
    width=4
)

# Small roof edge
canvas.create_line(
    175, 190, 545, 190,
    fill="darkred",
    width=7
)

# -----------------------------
# DOOR
# -----------------------------

canvas.create_rectangle(
    325, 270, 395, 370,
    fill="saddlebrown",
    outline="black",
    width=3
)

# Door knob
canvas.create_oval(
    375, 315, 383, 323,
    fill="gold",
    outline="black"
)

# -----------------------------
# WINDOWS
# -----------------------------

# Left window
canvas.create_rectangle(
    245, 230, 305, 290,
    fill="lightblue",
    outline="brown",
    width=3
)

# Left window cross
canvas.create_line(275, 230, 275, 290, fill="brown", width=2)
canvas.create_line(245, 260, 305, 260, fill="brown", width=2)

# Right window
canvas.create_rectangle(
    415, 230, 475, 290,
    fill="lightblue",
    outline="brown",
    width=3
)

# Right window cross
canvas.create_line(445, 230, 445, 290, fill="brown", width=2)
canvas.create_line(415, 260, 475, 260, fill="brown", width=2)

# -----------------------------
# CHIMNEY
# -----------------------------

canvas.create_rectangle(
    425, 115, 475, 175,
    fill="brown",
    outline="black",
    width=3
)

# Smoke
canvas.create_oval(
    440, 75, 475, 110,
    fill="lightgray",
    outline="gray"
)

canvas.create_oval(
    460, 45, 500, 85,
    fill="lightgray",
    outline="gray"
)

# -----------------------------
# PATH TO HOUSE
# -----------------------------

canvas.create_polygon(
    325, 370,
    395, 370,
    455, 500,
    250, 500,
    fill="burlywood",
    outline="brown"
)

# -----------------------------
# GARDEN
# -----------------------------

# Garden soil
canvas.create_rectangle(
    40, 390, 190, 465,
    fill="saddlebrown",
    outline="black",
    width=2
)

# Flowers
flower_positions = [
    (65, 415),
    (105, 435),
    (145, 410),
    (170, 445)
]

for x, y in flower_positions:

    # Stem
    canvas.create_line(
        x, y, x, y + 25,
        fill="green",
        width=3
    )

    # Leaves
    canvas.create_oval(
        x - 10, y + 10,
        x, y + 20,
        fill="green",
        outline="green"
    )

    # Flower petals
    canvas.create_oval(
        x - 8, y - 8,
        x + 2, y + 2,
        fill="pink",
        outline="red"
    )

    canvas.create_oval(
        x + 2, y - 3,
        x + 12, y + 7,
        fill="pink",
        outline="red"
    )

    canvas.create_oval(
        x - 8, y + 2,
        x + 2, y + 12,
        fill="pink",
        outline="red"
    )

    # Flower center
    canvas.create_oval(
        x - 2, y,
        x + 6, y + 8,
        fill="yellow",
        outline="orange"
    )

# -----------------------------
# SMALL TREES
# -----------------------------

# Left tree trunk
canvas.create_rectangle(
    80, 300, 100, 390,
    fill="saddlebrown",
    outline="black"
)

# Left tree leaves
canvas.create_oval(
    40, 245, 130, 330,
    fill="forestgreen",
    outline="darkgreen",
    width=3
)

# Right tree trunk
canvas.create_rectangle(
    585, 300, 605, 390,
    fill="saddlebrown",
    outline="black"
)

# Right tree leaves
canvas.create_oval(
    545, 245, 640, 330,
    fill="forestgreen",
    outline="darkgreen",
    width=3
)

# -----------------------------
# FENCE
# -----------------------------

for x in range(15, 210, 30):
    canvas.create_rectangle(
        x, 440, x + 10, 490,
        fill="white",
        outline="brown"
    )

# Horizontal fence lines
canvas.create_line(
    10, 455, 210, 455,
    fill="brown",
    width=3
)

canvas.create_line(
    10, 475, 210, 475,
    fill="brown",
    width=3
)

# -----------------------------
# HOUSE NAME
# -----------------------------

canvas.create_text(
    360, 425,
    text="My Little Home",
    font=("Arial", 18, "bold"),
    fill="darkgreen"
)

# Start the program
root.mainloop()