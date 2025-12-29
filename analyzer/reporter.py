def generate_table(data, title):
    lines = [title, "-" * len(title)]
    for key, value in data.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)

def write_report(error_messages, error_by_hour, output_file="report.txt"):
    with open(output_file, "w") as file:
        file.write("LOG FILE ANALYSIS REPORT\n")
        file.write("=" * 25 + "\n\n")

        file.write("Top Error Messages\n")
        file.write("------------------\n")
        for msg, count in error_messages.most_common(5):
            file.write(f"{msg} -> {count}\n")

        file.write("\nErrors by Hour\n")
        file.write("--------------\n")
        for hour in sorted(error_by_hour):
            file.write(f"{hour}:00 - {error_by_hour[hour]} errors\n")
