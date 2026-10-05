# Nama File: statusKarakter.py
# Tanggal: 5 Oktober 2026
# Deskripsi: Menentukan status karakter berdasarkan beberapa ketentuan

# Definisi dan Spesifikasi Type
# type karakter : <nama: string, level: integer [1..100], kelas: string>
# {kelas ∈ {"Ksatria","Penyihir","Pemanah"}}
# type atribut : <hp: integer [0..100], mana: integer [0..100],
# stamina: integer [0..100]>
# type lingkungan : <area: string, waktu: string, musuh: integer ≥ 0>
# {area ∈ {"Hutan","Gurun","Gua"}; waktu ∈ {"Siang","Malam"}}
# type statuskar : <nama: string, status: string>
# {status ∈ {"Aman","Siaga","Kritis","Gugur"}}

# Definisi dan spesifikasi konstruktor dan selektor
# KONSTRUKTOR
# MakeKarakter : string, integer [1..100], string → karakter
# {MakeKarakter(n,l,k) membentuk karakter bernama n, level l, kelas k}
# MakeAtribut : 3 integer [0..100] → atribut
# {MakeAtribut(h,m,s) membentuk atribut dengan HP h, mana m, stamina s}
# MakeLingkungan : 2 string, integer ≥ 0 → lingkungan
# {MakeLingkungan(a,w,e) membentuk lingkungan area a, waktu w, jumlah musuh e}
# MakeStatusKar : 2 string → statuskar
# {MakeStatusKar(n,s) membentuk status s untuk karakter n}

# SELEKTOR {setiap selektor memberikan komponen yang namanya bersesuaian}
# NamaKar : karakter → string
# Level : karakter → integer [1..100]
# Kelas : karakter → string
# HP : atribut → integer
# Mana : atribut → integer
# Stamina : atribut → integer
# Area : lingkungan → string
# Waktu : lingkungan → string
# JmlMusuh: lingkungan → integer ≥ 0
# NamaSt : statuskar → string
# StatusSt: statuskar → string

# Definisi, spesifikasi, dan realisasi Evaluasi_Karakter
# Evaluasi_Karakter : karakter, atribut, lingkungan → statuskar
# {Evaluasi_Karakter(K,A,L) menghasilkan nama karakter K dan statusnya
# menurut aturan (a)–(g) yang diperiksa berurutan}

# StatusKarakter : karakter, atribut, lingkungan → string {fungsi antara}

# REALISASI
# StatusKarakter(K,A,L) :
# let h = HP(A), e = JmlMusuh(L) in
# if h ≤ 0 then "Gugur" {a}
# else if h < 20 then "Kritis" {b}
# else if e > 5 and Level(K) < 10 then "Kritis" {c}
# else if Kelas(K) = "Penyihir" and Mana(A) < 15 then "Siaga" {d}
# else if h ≥ 80 and Stamina(A) ≥ 50 then "Aman" {e}
# else if (Area(L) = "Gua" and Waktu(L) = "Malam") or e ≥ 3
# then "Siaga" {f}
# else "Aman" {g}
# Evaluasi_Karakter(K,A,L) :
# MakeStatusKar(NamaKar(K), StatusKarakter(K,A,L))

# Realisasi Kode
type Karakter = tuple[int, int, str]
type Atribut = tuple[int, int, int]
type Lingkungan = tuple[str, str, int]
type Status = tuple[str, str]

def getNama(karakter: Karakter) -> str:
    return karakter[0]
def getLevel(karakter: Karakter) -> int:
    return karakter[1]
def getKelasKarakter(karakter: Karakter) -> str:
    return karakter[2]

def getHP(atribut: Atribut) -> int:
    return atribut[0]
def getMana(atribut: Atribut) -> int:
    return atribut[1]
def getStamina(atribut: Atribut) -> int:
    return atribut[2]

def getArea(lingkungan: Lingkungan) -> str:
    return lingkungan[0]
def getWaktu(lingkungan: Lingkungan) -> str:
    return lingkungan[1]
def getJumlahMusuh(lingkungan: Lingkungan) -> int:
    return lingkungan[2]

def getNamaKar(status: Status) -> str:
    return status[0]
def statusKar(status: Status) -> str:
    return status[1]

def MakeK(nama: str, level:int, kelas_karakter: str) -> Karakter:
    if (1 <= level) and (level <= 100):
        if (kelas_karakter == "Ksatria") or (kelas_karakter == "Penyihir") or (kelas_karakter == "Pemanah"):
            return (nama, level, kelas_karakter)
        else:
            return KeyError
    else:
        return KeyError 

def MakeA(HP: int, mana: int, stamina:int) -> Atribut:
    if ((1 <= HP) and (HP <= 100)) and ((1 <= mana) and (mana <= 100)) and ((1 <= stamina) and (stamina <= 100)):
        return (HP, mana, stamina)
    else:
        return KeyError

def MakeL(area: str, waktu: str, jumlahMusuh: int):
    if (area == "Hutan") or (area == "Gurun") or (area == "Gua"):
        if (waktu == "Siang") or (waktu == "Malam"):
            return (area, waktu, jumlahMusuh)
        else:
            return KeyError
    else:
        return KeyError

def MakeS(nama: str, status: str) -> Status:
    if (status == "Aman") or (status == "Siaga") or (status == "Kritis") or (status == "Gugur"): 
        return (nama, status)
    else:
        return KeyError

def statusKarakter(K,A,L):
    if getHP(A) <= 0:
        return "Gugur"
    elif getHP(A) < 20:
        return "Kritis"
    elif (getJumlahMusuh(L) > 5) and (getLevel(K) < 10):
        return "Kritis"
    elif (getKelasKarakter(K) == "Penyihir") and (getMana(A) < 15):
        return "Siaga"
    elif (getHP(A) >= 80) and (getStamina(A) >= 50):
        return "Aman"
    elif ((getArea(L) == "Gua") and (getWaktu(L) == "Malam")) or getJumlahMusuh(L) >= 3:
        return "Siaga"
    else:
        return "Aman"

def Evaluasi_Karakter(K, A, L):
    return MakeS(getNama(K), statusKarakter(K,A,L))

# Aplikasi
print(Evaluasi_Karakter(MakeK("Albedo", 5, "Penyihir"), MakeA(80,80,80), MakeL("Gua", "Malam", 2)))
print(Evaluasi_Karakter(MakeK("Sindra", 5, "Ksatria"), MakeA(70,80,30), MakeL("Gua", "Siang", 2)))