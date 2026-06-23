# opencv_basics

Podstawy OpenCV w drodze do vision-guided robotics / bin picking.
Pięć mini-projektów: od wczytania obrazu po automatyczne wykrywanie konturów.

## Mini-projekty

1. **01_load_display.py** — wczytanie i wyświetlenie obrazu, kolejność kanałów BGR, `img.shape`
2. **02_grayscale.py** — konwersja BGR → skala szarości, zapis do pliku
3. **03_detection_sim.py** — symulacja detekcji: ręcznie rysowane ramki i podpisy obiektów
4. **04_canny.py** — wykrywanie krawędzi (Gaussian blur + Canny, dwa progi)
5. **05_contours.py** — automatyczne ramki z konturów (`findContours` + `boundingRect`), filtrowanie po polu

## Kluczowy wniosek: granica klasycznego CV 2D

Ten sam pipeline (Canny + contours) na dwóch różnych scenach:

**Scena chaotyczna — pojemnik z metalowymi tulejami:** obiekty stykają się,
nakładają, mają identyczny kolor i jasność. Krawędzie zlewają się, kontury
łączą kilka obiektów w jeden. Klasyczne CV 2D tu zawodzi.

**Scena płaska — rozdzielone obiekty na kontrastowym tle:** obiekty osobno,
ciemne na jasnym, widok z góry. Każdy obiekt złapany czysto, osobną ramką.

Wniosek: klasyczne CV 2D działa dla rozdzielonych, kontrastowych obiektów,
ale na chaotycznej scenie bin pickingu potrzeba głębi (kamera 3D),
dopasowania w chmurze punktów (ICP) i metod uczonych (sieci neuronowe).

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install opencv-python numpy
python3 05_contours.py
```
