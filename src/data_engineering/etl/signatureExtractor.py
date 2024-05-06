import pandas as pd
import os

from utilities.videoSignatureUtilities import VideoSignatureUtilities
from data_engineering.data_wrangling.signatureCleaning import SignatureCleaning


class SignatureExtractor:
    def __init__(self) -> None:
        self.video_signature = VideoSignatureUtilities()
        self.clear = SignatureCleaning()

    def read_metadata(self, metadata_path: str, data_path: str) -> list:
        signature = []

        metadata_signature = pd.read_csv(
            filepath_or_buffer=metadata_path,
            usecols=["ID", "FIRMA"],
        )

        for row in metadata_signature.itertuples(index=False, name=None):
            signature_path = os.path.join(data_path, row[0])
            signature.append([signature_path, row[1]])

        return signature

    def extract_signatures(self, metadata_path: str, data_path: str) -> None:

        metadata = self.read_metadata(
            metadata_path=metadata_path,
            data_path=data_path,
        )

        videos = self.video_signature.upload_signature_video(
            signature_path=metadata[0][0]
        )

        print(videos.shape)
        vv = self.clear.signature_winnowing(videos)

        print(vv.shape)


a = SignatureExtractor()
b = a.extract_signatures(
    metadata_path="data/raw/10_words_3_people/000_10_words_3_people.csv",
    data_path="data/raw/10_words_3_people/raw_data/",
)
