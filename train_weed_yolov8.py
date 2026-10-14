"""
YOLOv8 training script for weed detection.
Based on the appendix notebook code from the thesis.
"""

from __future__ import annotations

from pathlib import Path

from roboflow import Roboflow
from ultralytics import YOLO


HOME = Path.cwd()
DATASETS_DIR = HOME / "datasets"
DATASETS_DIR.mkdir(exist_ok=True)


def main() -> None:
    # Replace with your own Roboflow API key if you use the cloud dataset workflow.
    rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
    project = rf.workspace("Farmbot-mwqke").project("weed-detection-txujb")
    dataset = project.version(1).download("yolov8")

    model = YOLO("yolov8s.pt")
    model.train(data=f"{dataset.location}/data.yaml", epochs=10, imgsz=800, plots=True)

    # Validation / prediction examples
    # model.val(data=f"{dataset.location}/data.yaml")
    # model.predict(source=f"{dataset.location}/test/images", save=True)


if __name__ == "__main__":
    main()
