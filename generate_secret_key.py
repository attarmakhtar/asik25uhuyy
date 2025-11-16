"""
Script untuk generate SECRET_KEY yang aman untuk Flask
Jalankan script ini untuk mendapatkan SECRET_KEY yang bisa digunakan di Render
"""
import secrets

# Generate random secret key
secret_key = secrets.token_hex(32)

print("=" * 60)
print("SECRET_KEY untuk Render:")
print("=" * 60)
print(secret_key)
print("=" * 60)
print("\nCara menggunakan:")
print("1. Copy SECRET_KEY di atas")
print("2. Di Render Dashboard → Environment Variables")
print("3. Tambahkan variable:")
print("   Key: SECRET_KEY")
print("   Value: (paste SECRET_KEY di sini)")
print("=" * 60)

