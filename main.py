# BirdRepellerUsingOpenCV
# This Project ensures that it reduces farmer effort in agricultural fields
import cv2
import pygame
import threading

pygame.init()

cascade_for_bird = cv2.CascadeClassifier('bird1.xml')

cap = cv2.VideoCapture("finalbird.mp4")

pygame.mixer.init()


audio_play_duration = 3 

def play_audio():
    pygame.mixer.music.load('bird_distress.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(int(audio_play_duration * 1000))  
    pygame.mixer.music.stop()

audio_thread = None

while True:
    try:
        ret, img = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        birds = cascade_for_bird.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        count = 0

        for (x, y, w, h) in birds:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            l = cv2.putText(img, 'BIRD', (x - w, y - h), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)

            
            if l.any():
                count += 1
                if count > 0 and (audio_thread is None or not audio_thread.is_alive()):
                    audio_thread = threading.Thread(target=play_audio)
                    audio_thread.start()

        cv2.imshow('BIRD REPELLER', img)

        if cv2.waitKey(70) & 0xFF == ord('x'):
            break
    except Exception as e:
        print("An error occurred:", e)
        break

cap.release()
cv2.destroyAllWindows()


pygame.mixer.quit()
pygame.quit()
