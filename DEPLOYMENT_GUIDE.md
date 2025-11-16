# Panduan Deployment ke Render

## ✅ File yang Sudah Disiapkan

1. **app.py** - Sudah diperbaiki dengan:
   - Path relatif (BASE_DIR)
   - Environment variable untuk SECRET_KEY
   - Konfigurasi port dan debug mode untuk production

2. **requirements.txt** - Lengkap dengan semua dependencies

3. **Procfile** - Untuk menjalankan aplikasi dengan gunicorn

4. **runtime.txt** - Menentukan Python version

5. **.gitignore** - Untuk exclude file yang tidak perlu di-commit

## 📋 Langkah-langkah Deployment

### 1. Push ke GitHub/GitLab

Pastikan semua file sudah di-commit dan push ke repository:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

**PENTING:** Pastikan file-file berikut ada di repository:
- ✅ app.py
- ✅ requirements.txt
- ✅ Procfile
- ✅ runtime.txt
- ✅ Semua file model (.pkl, .joblib)
- ✅ File CSV yang diperlukan
- ✅ Folder templates/
- ✅ Folder static/
- ✅ ikan.db (jika sudah ada data)

### 2. Buat Web Service di Render

1. Login ke [render.com](https://render.com)
2. Klik **"New +"** → **"Web Service"**
3. Connect repository GitHub/GitLab Anda
4. Pilih repository yang berisi aplikasi ini

### 3. Konfigurasi di Render

**Settings:**
- **Name:** (nama aplikasi Anda, misalnya: "asik-website")
- **Environment:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** (otomatis terdeteksi dari Procfile: `gunicorn app:app`)
- **Plan:** Pilih Free tier atau sesuai kebutuhan

### 4. Environment Variables

Di bagian **Environment Variables**, tambahkan:

```
SECRET_KEY = (generate random string yang panjang dan aman)
FLASK_DEBUG = False
```

**Cara generate SECRET_KEY:**
```python
import secrets
print(secrets.token_hex(32))
```

Atau gunakan online generator: https://randomkeygen.com/

### 5. Deploy

1. Klik **"Create Web Service"**
2. Render akan otomatis:
   - Install dependencies dari requirements.txt
   - Build aplikasi
   - Deploy aplikasi
3. Tunggu hingga status menjadi **"Live"**

### 6. Database Initialization

Setelah deployment pertama, database SQLite akan otomatis dibuat oleh `db.create_all()` di app.py.

**Catatan:** SQLite di Render memiliki keterbatasan:
- Data bisa hilang saat restart (ephemeral storage)
- Untuk production yang lebih stabil, pertimbangkan PostgreSQL (gratis di Render)

## ⚠️ Troubleshooting

### Build Error: "Module not found"
- Pastikan semua dependencies ada di requirements.txt
- Cek log build di Render dashboard

### Runtime Error: "File not found"
- Pastikan semua file model (.pkl) dan CSV sudah di-commit ke Git
- Cek bahwa BASE_DIR sudah menggunakan path relatif

### Database Error
- Pastikan `db.create_all()` sudah dipanggil di app.py (sudah ada)
- Jika perlu reset database, hapus `ikan.db` dan redeploy

### Port Error
- Render otomatis set PORT via environment variable
- Pastikan kode menggunakan `os.environ.get('PORT', 5000)`

## 🔒 Security Notes

1. **SECRET_KEY:** Pastikan menggunakan random string yang kuat di production
2. **Debug Mode:** Pastikan `FLASK_DEBUG=False` di production
3. **Database:** Pertimbangkan upgrade ke PostgreSQL untuk production

## 📝 Checklist Sebelum Deploy

- [ ] Semua file model (.pkl, .joblib) sudah di-commit
- [ ] File CSV yang diperlukan sudah di-commit
- [ ] Folder templates/ dan static/ sudah di-commit
- [ ] requirements.txt sudah lengkap
- [ ] Procfile sudah dibuat
- [ ] BASE_DIR sudah menggunakan path relatif
- [ ] SECRET_KEY sudah di-set di Render dashboard
- [ ] FLASK_DEBUG=False di environment variables

## 🎉 Setelah Deploy

Aplikasi akan tersedia di URL: `https://[nama-app].onrender.com`

Selamat! Aplikasi Anda sudah live! 🚀

