import sys, time, getpass
from base64 import b64decode

# Style ( Colors ) 
if sys.platform != "win32": R = '\033[1;31m'; T = '\033[1;33m'; B = '\033[1;34m'; G = '\033[1;32m'; W = '\033[1;37m'; U = '\033[1;4m'; F = '\033[1;7m'; N = '\033[0m'
else: R = T = B = G = W = U = F = N = str()

class Printer(object):
    """
    Prints Messages for anthor types  
    """
    def Mypass(self):
        """
        Utilities to get a password and/or the current user name.
        """
        mypass = getpass.getpass("%s[ * ]%s Password:" % (B, N))
        
        # Decode the Base64 encoded bytes-like object or ASCII string s.
        if mypass == b64decode("YWRtaW4K").decode().replace("\n", ""):  
            self.echo("\t%s->%s\t%sList Go\t%s!\n\n\n" % (T, N, G, T))
        else:
            self.echo("\t%s->%s\t%sError Password%s\n\n\n" % (R, N, W, N))
            sys.exit(0)

    def write(self, data: str, Time: int):
        for i in data + '\n':
            # Write string to stream.
            # Returns the number of characters written 
            # (which is always equal to the length of the string).
            sys.stdout.write(i)

            # This is not implemented for read-only and non-blocking streams. 
            sys.stdout.flush()

            # Delay execution for a given number of seconds.
            # The argument may be a floating point number for subsecond precision.
            time.sleep(Time / 100) 

    def print_index(self, name: str):
        print("%s%s%s" % (B, '--' * 20, N))
        self.write("%s\t\t%s\t%s" % (T, name, N), 5)
        print("%s%s%s" % (B, '--' * 20, N))

    def print_error(self, name: str, data: str): print("%s[ - ] %s %s : %s" % (R, N, name, data))

    def print_title(self, name: str): print("\n%s[ * ] %s %s :\n%s" % (B, N, name, '-' * (len(name) + 9)))

    def print_out1(self, name: str, data: str): print("\n%s[ + ] %s %s : %s" % (G, N, name, data))

    def print_out2(self, name: str, data: str): print("\t%s -> %s%s : %s" % (T, N, name, data))

    def echo(self, args): print(args)
        