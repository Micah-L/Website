from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from static.confusables import confusables, confusables2

app=Flask(__name__, subdomain_matching=True)
some_dict = {}

class Navbar_Item:
    pass
class Navbar:
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/obfuscate')
@app.route('/obf', methods=['GET'])
def obfs():
    default_alph = {'a': 'а', 'b': 'Ь', 'c': 'с', 'd': 'ԁ', 'e': 'е', 'f': 'ꬵ', 'g': 'ց', 'h': 'հ', 'i': 'і', 'j': 'ј', 'k': '𝚔', 'l': '𐌉', 'm': '𝗆', 'n': 'ո', 'o': 'о', 'p': 'р', 'q': 'ԛ', 'r': 'ꭈ', 's': 'ѕ', 't': '𝔱', 'u': 'ս', 'v': 'ѵ', 'w': 'ԝ', 'x': 'х', 'y': 'у', 'z': 'ꮓ', 'A': 'А', 'B': 'В', 'C': 'С', 'D': '𝖣', 'E': 'Ε', 'F': 'Ϝ',  'G': 'Ԍ', 'H': 'Н', 'I': 'ӏ', 'J': 'Ј', 'K': 'К', 'L': 'ᒪ', 'M': 'М', 'N': 'Ν', 'O': 'O', 'P': 'Р', 'Q': '𝚀', 'R': '𝖱', 'S': 'Ѕ', 'T': 'Τ', 'U': 'Ս', 'V': 'Ѵ', 'W': 'Ԝ', 'X': 'Х', 'Y': 'У', 'Z': 'Ζ', '0': '𝟶', '1': '𝟷', '2': '𝟸', '3': '𝟹', '4': '𝟺', '5': '𝟻', '6': '𝟼', '7': '𝟽', '8': '𝟾', '9': '𝟿'}
    list_of_keys = []
    list_of_keys.extend(default_alph.keys())
    for k in confusables.keys():
        list_of_keys.extend(confusables[k].keys())
    list_of_keys = list(set(list_of_keys))
    list_of_keys.sort()
    return render_template('obfuscate.html',confusables=confusables, default_alph=default_alph, list_of_keys=list_of_keys)


@app.route('/',subdomain='xyz')
def test_page():
    return render_template('display_info.html',info = some_dict)



@app.route('/<string:pnf>')
def otherwise(pnf):
    return render_template('page_not_found.html', page_name=pnf)


if __name__ == "__main__":
    app.run(debug=True)