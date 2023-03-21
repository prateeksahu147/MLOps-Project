import os
import sys
from datetime import datetime
from src.exception import CustomException
from src.logger import logging
from src.models.data_ingestion.PdfImageInfo import PdfImageInfo, ImageInfo
from dataclasses import dataclass
from pdf2image import convert_from_path, convert_from_bytes
from settings import BASE_DIR, Datetime_M_D_Y_H_M_S

# Constants and Paths
DOT_PDF = 'pdf'



@dataclass
class PdfToImageConfig:
    pdf_dir_path: str = os.path.join(BASE_DIR, 'data', 'pdf')
    image_dir_path: str = os.path.join(BASE_DIR, 'data', "image")
    csv_dir_path: str = os.path.join(BASE_DIR, 'data', "csv")

class PdfToImage:
    def __init__(self):
        self.ingestion_config = PdfToImageConfig()

    def convert_pdf_to_image(self, pdf_file: str):

        """
        #https://www.dennis-schneider.com/blog/how-to-extract-information-from-a-pdf-containing-images-using-python-tesseract-on-mac-os/#:~:text=pdf2image%20is%20a%20Python%20library,open%2Dsource%20library%20for%20Python.
        # img = convert_from_path(pdf)
        # print(img[0].save('output.jpg', 'jpeg'))
        """

        pdf_info = PdfImageInfo()
        try:
            splited = pdf_file.split('.')
            if splited[-1] == DOT_PDF:
                with open(os.path.join(self.ingestion_config.pdf_dir_path, pdf_file), 'rb') as p:
                    images = convert_from_bytes(p.read())
                    pdf_info.name = pdf_file
                    pdf_info.noOfPages = len(images)
                    pdf_info.imageObjList = images

                if pdf_info is not None:
                    return pdf_info

        except Exception as e:
            msg = CustomException(e, sys)
            logging.info(msg)
            raise CustomException(e, sys)


    def save_image(self, pdf_image_info:PdfImageInfo):
        pdf_image_info.ImageList = list()
        try:
            split_pdf_name=pdf_image_info.name.split(".")
            split_pdf_name.pop()
            img_dir = split_pdf_name[0]+"_"+f"{datetime.now().strftime(Datetime_M_D_Y_H_M_S)}"
            path = os.path.join(self.ingestion_config.image_dir_path, img_dir)
            os.makedirs(path, exist_ok=True)
            if pdf_image_info is not None:
                for idx, img in enumerate(pdf_image_info.imageObjList):
                    img_obj=ImageInfo()
                    img_obj.Name=split_pdf_name[0] + "_" + f"{idx}" + ".jpg"
                    img.save(os.path.join(self.ingestion_config.image_dir_path, img_dir, img_obj.Name), 'jpeg')
                    img_obj.Width, img_obj.Height = img.size
                    img_obj.IsSaved = True
                    pdf_image_info.ImageList.append(img_obj)
            return pdf_image_info

        except Exception as e:
            msg=CustomException(e, sys)
            logging.info(msg)
            raise CustomException(e, sys)


