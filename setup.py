import os
import re

def get_version():
    with open(os.path.join("golden_spices", "__init__.py")) as f:
        content = f.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", content).group(1)
