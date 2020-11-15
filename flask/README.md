# Flask

This Flask application has 2 key differences from the demo app in the course:

- It uses the Flask application factory pattern
- It uses gunicorn as a proper app server (this is safe to use in production)

The `gunicorn.py` file contains a few config settings. `accesslog = '-'` ensures
that things get logged to STDOUT.

View all of [gunicorn's documentation](http://docs.gunicorn.org/en/latest/index.html).

If you're a seasoned Flask developer and you prefer uWSGI instead of gunicorn,
by all means use that instead. You know what to change!

## Want to learn more about Flask?

I do have a full blown video based Flask course out that will teach you how to
build and maintain a large real world Flask application.

It's a 10 hour course where you get to see a software as a service application
get built up in stages. You'll learn how to deal with users, custom admin
dashboards, recurring billing, and so much more.

If you're interested, you can check that out at:

https://nickjanetakis.com/products/build-a-saas-app-with-flask?utm_source=diveintodocker
