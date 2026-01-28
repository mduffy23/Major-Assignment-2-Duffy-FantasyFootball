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
    input_dir: Path = RAW_DATA_DIR,
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # Get all csv files
    dfs = []
    for csv_path in input_dir.glob("*.csv"):
        df = pd.read_csv(csv_path)
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    df.drop(columns=['player_id'], inplace=True)
    df.to_csv(output_path, index=False)
if __name__ == "__main__":
    app()