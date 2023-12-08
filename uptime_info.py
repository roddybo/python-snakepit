import os
system_uptime = os.popen ('uptime') .read()[:-1]
print (system_uptime)
