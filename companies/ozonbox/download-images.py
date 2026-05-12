import os
import sys
import requests
from urllib.parse import urlparse
import re

sys.stdout.reconfigure(encoding='utf-8')

IMAGES_DIR = "E:\\Рабочий стол\\ozonbox\\ИИ асистент Ozonbox\\companies\\ozonbox\\wiki\\assets\\images"

image_urls = [
    # UV Barrier
    "https://optim.tildacdn.com/stor6630-3465-4837-b035-366632366161/-/format/webp/5ad54b231b20a07fcbe180723f5bb412.png.webp",
    # UV REC
    "https://optim.tildacdn.com/stor3761-3239-4138-b363-346236346333/-/format/webp/997fa6303fdadfe55418871b9ec35c9c.png.webp",
    # Air Max
    "https://thb.tildacdn.com/tild3665-3763-4436-b936-373139326366/-/format/webp/image.png.webp",
    # De Oxi
    "https://static.tildacdn.com/tild3161-6364-4230-b434-633737646664/image_111_1.jpg",
    # WS / MWS
    "https://static.tildacdn.com/tild3234-3736-4937-b461-316537333865/photo_2026-03-19_18-.jpg",
    # Oz Control
    "https://optim.tildacdn.com/stor6564-3535-4938-b137-336261663030/-/format/webp/13af885888eaf86e306e2a4d2e9a90f0.png.webp",
    # Схема маршрутов риска
    "https://static.tildacdn.com/tild3335-3936-4234-b830-666531323661/kandinsky-download-1.png",
    # Управляемый санитарный контур
    "https://static.tildacdn.com/tild6539-3232-4465-b765-383238343236/image_110.jpg",
    # Шкафы
    "https://static.tildacdn.com/tild3665-3466-4537-b834-616134396234/Frame_107.jpg",
    # Воздушный контур
    "https://static.tildacdn.com/tild6566-3833-4264-b063-646435353961/Frame_108_2.jpg",
    # Ozonbox Air (устройство)
    "https://thb.tildacdn.com/tild6339-3236-4330-b436-323737373938/-/resize/20x/photo.jpg",
    # Локальные санитарные барьеры
    "https://static.tildacdn.com/tild3564-3031-4932-a136-383036636337/XN1plG2iuCRZXi8x283o.jpg",
    # Ozonbox в работе
    "https://static.tildacdn.com/tild3733-3161-4835-b933-616435623230/ChatGPT_Image_19__20.png",
    # Управляемость
    "https://static.tildacdn.com/tild6566-6331-4764-a233-383134643132/image.png",
    # Схема санитарной системы
    "https://static.tildacdn.com/tild3964-6137-4666-b437-383036313163/ChatGPT_Image_19__20.png",
]

def download_image(url, save_dir):
    """Download a single image"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename or '.' not in filename:
            filename = f"image_{hash(url)}.jpg"

        filepath = os.path.join(save_dir, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"[OK] {filename}")
        return True
    except Exception as e:
        print(f"[FAIL] ({url}): {e}")
        return False

def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    print(f"Directory: {IMAGES_DIR}\n")

    success = 0
    failed = 0

    for url in image_urls:
        if download_image(url, IMAGES_DIR):
            success += 1
        else:
            failed += 1

    print(f"\n--- Result ---")
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print(f"Total: {success + failed}")

if __name__ == "__main__":
    main()