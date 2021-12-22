import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
fh = logging.FileHandler("SaveToFile.log")
fh.setFormatter(f)

logger.addHandler(fh)


def nameCheck(name):
    logger.debug(f"Checking name {name}...")
    if os.path.exists("data.txt"):
        with open ("data.txt","r") as readfile:
            for line in readfile:
                if line.lower().startswith(f"name: {name.lower()}"):
                    logger.error(f"name: {name} already exist")
                    return False
                if len(name) == 0:
                    logger.critical("Name can not be blank")
                    return False
                elif not name.isalpha():
                    logger.critical("Name must be an alphabet")
                    return False
                else:
                    logger.error(f"Check successfully")
                    return True
    else:
        logger.debug("No data found")
        return True

def saveData(name, age, email):
    logger.debug(f"Saving details of {name}...")
    with open("data.txt", "a") as appendfFile:
        appendfFile.write(f"name: {name} - Age: {age} - Email: {email}\n")
        logger.info(f"Details saved successfully!")
        print(f"Details saved successfully!")

logger.info("End of saveToFile program.")
logger.debug("#########################")
