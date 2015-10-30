#/usr/bin/env python
##
#http://fsociety.ninja

transport_security = True

from flask import Flask, render_template, make_response, request
import os

app = Flask(__name__, template_folder=os.getcwd())

if transport_security is True:
    from flask_sslify import SSLify
    sslify = SSLify(app)
    import ssl

##ERROR & Robots
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/robots.txt")
def robots_txt():
    return render_template("robots.txt")


##Page Handlers
@app.route('/')
def index_handler():
    ''' Index Handler '''
    domain = 'fsociety.ninja'
    resp = make_response(render_template(domain+'.html')) 
    resp.headers['Server'] = 'fsociety00.dat'
    return resp

@app.route("/data")
def data_handler():
    ''' BLog Handler '''
    resp = make_response(render_template('data.html')) 
    resp.headers['Server'] = 'fsociety00.dat'
    return resp


if __name__ == '__main__':

    if transport_security is True:
        #SSL Configuration
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(certfile="certs/current/validchain.pem", keyfile="certs/current/privkey.pem")

        ##Run SSL
        app.run(host = '0.0.0.0', port = 3000, ssl_context=context)
    else:
        ##Run App
        app.run(host = '0.0.0.0', port = 3000)
        
