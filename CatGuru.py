import os
from ctypes import windll
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
import requests

# Enhance DPI awareness for better scaling on high-DPI displays
windll.shcore.SetProcessDpiAwareness(1)

# API endpoint for fetching cat facts
URL_CAT_FACT = "https://catfact.ninja/fact"

# relative paths
dirname = os.path.dirname(__file__)


# List of available cat avatars
AVATARS = [
    os.path.join(dirname, "cat1.png"),
    os.path.join(dirname, "cat2.png"),
    os.path.join(dirname, "cat3.png"),
    os.path.join(dirname, "cat4.png"),
    os.path.join(dirname, "cat5.png"),
    os.path.join(dirname, "cat6.png"),
]

# Background color options for the app
BACKGROUND_COLORS = [
  "lightblue",  # Light blue
  "lightgrey",  # Light grey
  "lightgoldenrod", # Light goldenrod
  "pink", # Pink
]

class CatGuru:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("My Cat Guru")
        self.window.geometry("690x550")

        ico = Image.open(os.path.join(dirname, 'icon.jpg'))
        photo = ImageTk.PhotoImage(ico)
        self.window.wm_iconphoto(False, photo)

        # Set initial background color
        self.background_color_index = 0
        self.background_color = BACKGROUND_COLORS[self.background_color_index]
        self.background_label = tk.Label(self.window, bg=self.background_color)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover entire window

        # Set initial cat avatar
        self.avatar_index = 0
        self.avatar_image = self.get_image(AVATARS[self.avatar_index])
        self.avatar_label = tk.Label(self.window, image=self.avatar_image)                 

        self.avatar_label.pack(padx=20, pady=20)

        # Create options panel at the bottom
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Label to display the cat wisdom
        self.wisdom_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.wisdom_label.config(bg=self.background_color)    
        self.wisdom_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Button to generate wisdom
        self.wisdom_button = customtkinter.CTkButton(master=self.options_frame,
                                                    text="Ask the Cat Guru",
                                                    command=self.show_wisdom,
                                                    corner_radius=15,
                                                    text_color="snow2",
                                                    fg_color="#393D3F",
                                                    hover_color="#271F30") 
        self.wisdom_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Button to change avatar
        self.avatar_button = customtkinter.CTkButton(master=self.options_frame,
                                                    text="Change Avatar",
                                                    command=self.change_avatar,
                                                    corner_radius=15,
                                                    text_color="snow2",
                                                    fg_color="#393D3F",
                                                    hover_color="#271F30") 
        
        self.avatar_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Button to change background
        self.background_button = customtkinter.CTkButton(master=self.options_frame,
                                                        text="Change Background",
                                                        command=self.change_background,
                                                        corner_radius=15,
                                                        text_color="snow2",
                                                        fg_color="#393D3F",
                                                        hover_color="#271F30") 

        self.background_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Tooltips
        self.wisdom_age_button_tooltip = "Need some purrfect advice? Click here to unleash the wisdom of the Cat Guru!"
        self.avatar_button_tooltip = "Feeling like a different cat today? Switch up your avatar and show off your unique feline flair."
        self.background_button_tooltip = "Bored of your old background? Change it to a color that's meow-gical!"

        # Set tooltips
        Hovertip(self.wisdom_button, self.wisdom_age_button_tooltip)
        Hovertip(self.avatar_button, self.avatar_button_tooltip)
        Hovertip(self.background_button, self.background_button_tooltip)


    def show_wisdom(self):
        # Get a random cat fact from the API
        response = requests.get(URL_CAT_FACT)
        data = response.json()

        # Split the text into multiple lines for better readability
        wisdom_text = data["fact"]
        max_length = 45  # Maximum characters per line
        lines = []
        for word in wisdom_text.split():
            if lines:  # Check if lines is not empty
                if len(" ".join(lines[-1:])) + len(word) > max_length:
                    lines.append("")
            else:
                lines.append("")  # Add empty string if lines is empty
            lines[-1] += " " + word

        # Display the wisdom
        self.wisdom_label.config(text="\n".join(lines))

    def change_avatar(self):
        # Change avatar index
        self.avatar_index = (self.avatar_index + 1) % len(AVATARS)

        # Load and display new avatar
        self.avatar_image = self.get_image(AVATARS[self.avatar_index])
        self.avatar_label.config(image=self.avatar_image)

    def change_background(self):
        # Change background color index
        self.background_color_index = (self.background_color_index + 1) % len(BACKGROUND_COLORS)
        self.background_color = BACKGROUND_COLORS[self.background_color_index]

        # Update background label color
        self.background_label.config(bg=self.background_color)
        self.wisdom_label.config(bg=self.background_color)

    def get_image(self, filename):
        # Load image and resize it for GUI
        image = Image.open(filename)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        return photo

# Run the app
cat_guru = CatGuru()
cat_guru.window.mainloop()
