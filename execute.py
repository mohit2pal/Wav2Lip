#  this script is a simple way to execute the Wav2Lip algorithm on a specified 
#  input video and audio file. By changing the working directory to the Wav2Lip directory 
#  and executing the inference.py script with the appropriate arguments, users can generate 
#  realistic lip movements from an audio signal.

import os

# Change directory to Wav2Lip
os.chdir('Wav2Lip')

# Execute inference.py with the specified arguments
os.system('python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "../sample_data/input_vid.mp4" --audio "../sample_data/input_audio.wav" --pads 0 10 0 0 --resize_factor 1')