import os
import sys
import shlex

from engine import *
from cell import *

player = Player('Player','Generic desc.',5,5,5,5,5,5,map[0],0,100,7,0,0,0,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])

player_slots = [player.head, player.leftEye, player.rightEye,
             player.leftEar, player.rightEar, player.mouth, player.neck, player.upperBody,
             player.leftShoulder, player.leftUpperArm, player.leftLowerArm, player.leftWrist, player.leftHand,
             player.rightShoulder, player.rightUpperArm, player.rightLowerArm, player.rightWrist, player.rightHand,
             player.lowerBody, player.back, player.backStorage, player.leftUpperLeg, player.leftLowerLeg,
             player.leftFoot, player.rightUpperLeg, player.rightLowerLeg, player.rightFoot,
             player.leftHandHeld, player.rightHandHeld]

dev_item_list = []

#=========================[Parser]=========================
def parser(command=None, object=None, command2=None, object2=None, command3=None, object3=None):
    if command in Dictionary.WG001:  # North
        player.north(map)

    elif command in Dictionary.WG002:  # Northeast
        player.northEast(map)

    elif command in Dictionary.WG003:  # East
        player.east(map)

    elif command in Dictionary.WG004:  # Southeast
        player.southEast(map)

    elif command in Dictionary.WG005:  # South
        player.south(map)

    elif command in Dictionary.WG006:  # Southwest
        player.southWest(map)

    elif command in Dictionary.WG007:  # West
        player.west(map)

    elif command in Dictionary.WG008:  # Northwest
        player.northWest(map)

    elif command in Dictionary.WG009:  # Up
        player.up(map)

    elif command in Dictionary.WG010:  # Down
        player.down(map)

    elif command in Dictionary.WG011:  # Enter
        if player.location.enter is not None:
            player.location = player.location.enter
        else:
            print("nope no enter")


    elif command in Dictionary.WG012:  # Exit
        if player.location.exit is not None:
            player.location = player.location.exit
        else:
            print("nope no exit")

    elif command in Dictionary.WG031: # Open
        if object in Dictionary.WG001: # North
            player.openDoor(player.location.north.gateway)
        elif object in Dictionary.WG002: # Northeast
            player.openDoor(player.location.northEast.gateway)
        elif object in Dictionary.WG003: # East
            player.openDoor(player.location.east.gateway)
        elif object in Dictionary.WG004: # Southeast
            player.openDoor(player.location.southEast.gateway)
        elif object in Dictionary.WG005: # South
            player.openDoor(player.location.south.gateway)
        elif object in Dictionary.WG006: # Southwest
            player.openDoor(player.location.southWest.gateway)
        elif object in Dictionary.WG007: # West
            player.openDoor(player.location.west.gateway)
        elif object in Dictionary.WG008: # Northwest
            player.openDoor(player.location.northWest.gateway)
        elif object in Dictionary.WG009: # Up
            player.openDoor(player.location.up.gateBlock)
        elif object in Dictionary.WG010: # Down
            player.openDoor(player.location.down.gateBlock)

    elif command in Dictionary.WG032: # Close
        if object in Dictionary.WG001: # North
            player.closeDoor(player.location.north.gateway)
        elif object in Dictionary.WG002: # Northeast
            player.closeDoor(player.location.northEast.gateway)
        elif object in Dictionary.WG003: # East
            player.closeDoor(player.location.east.gateway)
        elif object in Dictionary.WG004: # Southeast
            player.closeDoor(player.location.southEast.gateway)
        elif object in Dictionary.WG005: # South
            player.closeDoor(player.location.south.gateway)
        elif object in Dictionary.WG006: # Southwest
            player.closeDoor(player.location.southWest.gateway)
        elif object in Dictionary.WG007: # West
            player.closeDoor(player.location.west.gateway)
        elif object in Dictionary.WG008: # Northwest
            player.closeDoor(player.location.northWest.gateway)
        elif object in Dictionary.WG009: # Up
            player.closeDoor(player.location.up.gateBlock)
        elif object in Dictionary.WG010: # Down
            player.closeDoor(player.location.down.gateBlock)

    elif command in Dictionary.WG028: # Unlock
        if command2 in Dictionary.WG030: # With
            if object in Dictionary.WG001: # North
                player.unlock(player.location.north.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG002: # Northeast
                player.unlock(player.location.northEast.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG003: # East
                player.unlock(player.location.east.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG004: # Southeast
                player.unlock(player.location.southEast.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG005: # South
                player.unlock(player.location.south.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG006: # Southwest
                player.unlock(player.location.southWest.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG007: # West
                player.unlock(player.location.west.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG008: # Northwest
                player.unlock(player.location.northWest.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG009: # Up
                player.unlock(player.location.up.gateBlock, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG010: # Down
                player.unlock(player.location.down.gateBlock, object2, player.rightHandHeld, player.leftHandHeld)

    elif command in Dictionary.WG029: # Lock
        if command2 in Dictionary.WG030: # With
            if object in Dictionary.WG001: # North
                player.lock(player.location.north.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG002: # Northeast
                player.lock(player.location.northEast.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG003: # East
                player.lock(player.location.east.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG004: # Southeast
                player.lock(player.location.southEast.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG005: # South
                player.lock(player.location.south.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG006: # Southwest
                player.lock(player.location.southWest.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG007: # West
                player.lock(player.location.west.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG008: # Northwest
                player.lock(player.location.northWest.gateway, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG009: # Up
                player.lock(player.location.up.gateBlock, object2, player.rightHandHeld, player.leftHandHeld)
            elif object in Dictionary.WG010: # Down
                player.lock(player.location.down.gateBlock, object2, player.rightHandHeld, player.leftHandHeld)

    elif command in Dictionary.WG033: # Press
        for x in range(len(player.location.roomContainer)):
            keyItem = player.location.roomContainer[x]
            if object == keyItem.name:
                keyItem.onPress(doors)
                break

    elif command in Dictionary.WG014:  # Status
        player.status(player.name, player.description, player.currentWeight, player.maxWeight, player.strength, player.endurance, player.agility, player.dexterity, player.intelligence, player.willpower, player.rightHandHeld, player.leftHandHeld)

    elif command in Dictionary.WG015:
        if command2 in Dictionary.WG024:
            if object2 in Dictionary.COLOURS:
                #Get *item* from <colour> [container]
                player.getItem(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player.location.roomContainer, None, object, object2, command3)

            else:
                #Get *item* from [container]
                player.getItem(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player.location.roomContainer, None, object, None, object2)

        elif object2 in Dictionary.WG024:
            if command3 in Dictionary.COLOURS:
                #Get <colour> *item* from <colour> [container]
                player.getItem(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player.location.roomContainer, object, command2, command3, object3)

            else:
                #Get <colour> *item* from [container]
                player.getItem(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player.location.roomContainer, object, command2, None, command3)

        elif command2 in Dictionary.WG022:
            if object2 in Dictionary.COLOURS:
                #Get *item* inside <colour> [container]
                player.getItemHeld(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player_slots, None, object, object2, command3)
            else:
                #Get *item* inside [container]
                player.getItemHeld(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player_slots, None, object, None, object2)

        elif object2 in Dictionary.WG022:
            if object in Dictionary.COLOURS and command3 in Dictionary.COLOURS:
                #Get <colour> *item* inside <colour> [container]
                player.getItemHeld(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player_slots, object, command2, command3, object3)
            else:
                #Get <colour> *item* inside [container]
                player.getItemHeld(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player_slots, object, command2, None, command3)

        else:
            if object in Dictionary.COLOURS:
                #Get <colour> *item*
                player.getItem(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player.location.roomContainer, object, command2, None, None)

            else:
                #Get *item*
                player.getItem(player.rightHandHeld, player.leftHandHeld, player.currentWeight, player.location.roomContainer, None, object, None, None)


    elif command in Dictionary.WG016:  # Drop
        if object in Dictionary.COLOURS:
            #Drop <colour> *item*
            player.dropColourItem(player.location.roomContainer, command2, object, player_slots)
        else:
            #Drop *item*
            player.dropItem(player.location.roomContainer, object, player_slots)


    elif command in Dictionary.WG017:  # Look
        if object in Dictionary.WG025:  # At
            if command2 in Dictionary.COLOURS:
                player.lookAtColour(player.location.roomContainer, command2, object2)
            else:
                player.lookAt(player.location.roomContainer, command2)

        elif object in Dictionary.WG022: # In
            if command2 in Dictionary.COLOURS:
                player.lookInColour(command2, object2, player_slots)
            else:
                player.lookIn(command2, player_slots)


    elif command in Dictionary.WG021: # Put
        if command2 in Dictionary.WG022: # In
            if object2 in Dictionary.COLOURS:
                #Put *item* in <colour> [container]
                player.putItemInColourContainer(player_slots, player.location.roomContainer, object, object2, command3)
            else:
                #Put *item* in [container]
                player.putItemInContainer(player_slots, player.location.roomContainer, object, object2)

        elif object2 in Dictionary.WG022: # In
            if command3 in Dictionary.COLOURS:
                #Put <colour> *item* in <colour> [container]
                player.putColourItemInColourContainer(player_slots, player.location.roomContainer, object, command2, command3, object3)
            else:
                #Put <colour> *item* in [container]
                player.putColourItemInContainer(player_slots, player.location.roomContainer, object, command2, command3)

        elif command2 in Dictionary.WG027: # Into
            if object2 in Dictionary.COLOURS:
                #Put *item* inside <colour> [container]
                player.putItemInMyColourContainer(player_slots, player.rightHandHeld, player.leftHandHeld, object, object2, command3)
            else:
                #Put *item* inside [container]
                player.putItemInMyContainer(player_slots, player.rightHandHeld, player.leftHandHeld, object, object2)

        elif object2 in Dictionary.WG027: # Into
            if object in Dictionary.COLOURS and command3 in Dictionary.COLOURS:
                #Put <colour> *item* inside <colour> [container]
                player.putColourItemInMyColourContainer(player_slots, player.rightHandHeld, player.leftHandHeld, object, command2, command3, object3)
            else:
                #Put <colour> *item* inside [container]
                player.putColourItemInMyContainer(player_slots, player.rightHandHeld, player.leftHandHeld, object, command2, command3)
        else:
            pass


    elif command in Dictionary.WG018:  # Examine
        if object in Dictionary.WG026: # My
            if command2 in Dictionary.COLOURS:
                player.examineMyColour(player_slots, command2, object2)
            else:
                player.examineMy(player_slots, command2)

        else:
            if object in Dictionary.COLOURS:
                player.examineColour(player.location.roomContainer, object, command2)
            else:
                player.examine(player.location.roomContainer, object)

    elif command == "doit":
        player.location.roomContainer.append(Item("Knife","For chopping vegetables.",None,1,1,[],[],[]))

    elif command == "quit":
        sys.exit()

#-------------------------[Dev commands]-------------------------
    elif command == "debug":
        for item in range(len(player.rightHandHeld)):
            item1 = player.rightHandHeld[item]
            print("right hand is holding " + item1.fullname)
        for item2 in range(len(player.leftHandHeld)):
            item3 = player.leftHandHeld[item2]
            print("left hand is holding " + item3.fullname)
            break

    elif command == "create":
        for x in range(len(devitemlist)):
            item = devitemlist[x]
            if object == item.name.lower() or object == item.fullname.lower():
                player.inventory.append(item)
                player.currentWeight = player.currentWeight + item.weight
                print("item created")
                break
#-------------------------[End of dev commands]-------------------------
#=========================[End of parser]=========================

while True:
    displayLocation(player.location)
    displayItems(player.location.roomContainer)
    print(player.getCoordinates())

    playerInput = input(">> ")
    modString = playerInput.lower()
    cutString = shlex.split(modString)

    if len(cutString) == 1:
        parser(cutString[0])
    elif len(cutString) == 2:
        parser(cutString[0], cutString[1])
    elif len(cutString) == 3:
        parser(cutString[0], cutString[1], cutString[2])
    elif len(cutString) == 4:
        parser(cutString[0], cutString[1], cutString[2], cutString[3])
    elif len(cutString) == 5:
        parser(cutString[0], cutString[1], cutString[2], cutString[3], cutString[4])
    elif len(cutString) == 6:
        parser(cutString[0], cutString[1], cutString[2], cutString[3], cutString[4], cutString[5])
