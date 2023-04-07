

from decouple import config

name = config("NAME", default="uniknown")
print(name)

