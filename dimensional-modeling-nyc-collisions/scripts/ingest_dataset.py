#!/usr/bin/env python3
"""
ingest_dataset.py

Download NYC collisions dataset and load into Postgres staging table.
"""

import os
import argparse
import pandas as pd
import psycopg2
from io import StringIO
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5430")

BASE_URL = "https://data.cityofnewyork.us/resource/h9gi-nx95.csv"

def main(limit: int):
    url = f"{BASE_URL}?$limit={limit}" if limit > 0 else BASE_URL
    print(f"📥 Downloading dataset from {url} ...")
    df = pd.read_csv(url)
    print(f"✅ Downloaded {df.shape[0]} rows, {df.shape[1]} columns")

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )
    cur = conn.cursor()

    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    print("Loading into Postgres table crashes_raw ...")
    cur.copy_expert(
        "COPY crashes_raw FROM STDIN WITH CSV NULL ''",
        buffer
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Ingestion complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest NYC collisions dataset into Postgres")
    parser.add_argument("--limit", type=int, default=50000,
                        help="Number of rows to load (default=50000, use 0 for full dataset)")
    args = parser.parse_args()

    main(args.limit)
