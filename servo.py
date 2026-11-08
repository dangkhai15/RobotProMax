
from machine import Pin, PWM

# ==================================================
# 1. KHAI BAO SERVO
# ==================================================

# SERVO DE
servo_de = PWM(Pin(18), freq=50)

# SERVO GAP
servo_gap = PWM(Pin(19), freq=50)

# SERVO NANG HA
servo_nang_ha = PWM(Pin(21), freq=50)

# SERVO DUOI
ser_duoi = PWM(Pin(22), freq=50)


# ==================================================
# 2. KHAI BAO VI TRI SERVO
# ==================================================

# SERVO DE
DE_HOME = 90
DE_TRAI = 180

# SERVO GAP (us)
GAP_HOME = 1500
GAP_MO = 700
GAP_DONG = 1300

# SERVO NANG HA (us)
NANG_HOME = 1000
NANG_HA = 500
NANG_TRUNG_GIAN = 700


# ==================================================
# 3. THONG SO TOC DO
# ==================================================

CHO_GAP = 1

DE_BUOC = 1
DE_DELAY = 0.015

NANG_BUOC = 20
NANG_DELAY = 0.01

NANG_BUOC_NHANH = 40
NANG_DELAY_NHANH = 0.005

CHO_HOME = 1


# ==================================================
# 4. CAC HAM DIEU KHIEN SERVO
# ==================================================

def dat_xung(servo, us):
    duty = int(us * 65535 / 20000)
    servo.duty_u16(duty)


def quay_de(goc):
    duty = int(1638 + (goc / 180) * 6553)
    servo_de.duty_u16(duty)


def dieu_khien_gap(us):
    dat_xung(servo_gap, us)


def dieu_khien_nang_ha(us):
    dat_xung(servo_nang_ha, us)


# ==================================================
# 5. DI CHUYEN SERVO DE TU TU
# ==================================================

def di_chuyen_de(goc_dau, goc_cuoi,
                 buoc=DE_BUOC, delay=DE_DELAY):

    if goc_cuoi > goc_dau:
        for goc in range(goc_dau, goc_cuoi + 1, buoc):
            quay_de(goc)
            from time import sleep
            sleep(delay)

    else:
        for goc in range(goc_dau, goc_cuoi - 1, -buoc):
            quay_de(goc)
            from time import sleep
            sleep(delay)

    quay_de(goc_cuoi)


# ==================================================
# 6. DI CHUYEN TAY NANG HA
# ==================================================

def di_chuyen_nang_ha(xung_dau, xung_cuoi,
                      buoc=NANG_BUOC,
                      delay=NANG_DELAY):

    from time import sleep

    if xung_cuoi < xung_dau:
        for us in range(xung_dau, xung_cuoi - 1, -buoc):
            dieu_khien_nang_ha(us)
            sleep(delay)

    else:
        for us in range(xung_dau, xung_cuoi + 1, buoc):
            dieu_khien_nang_ha(us)
            sleep(delay)

    dieu_khien_nang_ha(xung_cuoi)
