import ctypes


def get_screen_coordinates():
    """
    Return a tuple -> (width, height)
    """
    user32 = ctypes.windll.user32
    return (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))


if __name__ == "__main__":
    print(get_screen_coordinates())
