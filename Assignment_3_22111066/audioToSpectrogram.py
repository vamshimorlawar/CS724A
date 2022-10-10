import os
import librosa
import librosa.display
import IPython.display as ipd
import numpy as np
import matplotlib.pyplot as plt

# Loading audio files with Librosa
scale_file = "./audio.wav"


ipd.Audio(scale_file)

# load audio files with librosa
scale, sr = librosa.load(scale_file)

# Extracting Short-Time Fourier Transform
FRAME_SIZE = 2048
HOP_SIZE = 512

S_scale = librosa.stft(scale, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
print(S_scale.shape)


print(type(S_scale[0][0]))


Y_scale = np.abs(S_scale) ** 2
print(Y_scale.shape)

print(type(Y_scale[0][0]))


# Visualizing the spectrogram
def plot_spectrogram(Y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y, 
                             sr=sr, 
                             hop_length=hop_length, 
                             x_axis="time", 
                             y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.show()


plot_spectrogram(Y_scale, sr, HOP_SIZE)

# Log-Amplitude Spectrogram
Y_log_scale = librosa.power_to_db(Y_scale)
plot_spectrogram(Y_log_scale, sr, HOP_SIZE)

# Log-Frequency Spectrogram
plot_spectrogram(Y_log_scale, sr, HOP_SIZE, y_axis="log")