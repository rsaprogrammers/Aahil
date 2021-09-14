#AAHIL-------CODING-----

import platform, os

bit=platform.architecture()[0]

try:

    import requests

except ImportError:

    os.system("pip2 install requests")

if bit=="64bit":

    import freeb

    freeb.read()

elif bit=="32bit":

    import frees

    frees.read()
