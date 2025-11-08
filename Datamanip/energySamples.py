import time


class energySamples:
    timestamp = 0
    sample = 0

    def __init__(self,time,samp):
        self.timestamp = time
        self.sample = samp

    def adverageSamples(samp = [], length = 0):
        adv = 0
        for i in range (0, length):
            adv += samp[i]
        return adv