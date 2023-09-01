# String which represents rows in the game, X represents columns
# This is so the level layout can be easily visualized and modified

level_map = [
    '                            E',  # Row with an enemy for testing
    '                            ',  # Row 0 etc
    '                            ',
    '                            ',
    ' XX    XXX            XX    ',
    ' XX P                       ',
    ' XXXX         XX         XX ',
    ' XXXX       XX              ',
    ' XX    X  XXXX    XX  XX    ',
    '       X  XXXX    XX  XXX   ',
    '    XXXX  XXXXXX  XX  XXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXX  '
]

tile_size = 64
screen_width = 1920
screen_height = len(level_map) * tile_size  # Match the screen height to the dimensions of the level
