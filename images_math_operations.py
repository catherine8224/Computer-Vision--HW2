import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read First Image
gray_img= cv2.imread('ISIA_Food500/images/Doufunao/Doufunao_0318.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('ISIA_Food500/images/Doufunao/Doufunao_0318.jpg')[:,:,::-1]
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
gray_resized_img = cv2.resize(gray_img, dim, interpolation = cv2.INTER_AREA)
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


#Read Second Image
gray_img2 = cv2.imread('ISIA_Food500/images/Lebkuchen/Lebkuchen_0042.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('ISIA_Food500/images/Lebkuchen/Lebkuchen_0042.jpg')[:,:,::-1]
# scale_percent = 60 # percent of original size
# width = int(img2.shape[1] * scale_percent / 100)
# height = int(img2.shape[0] * scale_percent / 100)
# dim = (width, height)
gray_resized_img2 = cv2.resize(gray_img2, dim, interpolation = cv2.INTER_AREA)
resized_img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)


#Arithmetic + Logarithmic
#Addition
addition = cv2.add(resized_img, resized_img2)
scalar_addition = cv2.add(resized_img, (50,50,50,0))
log_add = cv2.subtract(cv2.add(gray_resized_img, gray_resized_img2), cv2.divide(cv2.multiply(gray_resized_img, gray_resized_img2), 255))
#addition = (resized_img + 50)

#Subtraction
subtraction = cv2.subtract(resized_img, resized_img2)
scalar_subtraction = cv2.subtract(resized_img, (50,50,50,0))
log_sub = cv2.multiply(255, cv2.divide(cv2.subtract(gray_resized_img, gray_resized_img2), cv2.subtract(255, gray_resized_img2)))
#subtraction = (resized_img - resized_img2)

#Division
gray_division = cv2.divide(gray_resized_img, 2)
division = cv2.divide(resized_img, np.ones(4), scale=2)
#division = (resized_img//2)

#Multiplication
gray_multiplication = cv2.multiply(gray_resized_img, 2)
multiplication = cv2.multiply(resized_img, np.ones(4), scale=2)
scalar_mult = cv2.subtract(255, cv2.multiply(255, cv2.subtract(1, cv2.divide(gray_resized_img, 255))**2))

theta_a = -255*np.log(cv2.subtract(1, gray_resized_img//255))
theta_b = -255*np.log(cv2.subtract(1, gray_resized_img//255))

theta_inverse_a = cv2.multiply(255, cv2.subtract(1, cv2.exp(cv2.subtract(cv2.multiply(theta_a, theta_b), 255))))
#log_mult = cv2.multiply(theta_inverse_a, cv2.multiply(theta_a, theta_b))

#Arithmetic Operations
plt.figure(1, figsize=(12,10), dpi=80)

plt.subplot(421),plt.imshow(resized_img)
plt.title('Image 1'), plt.xticks([]), plt.yticks([])

plt.subplot(422), plt.imshow(resized_img2)
plt.title('Image 2'), plt.xticks([]), plt.yticks([])

plt.subplot(423), plt.imshow(addition)
plt.title('Alg. addition to image'), plt.xticks([]), plt.yticks([])

plt.subplot(424), plt.imshow(subtraction)
plt.title('Alg. subtraction to image'), plt.xticks([]), plt.yticks([])

plt.subplot(425), plt.imshow(scalar_addition)
plt.title('Scalar addition'), plt.xticks([]), plt.yticks([])

plt.subplot(426), plt.imshow(scalar_subtraction)
plt.title('Scalar subtraction'), plt.xticks([]), plt.yticks([])

plt.subplot(427), plt.imshow(division)
plt.title('Alg. division'), plt.xticks([]), plt.yticks([])

plt.subplot(428), plt.imshow(multiplication)
plt.title('Alg. multiplication'), plt.xticks([]), plt.yticks([])
plt.savefig("arithmetic_operations.png")
#plt.subplot(122),plt.imshow(img,cmap = 'gray')
#plt.show()


#Logic Operations
plt.figure(1, figsize=(12,10), dpi=80)

#AND
bitwise_and = cv2.bitwise_and(resized_img, resized_img2)

#OR
bitwise_or = cv2.bitwise_or(resized_img, resized_img2)

#NOT
bitwise_not = cv2.bitwise_not(resized_img)
bitwise_not2 = cv2.bitwise_not(resized_img2)


#XOR
bitwise_xor = cv2.bitwise_xor(resized_img, resized_img2)

#NAND
bitwise_nand = cv2.bitwise_not(bitwise_and)

#NOR
bitwise_nor = cv2.bitwise_not(bitwise_or)

plt.figure(1, figsize=(12,10), dpi=80)

plt.subplot(421),plt.imshow(bitwise_and)
plt.title('Logic AND'), plt.xticks([]), plt.yticks([])

plt.subplot(422), plt.imshow(bitwise_or)
plt.title('Logic OR'), plt.xticks([]), plt.yticks([])

plt.subplot(423), plt.imshow(bitwise_not)
plt.title('Logic NOT-image1'), plt.xticks([]), plt.yticks([])

plt.subplot(424), plt.imshow(bitwise_not2)
plt.title('Logic NOT-image2'), plt.xticks([]), plt.yticks([])

plt.subplot(425), plt.imshow(bitwise_xor)
plt.title('Logic XOR'), plt.xticks([]), plt.yticks([])

plt.subplot(426), plt.imshow(bitwise_nand)
plt.title('Logic NAND'), plt.xticks([]), plt.yticks([])

plt.subplot(427), plt.imshow(bitwise_nor)
plt.title('Logic NOR'), plt.xticks([]), plt.yticks([])
plt.savefig("logic_operations.png")
#plt.show()


#Logarithmic Operation
plt.figure(1, figsize=(12,10), dpi=80)

plt.subplot(221), plt.imshow(log_add, cmap='gray')
plt.title('Log. addition'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2, 2), plt.imshow(log_sub, cmap='gray')
plt.title('Log. subtraction'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2, 3), plt.imshow(scalar_mult, cmap='gray')
plt.title('Log. scalar multiply'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2, 4), plt.imshow(theta_inverse_a, cmap='gray')
plt.title('Log. multiplication'), plt.xticks([]), plt.yticks([])
plt.savefig("logarithmic_operations.png")
#plt.subplot(122),plt.imshow(img,cmap = 'gray')
#plt.show()





