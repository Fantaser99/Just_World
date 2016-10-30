from service_functions import *


class Item:
    __free_item_id__ = 1

    @staticmethod
    def __get_new_item_id__():
        Item.__free_item_id__ += 1
        return Item.__free_item_id__ - 1

    def __init__(self, identifier, coords):  # int identifier, (int, int) coords.
        if identifier not in items.keys():
            raise ValueError('Id ' + str(identifier) + 'not found!')
        self.info = items[int(identifier)]
        self.on_ground = True
        self._id_ = identifier
        self.item_id = self.__get_new_item_id__()
        self.x = coords[BASE_X]
        self.y = coords[BASE_Y]
        # del self.getNewItemId  # this function shouldn't be in this class's objects.

    def get_item_id(self):
        return self._id_

    def get_id(self):
        return self.item_id

    def is_on_ground(self):
        return self.on_ground

    def get_icon(self):
        return self.info["icon"]

    def get_coords(self):
        # If item is in inventory, func returns inventory coords. Else it returns world-related coords.
        return {"on ground": self.is_on_ground(), "x": self.x, "y": self.y}

    def get_weight(self):
        return self.info["weight"]

    def get_cost(self):
        return self.info["cost"]

    def get_description(self):
        return self.info["description"]

    def get_time_left(self):
        if True:
            raise NotImplementedError('Class Item, method getTimeLeft. Method moveToGround is required.')
        if self.on_ground:
            if self.start + self.duration <= game_time:  # Time must be global.
                pass  # Here should be deletion of item.
            return self.start + self.duration - game_time
        else:
            return None

    def get_info(self):
        # This func isn't cool, it can work longer than other.
        info = self.info
        info["on_ground"] = self.is_on_ground()
        info["id"] = self.getId()
        info["coords"] = (self.x, self.y)
        return info

    def move_to_inventory(self):
        # Here should be choice of coord in player' inventory.
        # Will be realized after realization of Player class.
        raise NotImplementedError('Class Item, method move_to_inventory')

    def move_to_ground(self):
        # Here should be choice of coords based on player' coords and start of item's duration timer.
        # Will be realized after realization of Player class.
        raise NotImplementedError('Class Item, method move_to_ground')

    def move_in_inventory(self, x, y):
        # Here should be coords check and changing coords of item in Player's inventory too.
        if True:
            raise NotImplementedError('Class Item, method move_in_inventory')
        self.coords = (self.coords[BASE_X] + x, self.coords[BASE_Y] + y)
