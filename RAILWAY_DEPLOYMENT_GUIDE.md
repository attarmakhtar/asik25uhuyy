# 🚂 Panduan Deployment Website ke Railway

## 📋 Informasi Website

**Teknologi yang Digunakan:**
- **Backend:** Flask (Python 3.11.9)
- **Database:** SQLite (ikan.db)
- **ML Models:** Prophet, scikit-learn, joblib
- **Web Server:** Gunicorn
- **Static Files:** CSS, JavaScript, Images

**Struktur Folder:**
```
WEBSITE - Copy/
├── app.py                 # Main Flask application
├── wsgi.py                # WSGI config (untuk PythonAnywhere)
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version
├── Procfile               # Start command
├── railway.json           # Railway configuration
├── nixpacks.toml          # Nixpacks build config
├── data/                  # Data CSV files
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── img/
├── templates/             # HTML templates
│   ├── beranda.html
│   ├── grafik.html
│   ├── prediksi.html
│   ├── crud.html
│   ├── manajemen_kapal.html
│   ├── manajemen_harian.html
│   ├── laporan_bulanan.html
│   ├── laporan_tahunan.html
│   └── about.html
├── *.pkl                  # Machine learning models
├── *.joblib               # Encoders
└── ikan.db                # SQLite database
```

## 🚀 Langkah-langkah Deployment ke Railway

### **Langkah 1: Persiapan Repository Git**

1. Pastikan semua file sudah di-commit ke Git:
```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### **Langkah 2: Buat Akun dan Project di Railway**

1. Buka [railway.app](https://railway.app)
2. Login dengan GitHub/GitLab/Google
3. Klik **"New Project"**
4. Pilih **"Deploy from GitHub repo"**
5. Pilih repository Anda
6. Railway akan otomatis detect project Python

### **Langkah 3: Konfigurasi Environment Variables**

Di Railway Dashboard → **Variables** tab, tambahkan:

```
SECRET_KEY=<generate-random-string>
FLASK_DEBUG=False
PORT=<Railway otomatis set, jangan ubah>
```

**Cara Generate SECRET_KEY:**
```python
import secrets
print(secrets.token_hex(32))
```

Atau jalankan:
```bash
python generate_secret_key.py
```

### **Langkah 4: Verifikasi Konfigurasi Build**

Railway akan otomatis detect:
- ✅ **Builder:** Nixpacks (dari `railway.json`)
- ✅ **Build Command:** Dari `nixpacks.toml`
- ✅ **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`

**Jika perlu set manual di Railway Dashboard:**
- **Settings → Build:**
  - Builder: **Nixpacks**
  - Build Command: `pip install --upgrade pip setuptools wheel && pip install -r requirements.txt`
  
- **Settings → Deploy:**
  - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`

### **Langkah 5: Deploy**

1. Railway akan otomatis:
   - Clone repository
   - Install dependencies (dari `requirements.txt`)
   - Build aplikasi
   - Deploy aplikasi
2. Tunggu hingga status menjadi **"Active"** (bisa memakan waktu 5-10 menit karena Prophet installation)
3. Railway akan generate domain: `https://[project-name].up.railway.app`

### **Langkah 6: Inisialisasi Database**

Setelah deploy pertama kali, database SQLite akan otomatis dibuat oleh Flask saat aplikasi pertama kali dijalankan (karena ada `db.create_all()` di `app.py`).

**Catatan:** SQLite di Railway adalah **ephemeral** (akan hilang saat restart). Untuk production, pertimbangkan:
- Upgrade ke PostgreSQL (Railway menyediakan)
- Atau gunakan Railway Volume untuk persist data

## ⚠️ Troubleshooting

### **Error: Build Timeout**

**Penyebab:** Prophet installation memakan waktu lama

**Solusi:**
1. Pastikan `nixpacks.toml` sudah benar
2. Upgrade ke Railway Pro (jika build timeout terlalu sering)
3. Atau gunakan Dockerfile untuk build yang lebih cepat

### **Error: ModuleNotFoundError**

**Solusi:**
1. Pastikan `requirements.txt` lengkap
2. Cek build logs di Railway Dashboard
3. Pastikan Python version di `runtime.txt` sesuai: `python-3.11.9`

### **Error: Database tidak terbuat**

**Solusi:**
1. Pastikan aplikasi sudah running
2. Cek logs di Railway Dashboard
3. Database akan otomatis terbuat saat pertama kali aplikasi dijalankan

### **Error: Static files tidak muncul**

**Solusi:**
1. Pastikan folder `static/` sudah di-commit ke Git
2. Cek path di templates menggunakan `url_for('static', ...)`
3. Pastikan Flask static folder config benar

### **Error: Model files tidak ditemukan**

**Solusi:**
1. Pastikan semua file `.pkl`, `.joblib` sudah di-commit ke Git
2. Atau gunakan Railway Volume untuk store model files
3. Cek path di `app.py` menggunakan `BASE_DIR`

## 📝 Checklist Sebelum Deploy

- [ ] Semua file sudah di-commit ke Git
- [ ] `railway.json` sudah ada dan benar
- [ ] `nixpacks.toml` sudah ada dan benar
- [ ] `Procfile` sudah ada
- [ ] `runtime.txt` format benar: `python-3.11.9`
- [ ] `requirements.txt` lengkap
- [ ] `SECRET_KEY` sudah di-generate dan di-set di Railway
- [ ] `FLASK_DEBUG=False` di Railway Variables
- [ ] Semua model files (`.pkl`, `.joblib`) sudah di-commit
- [ ] Database akan otomatis terbuat (tidak perlu manual)

## 🔧 Upgrade ke PostgreSQL (Opsional)

Jika ingin menggunakan PostgreSQL untuk production:

1. Di Railway Dashboard → **New** → **Database** → **PostgreSQL**
2. Railway akan otomatis set `DATABASE_URL` environment variable
3. Update `app.py`:
```python
import os
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    # PostgreSQL
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
else:
    # SQLite (fallback)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'ikan.db')
```

## 🎉 Setelah Deploy Berhasil

1. Buka URL: `https://[project-name].up.railway.app`
2. Test semua fitur:
   - ✅ Homepage
   - ✅ Grafik
   - ✅ Prediksi
   - ✅ CRUD Data
   - ✅ Manajemen Kapal
   - ✅ Manajemen Harian
   - ✅ Laporan Bulanan/Tahunan

## 📞 Support

Jika masih ada masalah:
1. Cek **Logs** di Railway Dashboard
2. Cek **Metrics** untuk melihat resource usage
3. Railway Documentation: https://docs.railway.app

---

**Selamat Deploy! 🚀**

