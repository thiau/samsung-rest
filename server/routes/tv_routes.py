from server import app
from server import samsung_tv


@app.route('/power')
def power():
    samsung_tv.connect()
    samsung_tv.power()
    return 'Pronto'
