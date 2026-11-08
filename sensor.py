
from machine import Pin
from time import sleep_ms

# ==================================================
# 1. KHAI BAO CAM BIEN IR
# ==================================================

IR = Pin(34, Pin.IN)


# ==================================================
# 2. PHAT HIEN SAN PHAM
# ==================================================

def phat_hien_san_pham():

    if IR.value() == 0:
        sleep_ms(50)

        if IR.value() == 0:
            return True

    return False


# ==================================================
# 3. KIEM TRA SAN PHAM ROI KHOI CAM BIEN
# ==================================================

def cho_san_pham_roi():

    while IR.value() == 0:
        sleep_ms(100)

    sleep_ms(300)
