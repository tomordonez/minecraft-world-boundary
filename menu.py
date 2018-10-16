import logging

class Menu:

    def limit(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Loading Menu')

        print('Minecraft world boundary is the edge of the world')
        print('The world has 3 layers')
        print('The 1st layer world border is: X/Z +- 29,999,984')
        print('The 2nd layer border is: X/Z +- 30,000,000')
        print('The 3rd layer border is: X/Z +- 30,000,496')
        print('The max Y is 1.797x10^308')
        print('Interesting things happen at these borders')
        print('\n')
        print('1. First layer:  X/Z +- 29,999,984')
        print('2. Second layer: X/Z +- 30,000,000')
        print('3. Third layer:  X/Z +- 30,000,496')
        print('4. Go home to (0, 64, 0)')
        self.limit = int(input('Select the layer you want to test: '))

        return(self.limit)
