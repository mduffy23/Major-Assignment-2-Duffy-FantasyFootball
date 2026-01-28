from pathlib import Path
from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd


from major_assignment_2_duffy.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # To process multiple I could add a for loop, but the cleaning would be meaningless unless they all needed to be cleaned in the same way (which is simply unlikely)
    ## For that reason, we will rock with one file
    df = pd.read_csv(input_path)
    df.drop(columns=['player_id'], inplace=True)
    df.to_csv(output_path, index=False)
if __name__ == "__main__":
    app()