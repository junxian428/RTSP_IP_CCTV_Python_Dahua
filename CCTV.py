import cv2

# Replace with your actual RTSP URLs for each camera
rtsp_urls = [
    "rtsp://admin:XXXx@XX.XX.XX.XX:554/cam/realmonitor?channel=1&subtype=1",
    "rtsp://admin:XXXX@XX.XX.XX.XX:554/cam/realmonitor?channel=2&subtype=1",
    "rtsp://admin:XXXX@XX.XX.XX.XX:554/cam/realmonitor?channel=3&subtype=1",
    "rtsp://admin:XXXX@XX.XX.XX.XX:554/cam/realmonitor?channel=4&subtype=1"
]

# Scaling factor for zooming out
scaling_factor = 2.0

# Open each RTSP stream
caps = [cv2.VideoCapture(url) for url in rtsp_urls]

# Check if all streams are opened successfully
for i, cap in enumerate(caps):
    if not cap.isOpened():
        print(f"Error: Could not open stream {i+1}.")
    else:
        print(f"Connected to the RTSP stream {i+1}.")

# Read and display frames in a loop
while all(cap.isOpened() for cap in caps):
    for i, cap in enumerate(caps):
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Could not read frame from stream {i+1}.")
            break

        # Resize the frame to zoom out
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        # Display each frame in a separate window
        window_name = f"RTSP Stream {i+1} (Zoomed Out)"
        cv2.imshow(window_name, frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all resources
for cap in caps:
    cap.release()
cv2.destroyAllWindows()
