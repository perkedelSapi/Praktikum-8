class DNM:
    def __init__(self):
        self.data = {}

    def tambah(self, nama, nilai):
        self.data[nama] = nilai
        print(f"Data {nama} dengan nilai {nilai} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data:
            print("Belum ada data yang ditambahkan.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.data.items():
                print(f"{nama}: {nilai}")

    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data {nama} berhasil dihapus.")
        else:
            print(f"Data dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        if nama in self.data:
            self.data[nama] = nilai_baru
            print(f"Data {nama} berhasil diubah menjadi {nilai_baru}.")
        else:
            print(f"Data dengan nama {nama} tidak ditemukan.")


# Contoh penggunaan program
if __name__ == "__main__":
    daftar_nilai = DNM()
    
    while True:
        print("\nMenu:")
        print("1. Tambah data")
        print("2. Lihat data")
        print("3. Hapus data")
        print("4. Ubah data")
        print("5. Keluar")
        
        pilihan = input("(T)ambah,(L)ihat,(H)apus,(U)bah,(K)eluar: ")
        
        if pilihan == "t":
            nama = input("Masukkan nama: ")
            try:
                 # Pastikan nilai adalah angka

                nilai = float(input("Masukkan nilai: ")) 
                daftar_nilai.tambah(nama, nilai)
            except ValueError:
                print("Nilai harus berupa angka.")
        elif pilihan == "l":
            daftar_nilai.tampilkan()
        elif pilihan == "h":
            nama = input("Masukkan nama yang akan dihapus: ")
            daftar_nilai.hapus(nama)
        elif pilihan == "u":
            nama = input("Masukkan nama yang akan diubah: ")
            try:
                 # Pastikan nilai baru adalah angka

                nilai_baru = float(input("Masukkan nilai baru: ")) 
                daftar_nilai.ubah(nama, nilai_baru)
            except ValueError:
                print("Nilai baru harus berupa angka.")
        elif pilihan == "k":
            break
        else:
            print("Tidak valid.")
