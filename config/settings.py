import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv('AIML_API_KEY')
    BASE_URL = "https://api.aimlapi.com"
    MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct-Turbo"
    
    # Visualization settings
    PLOT_STYLE = 'darkgrid'
    COLOR_PALETTE = 'viridis'
    
    # Default weights
    DEFAULT_WEIGHTS = {
        'bandwidth': 0.2,
        'latency': 0.4,
        'packet_loss': 0.4
    }
    
    # Performance thresholds
    THRESHOLDS = {
        'bandwidth_critical': 90,
        'latency_critical': 45,
        'packet_loss_critical': 4
    }
