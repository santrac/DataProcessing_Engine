from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from src.engine.processor import DataProcessor
import os
import traceback

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar `flash` para mensajes

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para subir el archivo y ejecutar el pipeline
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No se encontró archivo en la solicitud.')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No se seleccionó ningún archivo.')
        return redirect(request.url)

    # Guardar el archivo en el servidor o procesarlo en memoria
    if file:
        filename = file.filename
        file_path = os.path.join("uploads", filename)
        file.save(file_path)  # Guardar en carpeta 'uploads'

        try:
            # Ejecutar el pipeline y esperar a que termine
            execute_pipeline(file_path)
            flash('Pipeline ejecutado exitosamente.')
        except Exception as e:
            # Si hay un error, mostrar en la interfaz
            flash(f'Error ejecutando el pipeline: {str(e)}')
            return redirect(url_for('index'))

        return redirect(url_for('index'))

# Función que ejecuta el pipeline
def execute_pipeline(file_path):
    try:
        # Ejecutar el pipeline con el archivo subido
        processor = DataProcessor(file_path)
        processor.run()
        return jsonify({"message": "Pipeline ejecutado con éxito"}), 200
    except Exception as e:
        # Imprimir el error en la consola y enviar un mensaje detallado en la respuesta
        print(f"Error al procesar la solicitud: {e}")
        return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

if __name__ == '__main__':
    # Crear carpeta 'uploads' si no existe
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)
