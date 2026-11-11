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
# Konso: elemen, List -> List
#   { Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# dari L. }
# REALISASI
def Konso(E: int, L: list) -> list:
    """Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
    dari L."""
    return [E] + L

# Konsi: List, elemen -> List
#   { Konsi(L, e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# dari L. }
# REALISASI
def Konsi(L: list, E: int) -> list:
    """Konsi(L, e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
    dari L."""
    return L + [E]

# KonsLo: list, list of list -> list of list
# {KonsLo(L, S) membentuk list baru dengan L sebagai elemen pertama S.}
# REALISASI
def KonsLo(L: list, S: ListOfList) -> ListOfList:
    """Konslo(L, S) menghasilkan sebuah list dari L dan S
   dengan L sebagai elemen pertama dari list of list S"""
    return [L] + S
 
# KonsLi: list of list, list -> list of list
# {KonsLi(S, L) membentuk list baru dengan L sebagai elemen terakhir S.}
# REALISASI
def KonsLi(S: ListOfList, L: list) -> ListOfList:
    """KonsLi(S, L) menghasilkan sebuah list dari L dan S
    dengan L sebagai elemen terakhir dari list of list S."""
    return S + [L]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong -> elemen (atom atau list)
# {FirstList(S) menghasilkan elemen pertama S.}
# REALISASI
def FirstList(S: ListOfList):
    """FirstList(S) menghasilkan elemen pertama S."""
    return S[0]
 
# LastList: list of list tidak kosong -> elemen (atom atau list)
# {LastList(S) menghasilkan elemen terakhir S.}
# REALISASI
def LastList(S: ListOfList):
    """LastList(S) menghasilkan elemen terakhir S."""
    return S[-1]
 
# TailList: list of list tidak kosong -> list of list
# {TailList(S) menghasilkan S tanpa elemen pertamanya.}
# REALISASI
def TailList(S: ListOfList) -> ListOfList:
    """TailList(S) menghasilkan S tanpa elemen pertamanya."""
    return S[1:]
 
# HeadList: list of list tidak kosong -> list of list
# {HeadList(S) menghasilkan S tanpa elemen terakhirnya.}
# REALISASI
def HeadList(S: ListOfList) -> ListOfList:
    """HeadList(S) menghasilkan S tanpa elemen terakhirnya."""
    return S[:-1]

# FirstElmt: List tidak kosong -> elemen
#   { FirstElmt(L) mengembalikan elemen pertama dari L. }
# REALISASI
def FirstElmt(L: list) -> int:
    """FirstElmt(L) mengembalikan elemen pertama dari L."""
    return L[0]

# Tail(L): List tidak kosong -> List
# {Tail(L) mengembalikan list L tanpa elemen pertama
#   dari L; dapat menghasilkan list kosong.}
# Realisasi:
def Tail(L: list) -> list:
    """Tail(L) mengembalikan list L tanpa elemen pertama
    dari L; dapat menghasilkan list kosong."""
    return L[1:]


# DEFINISI DAN SPESIFIKASI PREDIKTOR
# IsEmpty: list of list -> boolean
# {IsEmpty(S) benar jika S adalah list of list kosong.}
# REALISASI
def IsEmpty(S: ListOfList) -> bool:
    """IsEmpty(S) benar jika S adalah list of list kosong."""
    return S == []
 
# IsAtom: list of list -> boolean
# {IsAtom(S) benar jika S adalah sebuah atom.}
# REALISASI
def IsAtom(S: ListOfList) -> bool:
    """IsAtom(S) benar jika S adalah sebuah atom."""
    return (S * 0 == 0) or (S * 0 == "")
 
# IsList: list of list -> boolean
# {IsList(S) benar jika S adalah sebuah list.}
# REALISASI
def IsList(S: ListOfList) -> bool:
    """IsList(S) benar jika S adalah sebuah list."""
    return S * 0 == []

# IsMember: elemen, List -> boolean
# {IsMember(X, L) bernilai True apabila X merupakan elemen dari List.}
# REALISASI
def IsMember(X: int, L: list) -> bool:
    """IsMember(X, L) bernilai True apabila X merupakan elemen dari List."""
    if IsEmpty(L):
        return False
    elif X == FirstElmt(L):
        return True
    else:
        return IsMember(X, Tail(L))

# IsInventarisKosong: ListOfList -> boolean
# {IsInventarisKosong(inv) Memeriksa apakah inventory kosong atau tidak, True jika kosong, False jika ada isi inventory.}
# REALISASI
def IsInventarisKosong(inv: ListOfList) -> bool:
    """IsInventarisKosong(inv) Memeriksa apakah inventory kosong atau tidak."""
    return IsEmpty(inv)

# IsItemTersedia: ListOfList, string -> boolean
# {IsItemTersedia(inv, nama) Memeriksa apakah suatu item ada di dalam inventory atau tidak, 
#   True jika ada, false jika tidak ada.}
# REALISASI
def IsItemTersedia(inv: ListOfList, nama: str) -> bool:
    """IsItemTersedia(inv, nama) Memeriksa apakah suatu item ada di dalam inventory atau tidak.
    Berdasarkan nama itemnya"""
    if IsInventarisKosong(inv):
        return False
    elif IsMember(nama, FirstList(inv)):
        return True
    else:
        return IsItemTersedia(TailList(inv), nama)
 
# IsItemLangka: ListOfList, string, integer <= 100) ->  boolean
# {IsItemLangka(inv, nama, batas) Memeriksa apakah suatu item yang ada di dalam inventory bersifat langka, 
#   True jika nilai item melebihi batas kelangkaan, False jika tidak.}
# REALISASI
def IsItemLangka(inv: ListOfList, nama: str, batas: int) -> bool:
    """IsItemLangka(inv, nama, batas) Memeriksa apakah suatu item yang ada di dalam inventory bersifat langka.
    Jika banyaknya item tidak melebihi batas maka item dianggap langka."""
    if IsInventarisKosong(inv):
        return False
    elif IsItemTersedia(inv, nama):
        return JumElmtListOfList(inv, nama) <= batas
    else:
        return IsItemLangka(TailList(inv), nama, batas)

    
# DEFINISI DAN SPESIFIKASI FUNGSI TAMBAHAN
# TotalElmt(L): List -> integer
# {TotalElmt(L) menghasilkan total nilai elemen dalam list L.}
# REALISASI
def TotalElmt(L: list) -> int:
    """TotalElmt(L) menghasilkan total nilai elemen dalam list L."""
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + TotalElmt(TailList(L))

# JumElmtList: list, string -> integer
# {JumElmtList(L, nama) menghasilkan banyak kemunculan elemen (nama) di sebuah list.}
# REALISASI
def JumElmtList(L: list, nama: str) -> int:
    """JumElmtList(L, nama) menghasilkan banyak kemunculan elemen (nama) di sebuah list."""
    if IsEmpty(L):
        return 0
    elif FirstList(L) == nama:
        return 1 + JumElmtList(Tail(L), nama)
    else:
        return JumElmtList(Tail(L), nama)
 
# JumElmtListOfList: ListOfList, string -> integer
# {JumElmtListOfList(S, nama) menghasilkan banyak kemunculan elemen (nama) di list of list.}
# REALISASI
def JumElmtListOfList(S: ListOfList, nama: str) -> int:
    """JumElmtListOfList(S, nama) menghasilkan banyak kemunculan elemen (nama) di list of list."""
    if IsEmpty(S):
        return 0
    else:
        return JumElmtList(FirstList(S), nama) + JumElmtListOfList(TailList(S), nama)

# TotalItem: ListOfList -> int
# {TotalItem (inv) menghitung jumlah item yang ada di dalam inventory}
# REALISASI
def TotalItem(inv: ListOfList) -> int:
    """TotalItem (inv) menghitung jumlah item yang ada di dalam inventory"""
    if IsInventarisKosong(inv):
        return 0
    else:
        return TotalElmt(FirstList(inv)) + TotalItem(TailList(inv))

# FilterItem: ListOfList, String -> List of String
# {FilterItem (inv, nama) Menghasilkan list nama item yang namanya sama dengan parameter nama.
#   Jika tidak akan menghasilkan list kosong}
# REALISASI
def FilterItem(inv: ListOfList, nama: str) -> ListOfList:
    """FilterItem (inv, nama) Menghasilkan list of list item yang namanya sama dengan parameter nama."""
    if IsInventarisKosong(inv):
        return []
    elif IsAtom(FirstList(inv)):
        if FirstList(inv) == nama:
            return Konso(FirstList(inv), FilterItem(TailList(inv), nama))
        else:
            return FilterItem(TailList(inv), nama)
    else:
        return KonsLo(FilterItem(FirstList(inv), nama), FilterItem(TailList(inv), nama))


# APLIKASI
print("=== IsInventarisKosong ===")
print(IsInventarisKosong(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        []
    ]
))

print("=== IsItemTersedia ===")              
print(IsItemTersedia(
    [
        ["pedang", "perisai", "jamu"],
        ["kapak", "baja", "paracetamol"],
        []
    ], 
    "jamu"
))
   
print("=== IsItemLangka ===")           
print(IsItemLangka(
    [
        ["pedang", "perisai", "jamu"],
        ["jamu", "kapak"],
        []
    ], 
    "jamu", 2
))

print("=== TotalItem ===")
print(TotalItem(
    [
        [4, 4, 2], 
        [1, 2], 
        []
    ]
))

print("=== JumElmtListOfList ===")
print(JumElmtListOfList(
    [
        ["jamu", "pedang"], 
        [], 
        ["jamu"]
    ], 
    "jamu"
))

print("=== FilterJenis ===")                            
print(FilterItem(
    [
        ["pedang", "perisai", "jamu"],
        ["senjata", "armor", "potion"],
        []
    ], 
    "potion"
))
