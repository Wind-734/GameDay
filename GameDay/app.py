from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Index.html', title="Game Day")

@app.route('/about')
def about():
    return render_template('About.html', title="เกี่ยวกับเรา")

@app.route('/contact')
def contact():
    return render_template('Contact.html', title="ช่องทางการติดต่อ")

@app.route('/column')
def column():
    return render_template('Column.html', title="บทความเกี่ยวกับเกม")

if __name__ == '__main__':
    app.run(debug=True)
