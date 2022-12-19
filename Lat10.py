from abc import ABC, abstractmethod

class Hitung(ABC):
  @abstractmethod
  def return_nilai(self):
    pass
  
class Tempat(Hitung):
  def __init__(self, konteks):
    self.konteks = konteks
  def return_nilai(self):
    nilai = 0 
    for Hitung in self.konteks:
      nilai = nilai + Hitung.return_nilai()
    return nilai

class uangKuliah(Hitung):
  def __init__(self, nilai):
    self.nilai = nilai
  def return_nilai(self):
    return self.nilai
  
class uangKuliahPertama(Hitung):
  def __init__(self, nilai):
    self.nilai = nilai
  def return_nilai(self):
    return self.nilai

class uangMpt(Hitung):
  def __init__(self, nilai):
    tmp = 0
    for j in range(len(nilai)):
      tmp += nilai[j]
    self.nilai = tmp
    
  def return_nilai(self):
    return self.nilai
  
  
if __name__ == "__main__":
  # uangKuliah1 = []
  # uangKuliah1.append(uangKuliahPertama(10000))
  # uangKuliah1 = Tempat(uangKuliah1)
    
  uangKuliah2 = []
  uangKuliah2.append(uangKuliah(10000))
  uangKuliah2.append(uangKuliahPertama(100))
  uangKuliah2.append(uangMpt([100, 200, 300]))
  hitung1 = Tempat(uangKuliah2)
  
  print("Uang Pendaftaran    :", uangKuliah2[0].return_nilai())
  print("Uang Kuliah Pertama :", uangKuliah2[1].return_nilai())
  print("Uang MPT            :", uangKuliah2[2].return_nilai())

  print("Total Harga: "+ str(hitung1.return_nilai()))

    
