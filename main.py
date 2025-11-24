import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
def main():
    x = []
    for i in range(1,51):
        img=Image.open("dataset\\"+str(i)+".bmp")
        arrimg = np.array(img)
        arrimg = arrimg[:,:,0]
        arrimg = arrimg.flatten()
        x.append(arrimg)

    y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0,0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
    
    x_train , x_test , y_train,y_test = train_test_split(x , y , test_size=0.2)
    
    model = LogisticRegression()
    model.fit(x_train,y_train)
    try:
        path = input("enter the path of your image :") 
        pred_1 = Image.open(path)
    except:
        print("enter the correct path...")
        main()
        
    pred_1 = np.array(pred_1)
    pred_1 = pred_1[:,:,0]
    pred_1 = pred_1.flatten()
    pred_1 = pred_1.reshape(1,-1)
    pred = model.predict(pred_1)
    if pred == 0:
        print("circle")
    elif pred == 1:
        print("sqrt")
    elif pred == 2:
        print("it is tringle")

main()