import cv2
import numpy as np

# Kamera starten (0 = Standard-Webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera konnte nicht geöffnet werden")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kein Frame erhalten")
        break

    # Bild spiegeln (optional, fühlt sich natürlicher an)
    frame = cv2.flip(frame, 1)

    # BGR → HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rot hat zwei Bereiche im HSV!
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Masken erstellen
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Ergebnisbild (nur rote Bereiche sichtbar)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Anzeigen
    cv2.imshow("Original", frame)
    cv2.imshow("Maske (Rot)", mask)
    cv2.imshow("Erkanntes Objekt", result)

    # ESC zum Beenden
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()