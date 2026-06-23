import cv2

# --- WCZYTANIE + SZAROŚĆ + BLUR + CANNY (znasz to już) ---
img = cv2.imread("test.jpg")
if img is None:
    print("Nie znaleziono test.jpg!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
edges = cv2.Canny(blur, 50, 150)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
edges = cv2.dilate(edges, kernel, iterations=1)

# --- ZNAJDŹ KONTURY z krawędzi ---
# findContours grupuje białe piksele krawędzi w osobne kształty (kontury).
# RETR_EXTERNAL = bierz tylko ZEWNĘTRZNE kontury (pomijaj dziury w środku).
# CHAIN_APPROX_SIMPLE = kompresuj punkty (oszczędza pamięć).
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Znaleziono konturów: {len(contours)}")

# --- RYSUJ RAMKĘ wokół każdego KONTURU (automatycznie!) ---
result = img.copy()   # rysujemy na kopii, żeby nie psuć oryginału
licznik = 0

for c in contours:
    # Pole konturu — odsiewamy malutkie (szum, refleksy)
    area = cv2.contourArea(c)
    if area < 8000:        # próg powierzchni: ignoruj kontury mniejsze niż 500 px
        continue

    # boundingRect = najmniejszy prostokąt obejmujący kontur
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
    licznik += 1

print(f"Narysowano ramek (po odsianiu małych): {licznik}")

# --- ZAPIS + WYŚWIETLENIE ---
cv2.imwrite("output_contours.png", result)
print("Zapisano output_contours.png")

cv2.imshow("Automatyczne ramki (findContours)", result)
cv2.waitKey(0)
cv2.destroyAllWindows()