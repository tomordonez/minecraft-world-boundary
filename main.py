import logging
from banner import Banner
from menu import Menu
from teleport import Teleport

def main():
    banner = Banner()
    banner.load()

    limit = Menu().limit()

    if limit is 4:
        teleport = Teleport(limit)
        teleport.home()
    else:
        teleport = Teleport(limit)
        teleport.home()
        teleport.xcorner()
        #teleport.ycorner()
        #teleport.zcorner()
        #teleport.xycorner()
        #teleport.xzcorner()
        #teleport.xyzcorner()
        #teleport.random()
        #teleport.home()

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('output.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    main()