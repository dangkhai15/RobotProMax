
# RobotProMax
# CẤU TRÚC CÁC FILE CHƯƠNG TRÌNH

## 1. Giới thiệu

Chương trình RobotProMax được chia thành 5 file Python riêng biệt. Mỗi file đảm nhiệm một chức năng cụ thể, giúp mã nguồn có cấu trúc rõ ràng, dễ quản lý, chỉnh sửa và bảo trì.

## 2. Cấu trúc thư mục

```text
RobotProMax/
│
├── main.py
├── config.py
├── sensor.py
├── conveyor.py
├── robot.py
└── README.md
```

## 3. Mô tả chức năng các file

### 3.1. main.py – Chương trình chính

Là file điều khiển trung tâm, chịu trách nhiệm điều phối hoạt động của toàn bộ chương trình.

Các nhiệm vụ:
- Khởi tạo hệ thống.
- Đưa robot về vị trí ban đầu.
- Điều khiển trình tự chạy và dừng băng tải.
- Theo dõi tín hiệu cảm biến.
- Gọi chu trình gắp và thả sản phẩm.
- Quản lý vòng lặp hoạt động liên tục.
- Xử lý các trường hợp ngắt hoặc lỗi chương trình.

### 3.2. config.py – File cấu hình

Chứa các thông số cấu hình phần cứng và hoạt động của hệ thống.

Các nhiệm vụ:
- Khai báo chân GPIO.
- Khởi tạo các chân PWM điều khiển servo.
- Thiết lập vị trí các servo.
- Cấu hình thời gian chờ.
- Thiết lập bước di chuyển và tốc độ điều khiển servo.

### 3.3. sensor.py – File xử lý cảm biến

Chịu trách nhiệm đọc và xử lý tín hiệu từ cảm biến hồng ngoại.

Các nhiệm vụ:
- Đọc trạng thái cảm biến.
- Phát hiện sản phẩm.
- Xác nhận tín hiệu cảm biến với thời gian chống nhiễu 50 ms.
- Kiểm tra sản phẩm đã rời khỏi vùng cảm biến.

### 3.4. conveyor.py – File điều khiển băng tải

Chứa các hàm điều khiển động cơ băng tải thông qua module L298N.

Các chức năng chính:
- `bang_tai_chay()`: Khởi động băng tải.
- `bang_tai_dung()`: Dừng băng tải.

### 3.5. robot.py – File điều khiển robot

Chứa các hàm điều khiển chuyển động của cánh tay robot.

Các nhiệm vụ:
- Điều khiển servo đế.
- Điều khiển servo nâng/hạ.
- Điều khiển servo đầu gắp.
- Di chuyển servo theo từng bước nhỏ.
- Đưa robot về vị trí HOME.
- Thực hiện chu trình gắp và thả sản phẩm gồm 10 bước.

## 4. Mối quan hệ giữa các file

Các file được tổ chức theo mô hình phân chia chức năng:

- `main.py` là file trung tâm, gọi và phối hợp các chức năng từ những file còn lại.
- `config.py` cung cấp các thông số cấu hình dùng chung.
- `sensor.py` xử lý dữ liệu đầu vào từ cảm biến.
- `conveyor.py` đảm nhiệm việc điều khiển băng tải.
- `robot.py` đảm nhiệm việc điều khiển các cơ cấu servo.



