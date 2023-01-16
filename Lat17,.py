from abc import ABC, abstractmethod

class Mahasiswa(ABC):
    @abstractmethod
    def cetakMhs():
        pass

class Dosen(ABC):
    @abstractmethod
    def cetakDosen():
        pass

class CetakNama(Mahasiswa):
    def cetakMhs(Data):
        print(f"Nama Mahasiswa : {Data.nama}")

class CetakNama(Dosen):   
    def cetakDosen(Data):
        print(f"Nama Dosen : {Data.nama}")

class CetakNim(Mahasiswa):
    def cetakMhs(Data):
        print(f"Nim Mahasiswa : {Data.nim}")

class CetakNip(Dosen):
    def cetakDosen(Data):
        print(f"Nip Dosen  : {Data.nip}")

class CetakKelas(Mahasiswa):
    def cetakMhs(Data):
        print(f"Kelas Mahasiswa : {Data.kelas}")

class CetakJabatan(Dosen):
    def cetakDosen(Data):
        print(f"Jabatan Sebagai  :  {Data.jabatan}")

class CetakNoHp(Mahasiswa):
    def cetakMhs(Data):
        print(f"Nomor Hp Mahasiswa : {Data.noHp}")

class CetakNoHpDosen(Dosen): 
    def cetakDosen(Data):
        print(f"Nomor Hp Dosen : {Data.noHp}")

class DataMahasiswa:
    def __init__(self, nama, nim, kelas, noHp):
        self.nama = nama
        self.nim  = nim
        self.kelas = kelas
        self.noHp = noHp


class DataDosen:
    def __init__(self, nama, nip, jabatan, noHp):
        self.nama = nama
        self.nip = nip
        self.jabatan = jabatan
        self.noHp = noHp

if __name__ == "__main__":
    b = []
    data1 = DataMahasiswa("Alvin","211110558","IF-C Pagi","081375269852")
    data2 = DataDosen("Albert","132211","Dosen Tetap","0882015035158")
    b.append(data1)
    b.append(data2)
    
    for data in b:
        for proses in Mahasiswa.__subclasses__():
            try:
                proses.cetakMhs(data)
            except:
                continue
        print()
        
    # print(len(b))
    
    




