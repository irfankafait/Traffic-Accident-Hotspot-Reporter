from config import *
import pandas as pd

REQUIRED_COLUMNS = [
    'accident_id',
    'accident_date',
    'hour_of_day',
    'location_name',
    'zone',
    'road_type',
    'severity',
    'weather_condition'
]


def load_data(file_path):
    """
    Load accident CSV file.
    """

    try:
        df = pd.read_csv(file_path)

        print(
            f'Dataset loaded successfully.'
        )

        return df
    except Exception as e:

        raise Exception(
            f'Error loading file: {e}'
        )


def validate_columns(df):
    """
    Validate required columns.
    """

    missing_columns = [
        col
        for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:

        raise ValueError(
            f'Missing columns: {missing_columns}'
        )
    return df


def parse_dates(df):
    """
    Convert accident_date
    to datetime.
    """

    df['accident_date'] = pd.to_datetime(
        df['accident_date'],
        errors='coerce'
    )

    return df

def create_month_column(df):
    """
    Create month coumn.
    """

    df['month'] = (
        df['accident_date'].dt.strftime('%Y-%m')
    )

    return df

def remove_duplicates(df):
    """
    Remove duplicate accident IDs.
    """
    before_rows = len(df)

    df = df.drop_duplicates(
        subset = 'accident_id'
    )

    after_rows = len(df)

    print(
        f'Removed {before_rows - after_rows} duplicate rows.'
    )

    return df


def handle_missing_values(df):
    """
    Handle missing values.
    """

    object_cols = df.select_dtypes(
        include='object'
    ).columns

    df[object_cols] = (
        df[object_cols].fillna('Unknown')
    )

    return df



def handle_missing_values(df):
    ...
    return df


def clean_data(file_path):

    df = load_data(file_path)

    df = validate_columns(df)

    df = parse_dates(df)

    df = create_month_column(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    return df


def export_cleaned_data(df):

    df.to_csv(
    CLEANED_DATA_FILE,
    index = False
    )

    print(
        f'Cleaned file saved to:\n'
        f'{CLEANED_DATA_FILE}'
        )

def run_data_cleaning():
    """
    Run complete data cleaning pipeline.
    """

    cleaned_df = clean_data(
        RAW_DATA_FILE
    )

    export_cleaned_data(
        cleaned_df
    )

    return cleaned_df



if __name__ == "__main__":
    cleaned_df = run_data_cleaning()
    
    print(
        cleaned_df.head()
        )

    cleaned_df.info()