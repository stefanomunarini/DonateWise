import qrcode

from bottle import request, template, response, Bottle
from io import BytesIO

from static_routes import app as static_files_app

app = Bottle()


@app.route('/register', method='GET', name='generate_button')
def create():
    code = request.GET.get('code')
    return template('register_button.html', static_urls=static_files_app.get_url)


@app.route('/qr', method='GET')
def get_image():
    img = qrcode.make(request.query['url'])

    with BytesIO() as output:
        img.save(output, 'PNG')
        data = output.getvalue()

    response.set_header('Content-type', 'image/png')
    return data
