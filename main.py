import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import filedialog

def gui():
    global root,label
    root = tk.Tk()
    root.title("Shape Classifier")
    root.geometry("450x550")
    root.resizable(False, False)
    label = tk.Label(root, text="Welcome to Shape Classifier", font=("Arial", 14))
    label.pack(pady=20)

    instruction = tk.Label(root, text="Choose your file to classify your image", font=("Arial", 10))
    instruction.pack(pady=10)

    
    label = tk.Label(root, text="None",bg="white",bd=3,relief="sunken",width=20,height=2)
    label.pack(pady=4)

    choose_btn = tk.Button(root,text="choose file",command=choose_file)
    choose_btn.pack(pady=10)
        

    #tk.Canvas(root, width=350, height=250, bg="lightgray").pack(pady=15)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=5)
    root.mainloop()

def choose_file():
    global label , user_path
    user_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("All Files", "*.*"), ("Images", "*.png;*.jpg;*.bmp")]
    )
    main()



def main():
    global javab
    x = []
    for i in range(1,51):
        img=Image.open("dataset\\"+str(i)+".bmp")
        arrimg = np.array(img)
        arrimg = arrimg[:,:,0]
        arrimg = arrimg.flatten()
        x.append(arrimg)

    y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0,0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
    
    x_train , x_test , y_train,y_test = train_test_split(x , y )
    
    model = LogisticRegression(max_iter=5000)
    model.fit(x_train,y_train)
    try:
        path = user_path
        pred_1 = Image.open(path).convert("L")
        pred_1 = np.resize(pred_1,(64,64))

    except:
        pass
        
    pred_1 = np.array(pred_1)
    #pred_1 = pred_1[:,:,0]
    pred_1 = pred_1.flatten()
    pred_1 = pred_1.reshape(1,-1)
    pred = model.predict(pred_1)
    
    javab = "None"
    if pred == 0:
        javab = "circle"
    elif pred == 1:
        javab = "square"
    elif pred == 2:
        javab = "triangle"
    label.config(text=javab)
gui()