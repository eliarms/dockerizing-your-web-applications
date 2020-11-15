# Rails

Other than it being a general `rails new` project, the following changes were made:

- PostgreSQL is set up
- Rails has been configured to log to STDOUT (check `config/application.rb`)
- `config/database.yml`, `config/secrets.yml` and `config/puma.rb` were cleaned up

You need to run the following to initialize the Rails project before using it:

```
docker-compose run web rails db:reset
docker-compose run web rails db:migrate
```

## Looking for something more complete?

If you want even more opinions set, then check out the
[orats project](https://github.com/nickjj/orats).

This is a Dockerized Rails 5+ application that uses PostgreSQL, Redis, Sidekiq
and Action Cable.
