class Alvin:
    def __init__(self, nama, kelas, proses):
        self.nama = nama
        self.kelas = kelas
        self.proses = proses
    def nama1(self):
        print("Nama Mahasiswa  : {}".format(self.nama)) 
    def kelas2(self):
        print("Kelas Mahasiswa : {}".format(self.kelas))
    def proses3(self):
        print("Kelas Mahasiswa : {}".format(self.proses))

class Mhs:
    def __init__(self, nama, kelas, proses):
        self.nama = nama
        self.kelas = kelas
        self.proses = proses
    def namaMhs(self):
        print("Mahasiswa dengan nama : {}".format(self.nama), "sedang mengikuti kelas") 
    def kelasApa(self):
        print("Kelas Mahasiswa       : {}".format(self.kelas), "sedang dalam proses belajar")
    def prosesKelas(self):
        print("Kegiatan Belajar yang berlangsung : {}".format(self.proses))

class Absensi:
    def __init__(self, nama, kelas, proses):
       self.Alvin = Alvin(nama, kelas, proses)
       self.Mhs = Mhs(nama, kelas, proses)
    def proses(self):
        print("====================================================")
        self.Alvin.nama1()
        self.Alvin.kelas2()
        self.Alvin.proses3()
        print("====================================================")
        self.Mhs.namaMhs()
        self.Mhs.kelasApa()
        self.Mhs.prosesKelas()
        print("====================================================")

if __name__ == "__main__":
    nama = "Alvin"
    kelas = "IF-C"
    proses = "Pemograman Berorientasi Objek"
    cetak = Absensi(nama, kelas, proses)
    cetak.proses()
    print("\n")
    nama = "Bastian"
    kelas = "IF-B"
    proses = "Bahasa Inggris"
    cetak = Absensi(nama, kelas, proses)
    cetak.proses()

