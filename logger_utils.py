
from datetime import datetime
from pathlib import Path


def validate_sample(sample):
    """Accept non-empty sample text only."""
    return isinstance(sample, str) and bool(sample.strip())


def format_record(sample, timestamp=None):
    """Format one safe demo record."""
    if not validate_sample(sample):
        raise ValueError("Sample text cannot be empty.")

    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return (
        f"Time: {timestamp}\n"
        f"Sample text: {sample}\n"
        f"{'-' * 40}\n"
    )


def append_record(log_path, sample, timestamp=None):
    """Append a valid sample record to a local file."""
    record = format_record(sample, timestamp)
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        file.write(record)


def read_log(log_path):
    """Read the log, or return an empty string if absent."""
    path = Path(log_path)

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8")


def delete_log(log_path):
    """Delete the log if it exists."""
    path = Path(log_path)

    if path.exists():
        path.unlink()
