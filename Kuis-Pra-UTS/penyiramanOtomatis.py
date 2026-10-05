# Nama File: penyiramanOtomatis.py
# Tanggal: 5 Oktober 2026
# Deskripsi: Menentukan kekuatan sebuah alat penyiraman ke tanaman berdasarkan beberapa ketentuan

# Definisi Spesifikasi
# DEFINISI DAN SPESIFIKASI TYPE
# type tanaman : <nama: string, fase: string, butuh: real [0..100]>
# {fase ∈ {"Semai","Vegetatif","Generatif"}; butuh = kelembapan minimum (%)}
# type sensor : <lembap: real [0..100], suhu: real, cahaya: real ≥ 0>
# {kelembapan tanah (%), suhu udara (°C), intensitas cahaya (lux)}
# type tangki : <volume: real ≥ 0, pompa: boolean>
# {volume air (liter); pompa = true jika berfungsi}
# type tindakan : <nama: string, aksi: string>
# {aksi ∈ {"Siram Penuh","Siram Ringan","Tunda","Darurat"}}

# KONSTRUKTOR
# MakeTanaman : 2 string, real [0..100] → tanaman
# {MakeTanaman(n,f,b) membentuk tanaman bernama n, fase f, kebutuhan air b}
# MakeSensor : real [0..100], real, real ≥ 0 → sensor
# {MakeSensor(l,s,c) membentuk data sensor: kelembapan l, suhu s, cahaya c}
# MakeTangki : real ≥ 0, boolean → tangki
# {MakeTangki(v,p) membentuk tangki dengan volume v dan status pompa p}
# MakeTindakan : 2 string → tindakan
# {MakeTindakan(n,a) membentuk tindakan a untuk tanaman n}

# SELEKTOR {setiap selektor memberikan komponen yang namanya bersesuaian}
# NamaTanaman : tanaman → string
# Fase : tanaman → string
# Butuh : tanaman → real
# Lembap : sensor → real
# Suhu : sensor → real
# Cahaya : sensor → real
# Volume : tangki → real
# PompaOK : tangki → boolean
# NamaTdk : tindakan → string
# Aksi : tindakan → string

# DEFINISI DAN SPESIFIKASI
# Tentukan_Penyiraman : tanaman, sensor, tangki → tindakan
# {Tentukan_Penyiraman(T,S,K) menghasilkan nama tanaman T dan tindakan
# penyiramannya menurut aturan (a)–(g) yang diperiksa berurutan}
# AksiSiram : tanaman, sensor, tangki → string {fungsi antara}

# REALISASI
# AksiSiram(T,S,K) :
# let l = Lembap(S), b = Butuh(T), t = Suhu(S), v = Volume(K) in
# if not PompaOK(K) or v < 10 then "Darurat" {a}
# else if l < b − 20 then "Siram Penuh" {b}
# else if t > 35 and l < b then "Siram Penuh" {c}
# else if l < b then "Siram Ringan" {d}
# else if v < 50 and Fase(T) ≠ "Semai" then "Tunda" {e}
# else if t > 30 then "Siram Ringan" {f}
# else "Tunda" {g}
# Tentukan_Penyiraman(T,S,K) :
# MakeTindakan(NamaTanaman(T), AksiSiram(T,S,K))

# Realisasi Kode
type Tanaman = tuple[str,str, float]
type Sensor = tuple[float, float, float]
type Tangki = tuple[float, bool]
type Tindakan = tuple[str, str]

def getNama(T: Tanaman) -> str:
    return T[0]
def getFase(T: Tanaman) -> str:
    return T[1]
def getMinLembab(T: Tanaman) -> float:
    return T[2]

def getNowLembab(S: Sensor) -> float:
    return S[0]
def getSuhu(S: Sensor) -> float:
    return S[1]
def getIntensitas(S: Sensor) -> float:
    return S[2]

def getLiter(Tg: Tangki) -> float:
    return Tg[0]
def getBerfungsi(Tg: Tangki) -> bool:
    return Tg[1]

def getNamaT(Stat: Tindakan) -> str:
    return Stat[0]
def getStatus(Stat: Tindakan) -> str:
    return Stat[1]

def MakeT(nama: str, fase: str, min_lembab: float) -> Tanaman:
    if (fase == "Semai") or (fase == "Vegetatif") or (fase == "Generatif"):
        if (1 <= min_lembab) and (min_lembab <= 100):
            return (nama, fase, min_lembab)
        else:
            return KeyError
    else:
        return KeyError

def MakeS(now_lembab: float, suhu: float, intensitas: float) -> Sensor:
    if ((1 <= now_lembab) and (now_lembab <= 100)) and intensitas >= 0:
        return (now_lembab, suhu, intensitas)
    else:
        return KeyError

def MakeTg(liter: float, berfungsi: bool) -> Tangki:
    if (liter >= 0):
        return (liter, berfungsi)
    else:
        return KeyError

def MakeTin(namaT: str, tindakan: str) -> Tindakan:
    if (tindakan == "Siram Penuh") or (tindakan == "Siram Ringan") or (tindakan == "Tunda") or (tindakan == "Darurat"):
        return (namaT, tindakan)

def aturan_tindakan(T,S,Tg):
    if (getBerfungsi(Tg) == False) or (getLiter(Tg) < 10):
        return "Darurat"
    elif (getNowLembab(S) < (getMinLembab(T) - 20)):
        return "Siram Penuh"
    elif (getSuhu(S) > 35) and (getNowLembab(S) < getMinLembab(T)):
        return "Siram Penuh"
    elif (getNowLembab(S) < getMinLembab(T)):
        return "Siram Ringan"
    elif (getLiter(Tg) < 50) and (getFase(T) != "Semai"):
        return "Tunda"
    elif (getSuhu(S) > 30):
        return "Siram Ringan"
    else:
        return "Tunda"

def Tentukan_Penyiraman(T,S,Tg):
    return MakeTin(getNama(T), aturan_tindakan(T,S,Tg))

# Aplikasi
print(Tentukan_Penyiraman(MakeT("Olivera", "Vegetatif", 50), MakeS(50, 25, 50), MakeTg(30, False)))