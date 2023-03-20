import os
import sys
import json
import re


def _get_screen_size():
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        print("Пожалуйста, установите ADB и диск и настройте переменную среды")
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
    return "1920x1080"