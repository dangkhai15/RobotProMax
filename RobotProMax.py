
from machine import Pin, PWM
from time import sleep, sleep_ms

# ==================================================
# 1. KHAI BAO CHAN GPIO
# ==================================================

# CAM BIEN IR
IR = Pin(34, Pin.IN)

# L298N - BANG TAI
IN1 = Pin(26, Pin.OUT)
IN2 = Pin(27, Pin.OUT)

# SERVO DE
servo_de = PWM(Pin(13), freq=50)

# SERVO GAP
servo_gap = PWM(Pin(12), freq=50)

# SERVO NANG HA
servo_nang_ha = PWM(Pin(14), freq=50)


# ==================================================
# 2. KHAI BAO VI TRI SERVO
# ==================================================

# SERVO DE
DE_HOME = 90
DE_TRAI = 180

# SERVO GAP (DON VI: us)
GAP_HOME = 1500
GAP_MO = 700
GAP_DONG = 1300

# SERVO NANG HA (DON VI: us)
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

# TOC DO RIENG CHO BUOC 3 VA BUOC 5
NANG_BUOC_NHANH = 40
NANG_DELAY_NHANH = 0.005

CHO_HOME = 1


# ==================================================
# 4. DIEU KHIEN BANG TAI
# ==================================================

def bang_tai_chay():
    IN1.value(1)
    IN2.value(0)


def bang_tai_dung():
    IN1.value(0)
    IN2.value(0)


# ==================================================
# 5. DIEU KHIEN SERVO
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
# 6. DI CHUYEN SERVO DE TU TU
# ==================================================

def di_chuyen_de(goc_dau, goc_cuoi,
                 buoc=DE_BUOC, delay=DE_DELAY):

    if goc_cuoi > goc_dau:
        for goc in range(goc_dau, goc_cuoi + 1, buoc):
            quay_de(goc)
            sleep(delay)

    else:
        for goc in range(goc_dau, goc_cuoi - 1, -buoc):
            quay_de(goc)
            sleep(delay)

    quay_de(goc_cuoi)


# ==================================================
# 7. DI CHUYEN TAY NANG HA
# ==================================================

def di_chuyen_nang_ha(xung_dau, xung_cuoi,
                      buoc=NANG_BUOC, delay=NANG_DELAY):

    if xung_cuoi < xung_dau:
        for us in range(xung_dau, xung_cuoi - 1, -buoc):
            dieu_khien_nang_ha(us)
            sleep(delay)

    else:
        for us in range(xung_dau, xung_cuoi + 1, buoc):
            dieu_khien_nang_ha(us)
            sleep(delay)

    dieu_khien_nang_ha(xung_cuoi)


# ==================================================
# 8. KHOI TAO ROBOT VE HOME
# ==================================================

def ve_home_ban_dau():

    print("\n========== KHOI TAO HOME ==========")

    bang_tai_dung()

    print("DE QUAY VE HOME")
    quay_de(DE_HOME)
    sleep(1)

    print("TAY NANG HA VE HOME")
    dieu_khien_nang_ha(NANG_HOME)
    sleep(1)

    print("DAU GAP VE HOME")
    dieu_khien_gap(GAP_HOME)
    sleep(1)

    print("ROBOT DA KHOI TAO HOME")


# ==================================================
# 9. CHU TRINH GAP VA THA SAN PHAM
# ==================================================

def chu_trinh_gap_hang():

    print("\n========== BAT DAU CHU TRINH ==========")

    # BUOC 1: MO DAU GAP
    print("BUOC 1: MO DAU GAP")
    dieu_khien_gap(GAP_MO)
    sleep(CHO_GAP)

    # BUOC 2: HA TAY XUONG TU TU
    print("BUOC 2: HA TAY XUONG")
    di_chuyen_nang_ha(NANG_HOME, NANG_HA)
    sleep(1)

    # BUOC 3: DONG DAU GAP
    print("BUOC 3: DONG DAU GAP")
    dieu_khien_gap(GAP_DONG)
    sleep(0.5)

    # BUOC 4: NANG TAY LEN TRUNG GIAN - NHANH HON
    print("BUOC 4: NANG TAY LEN TRUNG GIAN")
    di_chuyen_nang_ha(
        NANG_HA,
        NANG_TRUNG_GIAN,
        buoc=NANG_BUOC_NHANH,
        delay=NANG_DELAY_NHANH
    )
    sleep(0.5)

    # BUOC 5: QUAY DE SANG TRAI
    print("BUOC 5: QUAY DE SANG TRAI")
    di_chuyen_de(DE_HOME, DE_TRAI)
    sleep(1)

    # BUOC 6: HA TAY XUONG LAI - NHANH HON
    print("BUOC 6: HA TAY XUONG LAI")
    di_chuyen_nang_ha(
        NANG_TRUNG_GIAN,
        NANG_HA,
        buoc=NANG_BUOC_NHANH,
        delay=NANG_DELAY_NHANH
    )
    sleep(0.5)

    # BUOC 7: MO DAU GAP DE THA SAN PHAM
    print("BUOC 7: THA SAN PHAM")
    dieu_khien_gap(GAP_MO)
    sleep(0.5)

    # BUOC 8: DAU GAP VE HOME
    print("BUOC 8: DAU GAP VE HOME")
    dieu_khien_gap(GAP_HOME)
    sleep(1)

    # BUOC 9: NANG TAY VE HOME
    print("BUOC 9: NANG TAY VE HOME")
    dieu_khien_nang_ha(NANG_HOME)
    sleep(CHO_HOME)

    # BUOC 10: DE QUAY VE HOME
    print("BUOC 10: DE QUAY VE HOME")
    di_chuyen_de(DE_TRAI, DE_HOME)
    sleep(1)

    print("\n========== HOAN THANH CHU TRINH ==========")


# ==================================================
# 10. PHAT HIEN SAN PHAM
# ==================================================

def phat_hien_san_pham():

    if IR.value() == 0:
        sleep_ms(50)

        if IR.value() == 0:
            return True

    return False


# ==================================================
# 11. CHUONG TRINH CHINH
# ==================================================

try:

    print("\n===================================")
    print(" HE THONG GAP HANG TU DONG")
    print("===================================")

    # KHOI TAO ROBOT
    ve_home_ban_dau()

    # BAT DAU CHO BANG TAI CHAY
    print("BANG TAI BAT DAU CHAY")
    bang_tai_chay()

    while True:

        if phat_hien_san_pham():

            print("\nPHAT HIEN SAN PHAM")

            # DUNG BANG TAI
            bang_tai_dung()
            sleep(0.5)

            # ROBOT GAP VA THA SAN PHAM
            chu_trinh_gap_hang()

            print("ROBOT DA VE HOME")

            # BANG TAI CHAY LAI
            print("BANG TAI CHAY LAI")
            bang_tai_chay()

            # CHO SAN PHAM ROI KHOI CAM BIEN
            print("CHO SAN PHAM ROI KHOI CAM BIEN")

            while IR.value() == 0:
                sleep_ms(100)

            sleep_ms(300)

            print("SAN PHAM DA ROI KHOI CAM BIEN")
            print("SAN SANG NHAN SAN PHAM TIEP THEO")

        sleep_ms(50)


except KeyboardInterrupt:

    print("\nNGUOI DUNG DA DUNG HE THONG")


except Exception as loi:

    print("\nCO LOI XAY RA:", loi)


finally:

    bang_tai_dung()
    print("BANG TAI DA DUNG")
