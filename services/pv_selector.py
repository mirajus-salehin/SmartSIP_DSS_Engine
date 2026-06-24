import pandas as pd
from math import radians, sin, cos, sqrt, atan2


def haversine_distance(lat1, lon1, lat2, lon2) -> float:

    R = 6371  # km

    lat1 = radians(lat1)
    lon1 = radians(lon1)

    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (sin(dlat/2)**2+ cos(lat1)* cos(lat2)* sin(dlon/2)**2)

    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return R * c


def find_nearest_panels(user_lat,user_lon,csv_path="db/SREDA_data_2026_updated.csv",n=10) -> pd.DataFrame:

    df = pd.read_csv(csv_path)

    df["distance_km"] = df.apply(
        lambda row: haversine_distance(user_lat,user_lon,row["Latitude"],row["Longitude"]),axis=1)

    nearest = (df.sort_values("distance_km").head(n).reset_index(drop=True))

    return nearest


def capacity_quartiles(nearest_df) -> dict:

    capacity = pd.to_numeric(
        nearest_df["DC Capacity"],
        errors="coerce"
    ).dropna()

    return {
        "Q1": capacity.quantile(0.25),
        "Median": capacity.quantile(0.50),
        "Q3": capacity.quantile(0.75),
        "Min": capacity.min(),
        "Max": capacity.max(),
        "Mean": capacity.mean()
    }

def capacity_range(nearest_df):

    capacity = pd.to_numeric(
        nearest_df["DC Capacity"],
        errors="coerce"
    ).dropna()

    return {
        "min_capacity": capacity.quantile(0.25),
        "max_capacity": capacity.quantile(0.75)
    }