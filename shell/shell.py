#!/usr/bin/python3

import os
import sys
import res


#method to accept input
def main():
    while True:
        command = input("$ ")
        args = command.split()
        
        if command == "exit":
            break
        elif command == "help":
            print("Type 'exit' to exit. That is all.")

        elif args[0] == "cd":
                try:
                    os.chdir(args[1])
                except FileNotFoundError:
                    print("cd "+args[1]+". File or directory not found.")

        elif "|" in args:
            print("Going to pipes")
            handle_pipes(command)

        elif not in command:
            #empty input. Nothing to do
        
        else:
            execute(command)
    sys.exit(1)
    
def execute(command):    
    pid = os.fork()

    if pid < 0:
        print("Fork failure")
        sys.exit(1)
    
    
def handle_pipes(command):
    
    r, w = os.pipe()

    pid = os.fork()

    if pid < 0:
        print("Fork failure")
        sys.exit(1)

    elif pid >0:
        #parent
        
    else:
        #child

        args = command.split()
        if args[0] == "ls":
            
