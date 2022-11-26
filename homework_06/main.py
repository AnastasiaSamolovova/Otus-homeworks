from os import getenv

from flask_migrate import Migrate
from flask import Flask, render_template, request, flash, redirect, url_for

from models import db, Post
from views.forms.Post import CreatePostForm

app = Flask(__name__)

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.app = app
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route('/', endpoint='index_page')
def index():
    return render_template('index.html')


@app.route('/about/', endpoint='about_page')
def about():
    return render_template('about.html')


@app.route('/list-posts/', endpoint='list_posts')
def list_posts():
    posts = Post.query.order_by(Post.id).all()
    return render_template('posts/list.html', posts=posts)


@app.route('/add-post/', methods=["GET", "POST"], endpoint='add_post')
def add_post():
    form = CreatePostForm()

    if request.method == "GET":
        return render_template('posts/add-post.html', form=form)

    if not form.validate_on_submit():
        return render_template('posts/add-post.html', form=form), 400

    post_title = form.title.data
    post_body = form.body.data

    post = Post(title=post_title, body=post_body)
    db.session.add(post)
    db.session.commit()

    flash(f"Successfully added product {post.title}!")
    url = url_for("list_posts")
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
