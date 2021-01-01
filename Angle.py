class Angle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

        number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


if __name__ == "__main__":
    obj1 = Angle(90, 30, 60)
    c_angles = obj1.check_angles()
    print(c_angles)

    obj2 = Angle(90, 30, 60)
