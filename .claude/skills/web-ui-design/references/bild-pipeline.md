# Bild-Pipeline

Ziel: aus einer großen Quelldatei kleine, schnelle, passende Varianten machen.

## 1. Quelle prüfen

```bash
# Größe, Format, Farbraum
sips -g pixelWidth -g pixelHeight -g format -g space DATEI.jpg
# Herkunft und Freigaben (iStock/Getty schreiben sie in XMP)
strings -n 6 DATEI.jpg | grep -i -E "istock|getty|credit|licens|released|headline"
```

Hinweise in den Metadaten, auf die zu achten ist: `Model and Property Released (MR&PR)`, `photoshop:Credit`, `photoshop:Source`, `AssetID`.

## 2. Foto aus einem SVG-Mantel lösen

Ein SVG mit nur `<image xlink:href="data:image/jpeg;base64,...">` ist ein Foto, kein Vektor.

```python
import re, base64
s = open("datei.svg", encoding="utf-8").read()
print(re.search(r"<image[^>]*>", s).group(0)[:200])          # Maße und Typ ansehen
b = re.search(r"data:image/(?:jpeg|png);base64,([A-Za-z0-9+/=]+)", s).group(1)
open("eingebettet.jpg", "wb").write(base64.b64decode(b))
```

Aufgerufen mit `python3 -I`. Die Datei danach öffnen und prüfen. Das SVG selbst nie ins Repo legen.

## 3. Zuschneiden und skalieren (Pillow)

```python
from PIL import Image
im = Image.open("quelle.jpg").convert("RGB")
w, h = im.size
quadrat = im.crop((x0, 0, x0 + h, h))            # x0 so wählen, dass das Motiv mittig liegt
for breite in (640, 960, 1280):
    quadrat.resize((breite, breite), Image.LANCZOS).save(f"tmp/hero-{breite}.png")
for breite in (800, 1600):                         # Querformat unbeschnitten
    im.resize((breite, round(breite * h / w)), Image.LANCZOS).save(f"tmp/wide-{breite}.png")
```

Den Ausschnitt immer ansehen, bevor er weiterverarbeitet wird (Vorschau mit `sips -Z 900`).

## 4. Exportieren

```bash
cwebp -quiet -q 90 -m 6 -sharp_yuv -pass 10 tmp/hero-960.png -o img/hero-960.webp
avifenc -q 76 -s 4 -y 444 -j 4 tmp/hero-960.png img/hero-960.avif
```

Qualität gewählt nach Vergleich im 200-%-Ausschnitt des Gesichts: AVIF q60 verliert Hautdetails, ab q70 nah am Original, q76 mit voller Farbauflösung (`-y 444`) ist ein guter Kompromiss. WebP q90 mit `-sharp_yuv`. Vor dem Export nach dem Verkleinern leicht schärfen (`ImageFilter.UnsharpMask(radius=0.8, percent=35, threshold=2)`).

Größen aus dem Original in einem Schritt mit Lanczos skalieren (nie Zwischenstufen). Quadrat-Hero: 640, 960, 1280, 1600. Querformat-Band: 800, 1280, 1920, 2400. Richtwerte AVIF: Hero 1280 px ca. 135 KB, Band 1920 px ca. 135 KB, Band 2400 px ca. 225 KB. Ein Gerät lädt nur eine Variante.

## 5. Einbinden

```html
<picture>
  <source type="image/avif" srcset="img/hero-640.avif 640w, img/hero-960.avif 960w, img/hero-1280.avif 1280w" sizes="(min-width: 1024px) 584px, 100vw">
  <source type="image/webp" srcset="img/hero-640.webp 640w, img/hero-960.webp 960w, img/hero-1280.webp 1280w" sizes="(min-width: 1024px) 584px, 100vw">
  <img src="img/hero-960.webp" width="1280" height="1280" alt="..." fetchpriority="high" decoding="async" class="h-full w-full object-cover">
</picture>
```

- `width` und `height` setzen (kein Springen beim Laden).
- Bild im ersten Bildschirm: `fetchpriority="high"`, nie `loading="lazy"`. Alle anderen: `loading="lazy"`.
- `sizes` an die echte Darstellungsbreite anpassen.
- Mobil bei stark abweichendem Motiv ein eigenes Bild per `media` im `<source>`.

## 6. Aufräumen

- Originale, Wrapper und Zwischendateien liegen außerhalb des Repos oder in `.gitignore`.
- Nicht mehr genutzte Varianten vor dem Commit löschen, wenn der User zustimmt.
