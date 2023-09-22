import SinhVien

class DanhSachSV:
    def __init__(self )->None:
        self.dssv=[]
    
    def themSV(self,sv:SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def DocFile(self):
        f=open("dssv.txt","r")
        a= True
        while(a):
            s=f.readline()
            info=s.split(",")
            date_format="%Y/%m/%d"
            dt=datetime.datetime.strptime(str(info[2]).strip('\n'),date_format)
            sv=SinhVien(info[0],info[1],dt)
            dssv.themSV(sv)
            if not f.readline():
             a=False
        f.close()
    def sortByName(self):
        self.self.sort(key=lambda x: x.hoTen, reverse=False)