from colorama import Fore, Style

def cprint(text: str, color: str):
    """
    Prints text in a specified color.

    Args:
        text (str): The text to print.
        color (str): The color to print the text in.
    """
    colors = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }

    if color not in colors:
        raise ValueError(f"Invalid color: {color}")

    print(colors[color] + text + Style.RESET_ALL)
