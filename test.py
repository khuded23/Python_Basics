import logging

#create a logger variable
logger = logging.getLogger(__name__)
#set logging level
logger.setLevel(logging.INFO)

#we need to formatter for logging format
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

#for logfile , we need a file handler variable
file_handler = logging.FileHandler('sample.log')
#add formatter to file_handler
file_handler.setFormatter(formatter)
#now we created a file-handler, we need to add that to our logger.
logger.addHandler(file_handler)


class Employee:

    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        logger.info(f'created new employee {self.firstname} {self.lastname}'
        )

    def email(self):
        return f'{self.firstname}.{self.lastname}@email.com'

    def fullname(self):
        return f'{self.firstname} {self.lastname}'


if __name__=="__main__":
    emp1 = Employee('kiran','Huded')
    emp2 = Employee('Shriniwas','Shukla')
    emp3 = Employee('Bharath','BR')



