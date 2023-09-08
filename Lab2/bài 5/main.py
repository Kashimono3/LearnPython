from datetime import datetime

from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSv


sv1 = SinhVienChinhQuy(2111875,"Lê Viết Đăng Quang", datetime.strptime("30/10/2003","%d/%m/%Y"),85)
sv2 = SinhVienChinhQuy(2111876,"Lê Viết Quang", datetime.strptime("2/10/2003","%d/%m/%Y"),80)
sv3 = SinhVienChinhQuy(2111877,"Lê Đăng Quang", datetime.strptime("5/10/2003","%d/%m/%Y"),70)
sv4 = SinhVienChinhQuy(2111878,"Lê Quang", datetime.strptime("3/10/2003","%d/%m/%Y"),60)
sv5 = SinhVienChinhQuy(2111879,"Viết Đăng Quang", datetime.strptime("1/10/2003","%d/%m/%Y"),90)
sv6 = SinhVienPhiCQ(2111880,"Đăng Quang", datetime.strptime("30/10/2003","%d/%m/%Y"),"Trung cấp",2)
sv7 = SinhVienPhiCQ(2111880,"Đăng Quang", datetime.strptime("30/10/2003","%d/%m/%Y"),"Cao Đẳng",2)
sv8 = SinhVienPhiCQ(2111880,"Đăng Quang", datetime.strptime("1/10/2003","%d/%m/%Y"),"Cao Đẳng",2)
dssv = DanhSachSv()

dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

dssv.xuat()
print("Danh sách sinh viên theo năm  :")
nam = datetime.strptime("5/10/2003","%d/%m/%Y")

kq = dssv.timSvCaoDangTheoNam(nam)



