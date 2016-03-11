TUBE_AMOUNT = 6
TUBE_GROUP_COUNT = 2

BROWN = (165, 42, 42)
TURQUOISE = (64, 244, 208)
BLUE = (0, 0, 255)
ORANGE = (255, 27, 0)
HOT_PINK = (255, 105, 180)
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

O_OFF = 0
O_SINE = 1
O_SQUARE = 2
O_TRIANGLE = 3
O_SAW_UP = 4
O_SAW_DOWN = 5

O_SPEED = {
    "1/16": 0,
    "1/8": 1,
    "3/16": 2,
    "1/4": 3,
    "3/8": 4,
    "1/2": 5,
    "3/4": 6,
    "1": 7,
    "2": 8,
    "3": 9,
    "4": 10,
    "6": 11,
    "8": 12,
    "12": 13,
    "16": 14,
    "24": 15
}


# Oscillator tuple has following int or float values
# (TYPE, AMOUNT, CHASE, SPEED, SHAPE)
# TYPE -> 0=disabled, 1=sine, 2=square, 3=triangle, 4=saw up, 5=saw down
# AMOUNT -> float 0.0 - 1.0
# Chase -> float 0.0 - 1.0
# Chase -> float 0.0 - 1.0
# Chase -> float 0.0 - 1.0
# Chase -> float 0.0 - 1.0


# (TYPE, AMOUNT, CHASE, SPEED, SHAPE)
OSCILLATOR_OFF = (O_OFF, 0, 0, 0, 0)
OSCILLATOR_SINE = (O_SINE, 1.0, 0.5, O_SPEED["1"], 0.3)

# The map has the value is this format:
# [ RGB_TUPLE, CHANNEL_VALUE_TUPLE, OSC_VALUE_TUPLE]
# for example
# [ (50, 100, 0), (1, 0.5, 0.2, 3, 0.7, False) ]


BROWN = (165, 42, 42)
TURQUOISE = (64, 244, 208)
BLUE = (0, 0, 255)
ORANGE = (255, 27, 0)
HOT_PINK = (255, 105, 180)
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

COLOR_TABLE = {
    "BLUE": BLUE,
    "TURQUOISE": TURQUOISE,
    "BROWN": BROWN,
    "ORANGE": ORANGE,
    "HOT_PINK": HOT_PINK,
    "PURPLE": PURPLE,
    "WHITE": WHITE,
    "YELLOW": YELLOW,
    "RED": RED,
    "GREEN": GREEN
}

FX_TABLE = {
    # "gay_rainbow": ((0, 0, 0), (1, 0.5, 0.2533333, 7, 0.5))
}

FX_TABLE_MULTI = {
    "fancy_pancy": {
        "r": (126, (1, 1.0, 0.0, 5, 0.0)),
        "g": (126, (1, 1.0, 0.44666659832000732, 5, 0.0)),
        "b": (126, (1, 1.0, 0.89333319664001465, 5, 0.0))

    },
    "trippy_party": {
        "r": (100, OSCILLATOR_SINE),
        "g": (123, OSCILLATOR_SINE),
        "b": (5, OSCILLATOR_SINE)
    },
    "super_gay": {
        "g": (0, (1, 0.5, 0.2533333, 7, 0.5)),
        "r": (0, (1, 0.5, 0.2533333, 7, 0.5)),
        "b": (0, (1, 0.5, 0.2533333, 7, 0.5))
    },
    "blue-with-white": {
        "r": (0, (2, 0.2333, 0.0767, 7, 0.26)),
        "g": (11, (2, 0.2333, 0.5267, 7, 0.26)),
        "b": (240, (0, 0, 0, 0, 0))
    },
    "blue-sparkly": {
        "r": (0, (0, 0, 0, 0, 0)),
        "g": (0, (0, 0, 0, 0, 0)),
        "b": (255, (2, 0.9967, 0.7033, 4, 0.1567))
    },
    "blue-cyan": {
        "g": (254, (1, 1.0, 0.02, 5, 0.9933)),
        "r": (0, (0, 0, 0, 0, 0)),
        "b": (252, (0, 0, 0, 0, 0))
    },
    "cyan-green": {
        "g": (252, (0, 0, 0, 0, 0)),
        "r": (0, (0, 0, 0, 0, 0)),
        "b": (254, (1, 1.0, 0.02, 5, 0.9933))
    },
    "cyan-white": {
        "g": (244, (0, 0, 0, 0, 0)),
        "r": (0, (1, 1.0, 0.01, 5, 0.0133)),
        "b": (208, (0, 0, 0, 0, 0))
    },

    "purple-white": {
        "r": (254, (0, 0, 0, 0, 0)),
        "g": (0, (1, 0.5, 0.05, 7, 0.4767)),
        "b": (72, (1, 0.053333, 0.1266, 7, 0.5))
    },
    "purple-white-down": {
        "r": (255, (0, 0, 0, 0, 0)),
        "g": (255, (2, 1.0, 0.0131, 4, 0.32)),
        "b": (255, (0, 0, 0, 0, 0))
    },
    "purple-animated": {
        "r": (254, (1, 1.0, 0.02, 5, 0.9933)),
        "g": (0, (0, 0, 0, 0, 0)),
        "b": (252, (0, 0, 0, 0, 0))
    },
    "purple-with-red-chase": {
        "r": (255, (4, 0.99, 0.2233, 3, 0.02)),
        "g": (0, (0, 0, 0, 0, 0)),
        "b": (255, (4, 0.99, 0.0483, 3, 0.02))
    },
    "purple-with-green-flash": {
        "r": (128, (1, 0.0533, 0.6726, 7, 0.5)),
        "g": (112, (5, 1.0, 0.4926, 5, 0.5)),
        "b": (128, (1, 0.5, 0.65, 7, 0.4767))
    },
    "green-animated": {
        "r": (0, (0, 0, 0, 0, 0)),
        "g": (2, (2, 1.0, 0.0131, 4, 0.32)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "green-blink": {
        "g": (255, (2, 0.9967, 0.7033, 4, 0.1567)),
        "r": (0, (0, 0, 0, 0, 0)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "green-lime": {
        "g": (255, (0, 0, 0, 0, 0)),
        "r": (0, (0, 0, 0, 0, 0)),
        "b": (43, (1, 0.1067, 0.0133, 7, 0.0733))
    },
    "green-slow": {
        "r": (240, (0, 0, 0, 0, 0)),
        "g": (0, (2, 0.2333, 0.6033, 7, 0.26)),
        "b": (11, (2, 0.2333, 0.0767, 7, 0.26))
    },
    "pink-hot": {
        "r": (240, (0, 0, 0, 0, 0)),
        "g": (0, (0, 0, 0, 0, 0)),
        "b": (11, (0, 0, 0, 0, 0))
    },
    "rainbow_candy": {
        "r": (11, (2, 0.9467, 0.3233, 7, 0.7533)),
        "g": (11, (2, 0.9467, 0.0, 7, 0.7533)),
        "b": (11, (2, 0.9467, 0.3233, 7, 0.7533))
    },
    "rainbow_colourful": {
        "r": (0, (1, 0.9467, 0.38, 7, 0.0567)),
        "g": (0, (1, 0.9467, 0.0, 7, 0.0567)),
        "b": (0, (1, 0.9467, 0.38, 7, 0.0567))
    },
    "rainbow_all-colors-changing": {
        "r": (255, (1, 1.0, 0.6674, 5, 0.0533)),
        "g": (255, (1, 1.0, 0.3326, 5, 0.0533)),
        "b": (255, (1, 1.0, 0.612, 5, 0.0533))
    },
    "red-with-purple-and-yellow": {
        "r": (240, (0, 0, 0, 0, 0)),
        "g": (0, (2, 0.2333, 0.6033, 7, 0.26)),
        "b": (11, (2, 0.2333, 0.0767, 7, 0.26))
    },
    "red-animated": {
        "r": (0, (1, 1.0, 0.0146, 2, 0.6933)),
        "g": (0, (0, 0, 0, 0, 0)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "red-blink": {
        "r": (255, (2, 0.9967, 0.7033, 4, 0.1567)),
        "g": (0, (0, 0, 0, 0, 0)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "red-white": {
        "r": (0, (3, 1.0, 0.02, 3, 0.5)),
        "g": (0, (0, 0, 0, 0, 0)),
        "b": (0, (3, 1.0, 0.44, 3, 0.5))
    },
    "strobe-fast": {
        "r": (0, (2, 1.0, 0.0, 0, 0.5)),
        "g": (0, (2, 1.0, 0.0, 0, 0.5)),
        "b": (0, (2, 1.0, 0.0, 0, 0.5))
    },
    "strobe-slow": {
        "r": (0, (2, 1.0, 0.0, 3, 0.5)),
        "g": (0, (2, 1.0, 0.0, 3, 0.5)),
        "b": (0, (2, 1.0, 0.0, 3, 0.5))
    },
    "orange-animated": {
        "r": (255, (0, 0, 0, 0, 0)),
        "g": (43, (1, 0.1067, 0.0133, 7, 0.0733)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "orange-sunrise": {
        "r": (255, (1, 0.6733, 0.0067, 8, 0.37)),
        "g": (27, (0, 0, 0, 0, 0)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "orange-yellow-blink": {
        "r": (255, (0, 0, 0, 0, 0)),
        "g": (1, (2, 0.9967, 0.1367, 5, 0.0667)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "yellow-white": {
        "r": (255, (0, 0, 0, 0, 0)),
        "g": (255, (0, 0, 0, 0, 0)),
        "b": (255, (2, 1.0, 0.0131, 4, 0.32))
    },
    "yellow-with-orange": {
        "r": (252, (0, 0, 0, 0, 0)),
        "g": (254, (1, 1.0, 0.02, 5, 0.9933)),
        "b": (0, (0, 0, 0, 0, 0))
    },
    "white-beams": {
        "r": (0, (3, 1.0, 0.02, 3, 0.5)),
        "g": (0, (3, 1.0, 0.02, 3, 0.5)),
        "b": (0, (3, 1.0, 0.42, 3, 0.5))
    }

}
