# ---------------------
# --- IMPORT LIBRARIES ---
# ---------------------

# Import required modules from Tkinter for GUI elements
from tkinter import Tk, Button, Label, filedialog

# Import Pillow (PIL) modules for image processing
from PIL import Image, ImageTk, ImageDraw, ImageFont

# ---------------------
# --- IMAGE LOADING FUNCTION ---
# ---------------------
def load_image():
    """Load an image from disk and display it in the GUI"""
    global img, tk_img

    # Open a file dialog to let the user choose an image file
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    if file_path:
        # Open the selected image and convert it to grayscale
        img = Image.open(file_path).convert("L")

        # Convert the PIL image into a Tkinter-compatible image
        tk_img = ImageTk.PhotoImage(img)

        # Display the image in the GUI label
        label.config(image=tk_img)

# ---------------------
# --- WANTED POSTER GENERATION FUNCTION ---
# ---------------------
def generate_wanted():
    """Generate a WANTED poster by adding top and bottom banners"""
    global img, tk_img, processed

    if img:
        # Get original image dimensions
        img_width, img_height = img.size

        # Define banner heights
        top_banner_height = 50
        bottom_banner_height = 50

        # Calculate final page dimensions
        page_height = img_height + top_banner_height + bottom_banner_height
        page_width = img_width

        # Create a new white background image
        page = Image.new("RGB", (page_width, page_height), color="white")

        # Paste the original image onto the page (below the top banner)
        page.paste(img.convert("RGB"), (0, top_banner_height))

        # Create a drawing context for adding text
        draw = ImageDraw.Draw(page)

        # ---------------------
        # --- FONT SETTINGS ---
        # ---------------------
        try:
            # Load custom font for poster text
            font_wanted = ImageFont.truetype(
                "Font/LibreBodoni-Medium.ttf", 40)
            font_reward = ImageFont.truetype(
                "Font/LibreBodoni-Medium.ttf", 20)
        except:
            # Fallback to default font if custom font is not found
            font_wanted = ImageFont.load_default()
            font_reward = ImageFont.load_default()

        # ---------------------
        # --- TOP BANNER TEXT (WANTED) ---
        # ---------------------
        text = "WANTED"

        # Calculate text bounding box for centering
        bbox = draw.textbbox((0, 0), text, font=font_wanted)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        # Draw centered "WANTED" text on the top banner
        draw.text(
            ((page_width - w) // 2, (top_banner_height - h) // 2),
            text,
            fill="black",
            font=font_wanted
        )

        # ---------------------
        # --- BOTTOM BANNER TEXT (REWARD) ---
        # ---------------------
        reward_text = "REWARD $5000"

        # Calculate reward text bounding box
        bbox2 = draw.textbbox((0, 0), reward_text, font=font_reward)
        w2 = bbox2[2] - bbox2[0]
        h2 = bbox2[3] - bbox2[1]

        # Draw centered reward text on the bottom banner
        draw.text(
            ((page_width - w2) // 2,
             top_banner_height + img_height + (bottom_banner_height - h2) // 2),
            reward_text,
            fill="black",
            font=font_reward
        )

        # Save the processed poster image
        processed = page

        # Convert processed image for Tkinter display
        tk_img = ImageTk.PhotoImage(processed)

        # Display the poster in the GUI
        label.config(image=tk_img)

# ---------------------
# --- SAVE AS PDF FUNCTION ---
# ---------------------
def save_as_pdf():
    """Save the generated poster as a PDF file"""
    if processed:
        # Open save dialog for PDF file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )

        if file_path:
            # Save the processed image as a PDF
            processed.save(file_path, "PDF")
            print("Poster saved as PDF:", file_path)

# ---------------------
# --- GUI SETUP ---
# ---------------------
root = Tk()  # Create the main application window
root.title("WANTED Poster Generator")  # Set window title
root.geometry("800x800")  # Set window size

# Initialize image variables
img = None         # Original loaded image
processed = None  # Processed poster image

# ---------------------
# --- BUTTONS ---
# ---------------------

# Button to upload an image
btn_load = Button(
    root,
    text="UPLOAD IMAGE",
    command=load_image
)
btn_load.pack(pady=5)

# Button to generate the wanted poster
btn_generate = Button(
    root,
    text="GENERATE WANTED",
    command=generate_wanted
)
btn_generate.pack(pady=5)

# Button to save the poster as PDF
btn_save_pdf = Button(
    root,
    text="SAVE AS PDF",
    command=save_as_pdf
)
btn_save_pdf.pack(pady=5)

# ---------------------
# --- IMAGE DISPLAY AREA ---
# ---------------------
label = Label(root)  # Label to display images
label.pack()

# ---------------------
# --- START GUI LOOP ---
# ---------------------
root.mainloop()  # Start the Tkinter event loop
