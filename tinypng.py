import sys
import tinify

apiKey = "DJzDkcwYxF3PPSkY7g5TZwZdCyBMmcry"

mode = "none"
targetWidth = 0
targetHeight = 0


def main():
    # 校驗輸入參數
    if not checkInputArg():
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    tinify.key = apiKey
    print("processing... at" + file1)
    source = tinify.from_file(file1)
    if mode == "none":
        source.to_file(file2)
    else:
        print("處理模式： mode=" + mode + ", width=" + targetWidth + ", height=" + targetHeight)
        resized = source.resize(
            method=mode,
            width=int(targetWidth),
            height=int(targetHeight)
        )
        resized.to_file(file2)
    print("done... at" + file2)


def checkInputArg():
    if len(sys.argv) < 3:
        print('至少需帶入兩個參數 example: --> tinypng.py file1 file2')
        return False

    print("輸入位置：" + sys.argv[1])
    print("輸出位置：" + sys.argv[2])

    if (len(sys.argv) >= 5):
        global mode, targetWidth, targetHeight
        mode = sys.argv[3]
        targetWidth = sys.argv[4]
        targetHeight = sys.argv[5]
        print("處理模式： mode=" + mode + ", width=" + targetWidth + ", height=" + targetHeight)
    return True


main()
