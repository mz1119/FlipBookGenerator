import cv2 as cv


def main():
    #type of image processing
    # 0 for original image
    # 1 for opencv techniques to make image look like a cartoon
    # 2 for canny edge detection to sort out edges (currently buggy as it filters out background a lot of the time)
    processingType = 1

    source = "VIDEO_NAME_HERE.mp4"

    cap = cv.VideoCapture(source)

    while True:
        ret, frame = cap.read()
        if processingType == 0:
            pass
        elif processingType == 1:
            frame = convertImage(frame)
        elif processingType == 2:
            frame = cv.Canny(frame, 0, 256)
        else:
            print("Pick a processing type between 0 and 2")
            break

        cv.imshow('frame', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


def convertImage(frame):
    grey_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    invert = cv.bitwise_not(grey_img)
    blur = cv.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv.bitwise_not(blur)
    sketch = cv.divide(grey_img, inverted_blur, scale=256.0)
    return sketch


while __name__ == "__main__":
    main()
    break
