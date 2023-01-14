import os
import platform
import random
import sys

import eel

# Use latest version of Eel from parent directory
sys.path.insert(1, '../../')

def start_eel(develop):
    """Start Eel with either production or development configuration."""

    if develop:
        eel.init('src')
        eel.start({"port": 3000}, host="localhost", port=8888)
    else:
        eel.init('build')
        eel.start('index.html')


if __name__ == '__main__':
    import sys

    # Pass any second argument to enable debugging
    start_eel(develop=len(sys.argv) == 2)
