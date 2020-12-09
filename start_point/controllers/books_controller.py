from flask import Flask, render_template, Blueprint, request, redirect
from repositories import author_repository
from repositories import book_repository

tasks_blueprint = Blueprint('books', __name__)

# NEW
# GET '/books/new'

# CREATE
# POST '/books'
@tasks_blueprint.route('/books')

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'

