# this command is used to download a pre-trained model checkpoint file for the Wav2Lip algorithm. 
# By downloading the checkpoint file, users can use the pre-trained model to generate realistic 
# lip movements from an audio signal without having to train the model from scratch.

import os

# Remove the sample_data directory
os.system('rmdir /s /content/sample_data')

# Create a new sample_data directory
os.system('mkdir /content/sample_data')

# Clone the Wav2Lip repository
os.system('git clone https://github.com/justinjohn0306/Wav2Lip')

# Download the wav2lip_gan.pth checkpoint file
os.system('wget "https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA" -O "Wav2Lip/checkpoints/wav2lip_gan.pth"')

# Install the ghc package
os.system('pip install https://raw.githubusercontent.com/AwaleSajil/ghc/master/ghc-1.0-py3-none-any.whl')

# Install the requirements for Wav2Lip
os.chdir('Wav2Lip')
os.system('pip install -r requirements.txt')

# Download the s3fd.pth file
os.system('wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "face_detection/detection/sfd/s3fd.pth"')

# Install the ffmpeg-python package
os.system('pip install ffmpeg-python')