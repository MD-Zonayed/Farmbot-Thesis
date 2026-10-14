"""
FarmBot object detection demo for tomato ripeness / disease and weed detection.

Usage:
  python farmbot_detection.py --mode tomato --model models/tomato.pt --source 0
  python farmbot_detection.py --mode weed   --model models/weed.pt   --source 0
"""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="FarmBot tomato/weed detection")
    parser.add_argument(
        "--mode",
        choices=["tomato", "weed"],
        required=True,
        help="Choose which model to run.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="",
        help="Path to YOLO model .pt file. If omitted, a default based on mode is used.",
    )
    parser.add_argument(
        "--source",
        type=str,
        default="0",
        help="Video source. Use 0 for webcam, or path to image/video.",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.10,
        help="Confidence threshold.",
    )
    return parser.parse_args()


def resolve_model_path(mode: str, model_arg: str) -> str:
    if model_arg:
        return model_arg
    return "models/tomato.pt" if mode == "tomato" else "models/weed.pt"


def main() -> None:
    args = parse_args()
    model_path = resolve_model_path(args.mode, args.model)

    if not Path(model_path).exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}. "
            "Place your trained YOLO weights in the models/ folder or pass --model."
        )

    model = YOLO(model_path)
    model.predict(source=args.source, show=True, conf=args.conf)

    # Keep window active until closed.
    while True:
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
