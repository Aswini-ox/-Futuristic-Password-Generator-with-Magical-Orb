import tkinter as tk
import random
import string
import math

# Password generator
def generate_password(length=14):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

# Reveal password with special effect
def open_orb():
    password = generate_password()
    orb_button.destroy()  # remove orb
    label_text.config(
        text="🔮 Your Secret Code 🔮",
        font=("Segoe Script", 22, "bold"),
        fg="#00FFCC"
    )
    password_label.config(
        text=password,
        font=("Consolas", 20, "bold"),
        fg="#FFD700",
        bg="black"
    )

# Animate galaxy particles
def animate_particles():
    for i, star in enumerate(stars):
        angles[i] += 0.02
        r = 120 + 40 * math.sin(angles[i]*2)
        x = 250 + r * math.cos(angles[i] + i)
        y = 200 + r * math.sin(angles[i] + i*0.5)
        canvas.coords(star, x, y, x+3, y+3)
    root.after(40, animate_particles)

# GUI Setup
root = tk.Tk()
root.title("Mystical Password Generator")
root.geometry("500x400")
root.config(bg="black")
root.resizable(False, False)

# Canvas for animated galaxy
canvas = tk.Canvas(root, width=500, height=400, bg="black", highlightthickness=0)
canvas.place(x=0, y=0)

# Stars (galaxy effect)
stars, angles = [], []
for i in range(25):
    s = canvas.create_oval(250, 200, 253, 203, fill="violet", outline="")
    stars.append(s)
    angles.append(i)

# Title text
label_text = tk.Label(root, text="🎁 Touch the Magical Orb 🎁", 
                      font=("Papyrus", 20, "bold"), fg="white", bg="black")
label_text.place(relx=0.5, rely=0.15, anchor="center")

# Orb (instead of gift)
orb_button = tk.Button(root, text="🔮", font=("Arial", 60), 
                       command=open_orb, bg="black", fg="cyan", bd=0, activeforeground="gold")
orb_button.place(relx=0.5, rely=0.5, anchor="center")

# Password label (initially empty)
password_label = tk.Label(root, text="", bg="black")
password_label.place(relx=0.5, rely=0.75, anchor="center")

# Start animation
animate_particles()
root.mainloop()
