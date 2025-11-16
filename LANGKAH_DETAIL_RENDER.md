# 🚀 Langkah Detail Deployment ke Render - Panduan Lengkap

## 📋 Persiapan Awal

### ✅ Pastikan Sudah Siap:
1. ✅ File sudah di-commit ke GitHub
2. ✅ Repository GitHub sudah dibuat
3. ✅ SECRET_KEY sudah di-generate (lihat di bawah)

---

## 🔑 LANGKAH 1: Generate SECRET_KEY

**Jika belum punya SECRET_KEY, jalankan:**

```bash
python generate_secret_key.py
```

**ATAU** generate manual:
```python
import secrets
print(secrets.token_hex(32))
```

**SIMPAN SECRET_KEY ini!** Contoh:
```
860e635aaf7b3479fb1183d9cb80ca13670377519aa6bdfe0e6789e9b00815c9
```

---

## 🌐 LANGKAH 2: Buat Account Render

### 2.1. Buka Website Render
1. Buka browser, kunjungi: **https://render.com**
2. Klik tombol **"Get Started for Free"** atau **"Sign Up"** (di pojok kanan atas)

### 2.2. Sign Up dengan GitHub (DISARANKAN)
1. Pilih **"Sign up with GitHub"**
2. Klik **"Authorize Render"** untuk memberikan akses
3. Render akan meminta akses ke:
   - ✅ Public repositories (untuk free tier)
   - ✅ Private repositories (jika pakai paid tier)

**Catatan:** 
- Free tier hanya bisa deploy dari **PUBLIC repository**
- Jika repo Anda private, perlu upgrade ke paid tier atau buat repo public

### 2.3. Verifikasi Email (jika diperlukan)
- Cek email untuk verifikasi (jika diminta)

---

## 📤 LANGKAH 3: Pastikan File Sudah di GitHub

### 3.1. Cek Repository GitHub
Pastikan repository Anda sudah berisi:
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `render.yaml`
- ✅ `Procfile`
- ✅ `runtime.txt`
- ✅ Semua file `.pkl` dan `.joblib`
- ✅ Semua file `.csv` yang diperlukan
- ✅ Folder `templates/`
- ✅ Folder `static/`

### 3.2. Jika Belum di GitHub, Push Sekarang:

```bash
# Cek status
git status

# Add semua file
git add .

# Commit
git commit -m "Prepare for Render deployment"

# Push ke GitHub
git push origin main
```

**PENTING:** Pastikan branch utama adalah `main` atau `master`

---

## 🚀 LANGKAH 4: Buat Web Service di Render

### 4.1. Masuk ke Dashboard Render
1. Setelah login, Anda akan masuk ke **Dashboard Render**
2. Dashboard akan kosong jika ini pertama kali

### 4.2. Buat Web Service Baru
1. Klik tombol **"New +"** (di pojok kiri atas, warna biru)
2. Pilih **"Web Service"** dari dropdown menu

### 4.3. Connect GitHub Repository
1. Render akan menampilkan daftar repository GitHub Anda
2. **Cari dan pilih repository** yang berisi aplikasi Flask Anda
3. Klik repository tersebut

**Jika repository tidak muncul:**
- Pastikan repository adalah **PUBLIC** (untuk free tier)
- Atau pastikan Anda sudah authorize akses ke private repo
- Refresh halaman atau reconnect GitHub

---

## ⚙️ LANGKAH 5: Konfigurasi Web Service

### 5.1. Basic Settings

Render akan otomatis detect konfigurasi dari `render.yaml`. **VERIFIKASI** setting berikut:

#### **Name:**
- Default: `asik-website` (atau sesuai nama repo)
- Bisa diubah sesuai keinginan
- Akan menjadi bagian dari URL: `https://[nama-ini].onrender.com`

#### **Region:**
- Pilih region terdekat (misalnya: **Singapore** atau **Oregon**)
- Untuk Indonesia, pilih **Singapore**

#### **Branch:**
- Default: `main` (atau `master`)
- Pastikan branch yang dipilih adalah branch yang berisi kode Anda

#### **Root Directory:**
- Biarkan kosong (jika semua file di root)
- Atau isi jika aplikasi ada di subfolder

### 5.2. Build & Deploy Settings

#### **Environment:**
- Harus: **Python 3**
- Render akan otomatis detect dari `render.yaml`

#### **Build Command:**
- Harus: `pip install --upgrade pip setuptools wheel && pip install -r requirements.txt`
- Render akan otomatis ambil dari `render.yaml`

#### **Start Command:**
- Harus: `gunicorn --bind 0.0.0.0:$PORT app:app`
- Render akan otomatis ambil dari `render.yaml`

**VERIFIKASI** bahwa kedua command di atas sudah benar!

### 5.3. Plan Selection

Pilih plan:
- **Free** - Untuk testing (disarankan untuk pertama kali)
  - ✅ Gratis
  - ⚠️ Build timeout ~15 menit
  - ⚠️ Aplikasi sleep setelah 15 menit tidak aktif
  - ⚠️ Hanya public repository

- **Starter** ($7/bulan) - Untuk production
  - ✅ Tidak ada sleep
  - ✅ Build timeout lebih lama
  - ✅ Support private repository

**Untuk testing, pilih FREE dulu.**

---

## 🔐 LANGKAH 6: Set Environment Variables

### 6.1. Buka Tab Environment
1. Scroll ke bawah, cari section **"Environment Variables"**
2. Atau klik tab **"Environment"** di bagian atas

### 6.2. Tambahkan SECRET_KEY

1. Klik **"Add Environment Variable"** atau **"Add Variable"**
2. Isi:
   - **Key:** `SECRET_KEY`
   - **Value:** (paste SECRET_KEY yang sudah di-generate di Langkah 1)
   
   Contoh:
   ```
   Key: SECRET_KEY
   Value: 860e635aaf7b3479fb1183d9cb80ca13670377519aa6bdfe0e6789e9b00815c9
   ```

3. Klik **"Save"** atau **"Add"**

### 6.3. Tambahkan FLASK_DEBUG

1. Klik **"Add Environment Variable"** lagi
2. Isi:
   - **Key:** `FLASK_DEBUG`
   - **Value:** `False`
   
3. Klik **"Save"**

**Catatan:** 
- `PORT` otomatis di-set oleh Render, **TIDAK PERLU** ditambahkan manual
- Jika `render.yaml` sudah ada `SECRET_KEY` dengan `generateValue: true`, Render akan otomatis generate (tapi lebih baik set manual)

### 6.4. Verifikasi Environment Variables

Pastikan ada 2 variables:
- ✅ `SECRET_KEY` = (value yang panjang)
- ✅ `FLASK_DEBUG` = `False`

---

## 🚀 LANGKAH 7: Deploy!

### 7.1. Review Settings
Sebelum deploy, pastikan:
- ✅ Name sudah benar
- ✅ Repository sudah benar
- ✅ Branch sudah benar
- ✅ Build Command sudah benar
- ✅ Start Command sudah benar
- ✅ Environment Variables sudah di-set
- ✅ Plan sudah dipilih

### 7.2. Klik Create Web Service
1. Scroll ke bawah
2. Klik tombol **"Create Web Service"** (warna biru/hijau)

### 7.3. Monitor Build Process

Render akan mulai proses build. Anda akan melihat log real-time:

#### **Tahap 1: Cloning Repository** ⏳
```
Cloning repository...
✓ Repository cloned successfully
```
**Waktu:** ~10-30 detik

#### **Tahap 2: Installing Dependencies** ⏳⏳⏳
```
Installing dependencies...
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
Installing Flask==3.0.0...
Installing numpy==1.26.4...
...
Installing prophet==1.1.5...  ← INI YANG PALING LAMA!
Installing cmdstanpy==1.1.0...
...
```
**Waktu:** 5-15 menit (Prophet memakan waktu lama!)

**⚠️ PENTING:** 
- Jangan tutup browser selama build
- Build bisa timeout di free tier jika terlalu lama
- Jika timeout, coba lagi atau upgrade ke Starter plan

#### **Tahap 3: Building Application** ⏳
```
Building application...
✓ Build completed successfully
```
**Waktu:** ~1-2 menit

#### **Tahap 4: Starting Application** ⏳
```
Starting application...
gunicorn --bind 0.0.0.0:$PORT app:app
✓ Application started successfully
```
**Waktu:** ~30 detik

### 7.4. Status: Live! ✅

Setelah semua tahap selesai, status akan berubah menjadi **"Live"** (hijau)

Anda akan melihat:
- ✅ Status: **Live**
- ✅ URL aplikasi: `https://[nama-app].onrender.com`
- ✅ Log menunjukkan aplikasi berjalan

---

## ✅ LANGKAH 8: Verifikasi Deployment

### 8.1. Buka URL Aplikasi
1. Klik URL yang ditampilkan di Render Dashboard
2. Atau copy-paste URL ke browser baru

URL format: `https://asik-website.onrender.com`

### 8.2. Test Halaman Utama
- Halaman harus load tanpa error
- Jika ada error, cek log di Render Dashboard

### 8.3. Test Fitur-Fitur
Test fitur penting:
- ✅ **Manajemen Kapal** - `/manajemen_kapal`
- ✅ **Manajemen Harian** - `/manajemen_harian`
- ✅ **Grafik** - `/grafik`
- ✅ **Prediksi** - `/prediksi`
- ✅ **CRUD Data** - `/crud`

### 8.4. Cek Log jika Ada Error
1. Di Render Dashboard, klik tab **"Logs"**
2. Scroll untuk melihat error (jika ada)
3. Error biasanya di bagian bawah log

---

## 🔧 LANGKAH 9: Troubleshooting (Jika Ada Masalah)

### ❌ Error: "Build Timeout"

**Penyebab:** Prophet installation terlalu lama (>15 menit)

**Solusi:**
1. Coba deploy lagi (kadang berhasil di attempt kedua)
2. Upgrade ke Starter plan ($7/bulan)
3. Atau gunakan Railway (timeout lebih lama)

### ❌ Error: "Module not found"

**Penyebab:** Dependency tidak terinstall

**Solusi:**
1. Cek `requirements.txt` sudah lengkap
2. Cek log build untuk melihat module mana yang error
3. Pastikan semua dependencies ada di `requirements.txt`

### ❌ Error: "File not found" (model atau CSV)

**Penyebab:** File tidak di-commit ke Git

**Solusi:**
1. Pastikan semua file `.pkl`, `.joblib`, `.csv` sudah di-commit
2. Cek di GitHub apakah file ada di repository
3. Push ulang jika perlu:
   ```bash
   git add .
   git commit -m "Add missing model files"
   git push origin main
   ```
4. Render akan otomatis redeploy setelah push

### ❌ Error: "Database locked" atau SQLite error

**Penyebab:** SQLite tidak cocok untuk concurrent access

**Solusi:**
1. Untuk testing: OK (tapi data bisa hilang saat restart)
2. Untuk production: Upgrade ke PostgreSQL (gratis di Render):
   - Di Render Dashboard, klik **"New +"** → **"PostgreSQL"**
   - Copy connection string
   - Update `app.py` untuk menggunakan PostgreSQL

### ❌ Error: "Application failed to start"

**Penyebab:** Gunicorn error atau port issue

**Solusi:**
1. Cek log untuk detail error
2. Pastikan `gunicorn` ada di `requirements.txt` ✅ (sudah ada)
3. Pastikan start command benar: `gunicorn --bind 0.0.0.0:$PORT app:app`

### ❌ Aplikasi bisa diakses tapi error 500

**Penyebab:** Error di aplikasi (bukan deployment)

**Solusi:**
1. Cek log di Render Dashboard → Logs
2. Cek apakah semua file model ada
3. Cek apakah database sudah dibuat
4. Cek environment variables sudah benar

---

## 🔄 LANGKAH 10: Auto-Deploy (Setelah Deploy Pertama)

### 10.1. Auto-Deploy dari GitHub
Render akan **otomatis deploy ulang** saat Anda:
- Push ke branch `main` (atau branch yang digunakan)
- Merge pull request ke branch utama

### 10.2. Manual Deploy
Jika perlu deploy manual:
1. Di Render Dashboard, klik service Anda
2. Klik tab **"Manual Deploy"**
3. Pilih branch dan commit
4. Klik **"Deploy"**

### 10.3. Rollback (Jika Perlu)
Jika deploy terbaru error:
1. Di Render Dashboard, klik tab **"Events"** atau **"Deploys"**
2. Cari deploy yang berhasil sebelumnya
3. Klik **"Redeploy"** pada deploy tersebut

---

## 📝 Catatan Penting

### ⚠️ Free Tier Limitations:
1. **Sleep Mode:** Aplikasi akan sleep setelah 15 menit tidak aktif
   - Request pertama setelah sleep akan lambat (~30 detik)
   - Request berikutnya normal

2. **Build Timeout:** ~15 menit
   - Prophet bisa memakan waktu lama
   - Jika timeout, coba lagi atau upgrade

3. **Public Repository Only:** 
   - Free tier hanya support public repo
   - Private repo perlu paid tier

### ✅ Best Practices:
1. **Monitor Logs:** Cek log secara berkala untuk error
2. **Backup Database:** SQLite di Render bisa hilang, backup penting data
3. **Environment Variables:** Jangan hardcode SECRET_KEY di code
4. **Test Sebelum Deploy:** Test lokal dulu sebelum push

---

## 🎉 Selesai!

Website Anda sekarang **LIVE** di: `https://[nama-app].onrender.com`

**Selamat! Deployment berhasil! 🚀**

---

## 📞 Butuh Bantuan Lebih Lanjut?

1. **Render Documentation:** https://render.com/docs
2. **Render Community:** https://community.render.com
3. **Cek Log:** Render Dashboard → Logs tab
4. **Support:** Render Dashboard → Support (untuk paid users)

---

**Tips:** Bookmark URL aplikasi dan Render Dashboard untuk akses cepat!

