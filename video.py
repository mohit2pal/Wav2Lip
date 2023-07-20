import os
import shutil
from base64 import b64encode
import moviepy.editor as mp

def get_video_resolution(video_path):
    """
    Function to get the resolution of a video
    
    Args:
    video_path (str): The path to the video file
    
    Returns:
    tuple: A tuple containing the width and height of the video
    """
    import cv2
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return (width, height)

def resize_video(video_path, new_resolution):
    """
    Function to resize a video
    
    Args:
    video_path (str): The path to the video file
    new_resolution (tuple): A tuple containing the new width and height of the video
    
    Returns:
    None
    """
    import cv2
    video = cv2.VideoCapture(video_path)
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
    fps = video.get(cv2.CAP_PROP_FPS)
    width, height = new_resolution
    output_path = os.path.splitext(video_path)[0] + '_720p.mp4'
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    while True:
        success, frame = video.read()
        if not success:
            break
        resized_frame = cv2.resize(frame, new_resolution)
        writer.write(resized_frame)
    video.release()
    writer.release()
    
PATH_TO_YOUR_VIDEO = 'C:/Github/Wav2Lip/test.mp4'

video_duration = mp.VideoFileClip(PATH_TO_YOUR_VIDEO).duration
if video_duration > 60:
    print("WARNING: Video duration exceeds 60 seconds. Please upload a shorter video.")
    raise SystemExit(0)

video_resolution = get_video_resolution(PATH_TO_YOUR_VIDEO)
print(f"Video resolution: {video_resolution}")
if video_resolution[0] >= 480 or video_resolution[1] >= 480:
    print("Resizing video to 720p...")
    os.system(f"ffmpeg -i {PATH_TO_YOUR_VIDEO} -vf scale=1280:720 C:/Github/Wav2Lip/sample_data/input_vid.mp4")
    PATH_TO_YOUR_VIDEO = "input_vid.mp4"
    print("Video resized to 720p")
else:
    print("No resizing needed")