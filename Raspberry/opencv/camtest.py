import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() is False:
  raise IOError

while(True):
  try:
    ret, frame = capture.read()
    if ret is False:
      raise IOError
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
  except KeyboardInterrupt:
    #CTRL when finished+Press C
    break

capture.release()
cv2.destroyAllWindows()