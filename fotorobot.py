from tkinter.messagebox import showinfo
from tkinter import simpledialog, Canvas
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import pygame
import os


OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# pygame.mixer.init()
# pygame.mixer.music.load("Betsy feat. Мария Янковская - Сигма Бой.mp3")  
# muusika_mängib = False  

pildid = {}
objektid = {}
olemas = {}

osa_pildid = {
    "silmad": ["silm1.png", "silm2.png", "silm3.png", "silm4.png", "silm5.png"],
    "nina": ["nos1.png", "nos2.png", "nos3.png", "nos4.png", "nos5.png", "nos6.png"],
    "suu": ["lips1.png", "lips2.png", "lips3.png", "lips4.png", "lips5.png"],
    "juuksur": ["hair1.png", "hair2.png", "hair3.png", "hair4.png", "hair5.png", "hair6.png"],
    "acs": ["acs1.png", "acs2.png", "acs3.png", "acs4.png", "acs5.png"],
}

osa_index = {
    "silmad": 1,
    "nina": 0,
    "suu": 2,
    "juuksur":3,
    "acs": 3
}

def uuenda_osa(nimi, x, y):
    osa_index[nimi] = (osa_index[nimi] + 1) % len(osa_pildid[nimi])
    fail = osa_pildid[nimi][osa_index[nimi]]

    if olemas.get(nimi):
        canvas.delete(objektid[nimi])

    pil_img = Image.open(fail).convert("RGBA").resize((400, 420))
    tk_img = ImageTk.PhotoImage(pil_img)
    pildid[nimi] = tk_img
    objektid[nimi] = canvas.create_image(x, y, image=tk_img)
    olemas[nimi] = True

# def toggle_muusika():
#     global muusika_mängib
#     if muusika_mängib:
#         pygame.mixer.music.stop()
#         muusika_nupp.configure(text="Mängi muusikat")
#         muusika_mängib = False
#     else:
#         pygame.mixer.music.play(loops=-1)
#         muusika_nupp.configure(text="Peata muusika")
#         muusika_mängib = True

def salvesta_nägu():
    failinimi = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita):")
    if not failinimi:
        return

    lõpp_pilt = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    kihid = {
        "nägu": "head.png",
        "silmad": osa_pildid["silmad"][osa_index["silmad"]],
        "nina": osa_pildid["nina"][osa_index["nina"]],
        "suu": osa_pildid["suu"][osa_index["suu"]],
        "juuksur": osa_pildid["juuksur"][osa_index["juuksur"]],
        "acs": osa_pildid["acs"][osa_index["acs"]]
    }

    for nimi, failitee in kihid.items():
        osa = Image.open(failitee).convert("RGBA").resize((400, 400))
        lõpp_pilt.alpha_composite(osa)

    save_path = os.path.join(OUTPUT_DIR, f"{failinimi}.png")
    lõpp_pilt.save(save_path)
    showinfo("Pilt salvestatud", f"Fail on salvestatud nimega {save_path}")

app = ctk.CTk()
app.geometry("800x500")
app.title("Näo looja")

canvas = Canvas(app, width=400, height=350, bg="white")
canvas.pack(side="right", padx=10, pady=10)


pil_img = Image.open("head.png").convert("RGBA").resize((400, 400))
tk_img = ImageTk.PhotoImage(pil_img)
pildid["nägu"] = tk_img
objektid["nägu"] = canvas.create_image(200, 220, image=tk_img)
olemas["nägu"] = True


for osa in osa_pildid.keys():
    uuenda_osa(osa, 200, 220)


def nupp_silmad(): uuenda_osa("silmad", 200, 220)
def nupp_nina(): uuenda_osa("nina", 200, 220)
def nupp_suu(): uuenda_osa("suu", 200, 220)
def nupp_juuksur(): uuenda_osa("juuksur", 200, 220)
def nupp_acs(): uuenda_osa("acs", 200, 220)

frame = ctk.CTkFrame(app)
frame.pack(side="left", padx=10, pady=10)


nuppu_seaded = {
    "width": 150, "height": 40,
    "fg_color": "grey",
    "text_color": "darkred",
    "corner_radius": 20
}

ctk.CTkLabel(frame, text="Valige näo osad:", **nuppu_seaded, font=("Segoe UI Emoji", 20)).pack(pady=5)
ctk.CTkButton(frame, text="Silmad", command=nupp_silmad, **nuppu_seaded, font=("Segoe UI Emoji", 20)).pack(pady=3)
ctk.CTkButton(frame, text="Nina", command=nupp_nina, **nuppu_seaded, font=("Segoe UI Emoji", 20)).pack(pady=3)
ctk.CTkButton(frame, text="Suu", command=nupp_suu, **nuppu_seaded, font=("Segoe UI Emoji", 20)).pack(pady=3)
ctk.CTkButton(frame, text="Juuksur", command=nupp_juuksur, **nuppu_seaded, font=("Segoe UI Emoji", 20)).pack(pady=3)
ctk.CTkButton(frame, text="Aksessuaarid", command=nupp_acs, **nuppu_seaded, font=("Segoe UI Emoji", 20)).pack(pady=3)
ctk.CTkButton(frame, text="Salvesta nägu", command=salvesta_nägu, **nuppu_seaded, font=("Segoe UI Emoji", 20)).pack(pady=10)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(padx=10, pady=10)

# muusika_nupp = ctk.CTkButton(
#     frame_mus,
#     text="Mängi muusikat",
#     fg_color="grey",
#     command=toggle_muusika,
#     font=("Segoe UI Emoji", 20)
# )
# muusika_nupp.pack(pady=10)












app.mainloop()
