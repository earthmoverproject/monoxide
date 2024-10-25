# from glaze_cloak import Glaze
from PIL import Image
from multiprocessing import Pool
import os
import numpy as np


def main() -> None:
    imageNames = np.array(
        list(os.listdir("src/images"))
    )  # Gets image paths and adds appends them to a numpy array
    pool = Pool()
    pool.map(processImage, imageNames)


def processImage(imageName: str) -> None:
    imageContents = Image.open(f"src/images/{imageName}").convert("RGB")
    imageContents.show()


def glazeImage() -> None:
    pass
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    # projectRootPath = os.getcwd()


def randomiseMetaData() -> None:
    pass


if __name__ == "__main__":
    main()
