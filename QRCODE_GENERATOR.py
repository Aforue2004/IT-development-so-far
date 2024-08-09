# import modules...
import validators
import pyqrcode
import io
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog, messagebox


class QRCodeApp:
    def __init__(self, root):
        # Code for GUI(Graphics user interface)
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("700x550")

        self.frame1 = ctk.CTkFrame(self.root, corner_radius=20)
        self.frame1.pack(pady=20)

        self.Enterlink_label = ctk.CTkLabel(self.frame1, anchor="center",
                                            text="Enter the Link Below: ", font=ctk.CTkFont(size=18, weight="bold"))
        self.Enterlink_label.pack(padx=30, pady=10)

        self.entry = ctk.CTkEntry(self.frame1,
                                  width=300, height=30, corner_radius=8, font=ctk.CTkFont(size=15, weight="normal"))
        self.entry.pack(padx=70, pady=20)
        self.colour_title = ctk.CTkLabel(self.frame1, anchor="center",
                                         text="Select Colour For QRcode", font=ctk.CTkFont(size=18, weight="bold"))

        # Drop down box for colour selection
        self.colour_title.pack(pady=10, padx=10)
        self.color_dropbox = ctk.CTkComboBox(self.frame1,
                                             values=["Red", "Green", "Blue", "Pink", "Black"])
        self.color_dropbox.pack(pady=5)

        # Create button
        self.button1 = ctk.CTkButton(self.root,
                                     text="Generate QRcode", font=ctk.CTkFont(size=15, weight="normal"),
                                     width=200, height=30, command=self.CreateQR)
        self.button1.pack(pady=5, padx=5, anchor="center")

        # Clear button
        self.button2 = ctk.CTkButton(self.root,
                                     text="Clear link", font=ctk.CTkFont(size=15, weight="normal"),
                                     width=200, height=30, command=self.Clear_all)
        self.button2.pack(pady=5, padx=5, anchor="center")

        # Holds the result for the Qrcode
        self.result = ctk.CTkLabel(root,
                                   text="", font=ctk.CTkFont(size=15), height=300, width=300)
        self.result.pack(anchor="center", padx=100, pady=10)

    # create function
    def CreateQR(self):
        # makes get_image available throughout the Function
        global get_image
        # holds the value entered
        data = self.entry.get()

        # collect the value of the dropbox
        drop_box = self.color_dropbox.get()

        # checks if the value entered is a valid URL
        if validators.url(data):
            if data:
                # if drop_box is Red, creates and displays red QRcode
                if drop_box == "Red":
                    # creates the QRcode
                    qr_image = pyqrcode.create(data, 'L', 4,
                                               "binary")

                    # creates a temporary memory location
                    qr_buffer = io.BytesIO()

                    # stores qr_image.png in the temporary location
                    qr_image.png(qr_buffer, scale=7, module_color="FF0000", quiet_zone=2)

                    # reads from the temporary location from the beginning
                    qr_buffer.seek(0)

                    # opens the temporary location as an image and saves in get_image
                    get_image = Image.open(qr_buffer)

                    # covert the image to Tkinter object to allow other objects to make use of it
                    ctk_image = ImageTk.PhotoImage(get_image)

                    # configure the result to be able to display the image
                    self.result.configure(image=ctk_image)
                    self.result.image = ctk_image

                    # if drop_box is Green, creates and displays red QRcode
                elif drop_box == "Green":
                    qr_image = pyqrcode.create(data, 'L', 4, "binary")
                    qr_buffer = io.BytesIO()
                    qr_image.png(qr_buffer, scale=6, module_color="00FF00", quiet_zone=2)
                    qr_buffer.seek(0)
                    get_image = Image.open(qr_buffer)
                    tk_image = ImageTk.PhotoImage(get_image)
                    self.result.configure(image=tk_image)
                    self.result.image = tk_image

                    # if drop_box is blue, creates and displays blue QRcode
                elif drop_box == "Blue":
                    qr_image = pyqrcode.create(data, 'L', 4, "binary")
                    qr_buffer = io.BytesIO()
                    qr_image.png(qr_buffer, scale=7, module_color="0000FF", quiet_zone=2)
                    qr_buffer.seek(0)
                    get_image = Image.open(qr_buffer)
                    tk_image = ImageTk.PhotoImage(get_image)
                    self.result.configure(image=tk_image)
                    self.result.image = tk_image

                    # if drop_box is pink, creates and displays pink QRcode
                elif drop_box == "Pink":
                    qr_image = pyqrcode.create(data, 'L', 4, "binary")
                    qr_buffer = io.BytesIO()
                    qr_image.png(qr_buffer, scale=7, module_color="FF69B4", quiet_zone=2)
                    qr_buffer.seek(0)
                    get_image = Image.open(qr_buffer)
                    tk_image = ImageTk.PhotoImage(get_image)
                    self.result.configure(image=tk_image)
                    self.result.image = tk_image

                    # if drop_box is Black, creates and displays Black QRcode
                elif drop_box == "Black":
                    qr_image = pyqrcode.create(data, 'L', 4, "binary")
                    qr_buffer = io.BytesIO()
                    qr_image.png(qr_buffer, scale=7, module_color="000000", quiet_zone=2)
                    qr_buffer.seek(0)
                    get_image = Image.open(qr_buffer)
                    tk_image = ImageTk.PhotoImage(get_image)
                    self.result.configure(image=tk_image)
                    self.result.image = tk_image

                # create path to store qr_image in the Storage
                input_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                          filetypes=[("PNG files", "*.png")])
                if input_path:
                    get_image.save(input_path)
                else:
                    messagebox.showerror("Error", "Error no Name")

        # Displays error if data is empty
        elif data == "":
            messagebox.showwarning("Error", "Enter link first")

            # Displays error if URL is invalid
        else:
            messagebox.showerror("Error", "Invalid URL")

    #clear function
    def Clear_all(self):
        # clear function for the link and Qrcode
        self.entry.delete(0, ctk.END)
        self.result.configure(image="")


# stores the import module Customtkinter
root = ctk.CTk()

# Calls the Class QRCodeAPP
app = QRCodeApp(root)

# makes Gui to display
root.mainloop()
