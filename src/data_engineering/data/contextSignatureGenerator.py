from data_engineering.etl.rawSignatureExtractor import RawSignatureExtractor

raw_signature_extractor = RawSignatureExtractor()

if __name__ == "__main__":
    metadata_path = "data/raw/10_words_3_people/10_words_3_people.csv"
    data_path = "data/raw/10_words_3_people/raw_data"

    save_path_context = "data/processed/10_words_3_people/context_signatures"
    save_path_sample = "data/processed/10_words_3_people/sample_signatures"

    print("DEBUG: inicio raw_signature_extractor")
    context_signatures, signatures_sample = raw_signature_extractor.extract_signatures(
        metadata_path=metadata_path,
        data_path=data_path,
    )

    print("DEBUG: Guardando raw_signature_context")
    raw_signature_extractor.save_signatures(
        data_signatures=context_signatures,
        save_path=save_path_context,
        view=False
    )

    print("DEBUG: Guardando raw_signature_sample")
    raw_signature_extractor.save_signatures(
        data_signatures=signatures_sample,
        save_path=save_path_sample,
        view=False
    )

    print("DEBUG: Finalización raw_signature_extractor")