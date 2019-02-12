#!/usr/bin/env python3

"""
@Author:	Andreas Maeurer
@Created:	11/15/2018
@Modified:	11/15/2018
@Scope:		A simple script to fix Spanish Devotions file names.

Example ->
	The files arrive in the format: med20181201_01.mp3
	The files are formated to: med20181201.mp3
	
With this script a batch of files are renamed all at once.
(The author is aware of multiple high quality ways to accomplish this task on both Windows and Linux)
	
@Tested:	runs on Ubuntu without problem
@Question:	Will it run on Windows10? What dependencies would this script have on Windows10?
"""

import os

for filename in os.listdir("."):
	if filename.startswith("med"):
		os.rename(filename, filename[:11]+".mp3")
