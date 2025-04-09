import sys
import traceback
from src.logger import logging
from datetime import datetime
import os


# Error handling
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_msg = f"Error occurred in Python script: [{file_name}] at line [{line_number}]: {str(error)}"
    return error_msg

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# Triggering and logging exception
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Exception occurred")
        raise CustomException(e, sys)
