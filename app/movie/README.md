# Movie

Movie is an app that can generate a movie from images of pets. The movie is a 4 x 4 grid with special effects.

## Movie Model

There is no movie model. Requests are put into the MovieBoss and performed 1 per core.

## Movie does not have a view set, it has a MovieView

You can push a movie request to Movie View

todo: wire up a end point that reports the stats from QueueBoss implementation in MovieBoss

## Movie has no tests.