
from time import sleep

from servo import (
    DE_HOME,
    DE_TRAI,
    GAP_HOME,
    GAP_MO,
    GAP_DONG,
    NANG_HOME,
    NANG_HA,
    NANG_TRUNG_GIAN,
    NANG_BUOC_NHANH,
    NANG_DELAY_NHANH,
    CHO_GAP,
    CHO_HOME,
    quay_de,
    dieu_khien_gap,
    dieu_khien_nang_ha,
    di_chuyen_de,
    di_chuyen_nang_ha
)


# ==================================================
# 1. KHOI TAO ROBOT VE HOME
# ==================================================

def ve_home_ban_dau():

    print("\n========== KHOI TAO HOME ==========")

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
# 2. CHU TRINH GAP VA THA SAN PHAM
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

    # BUOC 4: NANG TAY LEN TRUNG GIAN
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

    # BUOC 6: HA TAY XUONG LAI
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
