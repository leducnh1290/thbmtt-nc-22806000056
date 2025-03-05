from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__) 

caesar_cipher = CaesarCipher();
@app.route('/api/ceasar/encrypt', methods=['POST'])
def ceasar_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    return jsonify({'encrypted_text': caesar_cipher.encrypt_text(text, key)})
#Caesar
@app.route('/api/ceasar/decrypt', methods=['POST'])
def ceasar_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    return jsonify({'decrypted_text': caesar_cipher.decrypt_text(text, key)})
#Vigenere
vigenere_cipher = VigenereCipher()
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    return jsonify({'encrypted_text': vigenere_cipher.encrypt_text(text, key)})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    return jsonify({'decrypted_text': vigenere_cipher.decrypt_text(text, key)})
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)