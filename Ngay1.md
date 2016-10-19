## Ngày 1: Xem video tiếng Việt

### Một số lệnh cú pháp cơ bản:

- `print`: In ra màn hình
- `Các toán tử`: 
    - Cộng, trừ, nhân, chia (+-*/)
    - Mũ (**)
    - Thực hiện các phép toán trong ngoặc trước, ngoài ngoặc sau
- `raw_input`: Lấy input từ bàn phím ở pythonv2 (input với pythonv3)
- In chuỗi cùng với giá trị của một biến
    
    ```
    print("This is string " + var)   
    ```
- `Shebang`: Khai báo thư viện python ở mỗi shell hay file py
    
    ```
    #!/dir/of/python
    ```
- `Comment`: Dòng comment ở mỗi file python thường bắt đầu bằng dấu `#`

    ```
    # This is comment line.
    ```
- Khai báo một biến là string (Có thể sử dụng các \n, \t,...)

    ```
    Cách 1:
    a = "This is a"
    Cách 2:
    a = 'This is also a.'
    Cách 3:
    a = """
    This
    is 
    mutli-line
    """
    ```
- Format string
    - Cắt khoảng trắng 2 đầu `string.strip()`
    - Viết thường toàn bộ chuỗi `string.lower()`
    - Viết HOA toàn bộ chuỗi `string.upper()`
    - Đảo ngược (Ký tự HOA thành thường, thường thành HOA): `string.swapcase()`
    - Thay thế chuỗi `string.replace` : https://repl.it/EA5d/0
    - Đếm ký  tự/cụm từ xuất hiện trong string `string.count("foo")`
    - Độ dài của chuỗi `string.len()`
    
- Tupple <Mảng cố định, không thay đổi được giá trị>
    - `x = (0, 2, 4, 3)` Mảng cố định được khai báo ở cặp `()`
    - Truy xuất giá trị của mảng với `index` bắt đầu từ 0: x[0]
    - Truy xuất giá trị cuối cùng của mảng x[-1]

- List <Mảng động và có thể thay đổi giá trị bên trong>
    - `x = [0, 2, 4, 5]
    - Thêm giá trị vào cuối mảng `x.append('4')`
    - Thêm giá trị vào vị trí nào đó `x.insert(vị-trí, giá-trị)`
    - Xóa phần tử trong mảng `del x[vị-trí]`
    - Xóa phần tử cuối trong mảng `x.pop()`
    - Xóa theo giá trị của phần tử `x.remove(giá-trị)`
    - Lặp lại giá trị trong mảng 3 lần `x = x * 3`
    - Gộp 2 mảng: `x=x+y`, 2 mảng có thể là mảng số, mảng string hoặc `x.extent(y)`
    - Sắp 