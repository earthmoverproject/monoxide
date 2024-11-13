from PIL import Image
from multiprocessing import Pool
import os
import numpy as np


def main() -> None:
    imageNames = np.array(
        [str(path) for path in os.listdir("src/images")]
    )  # Gets image paths and adds appends them to a numpy array
    with Pool() as pool:
        pool.map(processImage, imageNames)


def processImage(imageName: str) -> None:
    imageContents = Image.open(f"src/images/{imageName}").convert("RGB")
    noiseImage(imageContents)


def noiseImage(imageContents) -> None:
    height, width = imageContents.size
    percentageOpacity: int = 10  # Percentage opacity of the mask
    opacityOfImageMask: int = int(
        float((percentageOpacity / 100) * 255)
    )  # Converting percentage to RGB value
    pixelArray = (
        np.random.rand(width, height, 3) * 255
    )  # Creates a mask of random colours
    imageMask = Image.fromarray(pixelArray.astype("uint8")).convert("RGBA")
    imageMask.putalpha(opacityOfImageMask)
    imageContents.paste(imageMask, (0, 0), mask=imageMask)
    imageContents.show()


def randomiseMetaData() -> None:
    pass


if __name__ == "__main__":
    main()
