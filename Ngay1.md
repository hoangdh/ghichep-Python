## Ngày 1: Xem video tiếng Việt

Một số lệnh cú pháp cơ bản:

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