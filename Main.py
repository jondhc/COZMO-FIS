import time
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.util import degrees, Pose

robot = cozmo.robot.Robot


def say_text(robot: cozmo.robot.Robot):
    print("Saying text")
    x = input("What do you want cozmo to say?")
    robot.say_text(x).wait_for_completed()


def drive_straight(robot: cozmo.robot.Robot):
    print("Driving straight")
    distance = int(input("Distance: "))
    speed = int(input("Speed: "))
    robot.drive_straight(distance_mm(distance), speed_mmps(speed)).wait_for_completed()


def turn_in_place(robot: cozmo.robot.Robot):
    print("Turning in place")
    degrees_ = int(input("Degrees: "))
    robot.turn_in_place(degrees(degrees_)).wait_for_completed()


def drive_in_square(robot: cozmo.robot.Robot):
    print("Driving in square")
    # Use a "for loop" to repeat the indented code 4 times
    # Note: the _ variable name can be used when you don't need the value
    for _ in range(4):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()

def move_head_(robot: cozmo.robot.Robot):
    print("Moving head")
    radiansps = input("Radians per second: ")
    robot.move_head(radiansps)
    time.sleep(9)

def move_lift_(robot: cozmo.robot.Robot):
    print("Moving lift")
    radiansps = input("Radians per second: ")
    robot.move_lift(radiansps)
    time.sleep(3)

def drive_wheels_(robot: cozmo.robot.Robot):
    print("Driving wheels motors")
    leftwheelspeed = input("Left wheel speed: ")
    rightwheelspeed = input("Right wheel speed: ")
    robot.drive_wheels(leftwheelspeed, rightwheelspeed)
    time.sleep(9)

def roomcreation(robot: cozmo.robot.Robot):
    initialPosition = 0
    origin1 = robot.world.create_custom_fixed_object(Pose(100, initialPosition-100, 0, angle_z=degrees(0)),100, 100, 100, relative_to_robot=True)
    origin2 = robot.world.create_custom_fixed_object(Pose(100,0, initialPosition, angle_z=degrees(0)), 100, 100, 100,
                                                    relative_to_robot=True)
    origin3 = robot.world.create_custom_fixed_object(Pose(100, initialPosition+100, 0, angle_z=degrees(0)), 100, 100, 100,
                                                    relative_to_robot=True)

    target1 = robot.world.create_custom_fixed_object(Pose(-300, initialPosition-100, 0, angle_z=degrees(0)), 100, 100, 100,
                                                     relative_to_robot=True)
    target2 = robot.world.create_custom_fixed_object(Pose(-300, initialPosition, 0, angle_z=degrees(0)), 100, 100, 100,
                                                     relative_to_robot=True)
    target3 = robot.world.create_custom_fixed_object(Pose(-300, initialPosition+100
                                                          , 0, angle_z=degrees(0)), 100, 100, 100,
                                                     relative_to_robot=True)

    if origin1 and origin2 and origin3:
        print("Created origins succesfully")
        robot.go_to_pose(Pose(100, 0, 0, angle_z=degrees(180)), relative_to_robot=True).wait_for_completed()
    if target1 and target2 and target3:
        print("Created targets succesfully")
        robot.go_to_pose(Pose(300, 0, 0, angle_z=degrees(180)), relative_to_robot=True).wait_for_completed()

##########################################
# program = say_text
# program = drive_straight
# program = turn_in_place
# program = drive_in_square
# program = move_head_
# program = move_lift_
# program = drive_wheels_
# program = roomcreation, use_3d_viewer=True


cozmo.run_program(roomcreation, use_3d_viewer=True)
