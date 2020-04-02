from fastapi import FastAPI
from pydantic import BaseModel
try:
    import RPi.GPIO as GPIO
except RuntimeError as e:
    from .Dummypi import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




class Valve(BaseModel):
    gpio : int
    is_open : bool = False

def init(self):
        GPIO.setup(self.gpio, GPIO.OUT)
        return self
def open(self):
        GPIO.output(self.gpio, GPIO.HIGH)
        self.is_open = True
def close(self):
        GPIO.output(self.gpio, GPIO.LOW)
        self.is_open = False


valve = Valve(gpio=19).init()





valve_app = FastAPI()
@valve_app.on_event("shutdown")
def close_valves():
    valve.close()
@valve_app.get("/valves/open", response_model=Valve)
def open_valve(id:int):
    valve.open()
    return valve
@valve_app.get("/valves/close", response_model=Valve)
def close_valve():
    valve.close()
    return valve
