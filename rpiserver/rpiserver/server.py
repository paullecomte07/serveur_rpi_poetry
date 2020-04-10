from fastapi import FastAPI
from pydantic import BaseModel
try:
    import RPi.GPIO as GPIO
except RuntimeError as e:
    from .Dummypi import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



class Comment(BaseModel):
    pseudo : str
    comment : str


class Led(BaseModel):
    id : int
    gpio : int
    is_on : bool = False
    color : str

    def init(self):
        GPIO.setup(self.gpio, GPIO.OUT)
        return self
    def turnOn(self):
        GPIO.output(self.gpio, GPIO.HIGH)
        self.is_on = True
    def turnOff(self):
        GPIO.output(self.gpio, GPIO.LOW)
        self.is_on = False




db = []



led_app = FastAPI()


@led_app.post("/led/create", response_model=Led)
def create_led(led: Led):
    led.init()
    db.append(led)
    return led

@led_app.get("/led/{led_id}", response_model=Led)
def get_led(led_id: int):
    for i in db:
        if i.id ==led_id:
            return i

@led_app.post("/led/{led_id}/on")
def turnOn(led_id:int):
    for i in db:
        if i.id == led_id:
            i.turnOn()
            return i

@led_app.post("/led/{led_id}/off")
def turnOff(led_id:int):
    for i in db:
        if i.id == led_id:
            i.turnOff()
            return i

