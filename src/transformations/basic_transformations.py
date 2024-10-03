from pyspark.sql import DataFrame

def filter_data(df: DataFrame, condition: str) -> DataFrame:
    """Filtra las filas del DataFrame basado en la condición."""
    return df.filter(condition)

def select_columns(df: DataFrame, columns: list) -> DataFrame:
    """Selecciona columnas específicas del DataFrame."""
    return df.select(columns)

def apply_transformations(df: DataFrame, transformations: list) -> DataFrame:
    """Aplica una lista de transformaciones a un DataFrame."""
    for transformation in transformations:
        if transformation['type'] == 'filter':
            df = filter_data(df, transformation['condition'])
        elif transformation['type'] == 'select':
            df = select_columns(df, transformation['columns'])
    return df