from PIL import Image, ImageDraw
import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)
process_this_frame = True
while True:
        ret, frame = video_capture.read()
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition_master uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            # image = face_recognition.load_image_file("biden.jpg")

            # Find all facial features in all the faces in the image
            face_landmarks_list = face_recognition.face_landmarks(rgb_small_frame)

            pil_image = Image.fromarray(rgb_small_frame)
            for face_landmarks in face_landmarks_list:
                d = cv2

                # Make the eyebrows into a nightmare
                d.polylines(face_landmarks['left_eyebrow'])
                d.polylines(face_landmarks['chin'])
                d.polylines(face_landmarks['right_eyebrow'])
                d.line(face_landmarks['left_eyebrow'])
                d.line(face_landmarks['right_eyebrow'])

                # Gloss the lips
                d.polylines(face_landmarks['top_lip'])
                d.polylines(face_landmarks['bottom_lip'])
                d.line(face_landmarks['top_lip'])
                d.line(face_landmarks['bottom_lip'])

                # Sparkle the eyes
                d.polylines(face_landmarks['left_eye'])
                d.polylines(face_landmarks['right_eye'])

                # Apply some eyeliner
                # d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
                # d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

                # pil_image.show()

                # Display the resulting image
            cv2.imshow('Video', frame)

                # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            process_this_frame = not process_this_frame

video_capture.release()
cv2.destroyAllWindows()
    # Display the results









# Load the jpg file into a numpy array
