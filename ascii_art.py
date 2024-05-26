import cv2

def normalize(arr):
    minimum = min(map(min, arr))
    maximum = max(map(max, arr))
    denom = maximum - minimum
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i, j] = ((arr[i, j] - minimum)/ denom)* 69
    return arr

def get_char(c):
    s = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    return s[c]

def main(): 
    img = cv2.imread("img3.png", cv2.IMREAD_GRAYSCALE) 
    file = open("img3.txt", "a")
    arr = normalize(img)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            file.write(get_char(arr[i,j]))
        file.write("\n")
    file.close()

if __name__ == "__main__":
    main()
