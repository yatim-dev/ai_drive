import os

from views.start_window import StartWindow

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    StartWindow(config_path)
