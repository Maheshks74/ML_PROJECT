import sys
from src.logger import logging

def error_msg_detail(error, error_detail: sys):
    _, _, exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_msg = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exe_tb.tb_lineno, str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        self.error_msg = error_msg_detail(error, error_detail=error_detail)
        super().__init__(self.error_msg)   # initialize Exception with the message

    def __str__(self):
        return self.error_msg


