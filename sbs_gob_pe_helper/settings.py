class Settings:
    def __init__(self):
        self.CACHE_DIR = "./cache_temporal"
        self.TIMEOUT = 30
        self.DB_HOST = "produccion.db.aws.com"

# Instanciamos la configuración para exportarla
config = Settings()