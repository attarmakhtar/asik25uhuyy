# WSGI configuration file for PythonAnywhere
# This file is used by PythonAnywhere to serve your Flask application
#
# CARA MENGGUNAKAN:
# 1. Copy isi file ini
# 2. Di PythonAnywhere → Web tab → WSGI configuration file
# 3. Paste isi file ini
# 4. GANTI 'yourusername' dengan username PythonAnywhere Anda
# 5. Generate SECRET_KEY dengan: python generate_secret_key.py
# 6. Paste SECRET_KEY di bawah

import sys
import os

# ===========================================
# KONFIGURASI PATH
# ===========================================
# GANTI 'yourusername' dengan username PythonAnywhere Anda!
# Contoh: '/home/john/ASIK25' jika username Anda adalah 'john'
username = 'yourusername'  # ← GANTI INI!
project_name = 'ASIK25'    # Atau sesuai nama folder project Anda

path = f'/home/{username}/{project_name}'
if path not in sys.path:
    sys.path.insert(0, path)

# Change to your project directory
os.chdir(path)

# ===========================================
# ENVIRONMENT VARIABLES
# ===========================================
# Generate SECRET_KEY dengan: python generate_secret_key.py
# Atau jalankan di Python: import secrets; print(secrets.token_hex(32))
os.environ['SECRET_KEY'] = 'GANTI-DENGAN-SECRET-KEY-YANG-AMAN'  # ← GANTI INI!
os.environ['FLASK_DEBUG'] = 'False'

# ===========================================
# IMPORT FLASK APP
# ===========================================
from app import app as application

# ===========================================
# CATATAN
# ===========================================
# Jika ada error, cek:
# 1. Path sudah benar (ganti yourusername)
# 2. SECRET_KEY sudah di-set
# 3. Semua file sudah di-upload/clone
# 4. Dependencies sudah diinstall: pip3.11 install --user -r requirements.txt
