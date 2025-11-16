# 🚀 Quick Start: Deploy ke Railway

## ✅ File Konfigurasi yang Sudah Disiapkan

- ✅ `railway.json` - Konfigurasi Railway
- ✅ `nixpacks.toml` - Build configuration
- ✅ `Procfile` - Start command
- ✅ `runtime.txt` - Python 3.11.9
- ✅ `requirements.txt` - Dependencies

## 📝 Langkah Cepat (5 Menit)

### 1. Commit ke Git
```bash
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

### 2. Deploy di Railway
1. Buka [railway.app](https://railway.app) → Login
2. **New Project** → **Deploy from GitHub repo**
3. Pilih repository Anda
4. Railway akan otomatis detect dan build

### 3. Set Environment Variables
Di Railway Dashboard → **Variables**, tambahkan:
```
SECRET_KEY=<jalankan: python generate_secret_key.py>
FLASK_DEBUG=False
```

### 4. Tunggu Deploy
- Build: ~5-10 menit (Prophet installation)
- Status: **Active** = Selesai! ✅

### 5. Akses Website
URL: `https://[project-name].up.railway.app`

## ⚠️ Catatan Penting

1. **Database SQLite** akan otomatis terbuat saat pertama kali run
2. **Model files** (`.pkl`, `.joblib`) harus sudah di-commit ke Git
3. **Static files** harus sudah di-commit ke Git

## 🔧 Jika Ada Error

Cek **Logs** di Railway Dashboard untuk detail error.

Lihat `RAILWAY_DEPLOYMENT_GUIDE.md` untuk troubleshooting lengkap.

---

**Selamat! Website Anda siap di-deploy! 🎉**

