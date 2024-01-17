from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

# Configuración de la carpeta de subidas
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se proporcionó un archivo'}), 400

    file = request.files['file']
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)
    return jsonify({'message': 'Archivo subido correctamente'}), 200

@app.route('/list', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({'files': files}), 200

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(filepath)
        return jsonify({'message': f'Archivo {filename} eliminado correctamente'}), 200
    except FileNotFoundError:
        return jsonify({'error': f'Archivo {filename} no encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
