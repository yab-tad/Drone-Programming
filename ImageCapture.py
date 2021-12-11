from djitello import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    # gives us individual image coming from tello drone
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitkey(1) #frame will shutdown before we can see it