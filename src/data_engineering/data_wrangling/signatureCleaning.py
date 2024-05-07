import numpy as np
import math


class SignatureCleaning:

    def __init__(
        self,
        context_window: int = 5,
        signature_length: int = 30,
    ) -> None:

        self.context_window = context_window
        self.signature_length = signature_length

        self.rng = np.random.default_rng(1711)

    def __sliding_window(
        self,
        window_divider: int,
        context_window: int,
        video_frames: np.ndarray,
    ) -> np.ndarray:

        raw_context_signatures = []
        min_window = 0
        max_window = context_window
        missing_data = video_frames.shape[0] - window_divider * context_window

        if missing_data > 0:
            window_divider = window_divider + math.floor(missing_data / context_window)

        for it in range(context_window):
            raw_context_signatures.append([])

        for index in range(window_divider):
            context_frames = video_frames[min_window:max_window]

            for it, frame in enumerate(context_frames):
                raw_context_signatures[it].append(frame)

            min_window = max_window
            max_window = context_window + max_window

        raw_context_signatures = np.asarray(raw_context_signatures)

        return raw_context_signatures

    def signature_winnowing(self, video_frames: np.ndarray) -> np.ndarray:

        window_divider = math.floor(video_frames.shape[0] / self.context_window)

        if window_divider < self.signature_length:
            context_window = math.floor(video_frames.shape[0] / self.signature_length)

            window_divider = math.floor(video_frames.shape[0] / self.signature_length)

            context_signatures = self.__sliding_window(
                context_window=context_window,
                window_divider=self.signature_length,
                video_frames=video_frames,
            )

            return context_signatures
        else:
            context_signatures = self.__sliding_window(
                context_window=self.context_window,
                window_divider=window_divider,
                video_frames=video_frames,
            )

            return context_signatures

    def extract_signature_winnowing(
        self,
        context_signatures: np.ndarray,
    ) -> np.ndarray:

        signatures_extracted = []
        frames_delete = []

        frame_difference = context_signatures.shape[1] - self.signature_length

        try:
            for it in range(context_signatures.shape[0]):
                frames_delete.append(
                    self.rng.choice(
                        context_signatures.shape[1],
                        size=frame_difference,
                        replace=False,
                    )
                )

            frames_delete = np.sort(frames_delete)

            for index, signature in enumerate(context_signatures):
                signatures_extracted.append(
                    np.delete(arr=signature, obj=frames_delete[index], axis=0)
                )

            signatures_extracted = np.asarray(signatures_extracted)
            return signatures_extracted

        except ValueError:
            filled_size = context_signatures.shape

            filled = np.zeros(
                [
                    filled_size[0],
                    abs(frame_difference),
                    filled_size[2],
                    filled_size[3],
                    filled_size[4],
                ]
            )

            signatures_extracted = np.append(arr=context_signatures, values=filled, axis=1)

            return signatures_extracted
