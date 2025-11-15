# Car-Detector

Car-Detector is a simple Python application that uses a custom YOLO model to detect cars in images, videos, or webcam feed. It uses a local `best.pt` custom model file and a minimal interface in `main.py` to choose between image, video, or camera input.

Key features

- Detect cars in a single image and display bounding boxes and labels
- Run detection on video files or live webcam feed
- Easy to configure model path and input file paths from `main.py`

Table of contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Setup and usage](#setup-and-usage)
- [How it works](#how-it-works)
- [Switching model versions (YOLOv5 ↔ YOLOv8)](#switching-model-versions-yolov5--yolov8)
- [Troubleshooting and tips](#troubleshooting-and-tips)
- [Contact](#contact)

---

## Requirements

- Python 3.8+ (recommended)
- See `requirements.txt` — main dependencies include `torch`, `opencv-python`, `ultralytics`/YOLO support and `numpy`.

Install all Python dependencies with:

```powershell
pip install -r requirements.txt
```

Note: Depending on your environment, you may want to install a GPU-enabled version of PyTorch. See https://pytorch.org/get-started/locally/

---

## Installation

1. Clone or copy this repository into a folder on your computer.
2. Ensure `best.pt` (your trained/custom YOLO model) is in the same folder as `main.py`.
3. Install dependencies (see command above).

---

## Setup and usage

1. Open `main.py` and check the `path` variable. By default it looks for `best.pt` in the same folder:

```python
path = "best.pt"
```

2. Set your input image or video path inside `main.py` if using the image or video option. By default the example code uses `image.jpg` and a sample video file name; update those file names or paths to your own files.
3. Run the script:

```powershell
python main.py
```

4. Follow interactive prompts in the console:

- Enter `1` for image input — program will open `image.jpg` and show detection results in a new window
- Enter `2` for video input — configure the filename inside `main.py` then the video will play with detections overlaid
- Enter any other number (e.g., `3`) for live webcam input — press `q` to quit the webcam
- Enter `0` to exit the program

Example — run detection on an image

1. Put `image.jpg` into the project folder (or set a different filename in the `image()` function).
2. Run `python main.py` and type `1` then Enter.

---

## How it works

- `main.py` loads a custom model with:

```python
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)
```

This uses Ultralytics' YOLOv5 repository via `torch.hub` to load a `custom` model saved in `best.pt`.

- For each frame (image/video/webcam), the script calls:

```python
results = model(frame_or_image)
frame_with_detections = np.squeeze(results.render())
```

`results.render()` returns a list of numpy images with bounding boxes drawn; the script uses `cv.imshow` to display the output.

---

## Switching model versions (YOLOv5 ↔ YOLOv8)

The current `main.py` uses `torch.hub` to fetch a YOLOv5 repository. If your `best.pt` is a YOLOv8 model (Ultralytics YOLOv8), you can use the `ultralytics` package API instead and call:

```python
from ultralytics import YOLO
# load YOLOv8 model
model = YOLO('best.pt')
results = model(frame)
img = results[0].plot()
```

If you prefer to keep the existing `main.py` structure and `best.pt` was exported from YOLOv8, the easiest route is to convert or re-export a YOLOv5-compatible `.pt` or adapt the code to the `ultralytics` API.

---

## Troubleshooting and tips

- If `torch.hub` fails to download the YOLO repository, make sure you have an active internet connection (the original repo is fetched from GitHub).
- If the model does not load: confirm `best.pt` is a valid YOLO model, in the expected format, and the `path` is correct.
- For performance: if you have a CUDA GPU and installed GPU PyTorch, it will run much faster. Use `torch.cuda.is_available()` to check.
- If OpenCV windows do not appear: on some systems you need to call `cv.waitKey(0)` properly or set the correct environment for GUI display (e.g., run locally, not via remote terminal that lacks GUI).

---

## Notes and suggestions

- To improve usability, you could extend `main.py` to accept command line arguments (e.g., with `argparse`) instead of using input() prompts.
- If you want to save output images, call `cv.imwrite('output.jpg', img)` after `results.render()`.
- For batch inference on many images, create a function to loop over files in a folder and save output results.

---

## Contact

Developer: Jatin Kevlani

- Email: jatinkevlani01@gmail.com
- LinkedIn: jatinkevlani

If you want the README adapted to use YOLOv8 explicitly or a GPU-ready setup, tell me which model version you used and I can update the instructions accordingly.
