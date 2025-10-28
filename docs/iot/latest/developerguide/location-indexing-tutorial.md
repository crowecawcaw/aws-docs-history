# Getting started tutorial

This tutorial demonstrates how to use [fleet indexing](iot-indexing.md "iot-indexing.md")
to [index your location data](location-indexing-geoquery.md "location-indexing-geoquery.md"). For
simplicity, you create a thing to represent your device and store the location data in a
named shadow, update thing indexing configuration for location indexing, and run example
geoqueries to search for devices within a radial boundary.

This tutorial takes about 15 minutes to complete.

###### In this topic:

- [Prerequisites](#location-indexing-tutorial-prerequisites "#location-indexing-tutorial-prerequisites")
- [Create thing and shadow](#location-indexing-create-resources "#location-indexing-create-resources")
- [Update thing indexing
  configuration](#location-indexing-update-configuration "#location-indexing-update-configuration")
- [Run geoquery](#location-indexing-run-geoquery "#location-indexing-run-geoquery")

## Prerequisites

- Install the latest version of [AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md").
- Familiarize yourself with [Location indexing
  and geoqueries](location-indexing-geoquery.md "location-indexing-geoquery.md"), [Manage thing indexing](managing-index.md "managing-index.md"),
  and [Query syntax](query-syntax.md "query-syntax.md").

## Create thing and shadow

You create a thing to represent your device, and a named shadow to store its location
data (coordinates 47.61564, -122.33584).

1. Run the following command to create your thing that represents your bike named
   Bike-1. For more information about how to create a thing using AWS CLI, see [create-thing](../../../cli/latest/reference/iot/create-thing.md "../../../cli/latest/reference/iot/create-thing.md") from _AWS CLI_ _Reference_.

```
aws iot create-thing --thing-name "Bike-1" \
--attribute-payload '{"attributes": {"model":"OEM-2302-12", "battery":"35", "acqDate":"06/09/23"}}'
```

The output of this command can look like the following:

```
{
    "thingName": "Bike-1",
    "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/Bike-1",
    "thingId": "df9cf01d-b0c8-48fe-a2e2-e16cff6b23df"
}
```

2. Run the following command to create a named shadow to store Bike-1's location data
   (coordinates 47.61564, -122.33584). For more information about how to create a named
   shadow using AWS CLI, see [update-thing-shadow](../../../cli/latest/reference/iot-data/update-thing-shadow.md "../../../cli/latest/reference/iot-data/update-thing-shadow.md") from _AWS CLI_ _Reference_.

```
aws iot-data update-thing-shadow \
--thing-name Bike-1 \
--shadow-name Bike1-shadow \
--cli-binary-format raw-in-base64-out \
--payload '{"state":{"reported":{"coordinates":{"lat": 47.6153, "lon": -122.3333}}}}' \
"output.txt" \
```

This command doesn't produce any output. To view the named shadow you created, you
can run the [list-named-shadows-for-thing](../../../cli/latest/reference/iot-data/list-named-shadows-for-thing.md "../../../cli/latest/reference/iot-data/list-named-shadows-for-thing.md") CLI command.

```
aws iot-data list-named-shadows-for-thing --thing-name Bike-1
```

The output of this command can look like the following:

```
{
    "results": [
        "Bike1-shadow"
    ],
    "timestamp": 1699574309
}
```

## Update thing indexing

configuration

To index your location data, you must update your thing indexing configuration to
include the location data. Because your location data is stored in a named shadow in this
tutorial, set `thingIndexingMode` to be `REGISTRY` (at a minimum
requirement), set `namedShadowIndexingMode` to be `ON`, and add your
location data to the configuration. In this example, you must add the name of your named
shadow and the shadow's location data path to `filter`.

1. Run the command to update your indexing configuration for location
   indexing.

```
aws iot update-indexing-configuration --cli-input-json '{
"thingIndexingConfiguration": { "thingIndexingMode": "REGISTRY",
"thingConnectivityIndexingMode": "OFF",
"deviceDefenderIndexingMode": "OFF",
"namedShadowIndexingMode": "ON",
"filter": {
    "namedShadowNames": ["Bike1-shadow"],
    "geoLocations":[{
        "name":"shadow.name.Bike1-shadow.reported.coordinates"
    }]
},
"customFields": [
{ "name":"attributes.battery",
"type":"Number"}] } }'
```

The command doesn't produce any output. You may need to wait for a moment until
the update is complete. To check the status, run the [describe-index](../../../cli/latest/reference/iot/describe-index.md "../../../cli/latest/reference/iot/describe-index.md") CLI
command. If you see `indexStatus` shows: `ACTIVE`, your thing
indexing update is complete. 2. Run the command to verify your indexing configuration. This step is
optional.

```
aws iot get-indexing-configuration
```

The output can look like the following:

```
{
    "thingIndexingConfiguration": {
        "thingIndexingMode": "REGISTRY",
        "thingConnectivityIndexingMode": "OFF",
        "deviceDefenderIndexingMode": "OFF",
        "namedShadowIndexingMode": "ON",
        "managedFields": [
            {
                "name": "shadow.name.*.hasDelta",
                "type": "Boolean"
            },
            {
                "name": "registry.version",
                "type": "Number"
            },
            {
                "name": "registry.thingTypeName",
                "type": "String"
            },
            {
                "name": "registry.thingGroupNames",
                "type": "String"
            },
            {
                "name": "shadow.name.*.version",
                "type": "Number"
            },
            {
                "name": "thingName",
                "type": "String"
            },
            {
                "name": "thingId",
                "type": "String"
            }
        ],
        "customFields": [
            {
                "name": "attributes.battery",
                "type": "Number"
            }
        ],
        "filter": {
            "namedShadowNames": [
                "Bike1-shadow"
            ],
            "geoLocations": [
                {
                    "name": "shadow.name.Bike1-shadow.reported.coordinates",
                    "order": "LatLon"
                }
            ]
        }
    },
    "thingGroupIndexingConfiguration": {
        "thingGroupIndexingMode": "OFF"
    }
}
```

## Run geoquery

Now you have updated your thing indexing configuration to include the location data.
Try to create some geoqueries and run them to see if you can get your desired search
results. A geoquery must follow the [Query syntax](query-syntax.md "query-syntax.md"). You
can find some useful example geoqueries in [Example geoqueries](location-indexing-geoquery.md#location-indexing-geoqueries "location-indexing-geoquery.md#location-indexing-geoqueries").

In the following example command, you use the geoquery
`shadow.name.Bike1-shadow.reported.coordinates:geo_distance,47.6204,-122.3491,15.5km`
to search for devices that are within the radial distance of 15.5 km from the center point
with coordinates (47.6204,-122.3491).

```
aws iot search-index --query-string "shadow.name.Bike1-shadow.reported.coordinates:geo_distance,47.6204,-122.3491,15.5km"
```

Because you have a device located at the coordinates "lat": 47.6153, "lon": -122.3333,
which falls within the distance of 15.5 km of the center point, you should be able to see
this device (Bike-1) in the output. The output can look like the following:

```
{
    "things": [
        {
            "thingName": "Bike-1",
            "thingId": "df9cf01d-b0c8-48fe-a2e2-e16cff6b23df",
            "attributes": {
                "acqDate": "06/09/23",
                "battery": "35",
                "model": "OEM-2302-12"
            },
            "shadow": "{\"reported\":{\"coordinates\":{\"lat\":47.6153,\"lon\":-122.3333}},\"metadata\":{\"reported\":{\"coordinates\":{\"lat\":{\"timestamp\":1699572906},\"lon\":{\"timestamp\":1699572906}}}},\"hasDelta\":false,\"version\":1}"
        }
    ]
}
```

For more information, see [Indexing location data](location-indexing-geoquery.md "location-indexing-geoquery.md").
