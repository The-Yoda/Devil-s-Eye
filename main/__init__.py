import os
import sys
sys.path.append('.')
path = os.path.dirname(os.path.realpath(__file__))
configPath = path + "/conf/"
libPath = path + "/lib/db/"
rootAbsDir = path
rootDir = os.path.basename(path)
__all__ = [configPath, libPath, rootDir]
