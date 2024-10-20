from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def carousel():
    # Datos de ejemplo para el carrusel
    filter = ['example_filter_1', 'example_filter_2']
    images = ['https://via.placeholder.com/150', 'https://via.placeholder.com/150']
    username = ['user1', 'user2']
    
    return render_template("index.html", filter=filter, images=images, username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
