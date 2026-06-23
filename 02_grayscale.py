import cv2

img = cv2.imread("test.jpg")
if img is None:
    print("Nie znaleziono test.jpg!")
    exit()

# Konwersja BGR -> skala szarości
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(f"Kolor  shape: {img.shape}")    # (H, W, 3) - 3 kanaly
print(f"Szarosc shape: {gray.shape}")   # (H, W)    - brak 3. wymiaru

cv2.imwrite("output_gray.png", gray)
print("Zapisano output_gray.png")

cv2.imshow("Kolor (BGR)", img)
cv2.imshow("Szarosc", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()