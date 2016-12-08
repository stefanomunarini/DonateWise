import os

from bottle import run, TEMPLATE_PATH

from demo import app as demo_app
from button_generator import app as generate_button_app
from static_routes import app as static_files_app

demo_app.merge(static_files_app)
demo_app.merge(generate_button_app)

TEMPLATE_PATH.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './static/html/')))
print(TEMPLATE_PATH)

if os.environ.get('APP_LOCATION') == 'heroku':
    run(demo_app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
else:
    run(demo_app, host='127.0.0.1', port=8000, reloader=True)
