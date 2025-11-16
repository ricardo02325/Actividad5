import cv2
import mediapipe as mp

# Inicializadores de MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles


# ---------------------------
# FUNCIÓN: Detectar dedos levantados
# ---------------------------
def dedos_levantados(hand_landmarks, handedness):
    tips = [4, 8, 12, 16, 20]  # Puntas de cada dedo
    dedos = []

    # Pulgar → depende de si es mano izquierda o derecha
    if handedness == "Right":
        dedos.append(1 if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x else 0)
    else:
        dedos.append(1 if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x else 0)

    # Otros dedos: comparación vertical
    for tip in tips[1:]:
        dedos.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0)

    return dedos


# ---------------------------
# FUNCIÓN: Detectar gesto
# ---------------------------
def detectar_gesto(dedos, handedness):
    suma = sum(dedos)

    # Gestos personalizados
    if dedos == [1, 0, 0, 0, 0]:
        return "👍 Like"

    if dedos == [0, 0, 0, 0, 1]:
        return "👎 Dislike"

    if dedos == [0, 1, 1, 0, 0]:
        return "✌ Amor y Paz"

    if dedos == [0, 1, 1, 1, 1]:
        return "🖐 Hola"

    # OK
    if dedos[0] == 1 and dedos[1] == 1 and dedos[2] == 0:
        return "👌 Okey"

    # Corazón con las dos manos
    if suma == 5:
        return f"✋ Mano {handedness}: Abierta"
    if suma == 10:
        return "❤️ Corazón (2 manos)"

    return f"Dedos: {suma}"


# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)   # espejado
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks, handed_label in zip(results.multi_hand_landmarks, results.multi_handedness):

                handedness = handed_label.classification[0].label  # Right o Left

                # Dibujar mano con estilos
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_styles.get_default_hand_landmarks_style(),
                    mp_styles.get_default_hand_connections_style()
                )

                dedos = dedos_levantados(hand_landmarks, handedness)
                gesto = detectar_gesto(dedos, handedness)

                cv2.putText(frame, f"{handedness}: {gesto}",
                            (10, 50 if handedness == "Right" else 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                            (0, 255, 0), 2)

        cv2.imshow("Detector de Gestos", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

cap.release()
cv2.destroyAllWindows()