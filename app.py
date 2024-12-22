import os
import wget
from flask import Flask, render_template, request, send_file,jsonify
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Ensure the static directory exists
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save the file to the static directory
        filepath = os.path.join('static', file.filename)
        file.save(filepath)
        return render_template('index.html', image_file=file.filename)

@app.route('/resize', methods=['POST'])
def resize_image():
    width = int(request.form.get('width'))
    height = int(request.form.get('height'))
    image_path = os.path.join('static', request.form.get('image_path'))

    img = Image.open(image_path)
    img_resized = img.resize((width, height))

    output = BytesIO()
    img_resized.save(output, format="JPEG")
    output.seek(0)
    return send_file(output, mimetype="image/jpeg", as_attachment=True, download_name="resized_image.jpg")

@app.route('/grayscale', methods=['POST'])
def grayscale_image():
    # Get the image path (replace this with the actual image path from the form)
   # image_path = 'static/MYPIC.jpg'  # This should be the actual path of the uploaded image
    image_path = os.path.join('static', request.form.get('image_path'))

    # Read the image from the file path
    img = cv2.imread(image_path)

    # Check if the image is loaded properly
    if img is None:
        return f"Error: Image not found at {image_path}. Please check the file path."

    # Convert the image to grayscale
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image (optional)
    output_path = 'static/grayscale_image.jpg'
    cv2.imwrite(output_path, grayscale_img)

    # Convert the grayscale image to BytesIO stream to send it directly
    output = BytesIO()
    is_success, buffer = cv2.imencode(".jpg", grayscale_img)
    if is_success:
        output.write(buffer)
        output.seek(0)
        return send_file(output, mimetype="image/jpeg", as_attachment=True, download_name="grayscale_image.jpg")
    else:
        return "Error processing the image"
    

if __name__ == '__main__':
    app.run(debug=True)
