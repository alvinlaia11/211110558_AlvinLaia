class Ryeinaldo:
    _CACHE = {}
    datas = []
    def __init__(self):
        self.__dict__ = self._CACHE
class absensi(Ryeinaldo):
    def __init__(self,**kwargs):
        Ryeinaldo.__init__(self)
        self._CACHE.update(kwargs)
        self.datas.append(self._CACHE)
    def cetakData(self):
        tmp = self._CACHE
        # data = self.datas
        for name,data in tmp.items():
            print(name,":",data)
        # for i in range(len(self.datas)):
        #     print(f'Pengunjung dengan nama {self.datas[i]["nama"]} hadir')
        print(f'Total jumlah pengunjung : {len(self.datas)}')

if __name__ == "__main__":
    a = absensi(nama="Ryeinaldo",kelas="IF C Pagi",nim="211111677")
    a.cetakData()