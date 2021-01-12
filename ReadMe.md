command：

diff file1 file2 #對比內容差異

tinypng file1 file2 [mode] [width] [height] 
 - mode 有幾種方式：
    1. scale 按比例缩小图片。您必须提供目标width或height，不能同时提供两者。缩小后的图片会有确定的宽度或者高度。
    2. fit 按比例缩小图片，使其适合（fit）给定的尺寸。你必须同时提供width和height。缩小后的图像不会超过这些尺寸中的任何一个。
    3. cover 按比例缩小图片，如有必要裁切图片。结果具有准确的给定尺寸。 图片中哪个部分将被裁切是自动决定的。智能算法确定图像中最重要的区域。
 