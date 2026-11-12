"""Single source of truth for all chosen settings and relative paths."""
from pathlib import Path
STUDENT_NAME="Rajesh Garg"
STUDENT_ID="2026AJ05869"
HIDDEN_SIZE=64
D_MODEL=128
N_HEADS=4
SEEDS=[7,17,27]
SMOKE_MODE=False
DEVICE_PREFERENCE="cuda"
BATCH_SIZE=128
LEARNING_RATE=1e-3
HAR_EPOCHS=2 if SMOKE_MODE else 30
ADDING_EPOCHS=1 if SMOKE_MODE else 40
ROOT=Path(__file__).resolve().parent
DATA_DIR=ROOT/"data"
RESULTS_CSV=ROOT/"results.csv"
P1_FIGURES=ROOT/"problem1"/"figures"
P2_FIGURES=ROOT/"problem2"/"figures"
def validate_config():
    assert STUDENT_ID=="2026AJ05869"
    assert D_MODEL % N_HEADS == 0
    assert len(SEEDS)==3 and len(set(SEEDS))==3
