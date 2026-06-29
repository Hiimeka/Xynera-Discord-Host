# ===== KONFIGURASI SELFBOT =====
# Xynera Protocol - Configuration File

# Token Discord (WAJIB diisi!)
TOKEN = "masukkan_token_anda_disini"

# Channel IDs (WAJIB diisi!)
CHANNEL_ID = 123456789012345678  # ID channel text untuk auto-typing
VOICE_CHANNEL_ID = 123456789012345678  # ID voice channel

# ===== AUTO-TYPING CONFIG =====
PESAN = [
    "Halo semua! 👋",
    "Apa kabar hari ini? 😊",
    "Selamat datang di server! 🎉",
    "Xynera Protocol is online! ⚡",
    "Semoga harimu menyenangkan! 🌟",
    "🚀 Selfbot aktif!",
    "💻 Automation running smoothly",
    "🎵 Voice features ready!"
]

INTERVAL_DETIK = 10  # Interval antar pesan (detik)
TYPING_DURATION = 3  # Durasi efek mengetik (detik)
RANDOM_DELAY = True  # Tambahkan variasi waktu

# ===== STATUS ROTATOR CONFIG =====
statuses = [
    {"type": "playing", "name": "⚡ Xynera Protocol"},
    {"type": "listening", "name": "🎵 Lofi Girl"},
    {"type": "watching", "name": "📺 System Monitor"},
    {"type": "competing", "name": "🏆 Discord Automation"},
    {"type": "streaming", "name": "🎥 Xynera Live", "url": "https://twitch.tv/xynera"}
]

STATUS_INTERVAL = 60  # Interval rotasi status (detik)
STATUS_ROTATOR_AUTO_START = False  # Auto-start saat bot jalan

# ===== VOICE STATE =====
# (Jangan diubah - di-set otomatis)
voice_client = None
is_connected = False
is_muted = False
is_deafened = False

# ===== INTERNAL =====
auto_task = None
status_rotator_running = False
status_index = 0
DEBUG_MODE = False  # Set True untuk debug mode