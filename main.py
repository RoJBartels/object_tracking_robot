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
    lower_red1 = np.array([0, 140, 50])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 140, 50])
    upper_red2 = np.array([180, 255, 255])

    # Masken erstellen
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Ergebnisbild (nur rote Bereiche sichtbar)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # 🔹 Konturen finden
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # größte Kontur wählen
        largest_contour = max(contours, key=cv2.contourArea)

        # kleine Objekte ignorieren (Rauschen)
        if cv2.contourArea(largest_contour) > 500:

            # Kreis um Objekt
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)

            # Mittelpunkt berechnen
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Zeichnen
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

                # Koordinaten anzeigen
                cv2.putText(frame, f"({cx}, {cy})", (cx + 10, cy),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


    # Anzeigen
    cv2.imshow("Tracking", frame)
    cv2.imshow("Maske (Rot)", mask)
    cv2.imshow("Erkanntes Objekt", result)

    # ESC zum Beenden
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()