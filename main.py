def on_forever():
    if input.compass_heading() == 0:
        basic.show_arrow(ArrowNames.NORTH)
    elif input.compass_heading() == 45:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif input.compass_heading() == 90:
        basic.show_arrow(ArrowNames.EAST)
    elif input.compass_heading() == 135:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif input.compass_heading() == 180:
        basic.show_arrow(ArrowNames.SOUTH)
    elif input.compass_heading() == 225:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif input.compass_heading() == 270:
        basic.show_arrow(ArrowNames.WEST)
    elif input.compass_heading() == 315:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    else:
        basic.show_icon(IconNames.SMALL_DIAMOND)
basic.forever(on_forever)
