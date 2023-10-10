import cv2
import numpy as np
import pygetwindow as gw
from PIL import ImageGrab
import pytesseract  # Placeholder for OCR, you can use more specialized libraries later

# Initialize the data aggregator list
data_aggregator = []

def capture_game_window(window_title):
    window = gw.getWindowsWithTitle(window_title)[0]
    return window

def process_frame(frame):
    # Convert to grayscale for contour detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Contour detection
    contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw the contours
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    
    return frame, contours

# def recognize_text(frame):
#     # Placeholder for text recognition
#     text = pytesseract.image_to_string(frame)
#     return text

def main():
    window_title = "EverQuest"
    window = capture_game_window(window_title)
    
    cv2.namedWindow('Processed Frame', cv2.WINDOW_NORMAL)  # Create a named window

    while True:
        # Capture the game frame
        frame = np.array(ImageGrab.grab(bbox=(window.left, window.top, window.width, window.height)))

        # Process the frame for object recognition
        processed_frame, contours = process_frame(frame)
        
        # # Recognize text (placeholder)
        # text = recognize_text(processed_frame)
        
        # Aggregate the data
        data_aggregator.append({
            'frame': processed_frame,
            'contours': contours,
            # 'text': text
        })
        
        # Show the processed frame (for debugging)
        cv2.imshow('Processed Frame', processed_frame)  # Use the same window name
        
        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()  # Destroy all windows



if __name__ == "__main__":
    main()
