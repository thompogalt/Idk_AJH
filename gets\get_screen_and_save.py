import importlib
import subprocess
import sys
import os
import time

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

with mss.MSS() as sct:
    for i, monitor in enumerate(sct.monitors):
        print(f"on monitor: {i}/{monitor} \n               recording 2 secends")
        for frame in range(record_screen(2, i)):
            print(f"on monitor: {i}/{monitor} \n               have recorded {frame} frames so far")

print()
print()
print()
print("                            DONE")
input("")
