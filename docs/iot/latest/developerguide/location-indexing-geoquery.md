# Indexing location data

You can use [AWS IoT fleet indexing](iot-indexing.md "iot-indexing.md") to index your devices' last sent location data and search for
devices using geoqueries. This feature resolves device monitoring and management use cases
such as location tracking and proximity search. Location indexing works similarly to other
fleet indexing features, and with additional configurations to specify in your [thing indexing](managing-fleet-index.md "managing-fleet-index.md").

Common use cases include: search and aggregate devices located within desired geographic
boundaries, get location specific insights using query terms related to device metadata and
state from indexed data sources, provide a granular view such as filtering results to a
specific geographic area to reduce rendering lags within your fleet monitoring maps and track
last reported device location, and identify devices that are outside of the desired boundary
limits and generate alarms using [fleet metrics](iot-fleet-metrics.md "iot-fleet-metrics.md"). To
get started with location indexing and geoqueries, see [Getting started tutorial](location-indexing-tutorial.md "location-indexing-tutorial.md").

## Supported data formats

AWS IoT fleet indexing supports the following location data formats:

1. ###### Well-known text representation of coordinate reference systems

A string that follows the [Geographic information -
Well-known text representation of coordinate reference systems](https://docs.ogc.org/is/12-063r5/12-063r5.html "https://docs.ogc.org/is/12-063r5/12-063r5.html") format. An
example can be `"POINT(long lat)"`. 2. ###### A string that represents the coordinates

A string with the format of `"latitude, longitude"` or `"longitude,
 latitude"` . If you use `"longitude, latitude"`, you must also
specify `order` in `geoLocations`. An example can be
`"41.12,-71.34"`. 3. ###### An object of lat(latitude), lon(longitude) keys

This format is applicable to classic shadow and named shadow. Supported keys:
`lat`, `latitude`, `lon`, `long`,
`longitude`. An example can be `{"lat": 41.12, "lon":
 -71.34}`. 4. ###### An array that represents the coordinates

An array with the format `[lat,lon]` or `[lon,lat]`. If you
use the format `[lon,lat]`, which is the same as the coordinates in [GeoJSON](https://geojson.org/ "https://geojson.org/") (applicable to classic shadow and named
shadow), you must also specify `order` in `geoLocations`.

An example can be:

```
{
  "location": {
    "coordinates": [
      **Longitude**,
      **Latitude**
    ],
    "type": "Point",
    "properties": {
      "country": "United States",
      "city": "New York",
      "postalCode": "*****",
      "horizontalAccuracy": 20,
      "horizontalConfidenceLevel": 0.67,
      "state": "New York",
      "timestamp": "2023-01-04T20:59:13.024Z"
    }
  }
}
```

## How to index location data

The following steps show how to update indexing configuration for your location data and
use geoqueries to search for devices.

1. ###### Know where your location data is stored

Fleet indexing currently supports indexing location data stored in classic shadows
or named shadows. 2. ###### Use supported location data formats

Make sure your location data format follows one of the [Supported data formats](#location-indexing-format "#location-indexing-format"). 3. ###### Update indexing configuration

At a minimum need, enable thing (registry) indexing configuration. You must also
enable indexing on classic shadow or named shadow that contain your location data. When
updating your thing indexing, you should include your location data in the indexing
configuration. 4. ###### Create and run geoqueries

Depending on your use cases, create geoqueries and run them to search for devices.
The geoqeury you compose must follow the [Query syntax](query-syntax.md "query-syntax.md"). You can find
some examples in [Example geoqueries](#location-indexing-geoqueries "#location-indexing-geoqueries").

## Update thing indexing

configuration

To index location data, you must update indexing configuration and include your location
data. Depending on where your location data is stored, follow the steps to update your
indexing configuration:

If your location data is stored in a classic shadow, you must set
`thingIndexingMode` to be `REGISTRY_AND_SHADOW` and specify your
location data in the `geoLocations` fields (`name` and
`order`) in [`filter`](../apireference/API_IndexingFilter.md "../apireference/API_IndexingFilter.md").

In the following thing indexing configuration example, you specify the location data
path `shadow.reported.coordinates` as `name` and
`LonLat` as `order`.

```
{
	"thingIndexingMode": "REGISTRY_AND_SHADOW",
	"filter": {
		"geoLocations": [
			{
				"name": "shadow.reported.coordinates",
				"order": "LonLat"
			}
		]
	}
}
```

- `thingIndexingMode`

The indexing mode controls if registry or shadow is indexed. When
`thingIndexingMode` is set to be `OFF`, thing indexing is
disabled.

To index location data stored in a classic shadow, you must set
`thingIndexingMode` to be `REGISTRY_AND_SHADOW`. For more
information, see [Thing indexing modes](managing-index.md#index-mode "managing-index.md#index-mode").

- `filter`

Indexing filter provides additional selections for named shadows and geolocation
data. For more information, see [Indexing filter](managing-index.md#thing-indexing-filter "managing-index.md#thing-indexing-filter").

- `geoLocations`

The list of geolocation targets that you select to index. The default maximum
number of geolocation targets for indexing is `1`. To increase the limit,
see [AWS IoT Device Management Quotas](../../../general/latest/gr/iot_device_management.md#fleet-indexing-limits "../../../general/latest/gr/iot_device_management.md#fleet-indexing-limits").

- `name`

The name of the geolocation target field. An example value of `name`
can be the location data path of your shadow:
`shadow.reported.coordinates`.

- `order`

The order of the geolocation target field. Valid values: `LatLon` and
`LonLat`. `LatLon` means latitude and longitude.
`LonLat` means longitude and latitude. This field is optional. The
default value is `LatLon`.

If your location data is stored in a named shadow, set
`namedShadowIndexingMode` to be `ON`, add your named shadow
name(s) to the `namedShadowNames` field in [`filter`](../apireference/API_IndexingFilter.md "../apireference/API_IndexingFilter.md"),
and specify your location data path in the `geoLocations` field in [`filter`](../apireference/API_IndexingFilter.md "../apireference/API_IndexingFilter.md").

In the following thing indexing configuration example, you specify the location data
path `shadow.name.namedShadow1.reported.coordinates` as `name` and
`LonLat` as `order`.

```
{
	"thingIndexingMode": "REGISTRY",
	"namedShadowIndexingMode": "ON",
	"filter": {
		"namedShadowNames": [
			"namedShadow1"
		],
		"geoLocations": [
			{
				"name": "shadow.name.namedShadow1.reported.coordinates",
				"order": "LonLat"
			}
		]
	}
}
```

- `thingIndexingMode`

The indexing mode controls if registry or shadow is indexed. When
`thingIndexingMode` is set to be `OFF`, thing indexing is
disabled.

To index location data stored in a named shadow, you must set
`thingIndexingMode` to be `REGISTRY` (or
`REGISTRY_AND_SHADOW`). For more information, see [Thing indexing modes](managing-index.md#index-mode "managing-index.md#index-mode").

- `filter`

Indexing filter provides additional selections for named shadows and geolocation
data. For more information, see [Indexing filter](managing-index.md#thing-indexing-filter "managing-index.md#thing-indexing-filter").

- `geoLocations`

The list of geolocation targets that you select to index. The default maximum
number of geolocation targets for indexing is `1`. To increase the limit,
see [AWS IoT Device Management Quotas](../../../general/latest/gr/iot_device_management.md#fleet-indexing-limits "../../../general/latest/gr/iot_device_management.md#fleet-indexing-limits").

- `name`

The name of the geolocation target field. An example value of `name`
can be the location data path of your shadow:
`shadow.name.namedShadow1.reported.coordinates`.

- `order`

The order of the geolocation target field. Valid values: `LatLon` and
`LonLat`. `LatLon` means latitude and longitude.
`LonLat` means longitude and latitude. This field is optional. The
default value is `LatLon`.

## Example geoqueries

After you complete the indexing configuration for your location data, run geoqueries to
search for devices. You can also combine your geoqueries with other query strings. For more
information, see [Query syntax](query-syntax.md "query-syntax.md") and [Example thing queries](example-queries.md "example-queries.md").

**Example query 1**

This example assumes the location data is stored in a named shadow
`gps-tracker`. The output of this command is the list of devices that are
within the radial distance of 15.5 km from the center point with coordinates
(47.6204,-122.3491).

```
aws iot search-index --query-string \
"shadow.name.gps-tracker.reported.coordinates:geo_distance,47.6204,-122.3491,15.5km"
```

**Example query 2**

This example assumes the location data is stored in a classic shadow. The output of this
command is the list of devices that are within the radial distance of 15.5 km from the
center point with coordinates (47.6204,-122.3491).

```
aws iot search-index --query-string \
"shadow.reported.coordinates:geo_distance,47.6204,-122.3491,15.5km"
```

**Example query 3**

This example assumes the location data is stored in a classic shadow. The output of this
command is the list of devices that are not connected and outside the radial distance of
15.5 km from the center point with coordinates (47.6204,-122.3491).

```
aws iot search-index --query-string \
"connectivity.connected:false AND (NOT shadow.reported.coordinates:geo_distance,47.6204,-122.3491,15.5km)"
```
