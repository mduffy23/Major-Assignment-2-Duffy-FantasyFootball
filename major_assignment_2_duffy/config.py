# src/major_assignment_2_duffy/config.py
from pathlib import Path

# __file__ is the location of this config.py
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"