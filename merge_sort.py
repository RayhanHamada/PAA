hitung = 0
h = 0

# untuk menampilkan proses
def tampil_proses(kiri: list, kanan: list, menaik: bool):
    global hitung, h
    print('PROSES ', h + 1)
    print(' ' * (5 * hitung), 'Nilai Kiri = ', kiri)
    print(' ' * (5 * hitung), 'Nilai Kanan = ', kanan)
    print()

    if len(kiri) == 1 and len(kanan) == 1:
        hitung -= 1
        li = (kiri + kanan)
        li.sort(reverse=not menaik)
        print('hasil sort: ', li)
    else:
        hitung += 1
    h += 1


# Mendefinisikan fungsi merge_sort
def merge_sort(list_saya: list, menaik: bool):
    # Jika panjang dari array lebih dari 1, maka array tidak perlu di sort
    if len(list_saya) > 1:
        # mid adalah panjang dari array yang dibagi 2
        mid = len(list_saya) // 2

        # ambil nilai kiri dan kanan dari array
        kiri = list_saya[:mid]
        kanan = list_saya[mid:]

        # untuk menampilkan proses step
        tampil_proses(kiri, kanan, menaik)

        # lalu panggil fungsi merge_sort untuk bagian kiri dan kanan
        merge_sort(kiri, menaik)
        merge_sort(kanan, menaik)

        # kita inisialisasikan nilai iterator untuk array bagian kiri dan kanan
        i = 0
        j = 0

        # Kita inisiasikan nilai iterator untuk array utama
        k = 0

        # Selama i dan j belum sepanjang array kanan dan kiri
        while i < len(kiri) and j < len(kanan):

            # jika ingin di urutkan secara menaik (ascending),
            if menaik:
                # jika elemen kiri ke-i kurang dari elemen kanan ke-j,
                if kiri[i] < kanan[j]:

                    # masukan elemen kiri ke-i ke array list_saya di posisi ke-k,
                    list_saya[k] = kiri[i]

                    # lalu increment iterator untuk kiri sebanyak 1
                    i += 1
                # tapi jika elemen kiri ke-i lebih besar atau sama dengan elemen kanan ke-j,
                else:
                    # masukkan elemen kanan ke-j ke array list_saya di posisi ke-k,
                    list_saya[k] = kanan[j]

                    # lalu increment iterator untuk kanan sebanyak 1
                    j += 1
            # namun jika ingin di urutkan secara menurun (descending),
            else:

                # jika elemen kiri ke-i lebih dari elemen kanan ke-j,
                if kiri[i] > kanan[j]:

                    # masukan elemen kiri ke-i ke array list_saya di posisi ke-k,
                    list_saya[k] = kiri[i]

                    # lalu increment iterator untuk kiri sebanyak 1,
                    i += 1

                # jika elemen kiri ke-i lebih besar atau sama dengan elemen kanan ke-j,
                else:
                    # masukkan elemen kanan ke-j ke array list_saya di posisi ke-k,
                    list_saya[k] = kanan[j]

                    # increment iterator untuk kanan sebanyak 1,
                    j += 1

            # lalu maju ke slot array utama selanjutnya.
            k += 1

        # selama iterator i tidak sama dengan panjang dari array kiri,
        while i < len(kiri):
            # masukan elemen kiri ke-i ke array list_saya di posisi ke-k,
            list_saya[k] = kiri[i]

            # lalu increment i dan k.
            i += 1
            k += 1

        # selama iterator j tidak sama dengan panjang dari array kanan,
        while j < len(kanan):
            # masukan elemen kiri ke-i ke array list_saya di posisi ke-k,
            list_saya[k] = kanan[j]

            # lalu increment j dan k.
            j += 1
            k += 1


list_saya = input('Masukkan array yang ingin di sort (tiap elemen dipisah spasi): ').split()
list_saya = [int(x) for x in list_saya]

print('1. Menaik\n2. Menurun')
asc_atau_desc = input('Urutkan secara (masukkan nomor): ')


merge_sort(list_saya, asc_atau_desc == '1')
print('Hasil Akhir Sorting : ', list_saya)
