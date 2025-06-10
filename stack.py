piring = []

def push(stack, add):
    for i in range(add):
        output = f"p-{len(stack)+1}"
        stack.append(output)
        print(f"Data {output} telah ditambahkan")

def pop(stack):
    top = len(stack)-1
    isempty = top < 0
    if isempty:
        print("Piring kotor nya kosong")
    else:    
        output = stack.pop()
        print(f"piring {output} sudah di ambil")
    
def top(stack):
    top = len(stack)-1
    isempty = top < 0
    if isempty:
        print("Piring kotor nya kosong")
    else:
        print(f"piring paling atas adalah: {stack[top]}")
    
def main(stack):
    print("="*10, "Selamat Datang", "="*10)
    print("\n")
    while True:
        print("Pilihan 1-5")
        print("1. Tambah piring kotor")
        print("2. Cuci piring")
        print("3. piring paling atas")
        print("4. Sisa piring kotor")
        print("5. Keluar")
        pilih = int(input("Masukan pilihan: "))
        print("\n")
        if pilih == 1:
            p = int(input("Masukan jumlah cucian piring: "))
            print("="*70)
            push(piring, p)
            print("="*70)
            print("\n")
        elif pilih == 2:
            print("="*70)
            pop(piring)
            print("="*70)
            print("\n")
        elif pilih == 3:
            print("="*70)
            top(piring)
            print("="*70)
            print("\n")
        elif pilih == 4:
            print("sisa piring")
            for i in piring:
                if i < 0:
                    print("gaada wak")
                else:
                    print(i)
            print("\n")
        elif pilih == 5:
            print("Terima kasih")
            break
        else:
            print("Pilihan gaada")
        
    
    
main(piring)