# import cv2

# # Open the camera (0 is usually the default camera)
# cap = cv2.VideoCapture(0)

# while True:
#     # Read a frame from the camera
#     ret, frame = cap.read()

#     if not ret:
#         print("Failed to grab frame")
#         break

#     # Flip the frame
#     # 0 = flip vertically, 1 = flip horizontally, -1 = flip both axes
#     flipped_frame = cv2.flip(frame, 1)  # Flip horizontally

#     # Show the flipped frame
#     cv2.imshow('Flipped Camera Feed', flipped_frame)

#     # Break the loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close all windows
# cap.release()
# cv2.destroyAllWindows()




# cvzone.cornerRect is a utility function that simplifies drawing aesthetically pleasing bounding boxes with rounded corners on images or video frames, often used in object detection and computer vision projects.

# import cv2
# import cvzone

# # Create a video capture object
# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     if success:
#         # Define a bounding box (x, y, w, h)
#         bbox = (100, 100, 200, 300)
        
#         # Draw a rectangle with corner lines around the bbox
#         img = cvzone.cornerRect(img, bbox, l=50, t=10, rt=2, colorR=(0, 255, 0))

#         # Display the image
#         cv2.imshow("Image", img)

#     # Break the loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()









# cv2.rectangle() is a simple but powerful function to draw rectangles of various sizes and colors on images or video frames. It is commonly used in computer vision tasks to highlight objects or regions of interest.



# import cv2

# # Create a blank image (black)
# img = cv2.imread("subham.jpg")

# # Define top-left and bottom-right coordinates of the rectangle
# pt1 = (100, 100)  # Top-left corner
# pt2 = (300, 300)  # Bottom-right corner

# # Define color in BGR (e.g., green)
# color = (0, 255, 0)

# # Draw the rectangle on the image with thickness 2
# cv2.rectangle(img, pt1, pt2, color, thickness=2)

# # Display the image
# cv2.imshow("Rectangle", img)

# # Wait for a key press and close the window
# cv2.waitKey(0)
# cv2.destroyAllWindows()






# cv2.putText() is a versatile function for adding custom text to images or video frames in OpenCV.



# import cv2

# # Create a blank image (black)
# img = cv2.imread("subham.jpg")

# # Define the text and position
# text = "Hello, OpenCV!"
# org = (50, 100)  # Bottom-left corner of the text

# # Define font properties
# font = cv2.FONT_HERSHEY_COMPLEX_SMALL
# fontScale = 1
# color = (255, 255, 255)  # White color
# thickness = 2

# # Add text to the image
# cv2.putText(img, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

# # Display the image
# cv2.imshow("Image with Text", img)

# # Wait for a key press and close the window
# cv2.waitKey(0)
# cv2.destroyAllWindows()
