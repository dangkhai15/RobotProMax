# Hệ Thống Băng Tải & Robot Gắp Hàng Tự Động (RobotProMax)

Dự án này sử dụng MicroPython (thường chạy trên vi điều khiển như ESP32) để điều khiển một hệ thống tự động bao gồm: một băng tải để di chuyển sản phẩm và một cánh tay robot 3 bậc tự do (đế, nâng/hạ, gắp) để gắp sản phẩm khi có tín hiệu từ cảm biến nhận diện.

## Sơ Đồ Chân Tín Hiệu (Pinout)

Hệ thống sử dụng các linh kiện chính với kết nối GPIO như sau:
* **Cảm biến hồng ngoại (IR Sensor):** Chân `34` (Input) - Dùng để phát hiện sản phẩm trên băng tải.
* **Module điều khiển động cơ L298N (Băng tải):** Chân `26` (IN1) và `27` (IN2) - Điều khiển động cơ DC của băng tải chạy/dừng.
* **Động cơ Servo (Cánh tay Robot):** Cấp xung PWM (tần số 50Hz)
  * **Servo Đế (Xoay trái/phải):** Chân `13`
  * **Servo Nâng/Hạ:** Chân `14`
  * **Servo Đầu Gắp (Đóng/mở):** Chân `12`

## Các Chức Năng Chính

Dưới đây là các module chức năng chính được lập trình trong file `RobotProMax.py`:

### 1. Điều Khiển Băng Tải
* `bang_tai_chay()`: Kích hoạt L298N để băng tải di chuyển sản phẩm.
* `bang_tai_dung()`: Ngắt tín hiệu L298N để dừng băng tải ngay lập tức khi phát hiện vật.

### 2. Điều Khiển Servo Mềm Mại (Smooth Movement)
Thay vì nhảy ngay lập tức đến góc chỉ định gây giật cục, code được thiết kế để cánh tay di chuyển từ từ (nội suy) thông qua các hàm:
* `di_chuyen_de()`: Xoay bệ đỡ từ góc hiện tại tới góc đích từng bước nhỏ.
* `di_chuyen_nang_ha()`: Nâng hoặc hạ cánh tay từ từ với các thông số bước (`buoc`) và độ trễ (`delay`) có thể tuỳ chỉnh, giúp tay gắp không bị văng sản phẩm.

### 3. Chu Trình Gắp - Thả Tự Động
Hàm `chu_trinh_gap_hang()` tự động hóa hoàn toàn quá trình xử lý 1 sản phẩm với 10 bước phối hợp nhịp nhàng:
1. Mở đầu gắp.
2. Hạ tay xuống sát sản phẩm.
3. Đóng đầu gắp để kẹp sản phẩm.
4. Nâng tay lên vị trí trung gian (tốc độ nhanh).
5. Xoay đế sang hướng thùng chứa (trái).
6. Hạ tay xuống vị trí thả.
7. Mở đầu gắp để thả sản phẩm.
8. Thu đầu gắp về vị trí mặc định (Home).
9. Nâng tay về vị trí an toàn (Home).
10. Xoay đế về vị trí ban đầu (Home) để sẵn sàng chu trình mới.

### 4. Xử Lý Cảm Biến & Chống Nhiễu (Debouncing)
* Hàm `phat_hien_san_pham()` không chỉ đọc giá trị cảm biến IR mà còn có cơ chế chờ 50ms và đọc lại lần 2. Điều này giúp loại bỏ tín hiệu nhiễu (chống rung ngẫu nhiên) nhằm đảm bảo vật thực sự đã đến đúng vị trí gắp.

## Quy Trình Hoạt Động (Main Loop)

Khi cấp nguồn, hệ thống sẽ hoạt động theo kịch bản sau:
1. **Khởi tạo:** Chạy hàm `ve_home_ban_dau()` để đưa tất cả servo về vị trí chuẩn và đảm bảo băng tải đang dừng.
2. **Khởi động băng tải:** Cho băng tải chạy để đưa vật phẩm tiến vào khu vực gắp.
3. **Vòng lặp giám sát (While True):**
   * Liên tục kiểm tra cảm biến hồng ngoại.
   * Nếu có vật phẩm che cảm biến $\rightarrow$ Dừng băng tải ngay lập tức.
   * Kích hoạt `chu_trinh_gap_hang()` để robot gắp vật sang vị trí khác.
   * Chờ vật phẩm rơi khỏi vùng cảm biến (đảm bảo không kẹt).
   * Bật lại băng tải và tiếp tục chờ sản phẩm tiếp theo.
4. **An toàn ngắt hệ thống:** Khối `try...except...finally` đảm bảo rằng nếu có lỗi xảy ra hoặc người dùng bấm dừng hệ thống (Ctrl+C), băng tải sẽ tự động được ngắt an toàn.
```eof

Tôi đã tổng hợp đầy đủ từ việc khai báo chân (GPIO), các cơ chế điều khiển mềm (smooth control), chu trình gắp 10 bước cho đến cách hoạt động của vòng lặp chính. Bạn có thể sử dụng trực tiếp file này cho kho lưu trữ Git hoặc tài liệu của dự án nhé!
