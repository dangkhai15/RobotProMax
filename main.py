
from time import sleep_ms

from conveyor import bang_tai_chay, bang_tai_dung
from sensor import phat_hien_san_pham, cho_san_pham_roi
from robot import ve_home_ban_dau, chu_trinh_gap_hang


# ==================================================
# 1. CHUONG TRINH CHINH
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

    # VONG LAP HOAT DONG LIEN TUC
    while True:

        if phat_hien_san_pham():

            print("\nPHAT HIEN SAN PHAM")

            # DUNG BANG TAI
            bang_tai_dung()
            sleep_ms(500)

            # ROBOT GAP VA THA SAN PHAM
            chu_trinh_gap_hang()

            print("ROBOT DA VE HOME")

            # BANG TAI CHAY LAI
            print("BANG TAI CHAY LAI")
            bang_tai_chay()

            # CHO SAN PHAM ROI KHOI CAM BIEN
            print("CHO SAN PHAM ROI KHOI CAM BIEN")

            cho_san_pham_roi()

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
