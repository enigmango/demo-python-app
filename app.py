from collections import defaultdict
from flask import Flask, render_template, request
from flask_toastr import Toastr
import os
import yaml

flask_app = Flask(__name__)
toastr = Toastr(flask_app)

with open("foods.yml", "r") as food_file:
    FOODS_BY_DEPT = yaml.safe_load(food_file)


def group_by_department(input_groceries):

    grouped_groceries = defaultdict(list)

    # Created grocery list (python dictionary, not a list) organized by dept
    for food in input_groceries:
        department = FOODS_BY_DEPT[food]
        grouped_groceries[department].append(food)

    # Create grocery list with foods in alphabetical order per department
    for department, foods in grouped_groceries.items():
        grouped_groceries[department] = sorted(foods)

    return grouped_groceries


@flask_app.route("/")
def index():
    return render_template(
        "index.html",
        all_foods=list(FOODS_BY_DEPT),
        environment_name=os.getenv("ENVIRONMENT_NAME", "UNKNOWN"),
        version=os.getenv("VERSION", "?.?.?")
    )


@flask_app.route("/result", methods=["POST"])
def result():
    grocery_list = request.form["groceries"].splitlines()
    grouped_groceries = group_by_department(grocery_list)
    return render_template("result.html", grocery_list=grouped_groceries)
