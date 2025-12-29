from analyzer import parse_log_line, analyze_logs, write_report


LOG_FILE = "logs/server.log"

def main():
    log_entries = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                log_entries.append(parsed)

    error_messages, error_by_hour = analyze_logs(log_entries)
    write_report(error_messages, error_by_hour)

    print("Log analysis completed. Report saved to report.txt")

if __name__ == "__main__":
    main()
