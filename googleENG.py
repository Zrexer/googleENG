#!/usr/bin/env python3
"""
[+] Google Searcher [+]

_< Search the Query in Google By Python >_

DEV#Host1let => R3D\|/R00m


License :

Copyright (c) 2023 R3D\|/R00m Host1let: googleENG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os 
import pystyle
import googlesearch
import requests
import sys
import time

os.system("")

class Box:
    def __init__(self,
                 msg: str = None
                 ) -> None:
        
        self.msg = msg
        self.writer = pystyle.Write.Print
        self.colors = pystyle.Colors
    
    @property
    def infoMessageBox(self):
        
        self.writer('[{}] [{}] {}'.format(time.strftime('%H:%M:%S'), "INFO", self.msg), self.colors.green_to_red, 0)
        print()
    
    @property
    def errorMessageBox(self):
        
        self.writer('[{}] [{}] {}'.format(time.strftime('%H:%M:%S'), "ERROR", self.msg), self.colors.red_to_yellow, 0)
        print()
     
    @property   
    def warningMessageBox(self):
        
        self.writer('[{}] [{}] {}'.format(time.strftime('%H:%M:%S'), "WARNING", self.msg), self.colors.yellow_to_green, 0)
        print()
    
    @property
    def findMessageBox(self):
        
        self.writer('[{}] [{}] {}'.format(time.strftime('%H:%M:%S'), "FIND", self.msg), self.colors.purple_to_blue, 0)
        print()
    
    @property
    def bannerMode(self):
        
        self.writer(self.msg, self.colors.purple_to_blue, 0)
        print()
    
    @property
    def createDash(self):
        
        self.writer('--------------------------------------------', self.colors.green_to_yellow, 0)
        print()
    
    def nullPrint():
        print("")

writer = pystyle.Write.Print
colors = pystyle.Colors
box = Box
lis = sys.argv

banner = """
                                      _____    _     _     __  
                            /         /    '   /|   /    /    )
----__----__----__----__---/----__---/__------/-| -/----/------
  /   ) /   ) /   ) /   ) /   /___) /        /  | /    /  --,  
_(___/_(___/_(___/_(___/_/___(___ _/____ ___/___|/____(____/___
    /                 /                                        
(_ /              (_ /   

                    
                    {}

""".format('#DEV:Host1let')




box(banner).bannerMode
box.nullPrint()

if len(lis) == 1:
    box('Faild: googleENG --help').errorMessageBox
    
if "--help" in lis:
    box('''Arguments: -q, -r, --check-connection
-q : query -> googleENG -q how i learn python?
-r : results -> googleENG -q how i learn python? -r 20 [default on 10]
--check-connection -> googleENG --check-connection 
''').infoMessageBox

if "-q" in lis:
    if lis[-2] == '-r':
        results = lis[lis.index('-r')+1]
        query = lis[lis.index('-q'):]
        query.remove('-q')
        query.remove('-r')
        query.remove(results)
        
        char = ''
        
        for c in query:
            char += f'{c} '
        
        box.createDash
        
        for sea in googlesearch.search(char, int(results)):
            box(sea).findMessageBox
    
    else:
        query = lis[lis.index('-q'):]
        query.remove('-q')
        query.remove('-r')
        
        char = ''
        
        for c in query:
            char += f'{c} '
        
        box.createDash
        
        for sea in googlesearch.search(char):
            box(sea).findMessageBox

if "--check-connection" in lis:
    reqData = requests.get('https://github.com/Zrexer').status_code
    
    if str(reqData) == "200":
        box('system is online').infoMessageBox
        
    else:
        box('system is offline').warningMessageBox
        box('you cannot use script, please first connect to internet and try again').errorMessageBox
    
    
