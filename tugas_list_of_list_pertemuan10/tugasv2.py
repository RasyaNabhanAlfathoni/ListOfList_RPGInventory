# Nama Kasus: Inventaris Game RPG

# Anggota 1:
# Nama: Rasya Nabhan Alfathoni
# NIM: 24060126130082

# Anggota 2:
# Nama: Ahza Rais Arya Triswardhana
# NIM: 24060126130094

# Definisi dan Spesifikasi Type
# Konstruktor menambahkan elemen di awal, notasi prefix 
# type List: [] atau [L o ListOfList]
# Konstruktor menambahkan elemen di akhir, notasi postfix  
# type List: [] atau [ListOfList o L]
type ListOfList = list[list]


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list -> list of list
# {KonsLo(L, S) membentuk list baru dengan L sebagai elemen pertama S.}
# REALISASI
def KonsLo(L, S):
    """Konslo(L, S) menghasilkan sebuah list dari L dan S
   dengan L sebagai elemen pertama dari list of list S"""
    return [L] + S
 
# KonsLi: list of list, list -> list of list
# {KonsLi(S, L) membentuk list baru dengan L sebagai elemen terakhir S.}
# REALISASI
def KonsLi(S, L):
    """KonsLi(S, L) menghasilkan sebuah list dari L dan S
    dengan L sebagai elemen terakhir dari list of list S."""
    return S + [L]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong -> elemen (atom atau list)
# {FirstList(S) menghasilkan elemen pertama S.}
# REALISASI
def FirstList(S):
    """FirstList(S) menghasilkan elemen pertama S."""
    return S[0]
 
# LastList: list of list tidak kosong -> elemen (atom atau list)
# {LastList(S) menghasilkan elemen terakhir S.}
# REALISASI
def LastList(S):
    """LastList(S) menghasilkan elemen terakhir S."""
    return S[-1]
 
# TailList: list of list tidak kosong -> list of list
# {TailList(S) menghasilkan S tanpa elemen pertamanya.}
# REALISASI
def TailList(S):
    """TailList(S) menghasilkan S tanpa elemen pertamanya."""
    return S[1:]
 
# HeadList: list of list tidak kosong -> list of list
# {HeadList(S) menghasilkan S tanpa elemen terakhirnya.}
# REALISASI
def HeadList(S):
    """HeadList(S) menghasilkan S tanpa elemen terakhirnya."""
    return S[:-1]

# KolomKe: ListOfList, integer >= 0 -> list
# {KolomKe(inv, n) menghasilkan list ke-n dari inv (indeks mulai 0).}
def KolomKe(inv: ListOfList, n: int) -> list:
    """KolomKe(inv, n) menghasilkan list ke-n dari inv (indeks mulai 0)."""
    if IsAtom(FirstList(inv)):
        return KolomKe(TailList(inv), n)
    elif n == 0:
        return FirstList(inv)
    else:
        return KolomKe(TailList(inv), n - 1)

# NamaItem(inv) : List of List -> List of String
# {NamaItem(inv) mengembalikan list nama item dari List Inventaris. List tipe datanya String.}
# REALISASI
def NamaItem(inv):
    """NamaItem(inv) mengembalikan list nama item dari List Inventaris. 
    List tipe datanya String."""
    return KolomKe(inv, 0)

# JenisItem(inv) : List of List -> List of String
# {JenisItem(inv) mengembalikan list jenis item dari List Inventaris. List tipe datanya String.}
# REALISASI
def JenisItem(inv):
    """JenisItem(inv) mengembalikan list jenis item dari List Inventaris. 
    List tipe datanya String."""
    return KolomKe(inv, 1)

# JumlahItem(inv) : List of List -> List of Integer
# {JumlahItem(inv) mengembalikan list jumlah item dari List Inventaris. List tipe datanya Integer.}
# REALISASI
def JumlahItem(inv):
    """JumlahItem(inv) mengembalikan list jumlah item dari List Inventaris. 
    List tipe datanya Integer."""
    return KolomKe(inv, 2)

# NilaiItem(inv) : List of List -> List of Integer
# {NilaiItem(inv) mengembalikan list nilai item dari List Inventaris. List tipe datanya Integer.}
# REALISASI
def NilaiItem(inv):
    """NilaiItem(inv) mengembalikan list nilai item dari List Inventaris. 
    List tipe datanya Integer."""
    return KolomKe(inv, 3)

# TailInv: ListOfList tidak kosong -> ListOfList
# {TailInv(inv) menghasilkan inv di mana setiap list-nya dibuang elemen pertamanya.
#  Jumlah list di dalam inv bebas.}
def TailInv(inv: ListOfList) -> ListOfList:
    """TailInv(inv) menghasilkan inv di mana setiap list-nya dibuang elemen pertamanya.
    Jumlah list di dalam inv bebas."""
    if IsEmpty(inv):
        return []
    elif IsAtom(FirstList(inv)):
        return TailInv(TailList(inv))
    else:
        return KonsLo(TailList(FirstList(inv)), TailInv(TailList(inv)))


# DEFINISI DAN SPESIFIKASI PREDIKTOR
# IsEmpty: list of list -> boolean
# {IsEmpty(S) benar jika S adalah list of list kosong.}
# REALISASI
def IsEmpty(S):
    """IsEmpty(S) benar jika S adalah list of list kosong."""
    return S == []
 
# IsAtom: list of list -> boolean
# {IsAtom(S) benar jika S adalah sebuah atom.}
# REALISASI
def IsAtom(S):
    """IsAtom(S) benar jika S adalah sebuah atom."""
    return type(S) != list
 
# IsList: list of list -> boolean
# {IsList(S) benar jika S adalah sebuah list.}
# REALISASI
def IsList(S):
    """IsList(S) benar jika S adalah sebuah list."""
    return type(S) == list

# IsInventarisKosong: ListOfList -> boolean
# {IsInventarisKosong(inv) Memeriksa apakah inventory kosong atau tidak, True jika kosong, False jika ada isi inventory.}
# REALISASI
def IsInventarisKosong(inv: ListOfList) -> bool:
    """IsInventarisKosong(inv) Memeriksa apakah inventory kosong atau tidak. 
    Berdasarkan nama suatu itemnya."""
    return IsEmpty(NamaItem(inv))

# IsItemTersedia: ListOfList, string -> boolean
# {IsItemTersedia(inv, nama) Memeriksa apakah suatu item ada di dalam inventory atau tidak, 
#   True jika ada, false jika tidak ada.}
# REALISASI
def IsItemTersedia(inv: ListOfList, nama: str) -> bool:
    """IsItemTersedia(inv, nama) Memeriksa apakah suatu item ada di dalam inventory atau tidak.
    Berdasarkan nama itemnya"""
    if IsInventarisKosong(inv):
        return False
    elif FirstList(NamaItem(inv)) == nama:
        return True
    else:
        return IsItemTersedia(TailInv(inv), nama)
 
# IsItemLangka: ListOfList, string, integer <= 100) ->  boolean
# {IsItemLangka(inv, nama, batas) Memeriksa apakah suatu item yang ada di dalam inventory bersifat langka, 
#   True jika nilai item melebihi batas kelangkaan, False jika tidak.}
# REALISASI
def IsItemLangka(inv: ListOfList, nama: str, batas: int) -> bool:
    """IsItemLangka(inv, nama, batas) Memeriksa apakah suatu item yang ada di dalam inventory bersifat langka.
    Jika nilai item melebihi batas maka item dianggap langka."""
    if IsInventarisKosong(inv):
        return False
    elif FirstList(NamaItem(inv)) == nama:
        return FirstList(NilaiItem(inv)) >= batas
    else:
        return IsItemLangka(TailInv(inv), nama, batas)

    
# DEFINISI DAN SPESIFIKASI FUNGSI TAMBAHAN
# TotalItem: ListOfList -> int
# {TotalItem (inv) menghitung jumlah item yang ada di dalam inventory}
# REALISASI
def TotalItem(inv: ListOfList) -> int:
    """TotalItem (inv) menghitung jumlah item yang ada di dalam inventory"""
    if IsInventarisKosong(inv):
        return 0
    else:
        return FirstList(JumlahItem(inv)) + TotalItem(TailInv(inv))

# TotalNilai: ListOfList -> int
# {TotalItem(inv) menjumlahkan nilai dari item di dalam inventory}
# REALISASI
def TotalNilai(inv: ListOfList) -> int:
    """TotalItem(inv) menjumlahkan nilai dari seluruh item di dalam inventory"""
    if IsInventarisKosong(inv):
        return 0
    else:
        return FirstList(NilaiItem(inv)) + TotalNilai(TailInv(inv))

# FilterJenis: ListOfList, String -> List of String
# {FilterJenis (inv, jenis) Menghasilkan list nama item yang jenisnya sama dengan parameter jenis.
#   Jika tidak akan menghasilkan list kosong}
# REALISASI
def FilterJenis(inv: ListOfList, jenis: str) -> list:
    """FilterJenis (inv, jenis) Menghasilkan list nama item yang jenisnya sama dengan parameter jenis."""
    if IsInventarisKosong(inv):
        return []
    elif FirstList(JenisItem(inv)) == jenis:
        return KonsLo(FirstList(NamaItem(inv)), FilterJenis(TailInv(inv), jenis))
    else:
        return FilterJenis(TailInv(inv), jenis)


# APLIKASI
print("=== IsInventarisKosong ===")
print(IsInventarisKosong(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        [4,4,2],
        [20, 40, 85]
    ]
))

print("=== IsItemTersedia ===")              
print(IsItemTersedia(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        [4,4,2],
        [20, 40, 85]
    ], 
    "jamu"
))
   
print("=== IsItemLangka ===")           
print(IsItemLangka(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        [4,4,2],
        [20, 40, 85]
    ], 
    "jamu", 80
))

print("=== TotalItem ===")
print(TotalItem(
    [
        ["Pedang", "Perisai", "Jamu"],
        ["Senjata", "Armor", "Potion"],
        [4, 4, 2],
        [20, 40, 85]
    ]
))

print("=== TotalNilai ===")
print(TotalNilai(
    [
        ["Pedang", "Perisai", "Jamu"],
        ["Senjata", "Armor", "Potion"],
        [4, 4, 2],
        [20, 40, 85]
    ]
))

print("=== FilterJenis ===")                            
print(FilterJenis(
    [
        ["pedang", "perisai", "jamu", "paracetamol"],
        ["senjata", "armor", "potion", "potion"],
        [4,4,2],
        [20, 40, 85]
    ], 
    "potion"
))
