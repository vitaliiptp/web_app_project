from flask import render_template, request, Blueprint
from webappflask.models import Post, Recipe

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/recipes")
def recipes_list():
    recipes = Recipe.query.order_by(Recipe.id.desc())
    return render_template('recipes.html', title='Recipes', recipes=recipes)


@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)
