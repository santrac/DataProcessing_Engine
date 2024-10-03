import yaml

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path

    def load_config(self):
        """Carga y valida la configuración desde un archivo YAML."""
        with open(self.config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # Validar que las secciones esenciales existan
        required_sections = ['input', 'transformations', 'output']
        for section in required_sections:
            if section not in config:
                raise ValueError(f"Configuración incompleta: Falta la sección '{section}' en el archivo YAML.")
        
        return config