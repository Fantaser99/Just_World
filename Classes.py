import pygame

CREATURE_COORD_X = 200
CREATURE_COORD_Y = 100

# hp, speed, danger level, damage, armor
bestiary = {
    'dummy': [5, 0, 0, 0, 0],
}

#
items = {
    0: {"name": "Nothing", "icon": None, "weight": 0, "cost": 0, "description": "Empty", "item_id": 0},
}

# forward, (left, backward, right)
images = {
    'dummy': ['dummy.png'],
}


class Creature:
    def __init__(self, creature='dummy', coordinates=[CREATURE_COORD_X, CREATURE_COORD_Y], direction='forward'):
        self.max_health_points = bestiary[creature][0]
        self.health_points = self.max_health_points
        self.move_speed = bestiary[creature][1]
        self.danger_level = bestiary[creature][2]
        self.attack_strength = bestiary[creature][3]
        self.damage_resist = bestiary[creature][4]
        self.forward_image = pygame.image.load(images[creature][0])
        if coordinates[0] < 0 or coordinates[1] < 0:
            print 'In class Creature:'
            print 'Negative coordinates do not have to be used.', coordinates
            coordinates = [CREATURE_COORD_X, CREATURE_COORD_Y]
            print 'Coordinates are', coordinates
            # if
        self.coordinates = coordinates
        self.direction = direction
        self.home_location = [[0, 0], [1, 1]]

    def moving(self, coordinates=[0, 0]):
        raise NotImplementedError('class Creature def moving')

    def deal_damage(self):
        raise NotImplementedError('class Creature def deal_damage')

    def take_damage(self):
        raise NotImplementedError('class Creature def take_damage')

    def __del__(self):
        # here's just nothing to do now
        pass


class Item:
    __free_item_id__ = 1
    
    def __getNewItemId__(self):
        Item.__free_item_id__ += 1
        return Item.__free_item_id__ - 1
    
    def __init__(self, identifier, coords):  # int identifier, (int, int) coords.
        if identifier not in items.keys():
            raise ValueError('Id ' + str(identifier) + 'not found!')
        self.info = items[int(identifier)]
        self.on_ground = True
        self._id_ = identifier
        self.item_id = self.__getNewItemId__()
        self.x = coords[0]
        self.y = coords[1]
        # del self.getNewItemId  # this function shouldn't be in this class's objects.

    def getItemId(self):
        return self._id_

    def getId(self):
        return self.item_id

    def isOnGround(self):
        return self.on_ground

    def getIcon(self):
        return self.info["icon"]

    def getCoords(self):
        # If item is in inventory, func returns inventory coords. Else it returns world-related coords.
        return {"on ground": self.isOnGround(), "x": self.x, "y": self.y}

    def getWeight(self):
        return self.info["weight"]

    def getCost(self):
        return self.info["cost"]

    def getDescription(self):
        return self.info["description"]

    def getTimeLeft(self):
        if True:
            raise NotImplementedError('Class Item, method getTimeLeft. Method moveToGround is required.')
        if self.on_ground:
            if self.start + self.duration <= game_time:  # Time must be global.
                pass  # Here should be deletion of item.
            return self.start + self.duration - game_time
        return None
    
    def getInfo(self):
        # This func isn't cool, it can work longer than other.
        info = self.info
        info["on_ground"] = self.isOnGround()
        info["id"] = self.getId()
        info["coords"] = (self.x, self.y)
        return info

    def moveToInventory(self):
        # Here should be choice of coord in player' inventory.
        # Will be realized after realization of Player class.
        raise NotImplementedError('Class Item, method moveToInventory')

    def moveToGround(self):
        # Here should be choice of coords based on player' coords and start of item's duration timer.
        # Will be realized after realization of Player class.
        raise NotImplementedError('Class Item, method moveToGround')

    def moveInInventory(self, x, y):
        # Here should be coords check and changing coords of item in Player's inventory too.
        if True:
            raise NotImplementedError('Class Item, method moveInInventory')
        self.coords = (self.coords[0] + x, self.coords[1] + y)


def init_screen(height=600, width=800):
    pygame.init()
    size = [width, height]
    return pygame.display.set_mode(size)


def main():
        test = Creature(coordinates=[200, -300])
        screen = init_screen()
        game_time = 0  # Global game time from start (in seconds).
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            screen.fill([0, 0, 0])
            screen.blit(test.forward_image, test.coordinates)
            game_time = game_time + 1
            pygame.display.update()
            pygame.time.delay(100)
            

try:
    main()
except NotImplementedError as error:
    print 'Oops! You used not finished function in', error.args
