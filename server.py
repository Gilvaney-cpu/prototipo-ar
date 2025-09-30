from flask import Flask, send_from_directory

app = Flask(__name__)

# Rota para servir o index.html e outros arquivos
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # adhoc cria um certificado temporário automaticamente
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')