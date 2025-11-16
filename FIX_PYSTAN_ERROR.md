# 🔧 Fix Error pystan Build

## ❌ Error yang Terjadi

```
error: subprocess-exited-with-error
× Preparing metadata (pyproject.toml) did not run successfully.
│ exit code: 1
╰─> [1 lines of output]
    Cython>=0.22 and NumPy are required.
```

## 🔍 Penyebab

`pystan` memerlukan **Cython** dan **NumPy** untuk build, tapi mereka diinstall bersamaan dengan dependencies lain. pip tidak bisa resolve dependency order dengan benar.

## ✅ Solusi yang Diterapkan

### **Update Dockerfile**

Install Cython dan NumPy **terlebih dahulu** sebelum install requirements.txt:

```dockerfile
# Install build dependencies first
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir cython==3.0.10 numpy==1.26.4

# Install remaining dependencies
RUN pip install --no-cache-dir -r requirements.txt
```

Dengan cara ini:
1. ✅ Cython dan NumPy diinstall dulu
2. ✅ pystan bisa build dengan sukses
3. ✅ Dependencies lain bisa diinstall setelahnya

## 🚀 Langkah Selanjutnya

1. **Commit dan push perubahan:**
   ```bash
   git add Dockerfile
   git commit -m "Fix: Install Cython and NumPy before pystan"
   git push origin main
   ```

2. **Railway akan otomatis rebuild** dengan konfigurasi baru

3. **Tunggu build selesai** (~5-10 menit untuk Prophet installation)

## 📝 Catatan

- pystan adalah dependency dari Prophet
- Prophet installation memakan waktu lama karena perlu compile C++ code
- Build akan lebih lama tapi akan berhasil

## ⚠️ Jika Masih Error

Jika masih ada error, coba:
1. Check build logs di Railway Dashboard
2. Pastikan semua system dependencies terinstall (gcc, g++)
3. Pastikan Python version sesuai (3.11)

---

**Commit dan push perubahan, Railway akan otomatis rebuild! 🚀**

