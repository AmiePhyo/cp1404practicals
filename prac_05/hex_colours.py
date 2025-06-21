COLOR_CODES = {
    "aliceblue": "#F0F8FF",
    "antiquewhite": "#FAEBD7",
    "aqua": "#00FFFF",
    "azure": "#F0FFFF",
    "beige": "#F5F5DC",
    "bisque": "#FFE4C4",
    "black": "#000000",
    "blanchedalmond": "#FFEBCD",
    "blue": "#0000FF",
    "brown": "#A52A2A",
    "cadetblue": "#5F9EA0",
    "cornsilk": "#FFF8DC"
}

max_name_length = max(len(name) for name in COLOR_CODES.keys())
for name, code in COLOR_CODES.items():
    print(f"{name:<{max_name_length}} : {code}")

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        hex_code = COLOR_CODES[color_name]
        print(f"The code for {color_name} is {hex_code}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()