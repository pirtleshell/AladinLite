# misc tools

> various tools for building needed server files.

## About

Fixing some of the things without access to Strasburg's servers is more easily accomplished by just creating the necessary data file and serving it yourself from your own server.

## Tools

### `nph-aladin.pl` shim

`nph-aladin.py` generates a properly formatted JSON with https links from data available from http servers and saves it in `data/nph-aladin.json`.

An https-served version for production is available [here](https://laniakean.com/data/nph-aladin.json).

## `Sesame.resolve` relay

`resolveNames.php` contains a script that relays requests to CDS's [Sesame object resolution service](http://cds.u-strasbg.fr/cgi-bin/Sesame). This is a hacky solution, but someday in the near future, CDS will implement implement the service under https protocol. It is currently live [here](https://laniakean.com/api/v1/resolveNames/?) as an endpoint in the [Laniakean API](https://laniakean.com/api#resolve-names-api).

## License

These tools are written by [Robert Pirtle](https://pirtle.xys). Their license is [MIT](http://choosealicense.com/licenses/mit/).
