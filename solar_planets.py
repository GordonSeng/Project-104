import cv2

img = cv2.imread("solar_planets.jpg")

cv2.putText(img, "Mercury", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (400, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (600, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn", (800, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus", (1000, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune", (1200, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

cv2.imshow("output", img)


cv2.imwrite("Solar_systemwithname.jpg", img)
            
cv2.waitKey(0)