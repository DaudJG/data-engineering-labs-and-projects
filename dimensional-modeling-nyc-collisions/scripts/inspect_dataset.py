import argparse
import pandas as pd

DEFAULT_URL = "https://data.cityofnewyork.us/resource/h9gi-nx95.csv?$limit=1000"

def inspect_dataset(url: str):
    print(f"\n🔎 Inspecting dataset from: {url}\n")
    df = pd.read_csv(url)

    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")
    print("Columns:")
    for col in df.columns:
        print(f" - {col}")

    print("\nSample rows:")
    print(df.head())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect a CSV dataset from URL")
    parser.add_argument("--url", type=str, default=DEFAULT_URL, help="CSV file URL")
    args = parser.parse_args()

    inspect_dataset(args.url)
