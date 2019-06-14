#!/usr/bin/env python

from flask import Flask


app = Flask(__name__)


@app.route("/")
@app.route("/categories")
def showCategories():
    return "This page will show all my categories and home page"


@app.route("/category/<int:category_id>/")
@app.route("/category/<int:category_id>/items")
def showCategoryItems(category_id):
    return "This page will be for showing items in the %s category" % category_id


@app.route("/category/<int:category_id>/items/<int:item_id>/")
def showItem(category_id, item_id):
    return "This page will be for showing details for item with ID %s" % item_id


@app.route("/newitem")
def createItem():
    return "This page will be for adding a new item"


@app.route("/category/<int:category_id>/items/<int:item_id>/edit")
def editItem(category_id, item_id):
    return "This page will be for editing item with ID %s" % item_id


@app.route("/category/<int:category_id>/items/<int:item_id>/delete")
def deleteItem(category_id, item_id):
    return "This page will be for deleting item with ID %s" % item_id


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
