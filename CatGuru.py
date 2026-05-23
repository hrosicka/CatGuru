# --- DPI Awareness Enhancement ---
# Improves scaling of the Tkinter window on high-DPI displays (e.g., 4K monitors)
# to prevent blurry text and improperly sized elements on Windows.
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except (ImportError, AttributeError):
    pass

from api_client import CatFactClient
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
import os
from config import * # Assumes 'config.py' exists and defines LOG_FILE, BACKGROUND_COLORS, AVATARS, MAX_WISDOM_LINE_LENGTH, dirname
import logging
import random

# --- Logging Configuration ---
# Basic logging setup to record application events and errors.
# Log messages are written to a file specified by LOG_FILE in config.py.
logging.basicConfig(filename=LOG_FILE,
                    level=logging.INFO, # Set logging level to INFO, capturing INFO, WARNING, ERROR, CRITICAL messages.
                    format='%(asctime)s - %(levelname)s - %(message)s' # Define the log message format.
                    )

# --- CatGuru Application Class ---
class CatGuru:
    """
    Main application class for the 'My Cat Guru' GUI.
    It displays a cat avatar, provides cat facts fetched from an API,
    and allows users to change the avatar and background color.
    """
    def __init__(self):
        """
        Initializes the main application window and its components.
        """
        # --- Main Window Setup ---
        self.window = tk.Tk()
        self.window.title("My Cat Guru")
        self.window.geometry("690x550") # Set initial window dimensions.

        # Set the application icon from a file defined in config.py.
        ico = Image.open(os.path.join(dirname, 'icon.jpg'))
        photo = ImageTk.PhotoImage(ico)
        self.window.wm_iconphoto(False, photo)

        # --- Data & API Initialization ---
        self.avatar_cache = {}  # Cache to store loaded avatar images to prevent reloading.
        self.cat_fact_url = "https://catfact.ninja/fact" # API endpoint for cat facts.
        self.cat_client = CatFactClient()

        # --- Background Setup ---
        # Initialize the background color and index.
        self.background_color_index = 0
        self.background_color = BACKGROUND_COLORS[self.background_color_index]
        # Create a label that covers the entire window to serve as the dynamic background.
        self.background_label = tk.Label(self.window, bg=self.background_color)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1) # Use .place for full window coverage.

        # --- Avatar Setup ---
        # Select a random initial cat avatar.
        self.avatar_index = random.randint(0, len(AVATARS) - 1)
        self.avatar_image = self.load_avatar_image(AVATARS[self.avatar_index])
        # Display the cat avatar.
        self.avatar_label = tk.Label(self.window, image=self.avatar_image)         
        self.avatar_label.pack(padx=20, pady=20) # Pack the avatar label into the window.

        # --- Options Panel (Buttons) Setup ---
        # Frame to hold the action buttons at the bottom of the window.
        self.options_frame = tk.Frame(self.window, bg=self.background_color) # Set background to current theme.
        self.options_frame.pack(side=tk.BOTTOM, pady=30) # Pack to the bottom, with vertical padding.

        # Label to display the fetched cat wisdom/fact.
        self.wisdom_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.wisdom_label.config(bg=self.background_color) # Ensure wisdom label background matches theme.
        self.wisdom_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10) # Pack below avatar, allow horizontal fill.

        # Inner frame to hold buttons, allowing for centering of the button group.
        self.button_container_frame = tk.Frame(self.options_frame, bg=self.background_color) # Match parent background.
        self.button_container_frame.pack(side=tk.TOP) # Pack within options_frame, enabling centering of buttons.

        # --- Buttons ---
        # "Ask the Cat Guru" button to fetch and display a new cat fact.
        self.wisdom_button = customtkinter.CTkButton(master=self.button_container_frame, # Master is the button container.
                                                     text="Ask the Cat Guru",
                                                     command=self.show_wisdom, # Callback function on click.
                                                     corner_radius=15,
                                                     text_color="snow2",
                                                     fg_color="#393D3F",
                                                     hover_color="#271F30") 
        self.wisdom_button.pack(side=tk.LEFT, padx=5) # Pack buttons side-by-side with horizontal padding.

        # "Change Avatar" button to cycle through available cat avatars.
        self.avatar_button = customtkinter.CTkButton(master=self.button_container_frame, 
                                                     text="Change Avatar",
                                                     command=self.change_avatar,
                                                     corner_radius=15,
                                                     text_color="snow2",
                                                     fg_color="#393D3F",
                                                     hover_color="#271F30") 
        self.avatar_button.pack(side=tk.LEFT, padx=5) 

        # "Change Background" button to cycle through predefined background colors.
        self.background_button = customtkinter.CTkButton(master=self.button_container_frame, 
                                                         text="Change Background",
                                                         command=self.change_background,
                                                         corner_radius=15,
                                                         text_color="snow2",
                                                         fg_color="#393D3F",
                                                         hover_color="#271F30") 
        self.background_button.pack(side=tk.LEFT, padx=5) 

        # --- Tooltips ---
        # Define tooltip messages for each button to provide user guidance.
        self.wisdom_age_button_tooltip = "Need some purrfect advice? Click here to unleash the wisdom of the Cat Guru!"
        self.avatar_button_tooltip = "Feeling like a different cat today? Switch up your avatar and show off your unique feline flair."
        self.background_button_tooltip = "Bored of your old background? Change it to a color that's meow-gical!"

        # Attach tooltips to their respective buttons.
        Hovertip(self.wisdom_button, self.wisdom_age_button_tooltip)
        Hovertip(self.avatar_button, self.avatar_button_tooltip)
        Hovertip(self.background_button, self.background_button_tooltip)

    # --- GUI Update Methods ---
    def show_wisdom(self):
        """
        Retrieves a cat fact and formats it into multiple lines
        for better readability within the wisdom_label,
        respecting MAX_WISDOM_LINE_LENGTH from config.py.
        """
        self.wisdom_label.config(text="Loading... 🐱")  # ✅ PŘIDEJ TUTO LINKU
        self.window.update()  # ✅ PŘIDEJ TUTO LINKU
        
        wisdom_text = self.cat_client.fetch_fact()  # ✅ ZMĚŇ NA TOTO
        lines = []
        current_line = ""
        # Iterate through words to build lines that fit the max length.
        for word in wisdom_text.split():
            # Check if adding the next word exceeds the line length limit.
            # (1 if current_line else 0) accounts for the space before the word.
            if len(current_line) + len(word) + (1 if current_line else 0) > MAX_WISDOM_LINE_LENGTH:
                if current_line: # If there's content in current_line, add it to lines.
                    lines.append(current_line.strip())
                current_line = word # Start a new line with the current word.
            else:
                # Add word to current line, with a space if it's not the first word.
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
        if current_line: # Add any remaining text as the last line.
            lines.append(current_line.strip())

        self.wisdom_label.config(text="\n".join(lines)) # Update the label with the formatted text.

    def change_avatar(self):
        """
        Cycles to the next cat avatar in the AVATARS list.
        Updates the avatar_label with the new image.
        """
        self.avatar_index = (self.avatar_index + 1) % len(AVATARS) # Increment index, wrapping around.
        self.avatar_image = self.load_avatar_image(AVATARS[self.avatar_index]) # Load the new avatar.
        self.avatar_label.config(image=self.avatar_image) # Update the displayed image.

    def change_background(self):
        """
        Cycles to the next background color in the BACKGROUND_COLORS list.
        Updates the background of the main label, wisdom label, and button frames.
        """
        self.background_color_index = (self.background_color_index + 1) % len(BACKGROUND_COLORS) # Increment index, wrapping around.
        self.background_color = BACKGROUND_COLORS[self.background_color_index] # Get the new color.

        # Update the background color for all relevant widgets.
        self.background_label.config(bg=self.background_color)
        self.wisdom_label.config(bg=self.background_color)
        self.options_frame.config(bg=self.background_color)
        self.button_container_frame.config(bg=self.background_color)

    def load_avatar_image(self, filename):
        """
        Loads an image from the given filename, resizes it, and converts it
        to a Tkinter PhotoImage. Caches images to improve performance.
        """
        if filename not in self.avatar_cache: # Check if the image is already cached.
            image = Image.open(filename)
            image = image.resize((200, 200)) # Resize for consistent display.
            self.avatar_cache[filename] = ImageTk.PhotoImage(image) # Store PhotoImage in cache.
        return self.avatar_cache[filename] # Return the cached (or newly loaded) PhotoImage.

# --- Application Entry Point ---
if __name__ == "__main__":
    # Create an instance of the CatGuru application.
    cat_guru = CatGuru()
    # Start the Tkinter event loop, which keeps the window open and responsive.
    cat_guru.window.mainloop()