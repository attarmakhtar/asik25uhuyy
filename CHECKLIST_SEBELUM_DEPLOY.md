# ✅ Checklist Sebelum Deploy ke Render

Gunakan checklist ini untuk memastikan semua file penting sudah siap sebelum deploy.

## 📦 File Model (WAJIB - Pastikan sudah di Git)

- [ ] `prophet_models.pkl`
- [ ] `model_stok_ikan_baru.pkl`
- [ ] `preprocessor_stok_ikan_baru.pkl`
- [ ] `time_series_models.pkl`
- [ ] `encoder_jenis_ikan.joblib`
- [ ] `encoder_nama_ikan.joblib`

**Cara cek:** Jalankan `git status` dan pastikan file-file ini tidak muncul sebagai "untracked"

## 📊 File Data CSV (WAJIB)

- [ ] `data_bersih_model_ready.csv`
- [ ] `data_produksi_perikanan_bersih.csv`
- [ ] `data/data_gabungan_new.csv` (jika digunakan)
- [ ] `data/data_kecamatan_new.csv` (jika digunakan)
- [ ] `data/jenis_alat_tangkap.csv` (jika digunakan)

## 📁 Folder (WAJIB)

- [ ] `templates/` - Semua file HTML
  - [ ] `about.html`
  - [ ] `beranda.html`
  - [ ] `crud.html`
  - [ ] `grafik.html`
  - [ ] `laporan_bulanan.html`
  - [ ] `laporan_tahunan.html`
  - [ ] `manajemen_harian.html`
  - [ ] `manajemen_kapal.html`
  - [ ] `prediksi.html`
  - [ ] `settings.html`

- [ ] `static/` - CSS, JS, Images
  - [ ] `static/css/` (semua file CSS)
  - [ ] `static/js/` (semua file JS)
  - [ ] `static/img/` (semua gambar)

## ⚙️ File Konfigurasi (WAJIB)

- [ ] `app.py`
- [ ] `requirements.txt` ✅ (sudah diupdate)
- [ ] `render.yaml` ✅ (sudah diperbaiki)
- [ ] `Procfile`
- [ ] `runtime.txt`

## 🗄️ Database (OPSIONAL)

- [ ] `ikan.db` - Bisa di-ignore jika kosong (akan dibuat otomatis di Render)

## 🚫 File yang BISA DI-IGNORE (tidak diperlukan untuk deploy)

- [ ] `package.json` - Tidak diperlukan (ini untuk Node.js)
- [ ] `node_modules/` - Tidak diperlukan
- [ ] `*.xlsx` - File Excel (jika tidak digunakan runtime)
- [ ] `step_1_cleaning_vscode.py` - Script training (opsional)
- [ ] `step_2_training_vscode.py` - Script training (opsional)
- [ ] `train_timeseries.py` - Script training (opsional)

## 🔍 Cara Verifikasi

Jalankan command berikut untuk cek file yang belum di-commit:

```bash
# Cek status Git
git status

# Cek file yang akan di-commit
git ls-files

# Cek file yang di-ignore
git status --ignored
```

## 📝 Command untuk Commit Semua File Penting

```bash
# Add semua file (kecuali yang di .gitignore)
git add .

# Commit
git commit -m "Prepare for Render deployment - all files ready"

# Push ke GitHub
git push origin main
```

## ⚠️ PENTING

1. **File .pkl dan .joblib BESAR** - Pastikan GitHub repository Anda bisa handle file besar
   - Jika file > 100MB, GitHub akan memperingatkan
   - Gunakan Git LFS jika perlu

2. **Repository harus PUBLIC** atau Render harus punya akses
   - Free tier Render hanya bisa deploy dari public repo
   - Atau connect GitHub account dengan akses ke private repo

3. **Test build lokal** (opsional tapi disarankan):
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

## ✅ Setelah Checklist Selesai

Lanjut ke file `RENDER_DEPLOYMENT_STEP_BY_STEP.md` untuk panduan deploy!

