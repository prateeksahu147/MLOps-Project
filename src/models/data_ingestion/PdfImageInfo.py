from typing import List

class ImageInfo:
    Name  : str
    IsSaved : bool
    ImageDirectory :str
    Width : float
    Height :  float


class PdfImageInfo:
    name : str
    size : float
    noOfPages : int
    imageObjList : List
    IsAllImagesSaved : bool
    ImageList : List[ImageInfo]
