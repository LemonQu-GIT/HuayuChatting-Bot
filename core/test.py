import subprocess
import os
from send import send_msg
import subprocess
output = subprocess.getstatusoutput('ping')[1]     
print(output)
send_msg({'msg_type': 'private', 'number': 173887664, 'msg': output})