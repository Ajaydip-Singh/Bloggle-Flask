from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Ajaydip Singh',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Jan 10 2021'
    },
    {
        'author': 'Harmeet Singh',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 11 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html', posts=posts)

@app.route('/about')
def about():
    return render_template('layout.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)

