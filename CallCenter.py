import time

class Call(object):
    def __init__(self, callerID, name, number, time, reason):
        self.id = callerID
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display():
        print self.id = callerID
        print self.name = name
        print self.number = number
        print self.time = time
        print self.reason = reason

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def add(self, callerID, name, number, reason):
        self.calls.append(Call(callerID, name, number, time.localtime()[3] + (float(time.localtime()[4]) / 100), reason))
        self.queue += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue -= 1
        return self
    def removeNumber(self, number):
        for i in range(0, len(self.calls)):
            if self.calls[i].number == number:
                self.calls.pop(i)
                self.queue -= 1
                return self
        print "Could not locate call"
    def sortCalls(self):
        self.calls = sorted(self.calls, key=lambda call: call.time)