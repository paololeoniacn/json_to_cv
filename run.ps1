# 🚀 Avvio dell'ambiente virtuale e raccolta dati di sistema
Write-Host "🔄 [INFO] Attivazione dell'ambiente virtuale..." -ForegroundColor Cyan

# Controlla se esiste già un ambiente virtuale
if (-Not (Test-Path "venv")) {
    Write-Host "🚀 Creazione di un nuovo ambiente virtuale..."
    python -m venv venv
}

# Attiva l'ambiente virtuale (Solo Windows, quindi niente IF)
Write-Host "🔄 Attivazione dell'ambiente virtuale..."
. .\venv\Scripts\Activate

# Avvia l'app Streamlit
Write-Host "🚀 Avvio dell'app ..."
python main.py

deactivate