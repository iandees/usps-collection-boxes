# USPS Collection Box locations

This is a self-updating repository of United States Postal Service collection boxes.

## How it works

A script runs periodically to scrape the [USPS Store Locator](https://tools.usps.com/find-location.htm) list of collection boxes. That list of collection boxes is sorted by ID, split into files by the first three characters of the ID, and then committed to this repository. [GitHub Actions](https://docs.github.com/en/actions) triggers that action and the scraping is done with a spider from [All The Places](https://github.com/alltheplaces/alltheplaces).

## Getting the data

The data is contained in this GitHub repository's `data` directory. You can download [the latest data](https://github.com/iandees/usps-collection-boxes/archive/master.zip) or browse the [history of the `data` directory](https://github.com/iandees/usps-collection-boxes/commits/master/data) to see how the data has changed over time.

The collection box ID's seem to be prefixed by the Zip Code of the route they sit on, so if you want to learn more about the collection boxes around you, look for the file that starts with the first 3 digits of your Zip Code.

The data is stored as [newline delimited](http://ndjson.org/) [GeoJSON Features](https://stevage.github.io/ndgeojson/). Recent GDAL and QGIS installs should be able to display this data without problems.
