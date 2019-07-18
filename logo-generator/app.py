from flask import Flask, send_file, request
from io import BytesIO
from image_generator import generate

app = Flask(__name__)

def send_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route("/generate")
def serve_image():
    print(request.form)
    image = generate()
    return send_pil_image(image)


if __name__ == '__main__':
    app.run(debug=True)