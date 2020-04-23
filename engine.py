#=========================[Classes]=========================
class Dictionary:
    COLOURS = ["Black","black","White","white","Red","red","Green","green","Blue","blue","Orange","orange","Purple","purple","Silver","silver"]
    WG001 = ["North", "N", "north", "n"]
    WG002 = ["Northeast", "NE", "northeast", "ne"]
    WG003 = ["East", "E", "east", "e"]
    WG004 = ["Southeast", "SE", "southeast", "se"]
    WG005 = ["South", "S", "south", "s"]
    WG006 = ["Southwest", "SW", "southwest", "sw"]
    WG007 = ["West", "W", "west", "w"]
    WG008 = ["Northwest", "NW", "northwest", "nw"]
    WG009 = ["Up", "U", "up", "u"]
    WG010 = ["Down", "D", "down", "d"]
    WG011 = ["Enter", "enter"]
    WG012 = ["Exit", "exit"]
    WG013 = ["Inventory", "Inv", "I", "inventory", "inv", "i"]
    WG014 = ["Status", "Stat", "St", "status", "stat", "st"]
    WG015 = ["Get", "get"]
    WG016 = ["Drop", "drop"]
    WG017 = ["Look", "look"]
    WG018 = ["Examine", "examine"]
    WG019 = ["Peek", "peek"]
    WG020 = ["Glance", "glance"]
    WG021 = ["Put", "put"]
    WG022 = ["In", "in", "Inside", "inside"]
    WG023 = ["Take", "take"]
    WG024 = ["From", "from"]
    WG025 = ["At", "at"]
    WG026 = ["My","my"]
    WG027 = ["Into", "into"]
    WG028 = ["Unlock","unlock"]
    WG029 = ["Lock","lock"]
    WG030 = ["With","with"]
    WG031 = ["Open","open"]
    WG032 = ["Close","close"]
    WG033 = ["Press","press"]
    WG034 = ["Use","use"]

class Cell:
    def __init__(self, title, description, roomContainer, x, y, z, north, northEast, east, southEast, south, southWest, west, northWest, up, down):

        self.title = title
        self.description = description
        self.roomContainer = roomContainer
        self.x = x
        self.y = y
        self.z = z
        self.north = north
        self.northEast = northEast
        self.east = east
        self.southEast = southEast
        self.south = south
        self.southWest = southWest
        self.west = west
        self.northWest = northWest
        self.up = up
        self.down = down

    def getCoordinates(self):
        return self.x, self.y, self.z

class Wall:
    def __init__(self, colour, contents, gateway, gateBlock, control):
        self.colour = colour
        self.contents = contents
        self.gateway = gateway
        self.gateBlock = gateBlock
        self.control = control

    def setColour(self, newColour):
        self.colour = newColour

    def getColour(self):
        return self.colour

    def addContents(self, item):
        self.contents.append(item)

    def removeContents(self, item):
        self.contents.remove(item)

    def getContents(self):
        return self.contents

class Floor:
    def __init__(self, colour, contents, gateway, gateBlock, control):
        self.colour = colour
        self.contents = contents
        self.gateway = gateway
        self.gateBlock = gateBlock
        self.control = control

    def setColour(self, newColour):
        self.colour = newColour

    def getColour(self):
        return self.colour

    def addContents(self, item):
        self.contents.append(item)

    def removeContents(self, item):
        self.contents.remove(item)

    def getContents(self):
        return self.contents

class Ceiling:
    def __init__(self, colour, contents, gateway, gateBlock, control):
        self.colour = colour
        self.contents = contents
        self.gateway = gateway
        self.gateBlock = gateBlock
        self.control = control

    def setColour(self, newColour):
        self.colour = newColour

    def getColour(self):
        return self.colour

    def addContents(self, item):
        self.contents.append(item)

    def removeContents(self, item):
        self.contents.remove(item)

    def getContents(self):
        return self.contents

class Door:
    def __init__(self, name, isOpen, isLocked, ID):
        self.name = name
        self.isOpen = isOpen
        self.isLocked = isLocked
        self.ID = ID

    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def getIsLocked(self):
        return self.isLocked

    def getIsOpen(self):
        return self.isOpen

    def toggleOpen(self, toggle):
        self.isOpen = toggle

    def toggleLock(self, toggle):
        self.isLocked = toggle

    def getState(self):
        if self.isOpen == False and self.isLocked == True:
            print("The door is locked.")
            return False
        elif self.isOpen == True and self.isLocked == False:
            return True
        elif self.isOpen == False and self.isLocked == False:
            print("You open the door and walk through.")
            self.isOpen = True
            return True

class Stairs:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Window:
    def __init__(self, name, isOpen, isLocked):
        self.name = name
        self.isOpen = isOpen
        self.isLocked = isLocked

    def getName(self):
        return self.name

    def toggleOpen(self, toggle):
        self.isOpen = toggle

    def toggleLock(self, toggle):
        self.isLocked = toggle

    def getState(self):
        if self.isOpen == False and self.isLocked == True:
            print("The window is locked.")
            return False
        elif self.isOpen == True and self.isLocked == False:
            return True
        elif self.isOpen == False and self.isLocked == False:
            print("You open the window and climb through.")
            self.isOpen = True
            return True

class Entity:
    def __init__(self, name, description, strength, endurance, agility,
                 dexterity, intelligence, willpower, location, currentWeight,
                 maxWeight, size, x, y, z):

        self.name = name
        self.description = description
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.willpower = willpower
        self.location = location
        self.currentWeight = currentWeight
        self.maxWeight = maxWeight
        self.size = size
        self.x = x
        self.y = y
        self.z = z

    def getCoordinates(self):
        return self.x, self.y, self.z

    def north(self, map):
        if self.location.north == None:
            self.y = self.y + 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.north) == Wall:
            if self.location.north.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.north.gateway) == Door or type(self.location.north.gateway) == Window:
                if self.location.north.gateway.getState() == True:
                    self.y = self.y + 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def northEast(self, map):
        if self.location.northEast == None:
            self.x = self.x + 1
            self.y = self.y + 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.northEast) == Wall:
            if self.location.northEast.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.northEast.gateway) == Door or type(self.location.northEast.gateway) == Window:
                if self.location.northEast.gateway.getState() == True:
                    self.x = self.x + 1
                    self.y = self.y + 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def east(self, map):
        if self.location.east == None:
            self.x = self.x + 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.east) == Wall:
            if self.location.east.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.east.gateway) == Door or type(self.location.east.gateway) == Window:
                if self.location.east.gateway.getState() == True:
                    self.x = self.x + 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def southEast(self, map):
        if self.location.southEast == None:
            self.x = self.x + 1
            self.y = self.y - 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.southEast) == Wall:
            if self.location.southEast.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.southEast.gateway) == Door or type(self.location.southEast.gateway) == Window:
                if self.location.southEast.gateway.getState() == True:
                    self.x = self.x + 1
                    self.y = self.y - 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def south(self, map):
        if self.location.south == None:
            self.y = self.y - 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.south) == Wall:
            if self.location.south.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.south.gateway) == Door or type(self.location.south.gateway) == Window:
                if self.location.south.gateway.getState() == True:
                    self.y = self.y - 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def southWest(self, map):
        if self.location.southWest == None:
            self.x = self.x - 1
            self.y = self.y - 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.southWest) == Wall:
            if self.location.southWest.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.southWest.gateway) == Door or type(self.location.southWest.gateway) == Window:
                if self.location.southWest.gateway.getState() == True:
                    self.x = self.x - 1
                    self.y = self.y - 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def west(self, map):
        if self.location.west == None:
            self.x = self.x - 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.west) == Wall:
            if self.location.west.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.west.gateway) == Door or type(self.location.west.gateway) == Window:
                if self.location.west.gateway.getState() == True:
                    self.x = self.x - 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def northWest(self, map):
        if self.location.northWest == None:
            self.x = self.x - 1
            self.y = self.y + 1
            for room in map.values():
                if self.getCoordinates() == room.getCoordinates():
                    self.location = room
                    return

        elif type(self.location.northWest) == Wall:
            if self.location.northWest.gateway == None:
                print("You can't walk through walls.")
                return

            elif type(self.location.northWest.gateway) == Door or type(self.location.northWest.gateway) == Window:
                if self.location.northWest.gateway.getState() == True:
                    self.x = self.x - 1
                    self.y = self.y + 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

    def up(self, map):
        if self.location.up == None:
            print("are you trying to climb the air?")
            return

        elif type(self.location.up) == Ceiling:
            if self.location.up.gateway == None:
                print("theres no way up its just a ceiling.")
                return

            elif type(self.location.up.gateway) == Stairs:
                if type(self.location.up.gateBlock) == None:
                    self.z = self.z + 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

                elif type(self.location.up.gateBlock) == Door:
                    if self.location.up.gateBlock.getState() == True:
                        self.z = self.z + 1
                        for room in map.values():
                            if self.getCoordinates() == room.getCoordinates():
                                self.location = room
                                return

    def down(self, map):
        if self.location.down == None: # Not relevent at the moment.
            print("are you trying to climb the air?")
            return

        elif type(self.location.down) == Floor:
            if self.location.down.gateway == None:
                print("do you intend on digging?.")
                return

            elif type(self.location.down.gateway) == Stairs:
                if type(self.location.down.gateBlock) == None:
                    self.z = self.z - 1
                    for room in map.values():
                        if self.getCoordinates() == room.getCoordinates():
                            self.location = room
                            return

                elif type(self.location.down.gateBlock) == Door:
                    if self.location.down.gateBlock.getState() == True:
                        self.z = self.z - 1
                        for room in map.values():
                            if self.getCoordinates() == room.getCoordinates():
                                self.location = room
                                return

class Human(Entity):
    def __init__(self, name, description, strength, endurance, agility,
                 dexterity, intelligence, willpower, location, currentWeight,
                 maxWeight, size, x, y, z, head, leftEye, rightEye,
                 leftEar, rightEar, mouth, neck, upperBody,
                 leftShoulder, leftUpperArm, leftLowerArm, leftWrist, leftHand,
                 rightShoulder, rightUpperArm, rightLowerArm, rightWrist, rightHand,
                 lowerBody, back, backStorage, leftUpperLeg, leftLowerLeg, leftFoot,
                 rightUpperLeg, rightLowerLeg, rightFoot, leftHandHeld, rightHandHeld):

        Entity.__init__(self, name, description, strength, endurance, agility, dexterity, intelligence, willpower, location, currentWeight, maxWeight, size, x, y, z)

        self.head = head
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.leftEar = leftEar
        self.rightEar = rightEar
        self.mouth = mouth
        self.neck = neck
        self.upperBody = upperBody
        self.leftShoulder = leftShoulder
        self.leftUpperArm = leftUpperArm
        self.leftLowerArm = leftLowerArm
        self.leftWrist = leftWrist
        self.leftHand = leftHand
        self.rightShoulder = rightShoulder
        self.rightUpperArm = rightUpperArm
        self.rightLowerArm = rightLowerArm
        self.rightWrist = rightWrist
        self.rightHand = rightHand
        self.lowerBody = lowerBody
        self.back = back
        self.backStorage = backStorage
        self.leftUpperLeg = leftUpperLeg
        self.leftLowerLeg = leftLowerLeg
        self.leftFoot = leftFoot
        self.rightUpperLeg = rightUpperLeg
        self.rightLowerLeg = rightLowerLeg
        self.rightFoot = rightFoot
        self.leftHandHeld = leftHandHeld
        self.rightHandHeld = rightHandHeld

    def getItem(self, rightHand, leftHand, playerWeight, location, itemColour, item, containerColour, container):
        #Get item from room.
        if itemColour == None and containerColour == None and container == None:
            for search in range(len(location)):
                foundItem = location[search]
                if item == foundItem.name.lower():
                    checkHands(rightHand, leftHand, playerWeight, location, foundItem)
                    return
            if item != foundItem.name.lower():
                print("Item doesn't exist.")
                return

        #Get coloured item from the room.
        elif containerColour == None and container == None:
            for search in range(len(location)):
                foundItem = location[search]
                if foundItem.colour == None:
                    continue
                elif itemColour == foundItem.colour.lower():
                    if item == foundItem.name.lower():
                        checkHands(rightHand, leftHand, playerWeight, location, foundItem)
                        return
            if item != foundItem.name.lower():
                print("Item doesn't exist.")
                return

        #Get item from container.
        elif itemColour == None and containerColour == None:
            for search in range(len(location)):
                foundItem = location[search]
                if container == foundItem.name.lower():
                    for contents in range(len(foundItem.contents)):
                        containedItem = foundItem.contents[contents]
                        if item == containedItem.name.lower():
                            checkHands(rightHand, leftHand, playerWeight, foundItem.contents, containedItem)
                            return
                    if item != containedItem.name.lower():
                        print("Item doesn't exist.")
                        return

        #Get item from coloured container.
        elif itemColour == None:
            for search in range(len(location)):
                foundItem = location[search]
                if containerColour == foundItem.colour.lower():
                    if container == foundItem.name.lower():
                        for contents in range(len(foundItem.contents)):
                            containedItem = foundItem.contents[contents]
                            if item == containedItem.name.lower():
                                checkHands(rightHand, leftHand, playerWeight, foundItem.contents, containedItem)
                                return
                            else:
                                print("Doesnt exist.")
                                return

        #Get coloured item from container.
        elif containerColour == None:
            for search in range(len(location)):
                foundItem = location[search]
                if container == foundItem.name.lower():
                    for contents in range(len(foundItem.contents)):
                        containedItem = foundItem.contents[contents]
                        if itemColour == containedItem.colour.lower():
                            if item == containedItem.name.lower():
                                checkHands(rightHand, leftHand, playerWeight, foundItem.contents, containedItem)
                                return
                            else:
                                print("Doesnt exist.")
                                return
                        else:
                            pass
                else:
                    pass

        #Get coloured item from coloured container.
        else:
            for search in range(len(location)):
                foundItem = location[search]
                if containerColour.lower() == foundItem.colour.lower():
                    if container == foundItem.name.lower():
                        for contents in range(len(foundItem.contents)):
                            containedItem = foundItem.contents[contents]
                            if itemColour == containedItem.colour.lower():
                                if item == containedItem.name.lower():
                                    checkHands(rightHand, leftHand, playerWeight, foundItem.contents, containedItem)
                                    return
                                else:
                                    print("Doesnt exist.")
                                    return
                            else:
                                pass
                    else:
                        pass
                else:
                    pass

    def getItemHeld(self, rightHand, leftHand, playerWeight, location, itemColour, item, containerColour, container):
        #Get item from held container
        if itemColour == None and containerColour == None:
            for i in range(len(location)):
                for i2 in range(len(location[i])):
                    heldItem = location[i][i2]
                    for i3 in range(len(heldItem.contents)):
                        containedItem = heldItem.contents[i3]
                        if container == heldItem.name.lower():
                            if item == containedItem.name.lower():
                                checkHands(rightHand, leftHand, playerWeight, heldItem.contents, containedItem)
                                return
                            else:
                                print("no item")
                                return
                        else:
                            pass

        #Get colour item from held container
        elif containerColour == None:
            for i in range(len(location)):
                for i2 in range(len(location[i])):
                    heldItem = location[i][i2]
                    for i3 in range(len(heldItem.contents)):
                        containedItem = heldItem.contents[i3]
                        if container == heldItem.name.lower():
                            if itemColour == containedItem.colour.lower():
                                if item == containedItem.name.lower():
                                    checkHands(rightHand, leftHand, playerWeight, heldItem.contents, containedItem)
                                    return
                                else:
                                    print("no item")
                                    return
                            else:
                                pass
                        else:
                            pass

        #Get item from held colour container
        elif itemColour == None:
            for i in range(len(location)):
                for i2 in range(len(location[i])):
                    heldItem = location[i][i2]
                    for i3 in range(len(heldItem.contents)):
                        containedItem = heldItem.contents[i3]
                        if containerColour == heldItem.colour.lower():
                            if container == heldItem.name.lower():
                                if item == containedItem.name.lower():
                                    checkHands(rightHand, leftHand, playerWeight, heldItem.contents, containedItem)
                                    return
                                else:
                                    print("no item")
                                    return
                            else:
                                pass
                        else:
                            pass

        #Get colour item from held colour container
        else:
            for i in range(len(location)):
                for i2 in range(len(location[i])):
                    heldItem = location[i][i2]
                    for i3 in range(len(heldItem.contents)):
                        containedItem = heldItem.contents[i3]
                        if containerColour == heldItem.colour.lower():
                            if container == heldItem.name.lower():
                                if itemColour == containedItem.colour.lower():
                                    if item == containedItem.name.lower():
                                        checkHands(rightHand, leftHand, playerWeight, heldItem.contents, containedItem)
                                        return
                                    else:
                                        print("no item")
                                        return
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass

    #Drop item
    def dropItem(self, location, item, search_slots):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if item == worn_item.name.lower():
                    location.append(worn_item)
                    search_slots[i].remove(worn_item)
                    print("dropped it")
                    return
                else:
                    print("no item")
                    return

    #Drop colour item
    def dropColourItem(self, location, item, item_colour, search_slots):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if item_colour == worn_item.colour.lower():
                    if item == worn_item.name.lower():
                        location.append(worn_item)
                        search_slots[i].remove(worn_item)
                        print("dropped it")
                        return
                    else:
                        print("no item")
                        return
                else:
                    pass

    #Put item in container(room)
    def putItemInContainer(self, search_slots, location, item, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if item == worn_item.name.lower():
                    for l in range(len(location)):
                        location_container = location[l]
                        if container == location_container.name.lower():
                            location_container.contents.append(worn_item)
                            search_slots[i].remove(worn_item)
                            print("You put the " + worn_item.getName() + " in the " + location_container.getName())
                            return
                        else:
                            return
                    else:
                        pass

    #Put item in colour container(room)
    def putItemInColourContainer(self, search_slots, location, item, colour, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if item == worn_item.name.lower():
                    for l in range(len(location)):
                        location_container = location[l]
                        if colour == location_container.colour.lower():
                            if container == location_container.name.lower():
                                location_container.contents.append(worn_item)
                                search_slots[i].remove(worn_item)
                                print("You put the " + worn_item.getName() + " in the " + location_container.getName())
                                return
                            else:
                                return
                        else:
                            pass
                    else:
                        pass

    #Put colour item in container(room)
    def putColourItemInContainer(self, search_slots, location, colour, item, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if colour == worn_item.colour.lower():
                    if item == worn_item.name.lower():
                        for l in range(len(location)):
                            location_container = location[l]
                            if container == location_container.name.lower():
                                location_container.contents.append(worn_item)
                                search_slots[i].remove(worn_item)
                                print("You put the " + worn_item.getName() + " in the " + location_container.getName())
                                return
                            else:
                                return
                    else:
                        pass
                else:
                    pass

    #Put colour item in colour container(room)
    def putColourItemInColourContainer(self, search_slots, location, item_colour, item, container_colour, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if item_colour == worn_item.colour.lower():
                    if item == worn_item.name.lower():
                        for l in range(len(location)):
                            location_container = location[l]
                            if container_colour == location_container.colour.lower():
                                if container == location_container.name.lower():
                                    location_container.contents.append(worn_item)
                                    search_slots[i].remove(worn_item)
                                    print("You put the " + worn_item.getName() + " in the " + location_container.getName())
                                    return
                                else:
                                    return
                            else:
                                pass
                    else:
                        pass
                else:
                    pass

    #Put item in container(player)
    def putItemInMyContainer(self, search_slots, rHand, lHand, item, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if container == worn_item.name.lower():
                    for r in range(len(rHand)):
                        rHand_item = rHand[r]
                        for l in range(len(lHand)):
                            lHand_item = lHand[l]
                            if item == rHand_item.name.lower():
                                worn_item.contents.append(rHand_item)
                                rHand.remove(rHand_item)
                                print("You put the " + rHand_item.getName() + " in the " + worn_item.getName())
                                return
                            elif item == lHand_item.name.lower():
                                worn_item.contents.append(lHand_item)
                                lHand.remove(lHand_item)
                                print("You put the " + lHand_item.getName() + " in the " + worn_item.getName())
                                return
                            else:
                                return
                else:
                    pass

    #Put item in colour container(player)
    def putItemInMyColourContainer(self, search_slots, rHand, lHand, item, container_colour, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if container_colour == worn_item.colour.lower():
                    if container == worn_item.name.lower():
                        for r in range(len(rHand)):
                            rHand_item = rHand[r]
                            for l in range(len(lHand)):
                                lHand_item = lHand[l]
                                if item == rHand_item.name.lower():
                                    worn_item.contents.append(rHand_item)
                                    rHand.remove(rHand_item)
                                    print("You put the " + rHand_item.getName() + " in the " + worn_item.getName())
                                    return
                                elif item == lHand_item.name.lower():
                                    worn_item.contents.append(lHand_item)
                                    lHand.remove(lHand_item)
                                    print("You put the " + lHand_item.getName() + " in the " + worn_item.getName())
                                    return
                                else:
                                    return
                    else:
                        pass
                else:
                    pass

    #Put colour item in container(player)
    def putColourItemInMyContainer(self, search_slots, rHand, lHand, item_colour, item, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if container == worn_item.name.lower():
                    for r in range(len(rHand)):
                        rHand_item = rHand[r]
                        for l in range(len(lHand)):
                            lHand_item = lHand[l]
                            if item_colour == rHand_item.colour.lower() or item_colour == lHand_item.colour.lower():
                                if item == rHand_item.name.lower():
                                    worn_item.contents.append(rHand_item)
                                    rHand.remove(rHand_item)
                                    print("You put the " + rHand_item.getName() + " in the " + worn_item.getName())
                                    return
                                elif item == lHand_item.name.lower():
                                    worn_item.contents.append(lHand_item)
                                    lHand.remove(lHand_item)
                                    print("You put the " + lHand_item.getName() + " in the " + worn_item.getName())
                                    return
                                else:
                                    return
                            else:
                                pass
                else:
                    pass

    #Put colour item in colour container(player)
    def putColourItemInMyColourContainer(self, search_slots, rHand, lHand, item_colour, item, container_colour, container):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if container_colour == worn_item.colour.lower():
                    if container == worn_item.name.lower():
                        for r in range(len(rHand)):
                            rHand_item = rHand[r]
                            for l in range(len(lHand)):
                                lHand_item = lHand[l]
                                if item_colour == rHand_item.colour.lower() or item_colour == lHand_item.colour.lower():
                                    if item == rHand_item.name.lower():
                                        worn_item.contents.append(rHand_item)
                                        rHand.remove(rHand_item)
                                        print("You put the " + rHand_item.getName() + " in the " + worn_item.getName())
                                        return
                                    elif item == lHand_item.name.lower():
                                        worn_item.contents.append(lHand_item)
                                        lHand.remove(lHand_item)
                                        print("You put the " + lHand_item.getName() + " in the " + worn_item.getName())
                                        return
                                    else:
                                        return
                                else:
                                    pass
                    else:
                        pass
                else:
                    pass

    def lock(self, door, keyName, rightHand, leftHand):
        if door == None:
            print("There is no door there.")
            return
        else:
            if door.getIsLocked() == True:
                print("the door is already locked.")
                return
            elif door.getIsOpen() == True:
                print("you should close the door first.")
                return
            else:
                for checkKey in range(len(rightHand)):
                    foundKey = rightHand[checkKey]
                    if type(foundKey) == ItemKey:
                        if keyName == foundKey.getName():
                            if foundKey.getID() == door.getID():
                                print("door locked.")
                                door.toggleLock(True)
                                return
                            elif foundKey.getID() != door.getID():
                                print("that isnt the right key.")
                                return
                    else:
                        break
                for checkKey in range(len(leftHand)):
                    foundKey = leftHand[checkKey]
                    if type(foundKey) == ItemKey:
                        if keyName == foundKey.getName():
                            if foundKey.getID() == door.getID():
                                print("door locked.")
                                door.toggleLock(True)
                                return
                            elif foundKey.getID() != door.getID():
                                print("that isnt the right key.")
                                return
                    else:
                        return

    def unlock(self, door, keyName, rightHand, leftHand):
        if door == None:
            print("There is no door there.")
            return
        else:
            if door.getIsLocked() == False:
                print("the door is already unlocked.")
                return
            else:
                for checkKey in range(len(rightHand)):
                    foundKey = rightHand[checkKey]
                    if type(foundKey) == ItemKey:
                        if keyName == foundKey.getName():
                            if foundKey.getID() == door.getID():
                                print("door unlocked.")
                                door.toggleLock(False)
                                return
                            elif foundKey.getID() != door.getID():
                                print("that isnt the right key.")
                                return
                    else:
                        break
                for checkKey in range(len(leftHand)):
                    foundKey = leftHand[checkKey]
                    if type(foundKey) == ItemKey:
                        if keyName == foundKey.getName():
                            if foundKey.getID() == door.getID():
                                print("door unlocked.")
                                door.toggleLock(False)
                                return
                            elif foundKey.getID() != door.getID():
                                print("that isnt the right key.")
                                return
                    else:
                        return

    def openDoor(self, door):
        if door == None:
            print("There is no door there.")
            return
        else:
            if door.getIsLocked() == True:
                print("The door is locked.")
                return
            else:
                if door.getIsOpen() == True:
                    print("the door is already open.")
                    return
                else:
                    print("you open the door.")
                    door.toggleOpen(True)
                    return

    def closeDoor(self, door):
        if door == None:
            print("There is no door there.")
            return
        else:
            if door.getIsLocked() == True:
                print("you should unlock the door first.")
                return
            else:
                if door.getIsOpen() == False:
                    print("the door is already closed.")
                    return
                else:
                    print("you close the door.")
                    door.toggleOpen(False)
                    return

class Player(Human):
    def __init__(self, name, description, strength, endurance, agility,
                 dexterity, intelligence, willpower, location, currentWeight,
                 maxWeight, size, x, y, z, head, leftEye, rightEye,
                 leftEar, rightEar, mouth, neck, upperBody,
                 leftShoulder, leftUpperArm, leftLowerArm, leftWrist, leftHand,
                 rightShoulder, rightUpperArm, rightLowerArm, rightWrist, rightHand,
                 lowerBody, back, backStorage, leftUpperLeg, leftLowerLeg,
                 leftFoot, rightUpperLeg, rightLowerLeg, rightFoot,
                 leftHandHeld, rightHandHeld):

        Human.__init__(self, name, description, strength, endurance, agility,
                 dexterity, intelligence, willpower, location, currentWeight,
                 maxWeight, size, x, y, z, head, leftEye, rightEye,
                 leftEar, rightEar, mouth, neck, upperBody,
                 leftShoulder, leftUpperArm, leftLowerArm, leftWrist, leftHand,
                 rightShoulder, rightUpperArm, rightLowerArm, rightWrist, rightHand,
                 lowerBody, back, backStorage, leftUpperLeg, leftLowerLeg,
                 leftFoot, rightUpperLeg, rightLowerLeg, rightFoot,
                 leftHandHeld, rightHandHeld)

    #Status
    def status(self, name, description, currentWeight, maxWeight, strength, endurance, agility, dexterity, intelligence, willpower, rHand, lHand):
        print(name)
        print(description)
        print("")
        print("Weight: ", currentWeight, "/", maxWeight)
        print("")
        print("Strength    ", strength)
        print("Endurance   ", endurance)
        print("Agility     ", agility)
        print("Dexterity   ", dexterity)
        print("Intelligence", intelligence)
        print("Willpower   ", willpower)
        print("")
        for x in rHand:
            print("Right Hand:", x.getName())
        for y in lHand:
            print("Left Hand:", y.getName())
        return

    #Look at container contents
    def lookAt(self, location, container_name):
        for i in range(len(location)):
            container = location[i]
            if container_name == container.name.lower():
                for i2 in range(len(container.contents)):
                    contained_items = container.contents[i2]
                    print(contained_items.getName())
            else:
                pass

    #Look at colour container contents
    def lookAtColour(self, location, container_colour, container_name):
        for i in range(len(location)):
            container = location[i]
            if container_colour == container.colour.lower():
                if container_name == container.name.lower():
                    for i2 in range(len(container.contents)):
                        contained_items = container.contents[i2]
                        print(contained_items.getName())
                else:
                    pass
            else:
                pass

    #Look in container contents (player)
    def lookIn(self, container_name, search_slots):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if container_name == worn_item.name.lower():
                    for i2 in range(len(worn_item.contents)):
                        contained_items = worn_item.contents[i2]
                        print(contained_items.getName())
                else:
                    pass

    #Look in colour container contents(player)
    def lookInColour(self, container_colour, container_name, search_slots):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if container_colour == worn_item.colour.lower():
                    if container_name == worn_item.name.lower():
                        for i2 in range(len(worn_item.contents)):
                            contained_items = worn_item.contents[i2]
                            print(contained_items.getName())
                    else:
                        pass
                else:
                    pass

    #Examine item (room)
    def examine(self, location, item):
        for scan in range(len(location)):
            room_item = location[scan]
            if item == room_item.name.lower():
                print(room_item.getName() + ": " + room_item.description)
                return
            else:
                print("Doesnt exist.")
                return

    #Examine colour item (room)
    def examineColour(self, location, colour, item):
        for scan in range(len(location)):
            room_item = location[scan]
            if colour == room_item.colour.lower():
                if item == room_item.name.lower():
                    print(room_item.getName() + ": " + room_item.description)
                    return
                else:
                    print("What item?")
                    return
            else:
                pass

    #Examine item (player)
    def examineMy(self, search_slots, item):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if item == worn_item.name.lower():
                    print(worn_item.getName() + ": " + worn_item.description)
                    return
                else:
                    print("Doesnt exist.")
                    return

    #Examine colour item (player)
    def examineMyColour(self, search_slots, colour, item):
        for i in range(len(search_slots)):
            for i2 in range(len(search_slots[i])):
                worn_item = search_slots[i][i2]
                if colour == worn_item.colour.lower():
                    if item == worn_item.name.lower():
                        print(worn_item.getName() + ": " + worn_item.description)
                        return
                    else:
                        print("What item?")
                        return
                else:
                    pass

class Dog(Entity):
    def __init__(self, name, description, strength, endurance, agility,
                 dexterity, intelligence, willpower, location, currentWeight,
                 maxWeight, size, head, leftEye, rightEye,
                 leftEar, rightEar, mouth, neck, body,
                 leftShoulder, front_leftUpperLeg, front_leftLowerLeg, front_left_paw,
                 rightShoulder, front_rightUpperLeg, front_rightLowerLeg, front_right_paw,
                 back, back_leftUpperLeg, back_leftLowerLeg, back_left_paw,
                 back_rightUpperLeg, back_rightLowerLeg, back_right_paw, tail):

        Entity.__init__(self, name, description, strength, endurance, agility, dexterity, intelligence, willpower, location, currentWeight, maxWeight, size)

        self.head = head
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.leftEar = leftEar
        self.rightEar = rightEar
        self.mouth = mouth
        self.neck = neck
        self.body = body
        self.leftShoulder = leftShoulder
        self.front_leftUpperLeg = front_leftUpperLeg
        self.front_leftLowerLeg = front_leftLowerLeg
        self.front_left_paw = front_left_paw
        self.rightShoulder = rightShoulder
        self.front_rightUpperLeg = front_rightUpperLeg
        self.front_rightLowerLeg = front_rightLowerLeg
        self.front_right_paw = front_right_paw
        self.back = back
        self.back_leftUpperLeg = back_leftUpperLeg
        self.back_leftLowerLeg = back_leftLowerLeg
        self.back_left_paw = back_left_paw
        self.back_rightUpperLeg = back_rightUpperLeg
        self.back_rightLowerLeg = back_rightLowerLeg
        self.back_right_paw = back_right_paw
        self.tail = tail

class Cat(Entity):
    def __init__(self, name, description, strength, endurance, agility,
                 dexterity, intelligence, willpower, location, currentWeight,
                 maxWeight, size, head, leftEye, rightEye,
                 leftEar, rightEar, mouth, neck, body,
                 leftShoulder, front_leftUpperLeg, front_leftLowerLeg, front_left_paw,
                 rightShoulder, front_rightUpperLeg, front_rightLowerLeg, front_right_paw,
                 back, back_leftUpperLeg, back_leftLowerLeg, back_left_paw,
                 back_rightUpperLeg, back_rightLowerLeg, back_right_paw, tail):

        Entity.__init__(self, name, description, strength, endurance, agility, dexterity, intelligence, willpower, location, currentWeight, maxWeight, size)

        self.head = head
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.leftEar = leftEar
        self.rightEar = rightEar
        self.mouth = mouth
        self.neck = neck
        self.body = body
        self.leftShoulder = leftShoulder
        self.front_leftUpperLeg = front_leftUpperLeg
        self.front_leftLowerLeg = front_leftLowerLeg
        self.front_left_paw = front_left_paw
        self.rightShoulder = rightShoulder
        self.front_rightUpperLeg = front_rightUpperLeg
        self.front_rightLowerLeg = front_rightLowerLeg
        self.front_right_paw = front_right_paw
        self.back = back
        self.back_leftUpperLeg = back_leftUpperLeg
        self.back_leftLowerLeg = back_leftLowerLeg
        self.back_left_paw = back_left_paw
        self.back_rightUpperLeg = back_rightUpperLeg
        self.back_rightLowerLeg = back_rightLowerLeg
        self.back_right_paw = back_right_paw
        self.tail = tail

class Bird(Entity):
    def __init__(self, name, description, strength, endurance, agility,
                 dexterity, intelligence, willpower, location, currentWeight,
                 maxWeight, size, head, leftEye, rightEye,
                 leftEar, rightEar, mouth, neck, body,
                 left_wing, right_wing, left_claw, right_claw, tail):

        Entity.__init__(self, name, description, strength, endurance, agility, dexterity, intelligence, willpower, location, currentWeight, maxWeight, size)

        self.head = head
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.leftEar = leftEar
        self.rightEar = rightEar
        self.mouth = mouth
        self.neck = neck
        self.body = body
        self.left_wing = left_wing
        self.right_wing = right_wing
        self.left_claw = left_claw
        self.right_claw = right_claw
        self.tail = tail

class Vehicle():
    def __init__(self, name, description, colour, weight,
                 components, speed, protection, visibility, seats):

        self.name = name
        self.description = description
        self.colour = colour
        self.weight = weight
        self.components = components
        self.speed = speed
        self.protection = protection
        self.visibility = visibility
        self.seats = seats

class Item():
    def __init__(self, name, description, colour, weight, size, components,
                 slot_type, tags):

        self.name = name
        self.description = description
        self.colour = colour
        self.weight = weight
        self.size = size
        self.components = components
        self.slot_type = slot_type
        self.tags = tags

    def getName(self):
        if self.colour == None:
            return self.name
        else:
            return self.colour + " " + self.name

class ItemKey(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, ID):
        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.ID = ID

    def getID(self):
        return self.ID

class ItemButtonLock(ItemKey):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, ID):
        ItemKey.__init__(self, name, description, colour, weight, size, components, slot_type, tags, ID)

    def onPress(self, doors):
        for correctDoor in doors.values():
            if self.getID() == correctDoor.getID():
                if correctDoor.getIsLocked() == True:
                    print("you hear a door unlock somewhere.")
                    correctDoor.toggleLock(False)
                    return
                elif correctDoor.getIsLocked() == False:
                    if correctDoor.getIsOpen() == True:
                        print("you should close the door first.")
                        return
                    elif correctDoor.getIsOpen() == False:
                        print("you hear a door lock somewhere.")
                        correctDoor.toggleLock(True)
                        return


class OneHanded(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, attack):

        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.attack = attack

class TwoHanded(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, attack):

        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.attack = attack

class Armour(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, protection):

        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.protection = protection

class Container(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, contents):

        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.contents = contents

class Food(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, hungerVal, thirstVal):

        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.hungerVal = hungerVal
        self.thirstVal = thirstVal

class Medical(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, healVal):

        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.healVal = healVal

class Component(Item):
    def __init__(self, name, description, colour, weight, size, components, slot_type, tags, amount):

        Item.__init__(self, name, description, colour, weight, size, components, slot_type, tags)

        self.amount = amount

#=========================[End of classes]=========================

#=========================[Functions]=========================
def checkHands(rightHand, leftHand, playerWeight, contents, item):
    if len(rightHand) == 0:
        rightHand.append(item)
        contents.remove(item)
        playerWeight += item.weight
        print("You picked up the " + item.name + " with your right hand.")
        return
    else:
        if len(leftHand) == 0:
            leftHand.append(item)
            contents.remove(item)
            playerWeight += item.weight
            print("You picked up the " + item.name + " with your left hand.")
            return
        else:
            print("Both hands are holding something.")
            return

def displayLocation(location):
    print("")
    print("===[" + location.title + "]===")
    print(location.description)
    print("")

def displayItems(location):
    if len(location) == 1:
        for x in range(len(location)):
            item = location[x]
            print("You see a " + item.getName())

    elif len(location) == 2:
        print("You see a " + " and a ".join(x.getName() for x in location))

    elif len(location) > 2:
        print("You see a " + ", ".join(x.getName() for x in location[0:-1]) + " and a " + "".join(x.getName() for x in location[-1:]))

#=========================[End of functions]=========================

if __name__ == "__main__":
    pass
