import re
import pandas as pd
from tabulate import tabulate
from datetime import datetime



# function replace dan isalpha
def func_re_pha(value_re_pha):
    while True:
        func_re_pha_in = input(value_re_pha)
        if func_re_pha_in.replace(" ", "").isalpha():
            return func_re_pha_in
        else :
            print("hanya boleh memasukan huruf!")

# function isnumeric
def func_num(value_num):
    while True:
        func_num_in = input(value_num)
        if func_num_in.isnumeric():          
            return func_num_in
        else :
            print("hanya boleh memasukan angka!")

# function nik
def func_nik(value_nik):
    data_karyawan = pd.read_csv("data_karyawan.csv")

    while True:
        func_nik_in = input(value_nik)
        if func_nik_in in data_karyawan["nik"].astype(str).values:
            print(f"data dengan nik {func_nik_in} sudah ada!")          
            continue
        if re.match(r"\b[\d]{10,20}\b", func_nik_in): 
            return func_nik_in
        else :
            print("masukan NIK dengan benar !")

# function alamat
def func_alamat(value_alamat):
    while True:
        func_alamat_in = input(value_alamat)
        if re.match(r"^(?:[a-z]{4,20}|[a-z]{2,5}\s[a-z]{4,30})\s[a-z]{4,30}\s[a-z]{4,30}\s[a-z]{4,30}\srt\.\d{1,3}/rw\.\d{1,3}$", func_alamat_in):
            return func_alamat_in
        else:
            print("masukan alamat yg sesuai ( cth : provinsi kota/kabupaten kecamatan desa rt.01/rw.01 )")

# function tanggal dd-mm-yyyy
def func_date(value_date):
    while True:
        func_date_in = input(value_date)
        if re.match(r"^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19\d{2}|20\d{2})$", func_date_in):
            return func_date_in
        else:
            print("masukan tanggal yg sesuai (cth : 01-01-2000)")

# function no tlpn
def func_no_tlpn(value_no_tlpn):
    while True:
        func_no_tlpn_in = input(value_no_tlpn)
        if re.match(r"^(?:\+62|0)8[1-9]\d{6,10}$", func_no_tlpn_in): # tanda ?: itu berfungsi agar grouping() tidak di baca ## tanda grouping () dan ?: untuk mengeluarkan grouping
            return func_no_tlpn_in
        else:
            print("masukan no tlpn yang sesuai (cth : 08xxxxxxxx / +628xxxxxxxxx)")

# function email
def func_email(value_email):
    while True:
        func_email_in = input(value_email)
        if re.match(r"^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}$", func_email_in):
            return func_email_in
        else:
            print("masukan email yang sesuai (cth : xxxxx@gmail.com)")

# function gender
def func_gender(value_gender):
    while True:
        list_gender = ["laki-laki", "perempuan"]
        func_gender_in = input(value_gender)
        if func_gender_in in list_gender:
            return func_gender_in
        else :
            print("pilih isi yang sesuai (laki-laki / perempuan) 'penulisan harus laki-laki'")

# function status perkawinan
def func_sta_per(value_sta_per):
    while True:
        list_sta_per = ["lajang", "menikah", "cerai"]
        func_sta_per_in = input(value_sta_per)
        if func_sta_per_in in list_sta_per:
            return func_sta_per_in
        else :
            print("pilih isi yang sesuai ( lajang / menikah / cerai)")

# function pendidikan terakhir
def func_pe_ter(value_pe_ter):
    while True:
        list_pe_ter = ["sd", "smp", "sma", "s1", "s2", "s3"]
        func_pe_ter_in = input(value_pe_ter)
        if func_pe_ter_in in list_pe_ter:
            return func_pe_ter_in
        else :
            print("pilih isi yang sesuai (sd/ smp/ sma/ s1/ s2/ s3)")

# function jabatan
def func_jabatan(value_jabatan):
    while True:
        list_jabatan = ["ceo", "direktur", "manager", "karyawan"]
        func_jabatan_in = input(value_jabatan)
        if func_jabatan_in in list_jabatan:
            return func_jabatan_in
        else :
            print("pilih isi yang sesuai (ceo/ direktur/ manager/ karyawan)")

# function manajemen
def func_manajemen(value_manajemen):
    while True:
        list_manajemen = ["manajemen exekutif", "keuangan", "marketing", "produksi", "it"]
                        
        func_manajemen_in = input(value_manajemen)
        if func_manajemen_in in list_manajemen:
            if func_manajemen_in.replace(" ", ""):
                return func_manajemen_in
        else :
            print("pilih isi yang sesuai (manajemen exekutif/ keuangan/ marketing/ produksi/ it)")

# function status pekerja
def func_sta_ker(value_sta_ker):
    while True:
        list_sta_ker = ["tetap", "kontrak", "magang"]
                        
        func_sta_ker_in = input(value_sta_ker)
        if func_sta_ker_in in list_sta_ker:
            return func_sta_ker_in
        else :
            print("pilih isi yang sesuai ( tetap / kontrak / magang )")

# function update data
def func_up_da(value_up_da):
    while True:
        list_up_da = ["nama", "nik", "tempat lahir", "tanggal lahir", "jenis kelamin" , "alamat", "no telp", "email", "status pernikahan", "pendidikan terakhir", "jabatan", "manajemen", "tanggal masuk", "status karyawan", "gaji pokok", "tunjangan" , "total gaji"]
                        
        func_up_da_in = input(value_up_da)
        if func_up_da_in in list_up_da:
            return func_up_da_in
        else :
            print("pilih isi yang sesuai ( nama/ nik/ tempat lahir/ tanggal lahir/ jenis kelamin , alamat/ no telp/ email/ status pernikahan/ pendidikan terakhir/ jabatan/ manajemen/ tanggal masuk/ status karyawan/ gaji pokok/ tunjangan/ total gaji )")

# function iya / tidak
def func_yes_no(value_yes_no):
    while True:
        list_yes_no = ["iya", "tidak"]
                        
        func_yes_no_in = input(value_yes_no)
        if func_yes_no_in in list_yes_no:
            return func_yes_no_in
        else :
            print("pilih isi yang sesuai! ( iya / tidak)")

# function validasi
def func_validasi(value_validasi):
    while True:
        list_validasi = [ "kembalikan", "hapus permanent" ]
                        
        func_validasi_in = input(value_validasi)
        if func_validasi_in in list_validasi:
            return func_validasi_in
        else :
            print("pilih isi yang sesuai! ( kembalikan / hapus permanent )")


###### READ DATA
# menampilkan semua data
def read_data():
    try :
        data_karyawan = pd.read_csv("data_karyawan.csv")
        data_karyawan.index = data_karyawan.index + 1
        print(tabulate(data_karyawan, headers="keys", tablefmt="fancy_grid" ))
    except :
        print("##### DATA TIDAK ADA #####")

# menampilkan simulasi pesangon
def read_simulasi():
    try:
        data_karyawan = pd.read_csv("data_karyawan.csv")

    except FileNotFoundError:
        print("\nTIDAK ADA DATA!")
        return

    input_nik = int(func_num("\nMASUKAN NIK 'untuk mencari data yang ingin dilihat': "))

    if input_nik in data_karyawan["nik"].values:
        data_karyawan["tanggal masuk"] = pd.to_datetime(data_karyawan["tanggal masuk"], dayfirst=True)
        data_karyawan["tanggal mulai kerja"] = data_karyawan["tanggal masuk"].dt.date

        data_karyawan["tahun masuk"] = data_karyawan["tanggal masuk"].dt.year
        data_karyawan["tahun sekarang"] = datetime.now().year

        data_karyawan["masa kerja(TAHUN)"] = data_karyawan["tahun sekarang"] -  data_karyawan ["tahun masuk"] - 1
        data_karyawan["simulasi pesangon"] = data_karyawan["total gaji"] * data_karyawan["masa kerja(TAHUN)"]

        hasil = data_karyawan[data_karyawan["nik"] == input_nik]
        print(tabulate(hasil[["nama","tanggal mulai kerja","tahun sekarang", "total gaji", "masa kerja(TAHUN)", "simulasi pesangon"]], headers="keys" , tablefmt="fancy_grid", showindex=False ))

    else :
        print(f"\nDATA DENGAN NIK : {input_nik} TIDAK ADA!! ")
        return

# menampilkan karyawan bedasarkan manajemen
def read_manajemen():
    try:
        data_karyawan = pd.read_csv("data_karyawan.csv")

    except FileNotFoundError:
        print("\nTIDAK ADA DATA!")
        return
        

    manajemen_in = func_manajemen("\nMASUKAN NAMA MANAGEMENT (manajemen exekutif/ keuangan/ marketing/ produksi/ it) : ").upper()

    if manajemen_in in data_karyawan["manajemen"].values:
        hasil = data_karyawan[data_karyawan["manajemen"] == manajemen_in]
        hasil.insert(0, "no", range(1, len(hasil) + 1))
        print(tabulate(hasil[["no", "nama", "manajemen", "jabatan"]], headers="keys", tablefmt="fancy_grid", showindex=False ))
    
    else :
        print(f"\nDATA MANAGEMENT {manajemen_in} TIDAK ADA!! ")
        return
    
# mencari data bedasarkan nik
def read_data_nik():
    try:
        data_karyawan = pd.read_csv("data_karyawan.csv")
    except FileNotFoundError:
        print("\nTIDAK ADA DATA!")
        return
        

    input_nik = int(func_num("\nMASUKAN NIK 'untuk mencari data yang ingin dicari': "))

    if input_nik in data_karyawan["nik"].values:
        hasil = data_karyawan[data_karyawan["nik"] == input_nik]
        print(tabulate(hasil, headers="keys", tablefmt="fancy_grid",  showindex=False))


##########
###  CREATE DATA
def create_data():
    try:
        data_karyawan = pd.read_csv("data_karyawan.csv")

    except FileNotFoundError:
        data_karyawan = pd.DataFrame(columns=[
            "nama", "nik", "tempat lahir", "tanggal lahir", "jenis kelamin" , "alamat", "no telp", "email", "status pernikahan", "pendidikan terakhir", "jabatan", "manajemen", "tanggal masuk", "status karyawan", "gaji pokok", "tunjangan" , "total gaji"
        ])

    
    jumlah_data = int(func_num("berapa data yang ingin di tambahkan ? "))

    for range_jum_data in range(jumlah_data):
        print(f"\ndata ke-{range_jum_data + 1} : ")

        nama = func_re_pha("NAMA : ").upper()
        nik = int(func_nik("NIK : "))
        tempat_lahir = func_re_pha("TEMPAT LAHIR : ").upper()
        tanggal_lahir = func_date("TANGGAL LAHIR ( cth : dd-mm-yyyy ) : ")
        jenis_kelamin = func_gender("JENIS KELAMIN ( laki-laki / perempuan ) : ").upper()
        alamat = func_alamat("ALAMAT ( cth : provinsi kota/kabupaten kecamatan desa rt.01/rw.01 ) : ").upper()
        no_telp = func_no_tlpn("NO TELP ( cth : 08xxxxxxxx / +628xxxxxxxxx ) : ")
        email = func_email("EMAIL ( cth : xxxxx@gmail.com ) : ")
        status_pernikahan = func_sta_per("STATUS PERKAWINAN ( lajang / menikah / cerai ) : ").upper()
        pendidikan_terakhir = func_pe_ter("PENDIDIKAN TERAKHIR ( sd/ smp/ sma/ s1/ s2/ s3) : ").upper()
        jabatan = func_jabatan("JABATAN ( ceo/ direktur/ manager/ karyawan) : ").upper()
        manajemen = func_manajemen("MANAJEMEN ( manajemen exekutif/ keuangan/ marketing/ produksi/ it) : ").upper()
        tanggal_masuk = func_date("TANGGAL MASUK ( cth : dd-mm-yyyy ) : ")
        status_karyawan = func_sta_ker("STATUS PEKERJA ( tetap / kontrak / magang ) : ").upper()
        gaji_pokok = int(func_num("GAJI POKOK : "))
        tunjangan = int(func_num("TUNJANGAN : "))
        total_gaji = gaji_pokok + tunjangan

        new_row = pd.DataFrame([{
            "nama": nama,
            "nik": nik,
            "tempat lahir" : tempat_lahir,
            "tanggal lahir" : tanggal_lahir,
            "jenis kelamin" : jenis_kelamin,
            "alamat" : alamat,
            "no telp" : no_telp,
            "email" : email,
            "status pernikahan" : status_pernikahan,
            "pendidikan terakhir" : pendidikan_terakhir,
            "jabatan" : jabatan,
            "manajemen" : manajemen,
            "tanggal masuk" : tanggal_masuk,
            "status karyawan" : status_karyawan,
            "gaji pokok" : gaji_pokok,
            "tunjangan" : tunjangan,
            "total gaji" :  total_gaji
            }])
        
        create_da_kar = pd.concat([data_karyawan, new_row], ignore_index=True)
        print(f"\ndata dengan nama {nama} berhasil ditambah!")

    create_da_kar.to_csv("data_karyawan.csv", index=False)

    tanya_ulang = func_yes_no("\nAPAKAH INGIN MEMAMBAH DATA LAGI ( iya / tidak ) ? ")
    if tanya_ulang == "iya":
        create_data()
    elif tanya_ulang == "tidak":
        return
    
### UPDATE DATA DENGAN NIK
def update_data():
    try:
        data_karyawan = pd.read_csv("data_karyawan.csv")
    except FileNotFoundError:
        print("\nTIDAK ADA DATA!")
        return
        

    input_nik = int(func_num("\nMASUKAN NIK 'untuk mencari data yang mau diubah': "))

    if input_nik in data_karyawan["nik"].values:
        hasil = data_karyawan[data_karyawan["nik"] == input_nik]
        print(tabulate(hasil, headers="keys", tablefmt="fancy_grid",  showindex=False))

        pilih_up_da = func_up_da("1.nama \n2.nik \n3.tempat lahir \n4.tanggal lahir \n5.jenis kelamin  \n6.alamat \n7.no telp \n8.email \n9.status pernikahan \n10.pendidikan terakhir \n11.jabatan manajemen \n12.tanggal masuk \n13.status karyawan \n14.gaji pokok \n15.tunjangan\n  \nMASUKAN NAMA DATA YANG INGIN UBAH : ")
        if pilih_up_da in data_karyawan.columns:
            if pilih_up_da in ("nama", "tempat lahir"):
                value_baru = func_re_pha(f"\nMASUKAN {pilih_up_da.upper()} BARU : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH")
            
            elif pilih_up_da == "nik":
                value_baru = int( func_nik(f"\nMASUKAN {pilih_up_da.upper()} BARU : "))
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "jenis kelamin":
                value_baru = func_gender(f"\nMASUKAN {pilih_up_da.upper()} BARU ( laki-laki / perempuan ) : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "alamat":
                value_baru = func_alamat(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : provinsi kota/kabupaten kecamatan desa rt.01/rw.01 ) : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da in ("tanggal lahir", "tanggal masuk"):
                value_baru = func_date(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : dd-mm-yyyy ) : ")
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "no telp":
                value_baru = func_no_tlpn(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : 08xxxxxxxx / +628xxxxxxxxx ) : ")
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "email":
                value_baru = func_email(f"\nMASUKAN {pilih_up_da.upper()} BARU ( cth : xxxxx@gmail.com ) : ")
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "status pernikahan":
                value_baru = func_sta_per(f"\nMASUKAN {pilih_up_da.upper()} BARU ( lajang / menikah / cerai ) : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "pendidikan terakhir":
                value_baru = func_pe_ter(f"\nMASUKAN {pilih_up_da.upper()} BARU ( sd/ smp/ sma/ s1/ s2/ s3) : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "jabatan":
                value_baru = func_jabatan(f"\nMASUKAN {pilih_up_da.upper()} BARU ( ceo/ direktur/ manager/ karyawan) : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "manajemen":
                value_baru = func_manajemen(f"\nMASUKAN {pilih_up_da.upper()} BARU ( manajemen exekutif/ keuangan/ marketing/ produksi/ it) : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da == "status karyawan":
                value_baru = func_sta_ker(f"\nMASUKAN {pilih_up_da.upper()} BARU ( tetap / kontrak / magang ) : ").upper()
                print(f"{pilih_up_da} BERHASIL DI UBAH!")

            elif pilih_up_da in ("gaji pokok", "tunjangan"):
                value_baru = int(func_num(f"\nMASUKAN {pilih_up_da.upper()} BARU : "))

            data_karyawan.loc[data_karyawan["nik"] == input_nik, pilih_up_da] = value_baru

            # Jika gaji pokok atau tunjangan diubah, maka total gaji di update otomatis
            if pilih_up_da in ("gaji pokok", "tunjangan"): 
                row = data_karyawan.loc[data_karyawan["nik"] == input_nik]
                gaji_pokok = int(row["gaji pokok"].values[0])
                tunjangan = int(row["tunjangan"].values[0])
                total_gaji = gaji_pokok + tunjangan
                data_karyawan.loc[data_karyawan["nik"] == input_nik, "total gaji"] = total_gaji

            data_karyawan.to_csv("data_karyawan.csv", index=False)

            tanya_ulang = func_yes_no("\nAPAKAH INGIN MENGUBAH DATA LAGI ( iya / tidak ) ? ")
            if tanya_ulang == "iya":
                update_data()
            elif tanya_ulang == "tidak":
                return

    else :
        print(f"\nDATA DENGAN NIK : {input_nik}, TIDAK ADA!! ")
        return
       
#DELETE DATA 
def delete_data():
    try:
        data_karyawan = pd.read_csv("data_karyawan.csv")
    except FileNotFoundError:
        print("\nTIDAK ADA DATA!")
        return
    
    input_nik = int(func_num("\nMASUKAN NIK 'untuk mencari data yang mau dihapus': "))

    if input_nik in data_karyawan["nik"].values:
        hasil = data_karyawan[data_karyawan["nik"] == input_nik]
        print(tabulate(hasil, headers="keys", tablefmt="fancy_grid",  showindex=False))
        tanya_ulang = func_yes_no("\nAPAKAH YAKIN INGIN MENGHAPUS DATA INI ( iya / tidak ) ? ")
        if tanya_ulang == "iya":
            hasil.to_csv("history_delete.csv",mode="a", header=False, index=False)
            delete_da_kar = data_karyawan[data_karyawan["nik"] != int(input_nik)]
            delete_da_kar.to_csv("data_karyawan.csv", index=False)          
            print(f"data dengan nik : {input_nik} berhasil di hapus")
            
        elif tanya_ulang == "tidak" :
            return
            
        tanya_ulang = func_yes_no("\nAPAKAH INGIN MENGHAPUS DATA LAGI ( iya / tidak ) ? ")
        if tanya_ulang == "iya":
            delete_data()
        elif tanya_ulang == "tidak":
            return

    else :
        print(f"\nDATA DENGAN NIK : {input_nik} TIDAK ADA!! ")
        return
    
#MENGEMBALIKAN DATA YANG DI HAPUS / RESTORE DAN HAPUS PERMANENT
def restore_data():
    try:
        history_delete = pd.read_csv("history_delete.csv")
    except FileNotFoundError:
        print("\nTIDAK ADA DATA!")
        return
    
    input_nik = int(func_num("\nMASUKAN NIK 'untuk mencari data yang mau di kembalikan': "))

    if input_nik in history_delete["nik"].values:
        hasil = history_delete[history_delete["nik"] == input_nik]
        print(tabulate(hasil, headers="keys", tablefmt="fancy_grid", showindex=False))
        tanya_ulang = func_validasi("\nAPAKAH BENAR DATA DIATAS MAU DI ( kembalikan / hapus permanent ) ? ")
        if tanya_ulang == "kembalikan":
            hasil.to_csv("data_karyawan.csv",mode="a", header=False, index=False)
            restore_da_kar = history_delete[history_delete["nik"] != int(input_nik)]
            restore_da_kar.to_csv("history_delete.csv", index=False)
            print(f"data dengan nik {input_nik} berhasil di hapus")
            return
        elif tanya_ulang == "hapus permanent" :
            restore_da_kar = history_delete[history_delete["nik"] != int(input_nik)]
            restore_da_kar.to_csv("history_delete.csv", index=False)
            return
            
    else :
        print(f"\nDATA DENGAN NIK : {input_nik} TIDAK ADA!! ")
        return
        

### MENU UTAMA ###
def menu_utama():
    print("\n### MENU UTAMA ###")
    print("\n1. MELIHAT SEMUA \n2. DATA BUAT DATA BARU \n3. MERUBAH DATA \n4. HAPUS DATA \n5. RESTORE/MENGEMBALIKAN DATA \n6. MELIHAT SIMULASI PESANGON \n7. CARI DATA BEDASARKAN MANAJEMEN \n8. MENCARI DATA BEDASARKAN NIK \n9. EXIT/KELUAR")
    while True :
        pilih_fungsi = func_num("SILAHKAN PILIH NO DIATAS : ")
        if pilih_fungsi == "1" :
            print(" \n## MELIHAT SEMUA DATA ## ")
            read_data()
            menu_utama()
            menu_utama()
            return
        elif pilih_fungsi == "2" :
            print(" \n## MEMBUAT DATA KARYAWAN BARU ## ")
            create_data()
            menu_utama()
            return    
        elif pilih_fungsi == "3" :
            print(" \n## MERUBAH DATA KARYAWAN ## ")
            update_data()
            menu_utama()
            return

        elif pilih_fungsi == "4" :
            print(" \n## HAPUS DATA KARYAWAN ## ")
            delete_data()
            menu_utama()
            return

        elif pilih_fungsi == "5" :
            print(" \n## RESTORE/MENGEMBALIKAN DATA KARYAWAN ## ")
            restore_data()
            menu_utama()
            return

        elif pilih_fungsi == "6" :
            print(" \n## DATA SIMULASI PERHITUNGAN PESANGON YANG AKAN DI TERIMA ## ")
            read_simulasi()
            menu_utama()
            return

        elif pilih_fungsi == "7" :
            print(" \n## DATA KARYAWAN BEDASARKAN MANAJEMEN ## ")
            read_manajemen()
            menu_utama()
            return
        
        elif pilih_fungsi == "8" :
            print(" \n## MENCARI DATA BEDASARKAN NIK ## ")
            read_data_nik()
            menu_utama()
            return

        elif pilih_fungsi == "9" :
            print("### TERIMA KASIH ###")
            return 
        
        else :
            print("pilihan tidak ada, silahkan pilih nomor di atas, atau tekan x jika ingin keluar")

if __name__ == "__main__":  
    menu_utama()