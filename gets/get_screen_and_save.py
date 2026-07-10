import importlib
import subprocess
import sys
import os
import time
from pathlib import Path

def import_install(module: str):
    try:
        importlib.import_module(module)
    except ModuleNotFoundError:
        subprocess.check_call(
            [f"{sys.executable}", "-m", "pip", "install", f"{module}"]
        )
        importlib.invalidate_caches()
        importlib.import_module(module)

import_install("mss")
import mss

def record_screen(duration_seconds, witch_monitor=1, output_dir='frames'):
    os.makedirs(output_dir, exist_ok=True)

    frames = []
    frames_in_total = 0

    with mss.MSS() as sct:
        monitor = sct.monitors[witch_monitor]
        start = time.time()

        while time.time() - start < duration_seconds:
            screenshot = sct.grab(monitor)
            frames.append(screenshot)

    for i, frame in enumerate(frames):
        frames_in_total += 1
        mss.tools.to_png(frame.rgb, frame.size, output=f'{output_dir}/frame_{i:05d}.png')

    return frames_in_total

if os.path.exists(f"{Path(__file__).resolve().parent}\\times.txt"):
    with open(f"{Path(__file__).resolve().parent}\\times.txt", "r") as file:
        t = file.readlines()
        for ti in t:
            time = ti
else:
    time = 2

with mss.MSS() as sct:
    for i, monitor in enumerate(sct.monitors):
        print(f"on monitor: {i}/{monitor} \n               recording {time} secends")
        for frame in range(record_screen(time, i)):
            print(f"on monitor: {i}/{monitor} \n               have recorded {frame} frames so far")

with open(f"{Path(__file__).resolve().parent}\\frames\\done.txt", "w") as file:
    file.write("laiuehrgliauehrgkyuaehrgkuhjeanriguaneriygbargbaeirgnaeiyrgh")

print()
print()
print()
print("                            DONE")
input("")
