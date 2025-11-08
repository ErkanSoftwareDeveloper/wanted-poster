# Tkinter kütüphanesinden gerekli modüller
from tkinter import Tk, Button, Label, filedialog
# Pillow kütüphanesi: resim işleme
from PIL import Image, ImageTk, ImageDraw, ImageFont

# --- Resim Yükleme Fonksiyonu ---


def load_image():
    """Dosyadan bir resim yükle"""
    global img, tk_img
    # Kullanıcıdan resim dosyası seçmesini istemek
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        img = Image.open(file_path).convert("L")  # Resmi gri tonlamaya çevir
        tk_img = ImageTk.PhotoImage(img)  # Tkinter için resmi hazırla
        label.config(image=tk_img)  # GUI üzerinde resmi göster

# --- WANTED Posteri Oluşturma Fonksiyonu ---


def generate_wanted():
    """Resmin üstüne ve altına WANTED ve REWARD banner ekleyerek poster oluştur"""
    global img, tk_img, processed
    if img:
        img_width, img_height = img.size  # Resmin boyutlarını al

        # Banner yükseklikleri
        top_banner_height = 50
        bottom_banner_height = 50
        page_height = img_height + top_banner_height + bottom_banner_height
        page_width = img_width

        # Beyaz bir sayfa oluştur
        page = Image.new("RGB", (page_width, page_height), color="white")

        # Orijinal resmi sayfaya yapıştır
        page.paste(img.convert("RGB"), (0, top_banner_height))

        draw = ImageDraw.Draw(page)  # Resim üzerine çizim yapmak için

        # Font ayarları
        try:
            font_wanted = ImageFont.truetype("Font/LibreBodoni-Medium.ttf", 40)
            font_reward = ImageFont.truetype("Font/LibreBodoni-Medium.ttf", 20)
        except:
            font_wanted = ImageFont.load_default()  # Font yoksa default font
            font_reward = ImageFont.load_default()

        # Üst banner: WANTED yazısı
        text = "WANTED"
        # Yazının boyutunu hesapla
        bbox = draw.textbbox((0, 0), text, font=font_wanted)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        # Yazıyı ortalayarak çiz
        draw.text(((page_width - w)//2, (top_banner_height - h)//2),
                  text, fill="black", font=font_wanted)

        # Alt banner: REWARD yazısı
        reward_text = "REWARD $5000"
        bbox2 = draw.textbbox((0, 0), reward_text, font=font_reward)
        w2 = bbox2[2] - bbox2[0]
        h2 = bbox2[3] - bbox2[1]
        draw.text(((page_width - w2)//2, top_banner_height + img_height + (bottom_banner_height - h2)//2),
                  reward_text, fill="black", font=font_reward)

        processed = page  # İşlenmiş posteri kaydet
        tk_img = ImageTk.PhotoImage(processed)  # Tkinter için hazırla
        label.config(image=tk_img)  # GUI üzerinde göster

# --- PDF Olarak Kaydetme Fonksiyonu ---


def save_as_pdf():
    """Oluşturulan posteri PDF olarak kaydet"""
    if processed:
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")])
        if file_path:
            processed.save(file_path, "PDF")
            print("Poster PDF olarak kaydedildi:", file_path)


# --- GUI Kurulumu ---
root = Tk()  # Ana pencere oluştur
root.title("WANTED Poster Generator")  # Pencere başlığı
root.geometry("800x800")  # Pencere boyutu

img = None  # Yüklenecek resim
processed = None  # İşlenmiş poster

# Butonlar
btn_load = Button(root, text="UPLOAD IMAGE",
                  command=load_image)  # Resim yükleme
btn_load.pack(pady=5)

btn_generate = Button(root, text="GENERATE WANTED",
                      command=generate_wanted)  # Poster oluştur
btn_generate.pack(pady=5)

btn_save_pdf = Button(root, text="SAVE AS PDF",
                      command=save_as_pdf)  # PDF kaydet
btn_save_pdf.pack(pady=5)

# Resmin gösterileceği alan
label = Label(root)
label.pack()

root.mainloop()  # GUI döngüsü başlat
