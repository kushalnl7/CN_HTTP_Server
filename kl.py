# import os
# import pathlib
# print(os.path.getmtime("CN/Project/access.log"))
# print(pathlib.Path.stat("access.log"))

import os.path, time
k = time.ctime(os.path.getmtime("CN/Project/access.log"))
print(k[0:3], k[4:7], k[9], k[11:19], k[20:24])
