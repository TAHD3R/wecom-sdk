class SDKException(Exception):
    def __init__(self, errcode: int, message: str):
        """
        通用错误返回类，用于抛出请求错误时的异常
        - 若请求返回的errcode不为0，则抛出此异常

        @param errcode: 错误码
        @param message: 错误信息
        """
        self.errcode = str(errcode)
        self.message = message

    def __str__(self):
        return f"Error Occured: {self.errcode} - {self.message}"
