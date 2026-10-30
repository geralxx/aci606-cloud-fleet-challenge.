from fastapi import FastAPI
import os
app = FastAPI(title="Fleet Telemetry API")
@app.get("/")
def read_root():
    return {"message": "Servicio de telemetría de robots activo y conectado a la nube"}
@app.get("/health")
def health_check():
    return {"status": "healthy"}
