from setuptools import setup, find_packages

setup(
    name='data_transformation_engine',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyspark>=3.1.2',
        'pyyaml>=6.0',
        'flask'  
    ],
    entry_points={
        'console_scripts': [
            'data_engine=src.interface.main:run_app',  # Comando para ejecutar la app
        ],
    },
)