class SinhVien:
    truong = "Đại học Đà Lạt"
    def _init_(self,maso: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh
        
    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self,maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso
    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso)) == 7
    @classmethod
    def doiTenTruong(self,tenmoi):
        self.truong = tenmoi
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    def xuat(self)
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    def themSinhVien(self,sv:SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def timSvTheoMssv(self,mssv:int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    def timVTSvTheoMssv(self,mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    def xoaSvTheoMssv(self,maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maso)
        if vt !=-1:
            del self.dssv[vt]
            return True
        else:
            return False
    
       pass
       
    def timSvSinhTruocNgay(self,ngay:datetime)
        pass
    def timSvTheoTen(self,ten:str):
        listSV = []
        if (self.soLuongSinhVien() > 0):
         for sv in self.listSinhVien:
            if (nam.upper() in sv.hoTen.upper()):
                listSV.append(sv)
        return listSV