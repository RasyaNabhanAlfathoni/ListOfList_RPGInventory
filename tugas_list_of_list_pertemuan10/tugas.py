# Anggota 1:
# Nama: Rasya Nabhan Alfathoni
# NIM: 24060126130082

# Anggota 2:
# Nama: Ahza Rais Arya Triswardhana
# NIM: 24060126130094

# Definisi dan Spesifikasi Type
# Konstruktor menambahkan elemen di awal, notasi prefix 
# type List: [] atau [e o List]  
# Konstruktor menambahkan elemen di akhir, notasi postfix  
# type List: [] atau [List o e] 
type ListOfList = list[list]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list -> list of list
# {KonsLo(L, S) membentuk list baru dengan L sebagai elemen pertama S.}
# REALISASI
def KonsLo(L, S):
    return [L] + S
 
# KonsLi: list of list, list -> list of list
# {KonsLi(S, L) membentuk list baru dengan L sebagai elemen terakhir S.}
# REALISASI
def KonsLi(S, L):
    return S + [L]

# Konso: elemen, List -> List
# {Konso(e, L) menghasilkan sebuah list dari e dan L
# dengan e sebagai elemen pertama dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# REALISASI
def Konso(e, L: list) -> list:
    return e + L

# Konsi: elemen, List -> List
# {Konsi(e, L) menghasilkan sebuah list dari e dan L
# dengan e sebagai elemen terakhir dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# REALISASI
def Konsi(L: list, e) -> list:
    return L + e

# MakeInv(N, J, Jum, Nil): List of String, List of String, List of Integer, List of Integer -> List of List
#   {Membuat daftar Inventory atau penyimpanan untuk item tertentu}
# REALISASI
def MakeInv(N: list, J: list, Jum: list, Nil: list) -> ListOfList:
    return [N, J, Jum, Nil]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# NamaItem(inv) : List of List -> List of String
#   {NamaItem(inv) mengembalikan list nama item dari List Inventaris. List tipe datanya String.}
# REALISASI
def NamaItem(inv):
    return inv[0]

# JenisItem(inv) : List of List -> List of String
#   {JenisItem(inv) mengembalikan list jenis item dari List Inventaris. List tipe datanya String.}
# REALISASI
def JenisItem(inv):
    return inv[1]

# JumlahItem(inv) : List of List -> List of Integer
#   {JumlahItem(inv) mengembalikan list jumlah item dari List Inventaris. List tipe datanya Integer.}
# REALISASI
def JumlahItem(inv):
    return inv[2]

# NilaiItem(inv) : List of List -> List of Integer
#   {NilaiItem(inv) mengembalikan list nilai item dari List Inventaris. List tipe datanya Integer.}
# REALISASI
def NilaiItem(inv):
    return inv[3]

# FirstList: list of list tidak kosong -> elemen (atom atau list)
# {FirstList(S) menghasilkan elemen pertama S.}
# REALISASI
def FirstList(S):
    return S[0]
 
# LastList: list of list tidak kosong -> elemen (atom atau list)
# {LastList(S) menghasilkan elemen terakhir S.}
# REALISASI
def LastList(S):
    return S[-1]
 
# TailList: list of list tidak kosong -> list of list
# {TailList(S) menghasilkan S tanpa elemen pertamanya.}
# REALISASI
def TailList(S):
    return S[1:]
 
# HeadList: list of list tidak kosong -> list of list
# {HeadList(S) menghasilkan S tanpa elemen terakhirnya.}
# REALISASI
def HeadList(S):
    return S[:-1]


# DEFINISI DAN SPESIFIKASI PREDIKTOR
# IsEmpty: list of list -> boolean
# {IsEmpty(S) benar jika S adalah list of list kosong.}
# REALISASI
def IsEmpty(S):
    return S == []
 
# IsAtom: list of list -> boolean
# {IsAtom(S) benar jika S adalah sebuah atom.}
# REALISASI
def IsAtom(S):
    return type(S) != list
 
# IsList: list of list -> boolean
# {IsList(S) benar jika S adalah sebuah list.}
# REALISASI
def IsList(S):
    return type(S) == list
 
# IsOneElmt: list of list -> boolean
# {IsOneElmt(S) benar jika S hanya mempunyai satu elemen.}
# REALISASI
def IsOneElmt(S):
    return len(S) == 1

# IsInventarisKosong: ListOfList -> boolean
# {IsInventarisKosong(inv) Memeriksa apakah inventory kosong atau tidak, True jika kosong, False jika ada isi inventory.}
# REALISASI
def IsInventarisKosong(inv: ListOfList) -> bool:
    return (IsEmpty(NamaItem(inv)) and IsEmpty(JenisItem(inv)) and IsEmpty(JumlahItem(inv)) and IsEmpty(NilaiItem(inv)))


# IsItemTersedia: ListOfList, string -> boolean
# {IsItemTersedia(inv, nama) Memeriksa apakah suatu item ada di dalam inventory atau tidak, True jika ada, false jika tidak ada. }
# REALISASI
def IsItemTersedia(inv: ListOfList, nama: str) -> bool:
    if IsInventarisKosong(inv):
        return False
    elif FirstList(NamaItem(inv)) == nama:
        return True
    else:
        return IsItemTersedia(MakeInv(
            TailList(NamaItem(inv)), 
            TailList(JenisItem(inv)),
            TailList(JumlahItem(inv)),
            TailList(NilaiItem(inv))
            ), nama)

 
# IsItemLangka: ListOfList, string, integer <= 100) ->  boolean
# {IsItemLangka(inv, nama, batas) Memeriksa apakah suatu item yang ada di dalam inventory bersifat langka, 
#   True jika nilai item melebihi batas kelangkaan, False jika tidak.}
# REALISASI
def IsItemLangka(inv: ListOfList, nama: str, batas: int) -> bool:
    if IsInventarisKosong(inv):
        return False
    elif FirstList(NamaItem(inv)) == nama:
        return FirstList(NilaiItem(inv)) >= batas
    else:
        return IsItemLangka(MakeInv(
            TailList(NamaItem(inv)),
            TailList(JenisItem(inv)),
            TailList(JumlahItem(inv)),
            TailList(NilaiItem(inv))
            ), nama, batas)

    
# DEFINISI DAN SPESIFIKASI FUNGSI TAMBAHAN
# TotalItem: ListOfList -> int
# {TotalItem (inv) menghitung jumlah item yang ada di dalam inventory}
# REALISASI
def TotalItem(inv: ListOfList) -> int:
    if IsInventarisKosong(inv):
        return 0
    else:
        return FirstList(JumlahItem(inv)) + TotalItem(MakeInv(
            TailList(NamaItem(inv)),
            TailList(JenisItem(inv)),
            TailList(JumlahItem(inv)),
            TailList(NilaiItem(inv))
            ))


# TotalNilai: ListOfList -> int
# {TotalItem(inv) menjumlahkan nilai dari item di dalam inventory}
# REALISASI
def TotalNilai(inv: ListOfList) -> int:
    if IsInventarisKosong(inv):
        return 0
    else:
        return FirstList(NilaiItem(inv)) + TotalNilai(MakeInv(
            TailList(NamaItem(inv)),
            TailList(JenisItem(inv)),
            TailList(JumlahItem(inv)),
            TailList(NilaiItem(inv))
            ))


# FilterJenis: ListOfList, String -> List of String
# {FilterJenis (inv, jenis) Menghasilkan list nama item yang jenisnya sama dengan parameter jenis.
#   Jika tidak akan menghasilkan list kosong}
# REALISASI
def FilterJenis(inv: ListOfList, jenis: str) -> list:
    if IsInventarisKosong(inv):
        return []
    elif FirstList(JenisItem(inv)) == jenis:
        return Konso([FirstList(NamaItem(inv))], FilterJenis(MakeInv(
            TailList(NamaItem(inv)),
            TailList(JenisItem(inv)),
            TailList(JumlahItem(inv)),
            TailList(NilaiItem(inv))
            ), jenis))
    else:
        return FilterJenis(MakeInv(
            TailList(NamaItem(inv)),
            TailList(JenisItem(inv)),
            TailList(JumlahItem(inv)),
            TailList(NilaiItem(inv))
            ), jenis)
              
# APLIKASI
print(IsInventarisKosong(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        [4,4,2],
        [20, 40, 85]
    ]
))
              
print(IsItemTersedia(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        [4,4,2],
        [20, 40, 85]
    ], 
    "pedang"
))
              
print(IsItemLangka(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        [4,4,2],
        [20, 40, 85]
    ], 
    "jamu", 80
))

print(TotalItem(
    [
        ["Pedang", "Perisai", "Jamu"],
        ["Senjata", "Armor", "Potion"],
        [4, 4, 2],
        [20, 40, 85]
    ]
))

print(TotalNilai(
    [
        ["Pedang", "Perisai", "Jamu"],
        ["Senjata", "Armor", "Potion"],
        [4, 4, 2],
        [20, 40, 85]
    ]
))
                            
print(FilterJenis(
    [
        ["pedang", "perisai", "jamu", "paracetamol"],
        ["senjata", "armor", "potion", "potion"],
        [4,4,2],
        [20, 40, 85]
    ], 
    "potion"
))
