import pandas as pd
import numpy as np
import os

from utilities.videoSignatureUtilities import VideoSignatureUtilities
from data_engineering.data_wrangling.signatureCleaning import SignatureCleaning


class RawSignatureExtractor:
    def __init__(self) -> None:
        self.video_signature = VideoSignatureUtilities()
        self.clean_signature = SignatureCleaning()

    def __read_metadata(self, metadata_path: str, data_path: str) -> list:
        signature = []

        metadata_signature = pd.read_csv(
            filepath_or_buffer=metadata_path,
            usecols=["ID", "FIRMA"],
        )

        for row in metadata_signature.itertuples(index=False, name=None):
            signature_path = os.path.join(data_path, row[0])
            signature.append([signature_path, row[1]])

        return signature

    def save_signatures(
        self,
        data_signatures: list,
        save_path: str,
        view: bool = False,
    ):

        for it, signatures in enumerate(data_signatures):
            for index, signature in enumerate(signatures[1]):
                save_signatures = {
                    "Firma": signatures[0],
                    "Data": signature,
                }

                name_file = str(it) + str(index) + "_" + signatures[0] + ".npy"
                name_path = os.path.join(save_path, name_file)
                np.save(name_path, save_signatures)  # type: ignore

                if view:
                    self.video_signature.view_signature(data_frames=signature)

    # def load_signatur(self):
    #     new_dict = np.load("data/processed/10_words_3_people/context_signatures/00_BUENOS_DIAS.npy", allow_pickle=True).tolist()

    #     print(new_dict['Firma'])
    #     pass

    def extract_signatures(self, metadata_path: str, data_path: str) -> tuple:
        context_signatures = []
        signatures_extracted = []

        metadata = self.__read_metadata(
            metadata_path=metadata_path,
            data_path=data_path,
        )

        for m in metadata:
            data_frames = self.video_signature.upload_signature_video(
                signature_path=m[0]
            )

            data_frames_context = self.clean_signature.signature_winnowing(
                video_frames=data_frames
            )

            data_frames_sample = self.clean_signature.extract_signature_winnowing(
                context_signatures=data_frames_context
            )

            context_signatures.append([m[1], data_frames_context])
            signatures_extracted.append([m[1], data_frames_sample])
        
        return context_signatures, signatures_extracted
