# ⚡ Quick Start - Deploy ke PythonAnywhere

## 🚀 Langkah Cepat (5 Menit)

### 1. Buat Account
- Buka https://www.pythonanywhere.com
- Sign up (gratis)

### 2. Clone Repository
```bash
# Di Console → Bash
cd ~
git clone https://github.com/attarmakhtar/ASIK25.git
cd ASIK25
```

### 3. Install Dependencies
```bash
pip3.11 install --user -r requirements.txt
```

### 4. Setup Web App
1. Tab **"Web"** → **"Add a new web app"**
2. Pilih **Flask** → **Python 3.11**
3. Path: `/home/yourusername/ASIK25`
4. Edit **WSGI file**, ganti dengan isi `wsgi.py` (jangan lupa ganti `yourusername`)

### 5. Set Environment Variables
Di WSGI file, tambahkan sebelum `from app import app`:
```python
import os
os.environ['SECRET_KEY'] = 'your-secret-key-here'  # Generate dengan: python generate_secret_key.py
os.environ['FLASK_DEBUG'] = 'False'
```

### 6. Set Static Files
Tab **"Web"** → **"Static files"**:
- URL: `/static/`
- Directory: `/home/yourusername/ASIK25/static/`

### 7. Reload
Tab **"Web"** → Klik **"Reload"**

### 8. Test
Buka: `https://yourusername.pythonanywhere.com`

---

**Detail lengkap ada di `PYTHONANYWHERE_DEPLOYMENT.md`**

