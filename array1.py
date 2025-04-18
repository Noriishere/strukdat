# cus = []
# def tambah_pelanggan():
#     while True:
#         inputcus = input("Masukkan nama customer: ")
#         cus.append(inputcus)
#         nocus = len(cus)
#         print(f"Customer yang ke-{nocus} sudah terdaftar")
#         choose = input("Apakah Anda ingin menambah customer lainnya? (y/n): ").lower()
#         while choose not in ["y", "n"]:
#             choose = input("Maaf, input Anda salah. Apakah Anda ingin menambah customer lainnya? (y/n): ").lower()
#         if choose == "n":
#             break
#         elif choose == "y":
#             print("-" * 10)
#     return cus
# tambah_pelanggan()
# print("\nDaftar pelanggan yang terdaftar:")
# for pelanggan in cus:
#     print(pelanggan)
print(("-"*10),"Selamat datang Workers NORI's INDUSTRIES-!",("-"*10),)
print("{:<15}".format("1."))