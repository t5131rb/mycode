#!/usr/bin/env python3

# import shutil module
import shutil

# import os module
import os

# start in home directory
os.chdir("/home/student/mycode/")

# copy the source file to the destination folder
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy entire source directory to the destination directory
shutil.copytree("5g_research/", "5g_research_backup/")


