# src/config.py
"""
Configuration constants for GestureBand.
"""

# Camera and window settings
CAMERA_INDEX = 0        # default webcam index (0 = first camera)
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Cooldown (seconds) to avoid repeated triggers while holding a gesture
ACTION_COOLDOWN = 0.6

# Default samples mapping (you'll add wav files later in assets/samples/)
DEFAULT_SAMPLES = {
    "piano": "piano_C4.wav",
    "guitar": "pluck_A3.wav",
    "drum": "kick.wav"
}
