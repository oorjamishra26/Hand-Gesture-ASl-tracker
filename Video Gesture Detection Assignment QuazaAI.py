import cv2

cap = cv2.VideoCapture('/Users/oorjamishra/Desktop/video detect/data/vecteezy_slow-motion-asian-sportswoman-wearing-black-sportswear_8777747.mov')

fgbg = cv2.createBackgroundSubtractorMOG2()


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if not ret:
        break


    fgmask = fgbg.apply(frame)


    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:

        area = cv2.contourArea(contour)


        min_area = 1000

        if area > min_area:

            x, y, w, h = cv2.boundingRect(contour)

    
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)


            cv2.putText(frame, 'DETECTED', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)


    out.write(frame)


    cv2.imshow('Frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
