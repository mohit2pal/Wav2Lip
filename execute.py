import os

# Change directory to Wav2Lip
os.chdir('Wav2Lip')

# Execute inference.py with the specified arguments
os.system('python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "../sample_data/input_vid.mp4" --audio "../sample_data/input_audio.wav" --pads 0 10 0 0 --resize_factor 1')