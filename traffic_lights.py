# *****************
# BY INBAR HAWKINS*
# *****************

traffic_lights = {'red': 'green', 'green': 'yellow', 'yellow': 'red'}


def update_light(curr_light):
    while True:
        if curr_light.lower() not in ('red', 'yellow', 'green'):
            curr_light = input("Invalid color. Please try again: ").lower()
        else:
            break
    return traffic_lights[curr_light.lower()]


if __name__ == "__main__":
    print(update_light('YELLOW'))
    print(update_light('green'))
    print(update_light('RED'))
