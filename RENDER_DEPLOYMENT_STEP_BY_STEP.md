# 🚀 Panduan Deployment ke Render - Step by Step

## ✅ Persiapan File (SUDAH DILAKUKAN)

File-file berikut sudah disiapkan dan siap digunakan:
- ✅ `requirements.txt` - Dependencies sudah diupdate
- ✅ `render.yaml` - Konfigurasi Render sudah siap
- ✅ `Procfile` - Start command sudah benar
- ✅ `runtime.txt` - Python version sudah ditentukan
- ✅ `.gitignore` - File penting tidak akan di-ignore

## 📋 Checklist Sebelum Deploy

Pastikan file-file berikut **SUDAH DI-COMMIT** ke Git repository:

### File Model (WAJIB):
- [ ] `prophet_models.pkl`
- [ ] `model_stok_ikan_baru.pkl`
- [ ] `preprocessor_stok_ikan_baru.pkl`
- [ ] `time_series_models.pkl`
- [ ] `encoder_jenis_ikan.joblib`
- [ ] `encoder_nama_ikan.joblib`

### File Data (WAJIB):
- [ ] `data_bersih_model_ready.csv`
- [ ] `data_produksi_perikanan_bersih.csv`
- [ ] File di folder `data/` (jika digunakan)

### Folder (WAJIB):
- [ ] `templates/` (semua file HTML)
- [ ] `static/` (CSS, JS, images)

### File Konfigurasi (WAJIB):
- [ ] `app.py`
- [ ] `requirements.txt`
- [ ] `render.yaml`
- [ ] `Procfile`
- [ ] `runtime.txt`

### File Database (OPSIONAL):
- [ ] `ikan.db` - Bisa di-ignore jika kosong (akan dibuat otomatis)

## 🔑 Step 1: Generate SECRET_KEY

Jalankan script untuk generate SECRET_KEY:

```bash
python generate_secret_key.py
```

**ATAU** generate manual di Python:

```python
import secrets
print(secrets.token_hex(32))
```

**SIMPAN SECRET_KEY ini** - akan digunakan di Step 4.

## 📤 Step 2: Push ke GitHub

Pastikan semua file sudah di-commit dan push:

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

**PENTING:** Pastikan repository Anda adalah **PUBLIC** atau Anda sudah connect GitHub account ke Render.

## 🌐 Step 3: Buat Account & Connect GitHub di Render

1. Buka [render.com](https://render.com)
2. Klik **"Get Started for Free"** atau **"Sign Up"**
3. Pilih **"Sign up with GitHub"** (disarankan)
4. Authorize Render untuk mengakses GitHub repositories Anda

## 🚀 Step 4: Deploy Web Service

### 4.1. Buat Web Service Baru

1. Di Render Dashboard, klik **"New +"** → **"Web Service"**
2. Pilih repository GitHub Anda yang berisi aplikasi ini
3. Render akan otomatis detect konfigurasi dari `render.yaml`

### 4.2. Konfigurasi Service

Render akan otomatis mengisi:
- **Name:** `asik-website` (atau sesuai render.yaml)
- **Environment:** Python 3
- **Build Command:** `pip install --upgrade pip setuptools wheel && pip install -r requirements.txt`
- **Start Command:** `gunicorn --bind 0.0.0.0:$PORT app:app`

**VERIFIKASI** bahwa semua setting sudah benar.

### 4.3. Set Environment Variables

Klik **"Environment"** tab, lalu tambahkan:

1. **SECRET_KEY:**
   - Key: `SECRET_KEY`
   - Value: (paste SECRET_KEY yang sudah di-generate di Step 1)

2. **FLASK_DEBUG:**
   - Key: `FLASK_DEBUG`
   - Value: `False`

**Catatan:** `PORT` otomatis di-set oleh Render, tidak perlu manual.

### 4.4. Pilih Plan

- Pilih **"Free"** untuk testing
- Atau **"Starter"** ($7/bulan) untuk production yang lebih stabil

### 4.5. Deploy!

1. Klik **"Create Web Service"**
2. Render akan mulai:
   - Clone repository
   - Install dependencies (ini bisa memakan waktu 5-10 menit karena Prophet)
   - Build aplikasi
   - Deploy aplikasi

## ⏳ Step 5: Monitor Build Process

### Build akan melalui tahap:

1. **Cloning repository** ✅ (cepat)
2. **Installing dependencies** ⏳ (5-10 menit - ini yang paling lama karena Prophet)
3. **Building application** ✅ (cepat)
4. **Starting application** ✅ (cepat)

### Jika Build Timeout:

- Prophet installation bisa memakan waktu lama
- Free tier memiliki build timeout ~15 menit
- **Solusi:** Upgrade ke Starter plan ($7/bulan) atau coba lagi

### Jika Build Error:

Cek log di Render Dashboard untuk melihat error detail.

## ✅ Step 6: Verifikasi Deployment

Setelah status menjadi **"Live"**:

1. Klik URL aplikasi (contoh: `https://asik-website.onrender.com`)
2. Test halaman utama
3. Test fitur-fitur penting:
   - Manajemen Kapal
   - Manajemen Harian
   - Grafik
   - Prediksi

## 🔧 Troubleshooting

### Error: "Module not found"

**Solusi:**
- Pastikan semua dependencies ada di `requirements.txt`
- Cek log build di Render untuk detail error

### Error: "File not found" (model atau CSV)

**Solusi:**
- Pastikan semua file .pkl, .joblib, dan .csv sudah di-commit ke Git
- Cek bahwa file ada di repository GitHub Anda

### Error: "Database locked" atau SQLite error

**Solusi:**
- SQLite di Render bisa bermasalah dengan concurrent access
- Pertimbangkan upgrade ke PostgreSQL (gratis di Render)

### Build Timeout

**Solusi:**
- Prophet installation memakan waktu lama
- Upgrade ke Starter plan atau coba deploy lagi
- Atau gunakan Railway (timeout lebih lama)

### Aplikasi tidak bisa diakses

**Solusi:**
- Cek log di Render Dashboard
- Pastikan `gunicorn` sudah terinstall
- Pastikan `PORT` environment variable sudah di-set oleh Render

## 📝 Catatan Penting

### Database SQLite di Render:

- ⚠️ **Data bisa hilang** saat service restart (ephemeral storage)
- ✅ Untuk testing: OK
- ⚠️ Untuk production: Pertimbangkan PostgreSQL

### Auto-Deploy:

- Render akan otomatis deploy ulang saat Anda push ke GitHub
- Pastikan `main` branch adalah branch yang digunakan

### Custom Domain:

- Render free tier menyediakan subdomain: `[nama-app].onrender.com`
- Untuk custom domain, perlu upgrade ke paid plan

## 🎉 Selesai!

Aplikasi Anda sekarang live di: `https://[nama-app].onrender.com`

**Selamat! Website Anda sudah ter-deploy! 🚀**

---

## 📞 Butuh Bantuan?

Jika ada masalah, cek:
1. Log di Render Dashboard
2. File `DEPLOYMENT_GUIDE.md` untuk detail teknis
3. Render Documentation: https://render.com/docs

