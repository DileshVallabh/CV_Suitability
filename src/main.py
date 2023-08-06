import sys
import File_Processor
import Text_Processor


def main() -> int:

    args: list[str] = sys.argv[1:]

    if len(args) != 2:
        print("Usage: python main.py <curriculum_vitae.pdf> <job_description.txt>")
        return 1

    cv_file: str = args[0]
    job_file: str = args[1]

    cv: str = File_Processor.pdf_to_string(cv_file)
    job: str = File_Processor.text_to_string(job_file)

    cv_processed = Text_Processor.clean_stop_words(cv)
    job_processed = Text_Processor.clean_stop_words(job)

    # Experimenting with different scoring methods.

    similarity: float = Text_Processor.similarity(
        cv_processed, job_processed
    )

    hash_score: float = Text_Processor.hash_score(
        cv_processed, job_processed
    )

    difference_score: float = Text_Processor.difference_score(
        cv_processed, job_processed
    )

    print(f"NLP Similarity: {similarity}")
    print(f"Hash Score: {hash_score}")
    print(f"Difference Score: {difference_score}")

    difference = Text_Processor.difference(cv_processed, job_processed)
    print(difference)

    return 0


if __name__ == "__main__":
    exit_status: int = main()
    sys.exit(exit_status)
