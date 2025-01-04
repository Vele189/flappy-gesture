import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,  # Set to False for real-time processing
    max_num_hands=1,  # Maximum number of hands to detect
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


def calculate_distance(point1, point2):
    """
    Calculate Euclidean distance between two 3D points.

    Args:
        point1: First point with x, y, z coordinates
        point2: Second point with x, y, z coordinates

    Returns:
        float: Euclidean distance between the points
    """
    return np.sqrt(
        (point1.x - point2.x) ** 2 +
        (point1.y - point2.y) ** 2 +
        (point1.z - point2.z) ** 2
    )


def get_finger_states(hand_landmarks):
    """
    Determine if each finger is extended based on joint positions.

    Args:
        hand_landmarks: List of hand landmarks detected by MediaPipe

    Returns:
        dict: Boolean state for each finger
    """
    finger_states = {
        'thumb': False,
        'index': False,
        'middle': False,
        'ring': False,
        'pinky': False
    }

    # Thumb logic (comparing with wrist)
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_base = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

    finger_states['thumb'] = calculate_distance(thumb_tip, wrist) > calculate_distance(thumb_base, wrist)

    # For other fingers, compare tip distance to pip (third) joint
    fingers = [
        (mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.INDEX_FINGER_PIP),
        (mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP),
        (mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_PIP),
        (mp_hands.HandLandmark.PINKY_TIP, mp_hands.HandLandmark.PINKY_PIP)
    ]

    finger_names = ['index', 'middle', 'ring', 'pinky']

    for (tip_id, pip_id), finger_name in zip(fingers, finger_names):
        tip = hand_landmarks.landmark[tip_id]
        pip = hand_landmarks.landmark[pip_id]
        # A finger is considered extended if its tip is higher than its pip joint (lower y value)
        finger_states[finger_name] = tip.y < pip.y

    return finger_states


def classify_gesture(hand_landmarks):
    """
    Classifies hand gesture as open palm or fist based on finger positions.

    Args:
        hand_landmarks: List of hand landmarks detected by MediaPipe

    Returns:
        str: "open", "fist", or "other"
    """
    finger_states = get_finger_states(hand_landmarks)

    # Count extended fingers
    extended_fingers = sum(finger_states.values())

    if extended_fingers >= 4:
        return "open"
    elif extended_fingers <= 1:  # Allow thumb to be either position for fist
        return "fist"
    else:
        return "other"


def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break

            # Convert the BGR image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the image with MediaPipe Hands
            results = hands.process(image)

            # Convert back to BGR for display
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw hand landmarks and classify gesture
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2),
                        mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                    )

                    gesture = classify_gesture(hand_landmarks)
                    # Display gesture classification
                    cv2.putText(
                        image,
                        f"Gesture: {gesture}",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )

            # Display the resulting frame
            cv2.imshow('Hand Gesture Recognition', image)

            # Break loop on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Clean up
        cap.release()
        cv2.destroyAllWindows()
        hands.close()


if __name__ == "__main__":
    main()