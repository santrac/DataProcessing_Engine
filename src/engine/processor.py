import yaml
from pyspark.sql import SparkSession
from src.transformations.basic_transformations import apply_transformations
from src.config.config_loader import ConfigLoader  
class DataProcessor:
    def __init__(self, config_path):
        # Usar ConfigLoader para cargar y validar la configuración.
        config_loader = ConfigLoader(config_path)
        self.config = config_loader.load_config()

        # Inicializar Spark
        self.spark = SparkSession.builder \
            .appName("Data Transformation Engine") \
            .getOrCreate()

    def load_data(self):
        """Carga el archivo de datos de acuerdo con la configuración."""
        input_config = self.config['input']
        return self.spark.read.format(input_config['format']).options(**input_config['options']).load(input_config['path'])

    def process_data(self, df):
        """Aplica las transformaciones definidas en el YAML."""
        transformations = self.config['transformations']
        return apply_transformations(df, transformations)

    def save_data(self, df):
        """Guarda el DataFrame resultante en la ubicación especificada en la configuración."""
        output_config = self.config['output']
        df.write.format(output_config['format']).save(output_config['path'])

    def run(self):
        """Carga, transforma y guarda los datos."""
        df = self.load_data()
        transformed_df = self.process_data(df)
        self.save_data(transformed_df)
        print("Pipeline completado con éxito.")
