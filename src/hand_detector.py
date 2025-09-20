# src/hand_detector.py
import mediapipe as mp
import cv2
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class HandState:
    fingers_up: List[int]

class HandDetector:
    def __init__(self, max_hands=1):
        self.hands = mp.solutions.hands.Hands(max_num_hands=max_hands)

    def detect(self, frame) -> Optional[HandState]:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = self.hands.process(img)
        if not res.multi_hand_landmarks:
            return None
        lm = res.multi_hand_landmarks[0]
        index_up = int(lm.landmark[8].y < lm.landmark[6].y)
        return HandState(fingers_up=[index_up])
