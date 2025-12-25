from pathlib import Path
import pandas as pd

def load_projects():
    file_path = Path("data/projects.csv")
    df = pd.read_csv(file_path)

    df["required_skills"] = df["required_skills"].apply(lambda x: set(x.split(";")))
    df["demonstrates"] = df["demonstrates"].apply(lambda x: set(x.split(";")))

    return df
