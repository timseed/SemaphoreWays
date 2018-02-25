import fcntl


class Lock:

    def __init__(self, filename):
        self.filename = filename
        # This will create it if it does not exist already
        self.handle = open("/tmp/"+filename, 'w')

    def acquire(self):
        try:
            rv= fcntl.flock(self.handle,fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except IOError:
            return False

    def release(self):
        #print("Releasing Lock")
        try:
            fcntl.flock(self.handle, fcntl.LOCK_UN)
        except Exception as err:
            print("Problem {}".format(str(err)))

    def __del__(self):
        self.handle.close()


