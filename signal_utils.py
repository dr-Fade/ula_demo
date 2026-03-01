import numpy as np


def power(signal: np.ndarray) -> np.float64:
    n = signal.shape[-1]
    return np.sum(np.abs(signal**2)) / n


def rms(signal: np.ndarray) -> np.float64:
    return np.sqrt(power(signal))


def add_noise(signal: np.ndarray, snr: float):
    signal_power = np.sum(np.abs(np.fft.fft(signal))**2)
    noise_power = signal_power / snr

    noise = np.random.randn(len(signal))

    current_noise_power = np.sum(np.abs(np.fft.fft(noise))**2)

    noise = np.sqrt(noise_power) * noise / np.sqrt(current_noise_power)

    return noise + signal
