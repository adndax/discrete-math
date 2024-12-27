# Implementasi Pohon Keputusan dan Metode Quine-McCluskey dalam Deteksi Gejala ADHD pada Anak Usia Dini

Repository ini berisi implementasi algoritma Quine-McCluskey yang dikombinasikan dengan pohon keputusan untuk mendeteksi gejala ADHD pada anak usia dini. Proyek ini bertujuan untuk menyederhanakan fungsi logika berdasarkan tabel kebenaran dari diagnosis non-ADHD.

Struktur Repository
```
.
├── main.py                          # Algoritma Quine-McCluskey
├── docs        
│   └── truth-table-non-adhd.pdf     # Tabel kebenaran diagnosis non-ADHD
├── test            
│   └── testfile.txt                 # Minterm hasil tabel kebenaran
└── README.md     
```

# File main.py

File ini berisi implementasi utama algoritma Quine-McCluskey. Algoritma ini digunakan untuk menyederhanakan fungsi logika berdasarkan minterm yang dihasilkan dari tabel kebenaran diagnosis.

# Folder docs

Folder ini berisi dokumentasi terkait proyek, termasuk tabel kebenaran diagnosis non-ADHD dalam format PDF:
1. truth-table-non-adhd.pdf: Tabel kebenaran diagnosis non-ADHD, disusun berdasarkan data gejala yang teramati.

# Folder test

Folder ini berisi file untuk pengujian algoritma:
1. testfile.txt: File ini berisi daftar minterm yang dihasilkan dari tabel kebenaran diagnosis. File ini digunakan sebagai input untuk algoritma Quine-McCluskey.

# Cara Penggunaan

1. Pastikan Python telah terinstal di sistem Anda (disarankan versi 3.8 atau lebih baru).
For Windows:
```
python --version
```
For MacOS:
```
python3 --version
```

2. Clone repository ini ke komputer Anda.
```
git clone https://github.com/adndax/discrete-math.git
```

3. Buka terminal di direktori repository dan jalankan file main.py.
For Windows:
```
python main.py
```
For MacOS:
```
python3 main.py
```
