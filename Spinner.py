def counterClockwise(inputList): # Fungsi counterClockwise dengan 1 parameter, yaitu List_awal yang akan diinput oleh user
    outputList = [[], [], []] # Menyatakan var outputList dengan tipe list untuk tempat menyimpan output agar listInput tetap dalam keadaan yang sama. Var ini dibuat sama dengan bentuk input untuk memudahkan konversi.
    for x in range(len(inputList)): # Loop dengan acuan angka 0, 1, 2 (range(len(inputList))) untuk mengakses index outputList. Loop ini ditempatkan di awal karena untuk meng-"append" 3 kali nilai, diperlukan index yang tetap selama prosesnya.
        for y in range(len(inputList)): # Nested loop dengan acuan angka 0, 1, 2 (range(len(inputList))) untuk mengakses index inputList. Loop ini ditempatkan di bawah karena diperlukan index yang dinamis untuk mengakses 3 nilai di inputList.
            outputList[x].append(inputList[y][len(inputList) - 1 - x]) # "Append" dilakukan di dalam blok kode loop kedua agar bisa mengakses index yang selalu berubah di inputList. Pada sisi lain, index untuk "append" ke outputList tidak berubah.

    return(outputList) # Mengembalikan outputList yang sudah selesai dan lengkap kepada user.

List_awal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Contoh inputList dari soal.
print(counterClockwise(List_awal)) # Mencetak jawaban. Fungsi "print" diperlukan agar hasil bisa tercetak karena output dalam fungsi hanya berupa "return".