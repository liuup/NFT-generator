import cv2 as cv
import numpy as np
import sys

def generator(argv):
    inputfile = str(argv[0])
    resolution = int(argv[1])

    # 读取原始图像
    ori = cv.imread(inputfile, cv.IMREAD_COLOR)
    # cv.imshow("input", ori)

    # 缩放到32*32
    img_resize = cv.resize(ori, (64, 64))
    # cv.imshow("final", img_resize)

    # 创建空白图像
    img_blank = np.zeros((resolution, resolution, 3), np.uint8)

    # resize后的图片高和宽
    h_resize, w_resize, _ = img_resize.shape

    #空白图像的高和宽
    h_blank, w_blank, _ = img_blank.shape

    # 图像分辨率相差的倍数， 作为步长
    ratio = int(h_blank / h_resize)

    for i_resize in range(0, h_resize):
        for j_resize in range(0,  w_resize):
            # 当前读取到的像素
            pixel = img_resize[i_resize, j_resize]
            # 对空白图像进行赋值
            for i_blank in range(i_resize * ratio, (i_resize + 1) * ratio):
                for j_blank in range(j_resize * ratio, (j_resize + 1) * ratio):
                    img_blank[i_blank, j_blank] = pixel

    # 保存生成后的文件
    cv.imwrite("./output.png", img_blank)

    #结束喽
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    generator(sys.argv[1:])
