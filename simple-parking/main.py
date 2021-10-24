from datetime import datetime
from csv import DictWriter
import pandas as pd


def append_dict_row(file_name, dict_of_elem, field_names):
    with open(file_name, "a+", newline="") as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)


def parking_system(luas):
    res = pd.read_csv("masuk/parkir_masuk.csv")
    res = len(res)

    if res < luas:
        try:
            # for i in range(luas):
            kode_daerah = input("\ninput Kode Daerah plat nomor kendaraan: ")
            if kode_daerah.isalpha():
                digit_angka = input("input Digit Angka plat nomor kendaraan: ")
                lenght = len(digit_angka)
                if digit_angka.isnumeric() and lenght == 4:
                    kode_akhir = input("input Kode Akhir plat nomor kendaraan: ")
                    if kode_akhir.isalpha():
                        plat_nomor = f"{kode_daerah}-{digit_angka}-{kode_akhir}"
                        T = f'{datetime.now().strftime("%H:%M:%S")}'
                        struk_parkir = f"Slot No.{res} - {plat_nomor} - jam masuk: {T}"
                        print(struk_parkir)
                        column = ["slot_nomor", "plat_nomor", "jam_masuk"]
                        row_dict = {
                            "slot_nomor": res + 1,
                            "plat_nomor": plat_nomor,
                            "jam_masuk": T,
                        }
                        append_dict_row("masuk/parkir_masuk.csv", row_dict, column)

                    else:
                        print("Kode Akhir harus karakter")
                else:
                    print("digit angka harus numeric dan berjumlah 4 digit")
            else:
                print("Kode Daerah Harus Karakter")
        except:
            print("parkir penuhh")
    else:
        print("parkir penuhh")
        exit()


if __name__ == "__main__":
    luas = input("input luas lahan: ")
    luas = int(luas)
    while True:
        try:
            parking_system(luas)
        except:
            pass
            exit()
