"""
YOLOv8 training script for tomato detection.
Based on the appendix notebook code from the thesis.
"""

from __future__ import annotations

import os
from pathlib import Path

from IPython.display import Image  # optional in notebook-style usage
from roboflow import Roboflow
from ultralytics import YOLO


HOME = Path.cwd()
DATASETS_DIR = HOME / "datasets"
DATASETS_DIR.mkdir(exist_ok=True)


def main() -> None:
    # Replace with your own Roboflow API key if you use the cloud dataset workflow.
    rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
    project = rf.workspace("Farmbot-mwqke").project("tomato-detection-dp74n")
    dataset = project.version(0).download("yolov8")

    model = YOLO("yolov8s.pt")
    model.train(data=f"{dataset.location}/data.yaml", epochs=10, imgsz=800, plots=True)

    # Validation / prediction examples
    # model.val(data=f"{dataset.location}/data.yaml")
    # model.predict(source=f"{dataset.location}/test/images", save=True)


if __name__ == "__main__":
    main()
