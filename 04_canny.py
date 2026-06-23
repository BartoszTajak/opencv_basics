import cv2

# --- WCZYTANIE + SZAROŚĆ ---
img = cv2.imread("test.jpg")
if img is None:
    print("Nie znaleziono test.jpg!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # Canny działa na szarości

# --- KROK 1: ROZMYCIE (usuwa szum przed wykrywaniem) ---
# GaussianBlur(obraz, rozmiar_jądra, 0)
# (5, 5) = siła rozmycia. Większe = mocniejsze. Musi być NIEPARZYSTE.
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# --- KROK 2: CANNY (dwa progi: dolny, górny) ---
# To są te dwie liczby z teorii. Start: 50 / 150.
edges = cv2.Canny(blur, 100, 250)

# --- ZAPIS ---
cv2.imwrite("output_edges.png", edges)
print("Zapisano output_edges.png")

# --- WYŚWIETLENIE: oryginał szary + krawędzie ---
cv2.imshow("1 - szarosc", gray)
cv2.imshow("2 - krawedzie Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()