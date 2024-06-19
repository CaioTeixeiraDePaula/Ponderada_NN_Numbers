from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = Flask(__name__)
model = load_model('src/model/pesos.h5')

def preprocess_image(image):
    image = image.convert('L')  # Converter para escala de cinza
    image = image.resize((28, 28))  # Redimensionar para 28x28
    image = np.array(image) / 255.0  # Normalizar para [0, 1]
    image = 1 - image  # Inverter cores se necessário (se o fundo for branco e o dígito preto)
    image = np.expand_dims(image, axis=0)  # Adicionar dimensão do batch
    image = np.expand_dims(image, axis=-1)  # Adicionar dimensão do canal
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file provided'}), 400
    
    try:
        image = Image.open(file.stream)
        image = preprocess_image(image)
        prediction = model.predict(image)
        predicted_digit = np.argmax(prediction, axis=1)[0]
        return jsonify({'digit': int(predicted_digit)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
