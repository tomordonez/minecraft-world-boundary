import logging
from random import randrange
from mcpi.minecraft import Minecraft

class Teleport:

    def __init__(self, limit):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Initializing Teleport instance')

        try:
            self.mc = Minecraft.create()
        except:
            self.logger.info('Cannot create Minecraft instance')
            raise

        self.origin = 0
        self.limit = limit

        if self.limit is 1:
            self.boundary = 29999984

        elif self.limit is 2:
            self.boundary = 30000000

        elif self.limit is 3:
            self.boundary = 30000496

    def home(self):
        self.logger.info('Loading Teleport.home')
        self.mc.player.setTilePos(self.origin, 64, self.origin)

    def xcorner(self):
        self.logger.info('Loading Teleport.xcorner')
        self.mc.player.setTilePos(self.boundary, 0, 0)

    def ycorner(self):
        self.logger.info('Loading Teleport.ycorner')
        self.mc.player.setTilePos(0, self.boundary, 0)

    def zcorner(self):
        self.logger.info('Loading Teleport.zcorner')
        self.mc.player.setTilePos(0, 0, self.boundary)

    def xycorner(self):
        self.logger.info('Loading Teleport.xycorner')
        self.mc.player.setTilePos(self.boundary, self.boundary, 0)

    def xzcorner(self):
        self.logger.info('Loading Teleport.xzcorner')
        self.mc.player.setTilePos(self.boundary, 0, self.boundary)

    def xyzcorner(self):
        self.logger.info('Loading Teleport.xyzcorner')
        self.mc.player.setTilePos(self.boundary, self.boundary, self.boundary)

    def random(self):
        self.logger.info('Loading Teleport.random')
        self.mc.player.setTilePos(randrange(-self.boundary, self.boundary),\
                               randrange(-self.boundary, self.boundary),\
                               randrange(-self.boundary, self.boundary))
