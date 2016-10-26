## Đọc slide

### Expressions:

#### Hằng (Constants)

- Giá trị được đặt sẵn như là số, ký tự, chuỗi,... và giá trị này không thay đổi được
- Hằng số là những con số kiểu float, interger,...
- Chuỗi ký tự cũng được coi là một hằng, được xác định trong dấu ngoặc đơn hoặc ngoặc kép

#### Biến (Variables)

- Biến là một tên định sẵn được lưu trên bộ nhớ, có chứa giá trị hoặc không
- Chúng ta có thể đặt tên cho biến
- Có thể thay đổi nội dung, giá trị bên trong biến
- Được gán trực tiếp cho các giá trị, hoặc gián tiếp qua các phép toán
- Các phép toán được thực hiện đúng trình tự nhân chia trước cộng trừ sau, trong ngoặc trước ngoài ngoặc sau và từ trái sang phải
- Giá trị mới sẽ được thay thế cho giá trị cũ
- Giá trị mặc định nhập từ bàn phím vào mang kiểu `string`, muốn sử dụng kiểu number phải ép kiểu
- Đặt tên biến theo kiểu gợi nhớ

#### Quy tắc đặt tên biến trong Python

- Thường bắt đầu bằng những kí tự hoặc dấu gạch dưới
- Bao gồm chữ, số và dấu gạch dưới
- Không được đặt tên biến với những từ đặc biệt, cú pháp khai báo của ngôn ngữ Python: add, del, is....

### Điều kiện (Conditions)

#### Toán tử so sánh

- Luôn trả về kết quả True hoặc False
- Chỉ so sánh các biến chứ không thay đổi giá trị của biến
- `=` là phép gán giá trị

| Toán tử | Ý nghĩa |
| --- | --- |
| < | Nhỏ hơn |
| <= | Nhỏ hơn hoặc bằng |
| == | So sánh bằng (`is`) |
| >= | Lớn hơn hoặc bằng |
| > | Lớn hơn |
| != | So sánh khác (`is not`) |

#### Câu lệnh rẽ nhánh

- So sánh với một hoặc nhiều điều kiện khác nhau
- Câu lệnh rẽ nhánh thực hiện khối lệnh bên trong

#### try / except

- Bắt lỗi khi input nhập vào không đúng kiểu

### Hàm - Functions

#### Các loại hàm trong Python

- Hàm được dựng sẵn: như type(), int(), raw_input()
- Hàm được chúng ta viết, định nghĩa và sử dụng
- Tên các hàm chúng ta định nghĩa phải khác với các từ có sẵn, các từ "resersed words"

#### Tạo hàm mới

- Trong Python, một hàm có thể được sử dụng nhiều lần vì thế ta có thể khai báo các argument (giống như các input) nhập vào để hàm xử lý và trả về kết quả
- Định nghĩa hàm bằng từ khóa `def`
- Chúng ta sử dụng hàm bằng các gọi tên hàm và truyền vào các argument

#### Arguments (Sử dụng hàm)

- Là giá trị truyền vào hàm giống như input khi chúng ta gọi hàm
- Sử dụng arguments giúp linh động input truyền vào
- Các argument được đặt trong dấu ngoặc sau tên hàm

#### Parameters (Khi Tạo hàm)

- Là các giá trị truyền vào tương ứng với argument

#### Hàm có Giá trị trả về

- Khi viết hàm, chúng ta muốn chúng xử lý một số công việc đôi khi không trả về kết quả gì nhưng đôi khi để kiểm tra, so sánh thì nó sẽ trả về kết quả
- Dùng `return` để trả về kết quả

#### Hàm không có giá trị trả về

- Trong python và các ngôn ngữ lập trình khác, các hàm không trả về giá trị được gọi làm hàm `void`

### Vòng lặp

#### Các bước được lặp lại

- Với kiểu lặp này, một biến được thay đổi giá trị đến khi gặp điều kiện dừng

### Vòng lặp vô tận

- Vòng lặp này sẽ làm việc liên tục và không dừng lại vì điều kiện luôn luôn đúng

### Thoát ra khỏi vòng lặp

- `break` là từ khóa dùng để thoát khỏi vòng lặp và không xử lý các câu lệnh tiếp theo bên trong vòng lặp

### Quay lại đầu vòng lặp

- `continue`, khi gặp từ khóa này, chương trình sẽ nhảy về đầu vòng lặp