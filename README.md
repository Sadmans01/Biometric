# WAV File Processing with FFT and IFFT

This Python script processes a WAV audio file using Fast Fourier Transform (FFT) and Inverse Fast Fourier Transform (IFFT). It allows modification of the magnitude of the frequency domain data and reconstructs the modified audio file.

## Features

- Extracts header and data from a WAV file.
- Performs FFT to convert time-domain data to frequency-domain data.
- Modifies the magnitude of the FFT data.
- Performs IFFT to convert frequency-domain data back to time-domain data.
- Reconstructs a new WAV file with the modified data.
- Prints the magnitude spectrum of the DFT data and the time-domain data obtained from the IDFT.

## Prerequisites

- Python 3.x
- NumPy
- `wave` module (standard library)

## Usage

1. **Extract the header and data from a WAV file**
2. **Perform FFT on the data**
3. **Modify the magnitude of the FFT data**
4. **Perform IFFT to get the time-domain data**
5. **Reconstruct the WAV file with modified data**
6. **Print the DFT magnitude and IDFT time-domain data**
