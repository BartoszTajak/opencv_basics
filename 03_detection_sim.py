import cv2

img = cv2.imread("test.jpg")
if img is None:
    print("Nie znaleziono test.jpg!")
    exit()

h, w = img.shape[:2]

# "Wykryte" obiekty - wspolrzedne wpisane RECZNIE (symulacja).
# W prawdziwym pipeline policzy je Canny+findContours (patrz 05).
pt1_a = (int(w * 0.15), int(h * 0.25)); pt1_b = (int(w * 0.45), int(h * 0.60))
pt2_a = (int(w * 0.55), int(h * 0.35)); pt2_b = (int(w * 0.85), int(h * 0.75))

cv2.rectangle(img, pt1_a, pt1_b, (0, 255, 0), 3)
cv2.rectangle(img, pt2_a, pt2_b, (0, 255, 0), 3)
cv2.putText(img, "obiekt 1", (pt1_a[0], pt1_a[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
cv2.putText(img, "obiekt 2", (pt2_a[0], pt2_a[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imwrite("output_detection.png", img)
print("Zapisano output_detection.png")

cv2.imshow("Symulacja detekcji (reczne ramki)", img)
cv2.waitKey(0)
cv2.destroyAllWindows()