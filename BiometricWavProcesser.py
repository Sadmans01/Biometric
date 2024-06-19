import wave
import numpy as np
import struct


# Step 1: Extract the header of a WAV file
def extract_wav_header(filename):
    with wave.open(filename, 'rb') as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)
    return params, frames


# Step 2: Perform a FFT on the data (FFT is used here for efficiency)
def perform_fft(frames, params):
    # Convert byte data to numpy array
    num_channels = params.nchannels
    sample_width = params.sampwidth
    frame_count = params.nframes
    data_type = {1: np.int8, 2: np.int16, 4: np.int32}[sample_width]
    samples = np.frombuffer(frames, dtype=data_type)
    if num_channels > 1:
        samples = samples.reshape((frame_count, num_channels))

    # Perform FFT
    fft_data = np.fft.fft(samples, axis=0)
    return fft_data


# Step 3: Modify the magnitude of the data
def modify_magnitude(fft_data, factor):
    magnitude = np.abs(fft_data)
    phase = np.angle(fft_data)
    modified_fft_data = magnitude * factor * np.exp(1j * phase)
    return modified_fft_data


# Step 4: Reverse IFFT on the data in little endian form
def perform_ifft(fft_data, params):
    ifft_data = np.fft.ifft(fft_data, axis=0).real
    ifft_data = ifft_data.astype({1: np.int8, 2: np.int16, 4: np.int32}[params.sampwidth])
    return ifft_data


# Step 5: Reconstruct the WAV based on new data and original header
def reconstruct_wav(output_filename, params, ifft_data):
    with wave.open(output_filename, 'wb') as wav_file:
        wav_file.setparams(params)
        if params.nchannels > 1:
            ifft_data = ifft_data.flatten()
        frames = ifft_data.tobytes()
        wav_file.writeframes(frames)


# New function to print the magnitude spectrum of the DFT data
def print_dft_magnitude(fft_data, num_points=1024):
    magnitude = np.abs(fft_data)
    for i in range(min(num_points, len(magnitude))):
        print(f'Frequency bin {i}: |S({i})| = {magnitude[i]}')


# New function to print the time-domain data obtained from the IDFT
def print_idft_data(ifft_data, num_points=1024):
    for i in range(min(num_points, len(ifft_data))):
        print(f'Time sample {i}: {ifft_data[i]}')


# Main process
def process_wav(input_filename, output_filename, magnitude_factor, num_points=1024):
    params, frames = extract_wav_header(input_filename)
    fft_data = perform_fft(frames, params)
    print_dft_magnitude(fft_data, num_points)  # Print DFT magnitude
    modified_fft_data = modify_magnitude(fft_data, magnitude_factor)
    ifft_data = perform_ifft(modified_fft_data, params)
    print_idft_data(ifft_data, num_points)  # Print IDFT time-domain data
    reconstruct_wav(output_filename, params, ifft_data)


# Example usage
input_wav = 'sample.wav' # Input wav file
output_wav = 'remake.wav'
magnitude_factor = 1  # Example modification factor
num_points_to_display = 24  # Number of DFT/IDFT points to display

process_wav(input_wav, output_wav, magnitude_factor, num_points_to_display)