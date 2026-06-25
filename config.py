from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent

# Folders
ASSETS_DIR = PROJECT_ROOT / 'assets'
OUTPUT_DIR = PROJECT_ROOT / 'outputs'
TEST_DIR = PROJECT_ROOT / 'tests'

# Create folders if missing
OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

TEST_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# Input File
RAW_DATA_FILE = (
    ASSETS_DIR /
    'roadsense_accident_records_raw_v1.csv'
)

# Output File

CLEANED_DATA_FILE = (
    OUTPUT_DIR /
    'roadsense_cleaned_records_v1.csv'
)

SUMMARY_METRICS_FILE = (
    OUTPUT_DIR / 
    'roadsense_summary_metrics_v1.csv'
)

HOTSPOT_RANKING_FILE = (
    OUTPUT_DIR /
    'roadsense_hotspot_ranking_v1.csv'
)

