"""
Simple panorama stitching for FarmBot image coverage.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stitch multiple FarmBot images into a panorama")
    parser.add_argument(
        "images",
        nargs="+",
        help="Input image paths in the order they should be stitched.",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display the result in a window.",
    )
    parser.add_argument(
        "--output",
        default="stitched_panorama.jpg",
        help="Output panorama filename.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    image_paths = [Path(p) for p in args.images]
    imgs = []
    for p in image_paths:
        img = cv2.imread(str(p))
        if img is None:
            raise FileNotFoundError(f"Could not read image: {p}")
        imgs.append(cv2.resize(img, (700, 550)))

    if len(imgs) < 2:
        raise ValueError("Provide at least 2 images for stitching.")

    stitcher = cv2.Stitcher.create()
    status, stitched_image = stitcher.stitch(imgs)

    if status == cv2.Stitcher_OK:
        print("Your panorama is ready!!!")
        cv2.imwrite(args.output, stitched_image)
        if args.show:
            cv2.imshow("Final Result", stitched_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        raise RuntimeError(f"Stitching failed with OpenCV status code: {status}")


if __name__ == "__main__":
    main()
