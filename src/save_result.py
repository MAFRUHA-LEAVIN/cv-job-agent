from datetime import datetime
from pathlib import Path

def save_analysis_result(result_text):
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = output_dir / f"analysis_{timestamp}.txt"

    file_path.write_text(result_text, encoding="utf-8")

    return file_path