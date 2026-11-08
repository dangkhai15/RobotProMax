
from machine import Pin

# ==================================================
# 1. KHAI BAO CHAN L298N
# ==================================================

IN1 = Pin(26, Pin.OUT)
IN2 = Pin(27, Pin.OUT)


# ==================================================
# 2. DIEU KHIEN BANG TAI
# ==================================================

def bang_tai_chay():
    IN1.value(1)
    IN2.value(0)


def bang_tai_dung():
    IN1.value(0)
    IN2.value(0)
