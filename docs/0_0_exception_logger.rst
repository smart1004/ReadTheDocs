

77     def exception(self, message, exc_info=None, *args): 
78         """Send a stack trace after exception""" 
79         self.logger.log(LOG_ERR, message, exc_info=(exc_info or sys.exc_info()), *args) 



https://realpython.com/python-testing/
