import os
import sys
sys.path.append('.')
path = os.path.dirname(os.path.realpath(__file__))
configPath = path + "/conf/"
__all__ = [configPath, 'utils']
