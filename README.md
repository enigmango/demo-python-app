## Aisles

Barebones grocery list sorter webapp using Python and Flask. Used as an example for a Heroku-to-Amplify demo.

### Operation
Type in foods on your grocery list - use plurals or use [uncountable nouns](http://www.ef.com/english-resources/english-grammar/countable-and-uncountable-nouns/) (e.g. milk)

Clicking the submit button will bring up a list of your foods grouped by department for easier shopping (or an error if the food is unknown). You can go back without losing any information as well.

### Run

```bash
# !! Install requirements first with pip install -r requirements.txt or pipenv install from the root directory !!
gunicorn app:flask_app
```



# heroku git:remote --app=tyler-doit-demo-staging -r heroku-staging
# --- no --- needs main --- git push heroku-staging staging
# git push heroku-staging staging:main