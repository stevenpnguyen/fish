import os
import sys

BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
GAME_PATH = os.path.join(BASE_DIR, "fish.py")

os.chdir(BASE_DIR)
sys.argv = [sys.argv[0], GAME_PATH]

from pgzero.runner import main

main()
