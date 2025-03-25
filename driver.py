import subprocess
import sys
def log_message(logger_stdin, message):
    logger_stdin.write(f"{message}\n")
    logger_stdin.flush()
def send_encryption_command(encryption_stdin, command):
    encryption_stdin.write(f"{command}\n")
    encryption_stdin.flush()
def receive_encryption_output(encryption_stdout):
    return encryption_stdout.readline().strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python driver.py <log_file>")
        return
    log_file = sys.argv[1]
    logger_proc = subprocess.Popen(['python', 'logger.py', log_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    encryption_proc = subprocess.Popen(['python', 'encryption.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    log_message(logger_proc.stdin, "START Driver started")

    history = []
    while True:
        print("Commands password, encrypt, decrypt, history, quit")
        command = input("Enter : ").strip().lower()
        log_message(logger_proc.stdin, f"COMMAND {command}")

        if command == "quit":

            send_encryption_command(encryption_proc.stdin, "QUIT")
            log_message(logger_proc.stdin, " river stopped")
            break
        elif command == "password":

            choice = input("string from history: ").strip().lower()
            if choice == "history" and history:

                for i, item in enumerate(history):
                    print(f"{i + 1}: {item}")
                index = int(input(" history item : ")) - 1
                password = history[index]
            else:
                password = input("password : ").strip()
            send_encryption_command(encryption_proc.stdin, f"PASS {password}")
            result = receive_encryption_output(encryption_proc.stdout)
            print(result)

        elif command == "encrypt":

            choice = input("string from history : ").strip().lower()
            if choice == "history" and history:

                for i, item in enumerate(history):
                    print(f"{i + 1}: {item}")
                index = int(input("number of  history item  ")) - 1
                text = history[index]
            else:

                text = input("Enter astring ): ").strip()
                history.append(text)

            send_encryption_command(encryption_proc.stdin, f"ENCRYPT {text}")
            result = receive_encryption_output(encryption_proc.stdout)
            print(result)
            if result.startswith("RESULT"):
                history.append(result.split(" ", 1)[1])

        elif command == "decrypt":

            choice = input(" string from history: ").strip().lower()
            if choice == "history" and history:

                for i, item in enumerate(history):
                    print(f"{i + 1}: {item}")
                index = int(input("history item : ")) - 1
                text = history[index]
            else:

                text = input("Enter string : ").strip()
                history.append(text)

            send_encryption_command(encryption_proc.stdin, f"DECRYPT {text}")
            result = receive_encryption_output(encryption_proc.stdout)
            print(result)
            if result.startswith("RESULT"):
                history.append(result.split(" ", 1)[1])
        elif command == "history":
            print(" strings:")
            for i, item in enumerate(history):
                print(f"{i + 1}: {item}")

    logger_proc.stdin.close()
    logger_proc.wait()
    encryption_proc.stdin.close()
    encryption_proc.wait()


