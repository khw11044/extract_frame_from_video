import os
import cv2
import glob
import argparse

parser = argparse.ArgumentParser(description="video_name")
parser.add_argument('--video_name', default='test_video', type=str,
                    help='videos or image files')
parser.add_argument('--frame', default=1, type=int,
                    help='fpn')
args = parser.parse_args()
dir=args.video_name + '/'

frame=args.frame

video_files = sorted(glob.glob(dir + "*.avi"))

print(video_files)

if not os.path.isdir('imageFrames'):
    os.makedirs('imageFrames')
    # os.makedirs('b_frame8')

for video in video_files:
    file_name = video.split('/')[-1]
    save_dir = 'imageFrames/' + file_name.split('.')[0]  # data/PoseVideos\2
    #another_dir = 'b_frame8/' + file_name.split('.')[0]  # data/PoseVideos\2
    video_name = save_dir.split('\\')[-1].split('/')[-1]
    print(save_dir)
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    #    os.makedirs(another_dir)

    vidcap = cv2.VideoCapture(video)
    
    count = 0
    while vidcap.isOpened():
        ret, image = vidcap.read()
        if not ret:
            break
        if int(vidcap.get(1)) % 1 == 0:
            print('Saved from number: ' + file_name + str(int(vidcap.get(1))))
            name = save_dir + '/' +video_name + '_{0:04d}.png'.format(count)
            # image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(name, image)
            count += 1

    vidcap.release()
