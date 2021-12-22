import logging
import SaveToFile as STF


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f= logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
fh= logging.FileHandler("employee.log")
fh.setFormatter(f)

logger.addHandler(fh)


name =input("Enter your Name: ")
age =input("Enter your age: ")
email =input("Enter your email: ")

if STF.nameCheck(name):
    STF.saveData(name, age, email)
else:
    logger.critical("Employee check failed")
    print("Employee check failed")

logger.debug("End of Employee Program")
logger.debug("#######################")