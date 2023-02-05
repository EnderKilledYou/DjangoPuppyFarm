# Django Puppy farm

> What

* Scaffold https://github.com/testdrivenio/django-on-docker
* Testing
* Sqlite and postgress depending on what you wanna do. I prefer django in SPACES or outside of docker

> Additions

- [x] [Vue3](view/README.md) app added
- [x] [Vue3](view/README.md) statically served.
- [x] [Doggo Admin Import](app/pets/README.md)
- [x] [Doggo Admin Keys](app/strings/README.md)
- [x] [Doggo Special Feature](app/movie/README.md)
- [ ] Testing
> Quickstart

* manage.py migrate
* manage.py createsuperuser --email puppy@farm.com --username woof

* Create a run config in jetbrains for easy debugging.
    * ![Jetbrains.png](Jetbrains.png)
* Set your env if you are on windows
    * ![Jetbrains2.png](Jetbrains2.png)
* if you build the docker you can set them as your interpreter and debug that way.
    * (I just don't like to leave docker
      running and prefer jetbrains spaces or similar where I can remote in and use docker on "not my machine")

### [Vue3-Vite](view/)

* On build compiles to the vue app folder in /app
* 100kb starting dist with tree shook tailwind.css

```

../app/vue/index.html 0.42 kB
../app/vue/assets/index-1952331e.css 11.75 kB │ gzip: 3.19 kB
../app/vue/assets/DogSelector-81caf4a5.js 3.73 kB │ gzip: 0.53 kB
../app/vue/assets/index-435d52f8.js 74.73 kB │ gzip: 29.94 kB

```