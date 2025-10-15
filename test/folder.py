import os
from pathlib import Path

def create_test_folder():
    base = Path(__file__).parent / "test_files"
    base.mkdir(exist_ok=True)

    samples = {
        "photo1.jpg": "image file",
        "photo2.png": "another image",
        "report.docx": "document",
        "slides.pptx": "presentation",
        "music.mp3": "audio file",
        "video.mp4": "movie file",
        "archive.zip": "compressed archive",
        "notes.txt": "text notes",
    }

    for name, content in samples.items():
        (base / name).write_text(content)

    print(f"테스트용 폴더 생성 완료: {base}")
    print("포함된 파일:")
    for f in samples:
        print("  └─", f)

if __name__ == "__main__":
    create_test_folder()
