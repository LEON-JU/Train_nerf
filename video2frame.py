import os
import cv2
def extract_images(video_path, output_folder):
    # 获取视频文件名
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # 新建文件夹
    output_path = os.path.join(output_folder)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # 打开视频
    cap = cv2.VideoCapture(video_path)
    # 设置帧间隔
    frame_interval = int(5)
    # 逐帧提取并保存满足间隔要求的帧
    count = 0
    num = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(count)
            if count % frame_interval == 0:
                # 图像名称00001.jpg,00002.jpg,00003.jpg...,且新建一个num用于记录当前保存的图片数量
                image_name = os.path.join(output_path, '{:05d}.jpg'.format(num))
                cv2.imwrite(image_name, frame)
                num += 1
            count += 1
        else:
            break
    cap.release()

if __name__ == '__main__':
    video_path = './rock.mp4'  # 视频文件路径
    output_folder = './rock/input'  # 输出文件夹路径
    extract_images(video_path, output_folder)

