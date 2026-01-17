import sys
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        self.LineNo = exc_tb.tb_lineno
        self.FileName = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error Occured in File [{0}] line number [{1}] due to the cause : [{2}]".format(self.FileName,self.LineNo,self.error_message)
    
# if __name__ == "__main__":
#     try :
#         a = 1/0
#         print("This will not be printed")
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)