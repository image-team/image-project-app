from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from flask_cors import CORS

# Load your model
model = load_model('./resnet50_inception_bs8_e80_lr0.001_nn256_c2_frTrue.h5')

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    # Check if an image is included in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Load the image from the request
    image = request.files['image']
    img = Image.open(image)

    # Resize the image to match the model's input shape
    img = img.resize((300, 300))

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Expand the dimensions to match the model's input shape
    img_array = np.expand_dims(img_array, axis=0)

    # Make the prediction
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)

    # Replace 'Your_Class_Names_List' with your actual list of class names
    class_names = ['Class1', 'Class2']  # Replace with your class names

    class_name = class_names[class_index]

    return jsonify({'class_name': class_name})

if __name__ == '__main__':
    app.run()
