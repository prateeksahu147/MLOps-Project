import logging, os, sys
from datetime import datetime
from settings import *
#from exception import CustomException

LOG_FILE=f"{datetime.now().strftime(Datetime_M_D_Y_H_M_S)}.log"

log_path=os.path.join(BASE_DIR, 'logs', LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

"""if __name__ =="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info(f"Divide by Zero Error {CustomException(e,sys)}")
        raise CustomException(e,sys)

    if __name__ == "__main__":
        try:
            a = 1 / 0
        except Exception as e:
            logging.info("Error occued in ", CustomException(e, sys))
            raise CustomException(e, sys)"""