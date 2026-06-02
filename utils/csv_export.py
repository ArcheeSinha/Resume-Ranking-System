import csv


def export_to_csv(results, output_file):

    with open(
        output_file,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Rank", "Candidate", "Match Score"]
        )

        for rank, candidate in enumerate(
            results,
            start=1
        ):

            writer.writerow(
                [
                    rank,
                    candidate["candidate"],
                    candidate["score"]
                ]
            )