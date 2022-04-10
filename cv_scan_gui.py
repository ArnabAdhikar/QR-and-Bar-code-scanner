from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import cv2
from pyzbar import pyzbar
text1 = ""
def start_scan():
    url = url1.get()+"/video"
    capture = cv2.VideoCapture(url)
    while True:
        success, frame = capture.read()
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.putText(frame, "q to exit.", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 100), 1)
        b_q_codes = pyzbar.decode(frame)
        for i in b_q_codes:
            (x, y, z, t) = i.rect
            cv2.rectangle(frame, (x, y), (x + z, y + t), (255, 100, 2), 1)
            content = i.data.decode("utf-8")
            type1 = i.type
            text1 = f"Barcode : {content}\nType : {type1}"
            cv2.putText(frame, text1, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow("code scanner", frame)
        if cv2.waitKey(1) == ord('q'):
            message = f"{text1}"
            text_box = Text(root, height=7, width=40)
            text_box.pack(expand=True)
            text_box.insert('end', message)
            text_box.config(state='disabled')
            break
    if text1:
        print(text1)
    capture.release()
    cv2.destroyAllWindows()
root = Tk()
root.title("Barcode or Qr code scanner")
root.minsize(600, 600)
root.maxsize(700, 700)
myFont = font.Font(family='Baguet Script', size=18)
myFont1 = font.Font(family='Baguet Script', size=12)
f1 = Frame(root, bg="blue", borderwidth=3, relief=GROOVE)
f1.pack(fill=X)
Label(f1, text="Bar code and QR code scanner.", font=myFont).pack(pady=20)
Label(root, text="Instructions:-", fg="red", font="18").pack(pady=9, anchor=W)
Label(root, text="->Install th IP Camera on your mobile.", font=myFont1).pack(anchor=W)
Label(root, text="->Connect the machine with mobile hotspot.", font=myFont1).pack(anchor=W)

img0 = Image.open("scanner.png")
resize_image = img0.resize((200, 30))
img = ImageTk.PhotoImage(img0)
label = Label(image=img)
label.img0 = img
label.pack()

f2 = Frame(root, borderwidth=1, relief=RIDGE)
f2.pack(fill=X)
Label(f2, text="Enter/Edit your mobile webcam URL:", font="12").pack(pady=9)

url1 = StringVar()
Entry(root, textvariable=url1).pack(fill=X)

img2 = PhotoImage(file=r"click.png")
Button(text="Start scan!!!", image=img2, compound=LEFT, command=start_scan, activebackground="green",
       activeforeground="yellow").pack(fill=X)

root.mainloop()
