
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys # use this to get the name of the log file
import time # allows us to get the current date and time

def log_message(log_file, action, message): # takes 3 arguments, log file, action and message
    stamp = time.strftime(' %Y-%m-%d %H:%M') # strftime takes time object and turns it into strings
    with open(log_file,'a') as f: # with open opens the file and automatcily closes after code executed
        f.write(f"{stamp} [{action}] {message}\n") # writes the time, action and mesage in this order

def main():
    log_file = sys.argv[1]
    log_message(log_file,"START", "logging started") #logging has started
    while True: # program constantly checks for input
        read = input().strip() # takes in the lines from user and strip() cleans any extra spaces
        if read == "QUIT":
            log_message(log_file,"QUIT", "logging finished")
            break
    if len(read.split(" ",1)) ==2: #split
        action,message = read.split(" ",1)
        message(log_file,action,message)

    if __name__ == "__main__":
        main()
