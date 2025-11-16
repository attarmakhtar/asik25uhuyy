# 🚀 Panduan Deployment ke PythonAnywhere

## ✅ Keuntungan PythonAnywhere

- ✅ **Gratis** untuk tier awal (dengan batasan)
- ✅ **SQLite persisten** - data tidak hilang saat restart
- ✅ **Mudah digunakan** - interface web yang user-friendly
- ✅ **Tidak perlu build** - langsung upload dan run
- ✅ **Cocok untuk Flask** - support native

## 📋 Persiapan File

### File yang Sudah Siap:
- ✅ `app.py` - Aplikasi Flask utama
- ✅ `requirements.txt` - Dependencies
- ✅ `wsgi.py` - WSGI configuration (BARU - untuk PythonAnywhere)
- ✅ `templates/` - Folder HTML templates
- ✅ `static/` - Folder CSS, JS, images
- ✅ Semua file model (.pkl, .joblib)
- ✅ Semua file CSV yang diperlukan

## 🔑 Step 1: Buat Account PythonAnywhere

1. Buka **https://www.pythonanywhere.com**
2. Klik **"Beginner: Sign up for free account"** atau **"Create a free account"**
3. Isi form:
   - Username (akan menjadi bagian dari URL: `yourusername.pythonanywhere.com`)
   - Email
   - Password
4. Verifikasi email jika diperlukan

## 📤 Step 2: Upload File ke PythonAnywhere

### Opsi A: Upload via Web Interface (Mudah)

1. **Login ke PythonAnywhere**
2. Klik tab **"Files"** di menu atas
3. **Buat folder project:**
   - Klik **"New directory"**
   - Nama: `ASIK25` atau sesuai keinginan
   - Klik **"Create"**

4. **Upload file satu per satu:**
   - Masuk ke folder `ASIK25`
   - Klik **"Upload a file"**
   - Upload file-file berikut:
     - `app.py`
     - `wsgi.py`
     - `requirements.txt`
     - Semua file `.pkl` dan `.joblib`
     - Semua file `.csv` yang diperlukan
     - File `ikan.db` (jika sudah ada data)

5. **Upload folder:**
   - Klik **"New directory"** untuk membuat folder `templates`
   - Upload semua file HTML ke folder `templates/`
   - Klik **"New directory"** untuk membuat folder `static`
   - Upload semua file CSS, JS, images ke folder `static/`

### Opsi B: Clone dari GitHub (Lebih Cepat)

1. **Buka tab "Consoles"** di PythonAnywhere
2. Klik **"Bash"** untuk buka terminal
3. **Clone repository:**
   ```bash
   cd ~
   git clone https://github.com/attarmakhtar/ASIK25.git
   cd ASIK25
   ```
4. **Install dependencies:**
   ```bash
   pip3.11 install --user -r requirements.txt
   ```
   (Ganti `3.11` dengan versi Python yang digunakan)

## ⚙️ Step 3: Install Dependencies

1. **Buka tab "Consoles"** → **"Bash"**
2. **Masuk ke folder project:**
   ```bash
   cd ~/ASIK25
   ```
3. **Install dependencies:**
   ```bash
   pip3.11 install --user -r requirements.txt
   ```
   
   **Catatan:**
   - Ganti `3.11` dengan versi Python yang akan digunakan (cek di tab "Web")
   - `--user` flag penting untuk install di user directory
   - Install bisa memakan waktu 5-10 menit (karena Prophet)

## 🔧 Step 4: Konfigurasi WSGI

1. **Buka tab "Web"** di PythonAnywhere
2. Klik **"Add a new web app"** (jika belum ada)
3. Pilih **"Flask"**
4. Pilih **Python version** (disarankan 3.11)
5. Pilih **Flask project path:**
   - Path: `/home/yourusername/ASIK25`
   - (Ganti `yourusername` dengan username Anda)

6. **Edit WSGI file:**
   - Klik link **"WSGI configuration file"**
   - Hapus semua isi file
   - Copy-paste isi dari `wsgi.py` yang sudah dibuat
   - **PENTING:** Ganti `yourusername` dengan username PythonAnywhere Anda
   - Klik **"Save"**

## 🔐 Step 5: Set Environment Variables

1. **Di WSGI configuration file**, tambahkan sebelum `from app import app`:
   ```python
   import os
   os.environ['SECRET_KEY'] = 'your-secret-key-here'  # Ganti dengan SECRET_KEY yang aman
   os.environ['FLASK_DEBUG'] = 'False'
   ```

2. **ATAU** buat file `.env` (jika menggunakan python-dotenv):
   - Di folder project, buat file `.env`
   - Isi:
     ```
     SECRET_KEY=your-secret-key-here
     FLASK_DEBUG=False
     ```

## 🌐 Step 6: Konfigurasi Web App

1. **Di tab "Web"**, scroll ke **"Static files"**
2. **Tambahkan static files mapping:**
   - URL: `/static/`
   - Directory: `/home/yourusername/ASIK25/static/`
   - Klik **"Add"**

3. **Scroll ke "Code"** section:
   - **Source code:** `/home/yourusername/ASIK25`
   - **Working directory:** `/home/yourusername/ASIK25`
   - **WSGI configuration file:** (sudah otomatis terisi)

## 🗄️ Step 7: Setup Database

1. **Database akan dibuat otomatis** saat pertama kali aplikasi dijalankan
2. **Jika perlu inisialisasi database:**
   - Buka tab **"Consoles"** → **"Bash"**
   - Jalankan:
     ```bash
     cd ~/ASIK25
     python3.11 app.py
     ```
   - Tekan Ctrl+C setelah database dibuat
   - Atau buat script terpisah untuk init database

## 🚀 Step 8: Reload Web App

1. **Di tab "Web"**, scroll ke bawah
2. Klik tombol **"Reload yourusername.pythonanywhere.com"**
3. Tunggu beberapa detik
4. Status akan berubah menjadi **"Enabled"** (hijau)

## ✅ Step 9: Test Aplikasi

1. **Buka URL aplikasi:**
   - Format: `https://yourusername.pythonanywhere.com`
   - Atau klik link di tab "Web"

2. **Test fitur-fitur:**
   - ✅ Halaman utama
   - ✅ Manajemen Kapal
   - ✅ Manajemen Harian
   - ✅ Grafik
   - ✅ Prediksi

## 🔧 Troubleshooting

### Error: "Module not found"

**Solusi:**
1. Pastikan dependencies sudah diinstall:
   ```bash
   pip3.11 install --user -r requirements.txt
   ```
2. Cek versi Python di Web tab harus sama dengan versi pip

### Error: "File not found" (model atau CSV)

**Solusi:**
1. Pastikan semua file sudah di-upload
2. Cek path di `app.py` menggunakan `BASE_DIR` (sudah benar)
3. Pastikan file ada di folder project

### Error: "Database locked"

**Solusi:**
- SQLite di PythonAnywhere lebih stabil
- Pastikan hanya satu instance aplikasi yang berjalan
- Restart web app jika perlu

### Error: "500 Internal Server Error"

**Solusi:**
1. Cek **"Error log"** di tab "Web"
2. Scroll ke bawah untuk melihat error detail
3. Cek apakah semua dependencies terinstall
4. Cek apakah SECRET_KEY sudah di-set

### Error: "Import Error"

**Solusi:**
1. Pastikan path di `wsgi.py` benar
2. Pastikan semua file ada di folder project
3. Cek apakah dependencies terinstall dengan benar

## 📝 Checklist Deployment

- [ ] Account PythonAnywhere sudah dibuat
- [ ] File sudah di-upload atau clone dari GitHub
- [ ] Dependencies sudah diinstall (`pip3.11 install --user -r requirements.txt`)
- [ ] WSGI configuration sudah di-set dengan path yang benar
- [ ] Environment variables (SECRET_KEY) sudah di-set
- [ ] Static files mapping sudah di-set
- [ ] Web app sudah di-reload
- [ ] Aplikasi bisa diakses dan berfungsi

## 🎉 Selesai!

Website Anda sekarang **LIVE** di: `https://yourusername.pythonanywhere.com`

**Selamat! Website Anda sudah ter-deploy di PythonAnywhere! 🚀**

## 📞 Catatan Penting

### Free Tier Limitations:
- ⚠️ **1 web app** per account
- ⚠️ **100 second CPU time** per day
- ⚠️ **512 MB disk space**
- ⚠️ **Domain:** `yourusername.pythonanywhere.com`
- ✅ **SQLite persisten** - data tidak hilang

### Upgrade ke Paid Tier:
- **Hacker ($5/bulan):** 
  - Unlimited CPU time
  - Custom domain
  - More disk space

---

**Tips:** Bookmark URL aplikasi dan PythonAnywhere dashboard untuk akses cepat!

