

class battery:
    capacity_kwh = 3.0
    maxcharge_kw = 3.0
    maxdischarge_kw = 3.0
    capacitynow_kwh = 0.0

    def __init__(self, current_kwh, initcapacity_kwh):
        self.capacity_kwh = initcapacity_kwh
        self.capacitynow_kwh = current_kwh 

    def init_percent(self, percent, initcapacity_kwh):
        if (0 <= percent <= 100):
            self.capacity_kwh = initcapacity_kwh
            self.capacitynow_kwh = initcapacity_kwh * percent / 100
            return 0
        else:
            return -1
        
    def getPercent(self):
        if self.capacitynow_kwh > self.capacity_kwh:
            return -1
        return self.capacitynow_kwh / self.capacity_kwh
    
    def batterytick(self, kwdraw, minutes):
        if kwdraw > maxdischarge_kw:
            kwdraw = maxdischarge_kw
        if kwdraw < -maxcharge_kw:
            kwdraw = maxcharge_kw
        self.capacitynow_kwh += kwdraw/60*minutes
            