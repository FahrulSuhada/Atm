class ATM:
  def __init__(self, saldo=0 ,BAdmin=5, Tsaldo=0):
      self.saldo = saldo
      self.transaksi = []
      self.BAdmin = BAdmin
      self.Tsaldo = Tsaldo
  def bunga(self):
      bunga = 0
      if self.saldo >= 1000 :
          bunga = 0.005*self.saldo
  def tambah(self, Ttambah):
      self.saldo += Ttambah-self.BAdmin
      self.transaksi.append(f"Saldo Ditambahkan +${Ttambah}")
      print(f"Saldo berhasil ditambahkan sebesar ${Ttambah} dipotong pajak,\n Saldo anda sekarang adalah : {self.saldo}")
  def tampil(self):
      self.bunga()
      print(f"Saldo anda sekarang adalah : {self.saldo}+{self.bunga}")
  def tarik(self, Ttarik):
      if Ttarik+self.BAdmin > self.Tsaldo:
          print(f"Gagal!, Saldo tidak mencukupi")
      else:
          self.Tsaldo -= Ttarik+self.BAdmin
          self.transaksi.append(f"Saldo Ditarik -{Ttarik}")
          print(f"Sucses!, Saldo berhasil ditarik sebesar {Ttarik} \n Sisa saldo anda sekarang adalah {self.saldo}")
  def mutasi(self):
      print("Mutasi Rekening")
      for transaksi in self.transaksi:
          print(transaksi)
  def transfer(self, Ttransfer, NoTransfer):
     if NoTransfer == '':
         print("Nomer tidak bisa kosong!")
     else:
         if Ttransfer+self.BAdmin > self.saldo:
              print(f"Gagal!, Saldo tidak mencukupi")
         else:
              self.saldo -= Ttransfer+self.BAdmin
              self.transaksi.append(f"Saldo ditransfer sebesar {Ttransfer} ke nomer {NoTransfer}")
              print(f"Sucses!, Saldo berhasil transfer sebesar {Ttransfer} \n Sisa saldo anda sekarang adalah {self.saldo}")

atm = ATM()
Max = 2
count = 0
if count < Max:
    while True:
      pw = input("Masukan password : ")
      if pw == '123' :
          while True :
              print("--Aplikasi ATM")
              print("1. Tambah saldo")
              print("2. Tarik saldo")
              print("3. Tampilkan saldo")
              print("4. Mutasi Rekening")
              print("5. Transfer")
              print("6. exit")
    
              key = input("Pilih salah satu (1-5) : ")
    
              if key == '1' :
                  Ttambah = float(input("Masukan Jumlah yang ingin ditambahkan : "))
                  atm.tambah(Ttambah)
              elif key == '2':
                  Ttarik = float(input("Masukan Jumlah yang ingin ditarik : "))
                  atm.tarik(Ttarik)
              elif key == '3':
                  atm.tampil()
              elif key == '4':
                  atm.mutasi()
              elif key == '5':
                  NoTransfer = float(input("Masukan nomer tujuan : "))
                  Ttransfer = float(input("Masukan nominal transfer : "))
                  atm.transfer(Ttransfer,NoTransfer)
              elif key == '6':
                  break
              else:
                  print("Keyword tidak terdafta!")
      else:
          if count < Max:
              print("Password Salah!")
              count += 1
          else:
              print("Akun di blokir!")
              break
else:
    print("BLOCKED!")