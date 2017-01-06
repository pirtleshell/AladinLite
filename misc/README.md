# misc tools

> various tools for building needed server files.

## About

Fixing some of the things without access to Strasburg's servers is more easily accomplished by just creating the necessary data file and serving it yourself from your own server.

## Tools

### `nph-aladin.pl` shim

`nph-aladin.py` generates a properly formatted JSON with https links from data available from http servers and saves it in `data/nph-aladin.json`.

#### Currently unavailable surveys:

These are the surveys currently available to AladinLite that have no https mirror. There are [more surveys](), but these are the unavailable ones originally provided by default:

* P/Finkbeiner not found in available mirrors, [current link](http://alasky.u-strasbg.fr/FinkbeinerHalpha)
* P/GLIMPSE360 not found in available mirrors, [current link](http://www.spitzer.caltech.edu/glimpse360/aladin/data)
* P/MAXI_SSC_SUM not found in available mirrors, [current link](http://alasky.u-strasbg.fr//JAXA/JAXA_P_MAXI_SSC_SUM)
* P/SWIFT_BAT_FLUX not found in available mirrors, [current link](http://alasky.u-strasbg.fr//JAXA/JAXA_P_SWIFT_BAT_FLUX)
* P/XMM/PN/color not found in available mirrors, [current link](http://saada.unistra.fr/xmmpnsky)


## License

These tools are written by [Robert Pirtle](https://pirtle.xys). Their license is [MIT](http://choosealicense.com/licenses/mit/).
