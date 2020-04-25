import cv2
import numpy as np
import copy
import base64



def computeGradients(img):
    image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    topCornerImg = copy.copy(img)
    k = np.zeros((image.shape[0],image.shape[1],1),np.float32)
    ix = np.zeros((image.shape[0],image.shape[1],1),np.float32)
    iy = np.zeros((image.shape[0], image.shape[1], 1), np.float32)
    ixx = np.zeros((image.shape[0], image.shape[1], 1), np.float32)
    ixy = np.zeros((image.shape[0], image.shape[1], 1), np.float32)
    iyy = np.zeros((image.shape[0], image.shape[1], 1), np.float32)

    print(image.shape[0])
    print(image.shape[1])
    print(len(ix))

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            topCornerImg[i][j][0] = img[i][j][0]
            topCornerImg[i][j][1] = img[i][j][1]
            topCornerImg[i][j][2] = img[i][j][2]



    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(j>0 and j<image.shape[1]-1):
                ix[i][j] = int(image[i][j-1]) - int(image[i][j+1])


    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(i>0 and i<image.shape[0]-1):
                iy[i][j] = int(image[i-1][j]) - int(image[i+1][j])

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            ixx[i][j] = ix[i][j]*ix[i][j]





    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            iyy[i][j] = iy[i][j]*iy[i][j]





    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            ixy[i][j] = ix[i][j]*iy[i][j]



    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            ixxsum = 0
            iyysum = 0
            ixysum = 0
            for l in range(-1,2):
                for m in range(-1,2):
                    if((i+l>0 and i+l<image.shape[0]) and (j+m>0 and j+m<image.shape[1])):

                        print("i: ", i, "l: ", l)
                        print("j: ", j, "m: ", m)
                        print(image.shape[1])


                        ixxsum += ixx[i+l][j+m]
                        iyysum += iyy[i + l][j + m]
                        ixysum += ixy[i + l][j + m]


            k[i][j] = ((ixxsum * iyysum) - (ixysum * ixysum)) - .05*((ixxsum +iyysum)**2)

            #print("Det at i,j ", i,",",j, " is ",(ixx[i][j] * iyy[i][j]) - (ixy[i][j] * ixy[i][j]))

    maxk = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(k[i][j] > maxk):
                maxk = k[i][j]
    print("Max k value: ",maxk)
    cornerList = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(k[i][j] > (.2 * maxk)):
                cornerList.append([i,j,k[i][j]])

                cv2.circle(img,(j,i),1,(0,0,255),1)
    cornerList.sort(key=lambda x:x[2],reverse=True)

    for i in range(10):
        cv2.circle(topCornerImg,(cornerList[i][1],cornerList[i][0]),1,(0,0,255),1)
    print(cornerList)




    cv2.imshow("cornerdetection",img)




    
    cv2.waitKey()
    cv2.waitKey()

    cv2.imshow("topncorners",topCornerImg)
    cv2.waitKey()
    return k,maxk


def getThird(arr):
    return arr[2]


def main():
    image = cv2.imread("corvette.jpg")


    
    #cv2.imshow("test",gScale)
    #cv2.waitKey()
    computeGradients(image)








if __name__ == "__main__":
    main()