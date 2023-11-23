import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import filedialog
import pygame

# Initialize pygame
pygame.init()

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


def random_game():
    global photo_images, sorted_photo_images
    image = Image.open(f"./images/{choice_image}")
    width, height = image.size
    tile_width, tile_height = width // 4, height // 4
    tiles = []
    for z in range(4):
        for j in range(4):
            x0, y0 = j * tile_width, z * tile_height
            x1, y1 = x0 + tile_width, y0 + tile_height
            if z == 3 and j == 3:
                tile = Image.new('RGB', (tile_width, tile_height), (255, 255, 255))
            else:
                tile = image.crop((x0, y0, x1, y1))
            tiles.append(tile)
    sorted_photo_images = []
    for tile in tiles:
        photo_image = ImageTk.PhotoImage(tile)
        sorted_photo_images.append(photo_image)
    for h in range(200):
        t = random.randint(2, 14)
        sorted_photo_images[t], sorted_photo_images[t-2] = sorted_photo_images[t-2], sorted_photo_images[t]
    photo_images = sorted_photo_images


def click(button_click):
    def change_button():
        play_sound("sounds/tapping_sound.wav")
        global close, c
        for j in range(4):
            row = [buttons[j * 4 + x]["image"] for x in range(4)]
            check_a, check_b, check_c, check_g = [], [], [], []
            for k in range(2):
                if row[k] != f"pyimage{str(6+(c*16))}" and row[k] != button_click["image"]:
                    check_a.append(row[k])
                if row[k + 1] != f"pyimage{str(6+(c*16))}" and row[k + 1] != button_click["image"]:
                    check_b.append(row[k + 1])
                if row[k + 2] != f"pyimage{str(6+(c*16))}" and row[k + 2] != button_click["image"]:
                    check_c.append(row[k + 2])
            if len(check_a) < 1 or len(check_b) < 1 or len(check_c) < 1:
                close = True
        for j in range(4):
            col = [buttons[x * 4 + j]["image"] for x in range(4)]
            check_d, check_e, check_f = [], [], []
            for k in range(2):
                if col[k] != f"pyimage{str(6+(c*16))}" and col[k] != button_click["image"]:
                    check_d.append(col[k])
                if col[k + 1] != f"pyimage{str(6+(c*16))}" and col[k + 1] != button_click["image"]:
                    check_e.append(col[k + 1])
                if col[k + 2] != f"pyimage{str(6+(c*16))}" and col[k + 2] != button_click["image"]:
                    check_f.append(col[k + 2])
            if len(check_d) < 1 or len(check_e) < 1 or len(check_f) < 1:
                close = True
        if button_click["image"] != f"pyimage{str(6 + (c * 16))}" and close:
            for b in buttons:
                if b["image"] == f"pyimage{str(6+(c*16))}":
                    b["image"] = button_click["image"]
            button_click["image"] = f"pyimage{str(6 + (c * 16))}"
            close = False
            check_win()
    return change_button


def check_win():
    list_sorted = [f"pyimage{str(u + 1)}" for u in range(6 + ((c - 1) * 16), 6 + (c * 16))]
    if [b["image"] for b in buttons] == list_sorted:
        msg_won["text"] = "👍 כל הכבוד"
        play_sound("sounds/win_sound.wav")



def restart_game():
    global c
    c += 1
    random_game()
    for g in range(16):
        buttons[g]["image"] = photo_images[g]
    msg_won["text"] = ""


def change_image(button_click):
    def new_image():
        global choice_image, c
        c += 1
        if button_click == buttons_write[0]:
            choice_image = "horse.png"
        if button_click == buttons_write[1]:
            choice_image = "waterfall.jpg"
        if button_click == buttons_write[2]:
            choice_image = "Islands.jpg"
        if button_click == buttons_left[0]:
            choice_image = "city.jpg"
        if button_click == buttons_left[1]:
            choice_image = "house.jpg"
        if button_click == buttons_left[2]:
            choice_image = "london.jpg"
        random_game()
        restart_game()
    return new_image


root = Tk()
tkinter.filedialog.Open()
root.title("משחק פאזל")
root.configure(bg="#F5F5DC")

choice_image = "horse.png"

wrap = tkinter.Frame(root, bg="#F5F5DC")
wrap.grid(row=1, column=2, padx=5, pady=25)

images_write = []
image_1 = Image.open("./images/horse.png")
tile_1 = image_1.resize((256, 170), Image.LANCZOS)
photo_image_1 = ImageTk.PhotoImage(tile_1)
images_write.append(photo_image_1)
image_2 = Image.open("./images/waterfall.jpg")
tile_2 = image_2.resize((256, 170), Image.LANCZOS)
photo_image_2 = ImageTk.PhotoImage(tile_2)
images_write.append(photo_image_2)
image_3 = Image.open("./images/Islands.jpg")
tile_3 = image_3.resize((256, 170), Image.LANCZOS)
photo_image_3 = ImageTk.PhotoImage(tile_3)
images_write.append(photo_image_3)


images_left = []
image_4 = Image.open("./images/city.jpg")
tile_4 = image_4.resize((256, 170), Image.LANCZOS)
photo_image_4 = ImageTk.PhotoImage(tile_4)
images_left.append(photo_image_4)
image_5 = Image.open("./images/house.jpg")
tile_5 = image_5.resize((256, 170), Image.LANCZOS)
photo_image_5 = ImageTk.PhotoImage(tile_5)
images_left.append(photo_image_5)
image_6 = Image.open("./images/london.jpg")
tile_6 = image_6.resize((256, 170), Image.LANCZOS)
photo_image_6 = ImageTk.PhotoImage(tile_6)
images_left.append(photo_image_6)


c = 1
close = False
game_over = False
photo_images = []
sorted_photo_images = []
buttons = []
random_game()
for i in range(16):
    button = Button(wrap)
    button["image"] = photo_images[i]
    button.configure(command=click(button))
    button.grid(row=i // 4, column=i % 4)
    buttons.append(button)
msg_won = Label(wrap, text="", bg="#F5F5DC", fg="#756035", width=15, height=2, font=("Ariel", 26, "bold"))
msg_won.grid(row=4, columnspan=4)
restart_button = Button(wrap, text="משחק חדש", bg="#756035", width=10, fg="#F5F5DC", font=("Ariel", 14, "bold"),
                        command=restart_game)
restart_button.grid(row=5, columnspan=4)

wrap_1 = tkinter.Frame(root, bg="#F5F5DC")
wrap_1.grid(row=1, column=1, padx=5, pady=25)
wrap_2 = tkinter.Frame(root, bg="#F5F5DC")
wrap_2.grid(row=1, column=3, padx=5, pady=25)

buttons_write = []
for i in range(3):
    button = Button(wrap_1, image=images_write[i])
    button.configure(command=change_image(button))
    button.pack(padx=10, pady=25)
    buttons_write.append(button)

buttons_left = []
for i in range(3):
    button = Button(wrap_2, image=images_left[i])
    button.configure(command=change_image(button))
    button.pack(padx=10, pady=25)
    buttons_left.append(button)
print(buttons_left)


root.mainloop()