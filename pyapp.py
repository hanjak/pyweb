from flask import Flask
from flask import render_template, redirect, url_for, request


app = Flask (__name__)


@app.route ('/')
def uvodni_strana():
    return render_template ('uvodni_strana.html')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True #automaticke nacitani zmen sablon
    app.run (debug=True)