import MySQLdb

def laythongtin():
	try:
		r = open("info.cfg","r")
		r = r.read()
		for x in r.split():
			x = x.split("=")
			if x[0] == "SERVER":
				laythongtin.host = x[1]
			if x[0] == "USER":
				laythongtin.user = x[1]
			if x[0] == "PASSWORD":
				laythongtin.pw = x[1]
		laythongtin.f = True
		pass
	except:
		print "Khong tim thay file cau hinh.\nVui long nhap thong tin SERVER: "
		laythongtin.host=raw_input("SERVER: ")
		laythongtin.user=raw_input("USER: ")
		laythongtin.pw=raw_input("PASSWORD: ")
		r = open("info.cfg", 'w')
		r.write("SERVER={0}\nUSER={1}\nPASSWORD={2}".format(laythongtin.host.strip(),laythongtin.user.strip(),laythongtin.pw.strip()))
		laythongtin.f = False

def ketnoi_db(qr):
	if laythongtin.f == False:
		db = "mysql"
	else:
		db = "db_qlsv"
	cmd = MySQLdb.connect(host,user,pw,db)
	cursor = cmd.cursor()
	cursor.execute(qr)
	result=cursor.fetchall()
	cmd.commit()
	return result
	cmd.close()

def xemchitiet(xem):
	re = xem
	print "ID\t Ten\t Gioi Tinh\t Ngay Sinh\t Lop\t Truong"
	for x in xem:
		if int(x[2]) == 0:
			gt = "Nu "
		else:
			gt = "Nam"
	 	print "{0}\t {1}\t {2}\t\t {3}\t {4}\t {5} ".format(x[0], x[1], gt, x[3], x[4], x[5])
	print "--------------------------------------------------"

def tao_DB():
	qr = "create database db_qlsv"
	re = ketnoi_db(qr)
	qr = """CREATE TABLE sinhvien(
   masv INT NOT NULL,
   ten VARCHAR(100) NOT NULL,
   gioitinh int(2) NOT NULL,
   ngaysinh VARCHAR(50),
   lop VARCHAR(10) NOT NULL,
   truong VARCHAR(100) NOT NULL,
   PRIMARY KEY ( masv )
	);
	"""
	laythongtin()
	re = ketnoi_db(qr)
	print "Da tao DB"

def them(masv, ten, gioitinh, ngaysinh, lop, truong):
	qr = "INSERT INTO sinhvien(masv, ten, gioitinh, ngaysinh, lop, truong) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(int(masv), ten, gioitinh, ngaysinh, lop, truong)
	db = "db_qlsv"
	re = ketnoi_db(qr)

def sua(id_sua, masv, ten, gioitinh, ngaysinh, lop, truong):
	
	qr = "Select * from sinhvien where masv = '{0}'".format(id_sua)

	re = ketnoi_db(qr)
	for item in re:
		print item[0], item[1], item[2], item[3], item[4], item[5]
		if masv.strip() == "":
			masv = item[0]
		if ten.strip() == "":
			ten = item[1]
		if gioitinh.strip() == "":
			gioitinh = item[2]
		if ngaysinh.strip() == "":
			ngaysinh = item[3]
		if lop.strip() == "":
			lop = item[4]
		if truong.strip() == "":
			truong = item[5]
	qr = "UPDATE `sinhvien` SET `masv`='{0}', `ten`='{1}', `gioitinh`='{2}', `ngaysinh`='{3}', `lop`='{4}', `truong`='{5}' WHERE (`masv`='{6}')".format(int(masv), ten, gioitinh, ngaysinh, lop, truong, item[0])
	re = ketnoi_db(qr)
def xoa(masv):
	confirm=raw_input("Ban co muon xoa ban ghi '{0}'? (Y/n)".format(masv))
	if confirm == "Y" or confirm == "y":
		qr = "DELETE FROM sinhvien WHERE masv='{0}'".format(masv)
		re = ketnoi_db(qr)
	else:
		print "Thao tac da bi huy bo."
def timkiem(tukhoa):
	qr = "SELECT * FROM sinhvien WHERE masv LIKE '%{0}%' OR ten LIKE '%{0}%' OR gioitinh LIKE '%{0}%' OR ngaysinh LIKE '%{0}%' OR lop LIKE '%{0}%' OR truong LIKE '%{0}%' ORDER BY ten ASC".format(tukhoa.strip())
	re = ketnoi_db(qr)
	return re

# Lay thong tin tu file cau hinh, tao DB khi chua co
laythongtin()
host=laythongtin.host
user=laythongtin.user
pw=laythongtin.pw
if laythongtin.f == False:
	print "Dang tao DB..."
	tao_DB()

# # Them Sinh Vien
print "Them Moi sinh vien (* Truong bat buoc) "
masv=raw_input("Nhap ID*: ")
ten=raw_input("Nhap Ten: ")
gioitinh=raw_input("Nhap Gioi tinh: ")
ngaysinh=raw_input("Nhap ngay sinh: ")
lop=raw_input("Nhap lop: ")
truong=raw_input("Nhap truong: ")
them(masv,ten,gioitinh,ngaysinh,lop,truong)


# Sua thong tin sinh vien, truong nao khong sua thi de trong

suama=raw_input("Truong nao khong sua vui long bam Enter\nNhap ID can sua: ")
print "Ban dang sua sinh vien ma so: ", suama
qr = "select * from sinhvien where masv='%s'" % suama
xemchitiet(ketnoi_db(qr))
masv=raw_input("Nhap ID: ")
ten=raw_input("Nhap Ten: ")
gioitinh=raw_input("Nhap Gioi tinh: ")
ngaysinh=raw_input("Nhap ngay sinh: ")
lop=raw_input("Nhap lop: ")
truong=raw_input("Nhap truong: ")
sua(suama,masv,ten,gioitinh,ngaysinh,lop,truong)


# Xoa Sinh Vien thong qua ID cua sinh vien

masv=raw_input("Xoa Thong tin sinh vien\nNhap ID: ")
qr = "select * from sinhvien where masv='%s'" % masv
xemchitiet(ketnoi_db(qr))
xoa(masv)

#Tim kiem sinh vien: Nhap keyword muon tim, Neu key word rong se hien thi ra tat ca
tukhoa=raw_input("Tim kiem sinh vien\nNhap tu khoa can tim kiem: ")
timkiem=timkiem(tukhoa) 
xemchitiet(timkiem)
