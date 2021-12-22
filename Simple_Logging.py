import logging

logging.basicConfig(filename="loggingDemo.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def nameCheck(name):
    if len(name) < 2:
        logging.info("checking for name length...")
        return "Invalid Name!"
    elif name.isspace():
        logging.info("checking if name is space...")
        return "Invalid Name!"
    elif name.isalpha():
        logging.info("checking if name is an alphbet...")
        return "Name is valid"
    elif name.replace(' ','').isalpha():
        logging.info("checking for full name...")
        return "Name is valid"
    else:
        logging.info("Failed all checks")
        return "Invalid Name!"

print(nameCheck("Ravi"))