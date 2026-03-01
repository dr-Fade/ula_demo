import numpy as np
from signal_utils import rms

class ULA:
    def __init__(self, N: int, d: float | None = None):
        self.N = N

        if d is None:
            self.d = 1 / 2
        else:
            self.d = d


    def steer_signal(self, signal: np.ndarray, θ: float) -> np.ndarray:
        x = signal.reshape(1,-1)
        steering = self._get_steering(θ)
        return steering @ x


    def delay_and_sum(self, steered_signal: np.ndarray, θ: float):
        if steered_signal.shape[0] != self.N:
            raise Exception(f"invalid signal dimensions {steered_signal.shape}, expected ({self.N} x n)")

        steering = self._get_steering(θ).conj().T
        return (steering @ steered_signal).squeeze()


    def get_θ_scan(self, steered_signal: np.ndarray, n: int = 360) -> tuple[np.ndarray, np.ndarray]:
        if steered_signal.shape[0] != self.N:
            raise Exception(f"invalid signal dimensions {steered_signal.shape}, expected ({self.N} x n)")

        Θ = np.linspace(-np.pi, np.pi, n)
        p = np.array([
            rms(self.delay_and_sum(steered_signal, θ))
            for θ in Θ
        ])

        return (Θ, p)


    def music(self, steered_signal: np.ndarray, n_signals: int, n: int = 360) -> tuple[np.ndarray, np.ndarray]:
        R = np.cov(steered_signal)
        w, v = np.linalg.eig(R)
        eig_val_order = np.argsort(np.abs(w))
        v = v[:, eig_val_order]

        V = np.zeros((self.N, self.N - n_signals), dtype=np.complex64)
        for i in range(self.N - n_signals):
            V[:, i] = v[:, i]

        Θ = np.linspace(-1*np.pi, np.pi, n)
        results = []
        for θ in Θ:
            steering = self._get_steering(θ)
            metric = 1 / (steering.conj().T @ V @ V.conj().T @ steering)
            metric = np.abs(metric.squeeze())
            metric = 10*np.log10(metric)
            results.append(metric)

        results -= np.min(results)
        results /= np.max(results)

        return (Θ, np.array(results))


    def _get_steering(self, θ):
        return np.exp(2j * np.pi * self.d * np.arange(self.N) * np.sin(θ)).reshape(-1, 1)
