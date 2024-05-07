import cv2
import numpy as np
import time

class VideoSignatureUtilities:
    def __init__(self, resolution: int = 144, color: int = 0) -> None:

        aspect_ratio = 16 / 9

        colors = {
            0: cv2.COLOR_BGR2RGB,
            1: cv2.COLOR_BGR2GRAY,
        }

        self.resolution_h = int(resolution)
        self.resolution_w = int(aspect_ratio * resolution)
        self.color = colors[color]

    def __resize_signature_video(self, frame: np.ndarray) -> np.ndarray:
        new_frame = cv2.resize(
            src=frame,
            dsize=(self.resolution_w, self.resolution_h),
            interpolation=cv2.INTER_AREA,
        )

        return new_frame

    def __color_change(self, frame: np.ndarray) -> np.ndarray:
        new_frame = cv2.cvtColor(src=frame, code=self.color)

        return new_frame

    def upload_signature_video(self, signature_path: str) -> np.ndarray:

        data_frames = []
        cap = cv2.VideoCapture(signature_path)

        if not cap.isOpened():
            exit()

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            frame = self.__color_change(frame=frame)
            frame = self.__resize_signature_video(frame=frame)

            # cv2.imshow("Video", frame)
            # if cv2.waitKey(1) == ord("q"):
            #     break

            data_frames.append(frame)

        cap.release()
        cv2.destroyAllWindows()

        data_frames = np.asarray(data_frames)

        return data_frames
    
    def view_signature(self, data_frames: np.ndarray) -> None:
        for frame in data_frames:
            time.sleep(0.04)
            cv2.imshow('Signature', frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cv2.destroyAllWindows()
