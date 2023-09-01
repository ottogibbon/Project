# string which represents rows in my game, X represents collums
# This is so I can see exactly how my level is displayed


level_map = [
    '                            E',  # row with an enemy for testing
'                            ', # row 0 etc
'                            ',
'                            ',
' XX    XXX            XX    ',
' XX P                       ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

tile_size = 64
screen_width = 1920
screen_height = len(level_map) * tile_size # so my screen height matches the computer dimensions it's run on
