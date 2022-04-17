import time
from datetime import datetime

class Tube:
    def __init__(self, name, watering_frequency):
        self.name = name
        self.watering_frequency = watering_frequency
        self.last_date = datetime.now()

    def get_name(self):
        return self.name;
        
    def get_last_date(self):
        return self.last_date;
        
    def get_watering_frequency(self):
        return self.watering_frequency;

    def water(self):
        self.last_date = datetime.now()

def wait_for_second(time_in_seconds):
    while time_in_seconds:
        divmod(time_in_seconds, 60)
        time.sleep(1)
        time_in_seconds -= 1

tubes = []
tubes.append(Tube("tube1", 12));
tubes.append(Tube("tube2", 24));
tubes.append(Tube("tube3", 48));

def writeTubes():
    for tube in tubes:
        print(tube.name, end=' ')
        print(tube.last_date)

    