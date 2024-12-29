# Implementasi Pohon Keputusan dan Metode Quine-McCluskey dalam Deteksi Gejala ADHD pada Anak Usia Dini

Selamat datang di repository ADHD Checker, sebuah aplikasi yang dirancang untuk mendeteksi gejala ADHD (Attention Deficit Hyperactivity Disorder) pada anak usia dini. Aplikasi ini memanfaatkan algoritma Pohon Keputusan dan metode Quine-McCluskey untuk menganalisis data gejala.

Struktur Repository
```
.
├── main.py                          # ADHD Checker
├── docs        
│   └── truth-table-non-adhd.pdf     # Tabel kebenaran diagnosis non-ADHD
├── test            
│   ├── testfile.txt                 # Minterm hasil tabel kebenaran
│   └── quine-mccluskey.py           # Algoritma Quine-McCluskey
└── README.md     
```

# File main.py

File ini berisi aplikasi utama ADHD Checker. Aplikasi ini bertujuan untuk mendeteksi Gejala ADHD berdasarkan masukan pengguna.

# Folder docs

Folder ini berisi dokumentasi terkait proyek, termasuk tabel kebenaran diagnosis non-ADHD dalam format PDF:
1. truth-table-non-adhd.pdf: Tabel kebenaran diagnosis non-ADHD, disusun berdasarkan data gejala yang teramati.

# Folder test

Folder ini berisi file untuk pengujian algoritma Quine-McCluskey:
1. testfile.txt: File ini berisi daftar minterm yang dihasilkan dari tabel kebenaran diagnosis. File ini digunakan sebagai input untuk algoritma Quine-McCluskey.
2. quine-mccluskey.py: File ini berisi algoritma penyederhanaan aljabar Boolean dengan metode Quine-McCluskey. Algoritma ini digunakan untuk menyederhanakan fungsi logika berdasarkan minterm yang dihasilkan dari tabel kebenaran diagnosis.

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
