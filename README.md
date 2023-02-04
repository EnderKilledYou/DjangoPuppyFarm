# Django Puppy farm

> Why

* Scaffold https://github.com/testdrivenio/django-on-docker
* Testing
* Sqlite and postgress depending on what you wanna do. I prefer django in SPACES or outside of docker

> Additions

- [x]  Vue3 app added
- [x] Vue3 statically served.
- [ ] Doggo Admin Import
- [ ] Doggo Admin Keys
- [ ] Doggo Admin Special Feature

> Quickstart

* manage.py migrate
* manage.py createsuperuser --email puppy@farm.com --username woof

* Create a run config in jetbrains for easy debugging. You can also use the docker here as the
  interpreter. ![Jetbrains.png](Jetbrains.png)
* Set your env if you are on windows ![Jetbrains2.png](Jetbrains2.png)

> TestDriven.io Readme

## Dockerizing Django with Postgres, Gunicorn, and Nginx

#### For it's good set up.

I felt no need to repeat all of this work when such a well made example existed.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).

## Want to use this project?

### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

   Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and
   your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment
   variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

   Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must
   be re-built.
