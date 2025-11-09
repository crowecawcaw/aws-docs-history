# Manage thing indexing

The index created for all of your things is `AWS_Things`. You can control
what to index from the following data sources: [AWS IoT
registry](thing-registry.md "thing-registry.md") data, [AWS IoT Device Shadow](iot-device-shadows.md "iot-device-shadows.md") data,
[AWS IoT connectivity](life-cycle-events.md "life-cycle-events.md") data, and [AWS IoT Device Defender](../../../iot-device-defender/latest/devguide/what-is-device-defender.md "../../../iot-device-defender/latest/devguide/what-is-device-defender.md")
violations data.

###### In this topic:

- [Enabling thing indexing](#enable-index "#enable-index")
- [Describing a thing index](#describe-index "#describe-index")
- [Querying a thing index](#search-index "#search-index")
- [Restrictions and limitations](#index-limitations "#index-limitations")
- [Authorization](#query-auth "#query-auth")

## Enabling thing indexing

You use the [update-indexing-configuration](../../../cli/latest/reference/iot/update-indexing-configuration.md "../../../cli/latest/reference/iot/update-indexing-configuration.md") CLI command or the [UpdateIndexingConfiguration](../apireference/API_UpdateIndexingConfiguration.md "../apireference/API_UpdateIndexingConfiguration.md") API operation to create the `AWS_Things`
index and control its configuration. By using the
`--thing-indexing-configuration` (`thingIndexingConfiguration`)
parameter, you control what kind of data (for example, registry, shadow, device
connectivity data, and Device Defender violations data) is indexed.

The `--thing-indexing-configuration` parameter takes a string with the
following structure:

```
{
  "thingIndexingMode": "OFF"|"REGISTRY"|"REGISTRY_AND_SHADOW",
  "thingConnectivityIndexingMode": "OFF"|"STATUS",
  "deviceDefenderIndexingMode": "OFF"|"VIOLATIONS",
  "namedShadowIndexingMode": "OFF"|"ON",
  "managedFields": [
    {
      "name": "string",
      "type": "Number"|"String"|"Boolean"
    },
    ...
  ],
  "customFields": [
    {
      "name": "string",
      "type": "Number"|"String"|"Boolean"
    },
    ...
  ],
  "filter": {
     "namedShadowNames": [ "string" ],
     "geoLocations": [
        {
            "name": "String",
            "order": "LonLat|LatLon"
        }
    ]
  }
}
```

### Thing indexing modes

You can specify different thing indexing modes in your indexing configuration,
depending on what data sources you want to index and search devices from:

- `thingIndexingMode`: Controls if registry or shadow is indexed. When
  `thingIndexingMode` is set to be `OFF`, thing indexing is
  disabled.

- `thingConnectivityIndexingMode`: Specifies if thing connectivity data
  is indexed.

- `deviceDefenderIndexingMode`: Specifies if Device Defender violations
  data is indexed.
- `namedShadowIndexingMode`: Specifies if named shadow data is indexed.
  To select named shadows to add to your fleet indexing configuration, set
  `namedShadowIndexingMode` to be `ON` and specify your named
  shadow names in [`filter`](../apireference/API_IndexingFilter.md "../apireference/API_IndexingFilter.md").

The table below shows the valid values for each indexing mode and the data source
that's indexed for each value.

| Attribute                       | Valid values     | Registry | Shadow | Connectivity | DD violations | Named shadow |
| ------------------------------- | ---------------- | -------- | ------ | ------------ | ------------- | ------------ |
| `thingIndexingMode`             | OFF              |          |        |              |               |              |
| REGISTRY                        | ✓                |          |        |              |               |
| REGISTRY_AND_SHADOW             | ✓                | ✓        |        |              |               |
| `thingConnectivityIndexingMode` | _Not specified._ |          |        |              |               |              |
| OFF                             |                  |          |        |              |               |
| STATUS                          |                  |          | ✓      |              |               |
| `deviceDefenderIndexingMode`    | _Not specified._ |          |        |              |               |              |
| OFF                             |                  |          |        |              |               |
| VIOLATIONS                      |                  |          |        | ✓            |               |
| `namedShadowIndexingMode`       | _Not specified._ |          |        |              |               |              |
| OFF                             |                  |          |        |              |               |
| ON                              |                  |          |        |              | ✓             |

### Managed fields and custom fields

**Managed fields**

Managed fields contain data associated with things, thing groups, device shadows,
device connectivity, and Device Defender violations. AWS IoT defines the data type in
managed fields. You specify the values of each managed field when you create an AWS IoT
thing. For example, thing names, thing groups, and thing descriptions are all managed
fields. Fleet indexing indexes managed fields based on the indexing mode that you
specify. Managed fields can't be changed or appear in `customFields`.

**Custom fields**

You can aggregate attributes, Device Shadow data, and Device Defender violations
data by creating custom fields to index them. The `customFields` attribute is
a list of field name and data type pairs. You can perform aggregation queries based on
data type. The indexing mode that you choose affects fields can be specified in
`customFields`. For example, if you specify the `REGISTRY`
indexing mode, you can't specify a custom field from a thing shadow. You can use the
[update-indexing-configuration](../../../cli/latest/reference/iot/update-indexing-configuration.md "../../../cli/latest/reference/iot/update-indexing-configuration.md") CLI command to create or update the custom
fields (see an example command in [Updating
indexing configuration examples](#update-index-examples "#update-index-examples")). For more information, see [Custom fields](managing-fleet-index.md#custom-field "managing-fleet-index.md#custom-field").

### Indexing filter

Indexing filter provides additional selections for named shadows and geolocation
data.

**`namedShadowNames`**

To add named shadows to your fleet indexing configuration, set
`namedShadowIndexingMode` to be `ON` and specify your named
shadow names in `namedShadowNames` filter.

**Example**

```
"filter": {
     "namedShadowNames": [ "namedShadow1", "namedShadow2" ]
}
```

`**geoLocations**`

To add geolocation data to your fleet indexing configuration:

- If your geolocation data is stored in a classic (unnamed) shadow, set
  `thingIndexingMode` to be REGISTRY_AND_SHADOW, and specify your
  geolocation data in `geoLocations` filter.

The example filter below specifies a geoLocation object in a classic (unnamed)
shadow:

```
"filter": {
     "geoLocations": [
        {
            "name": "shadow.reported.location",
            "order": "LonLat"
        }
     ]
  }
```

- If your geolocation data is stored in a named shadow, set
  `namedShadowIndexingMode` to be ON, add the shadow name in
  `namedShadowNames` filter, and specify your geolocation data in
  `geoLocations` filter.

The example filter below specifies a geoLocation object in a named shadow
(`nameShadow1`):

```
"filter": {
     "namedShadowNames": [ "namedShadow1" ],
     "geoLocations": [
        {
            "name": "shadow.name.namedShadow1.reported.location",
            "order": "LonLat"
        }
     ]
  }
```

For more information, see [IndexingFilter](../apireference/API_IndexingFilter.md "../apireference/API_IndexingFilter.md") from
_AWS IoT_
_API Reference_.

### Updating indexing configuration examples

To update your indexing configuration, use the AWS IoT
**update-indexing-configuration** CLI command . The following examples
show how to use **update-indexing-configuration**.

Short syntax:

```
aws iot update-indexing-configuration --thing-indexing-configuration \
'thingIndexingMode=REGISTRY_AND_SHADOW, deviceDefenderIndexingMode=VIOLATIONS,
namedShadowIndexingMode=ON,filter={namedShadowNames=[thing1shadow]}, thingConnectivityIndexingMode=STATUS,
customFields=[{name=attributes.version,type=Number},
{name=shadow.name.thing1shadow.desired.DefaultDesired, type=String}, {name=shadow.desired.power, type=Boolean},
{name=deviceDefender.securityProfile1.NUMBER_VALUE_BEHAVIOR.lastViolationValue.number, type=Number}]'
```

JSON syntax:

```
aws iot update-indexing-configuration --cli-input-json \ '{
          "thingIndexingConfiguration": { "thingIndexingMode": "REGISTRY_AND_SHADOW",
          "thingConnectivityIndexingMode": "STATUS",
          "deviceDefenderIndexingMode": "VIOLATIONS",
          "namedShadowIndexingMode": "ON",
          "filter": { "namedShadowNames": ["thing1shadow"]},
          "customFields": [ { "name": "shadow.desired.power", "type": "Boolean" },
          {"name": "attributes.version", "type": "Number"},
          {"name": "shadow.name.thing1shadow.desired.DefaultDesired", "type": "String"},
          {"name": "deviceDefender.securityProfile1.NUMBER_VALUE_BEHAVIOR.lastViolationValue.number", "type": Number} ] } }'
```

This command doesn't produce any output.

To check the thing index status, run the `describe-index` CLI command:

```
aws iot describe-index --index-name "AWS_Things"
```

The output of the `describe-index` command looks like the
following:

```
{
    "indexName": "AWS_Things",
    "indexStatus": "ACTIVE",
    "schema": "MULTI_INDEXING_MODE"
}
```

###### Note

It can take a moment for fleet indexing to update the fleet index. We recommend
waiting until the `indexStatus` shows ACTIVE before using it. You can have
different values in the schema field depending on what data sources you've configured.
For more information, see [Describing a thing
index](#describe-index "#describe-index").

To get your thing indexing configuration details, run the
`get-indexing-configuration` CLI command:

```
aws iot get-indexing-configuration
```

The output of the `get-indexing-configuration` command looks like the
following:

```
{
    "thingIndexingConfiguration": {
        "thingIndexingMode": "REGISTRY_AND_SHADOW",
        "thingConnectivityIndexingMode": "STATUS",
        "deviceDefenderIndexingMode": "VIOLATIONS",
        "namedShadowIndexingMode": "ON",
        "managedFields": [
            {
                "name": "connectivity.disconnectReason",
                "type": "String"
            },
            {
                "name": "registry.version",
                "type": "Number"
            },
            {
                "name": "thingName",
                "type": "String"
            },
            {
                "name": "deviceDefender.violationCount",
                "type": "Number"
            },
            {
                "name": "shadow.hasDelta",
                "type": "Boolean"
            },
            {
                "name": "shadow.name.*.version",
                "type": "Number"
            },
            {
                "name": "shadow.version",
                "type": "Number"
            },
            {
                "name": "connectivity.version",
                "type": "Number"
            },
            {
                "name": "connectivity.timestamp",
                "type": "Number"
            },
            {
                "name": "shadow.name.*.hasDelta",
                "type": "Boolean"
            },
            {
                "name": "registry.thingTypeName",
                "type": "String"
            },
            {
                "name": "thingId",
                "type": "String"
            },
            {
                "name": "connectivity.connected",
                "type": "Boolean"
            },
            {
                "name": "registry.thingGroupNames",
                "type": "String"
            }
        ],
        "customFields": [
            {
                "name": "shadow.name.thing1shadow.desired.DefaultDesired",
                "type": "String"
            },

            {
                "name": "deviceDefender.securityProfile1.NUMBER_VALUE_BEHAVIOR.lastViolationValue.number",
                "type": "Number"
            },
            {
                "name": "shadow.desired.power",
                "type": "Boolean"
            },
            {
                "name": "attributes.version",
                "type": "Number"
            }
        ],
        "filter": {
              "namedShadowNames": [
                  "thing1shadow"
              ]
          }
      },
    "thingGroupIndexingConfiguration": {
        "thingGroupIndexingMode": "OFF"
    }
}
```

To update the custom fields, you can run the
`update-indexing-configuration` command. An example is as follows:

```
aws iot update-indexing-configuration --thing-indexing-configuration
          'thingIndexingMode=REGISTRY_AND_SHADOW,customFields=[{name=attributes.version,type=Number},{name=attributes.color,type=String},{name=shadow.desired.power,type=Boolean},{name=shadow.desired.intensity,type=Number}]'
```

This command added `shadow.desired.intensity` to the indexing
configuration.

###### Note

Updating the custom field indexing configuration overwrites all existing custom
fields. Make sure to specify all custom fields when calling
**update-indexing-configuration**.

After the index is rebuilt, you can use an aggregation query on the newly added
fields, search registry data, shadow data, and thing connectivity status data.

When changing the indexing mode, make sure all of your custom fields are valid by
using the new indexing mode. For example, if you start off using
`REGISTRY_AND_SHADOW` mode with a custom field called
`shadow.desired.temperature`, you must delete the
`shadow.desired.temperature` custom field before changing the indexing mode
to `REGISTRY`. If your indexing configuration contains custom fields that
aren't indexed by the indexing mode, the update fails.

## Describing a thing index

The following command shows you how to use the **describe-index** CLI
command to retrieve the current status of the thing index.

```
aws iot describe-index --index-name "AWS_Things"
```

The response of the command can look like the following:

```
{
    "indexName": "AWS_Things",
    "indexStatus": "BUILDING",
    "schema": "REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS"
}
```

The first time that you fleet indexing, AWS IoT builds your index. When
`indexStatus` is in the `BUILDING` state, you can't query the
index. The `schema` for the things index indicates which type of data
(`REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS`) is indexed.

Changing the configuration of your index causes the index to be rebuilt. During this
process, the `indexStatus` is `REBUILDING`. You can run queries on
data in the things index while it's being rebuilt. For example, if you change the index
configuration from `REGISTRY` to `REGISTRY_AND_SHADOW` while the
index is being rebuilt, you can query registry data, including the latest updates.
However, you can't query the shadow data until the rebuild is complete. The amount of time
it takes to build or rebuild the index depends on the amount of data.

You can see different values in the schema field depending on the data sources that
you've configured. The following table shows the different schema values and the
corresponding descriptions:

| Schema                                      | Description                                                                                                                            |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| OFF                                         | No data sources are configured or indexed.                                                                                             |
| REGISTRY                                    | Registry data is indexed.                                                                                                              |
| REGISTRY_AND_SHADOW                         | Registry data and unnamed (classic) shadow data are indexed.                                                                           |
| REGISTRY_AND_CONNECTIVITY                   | Registry data and connectivity data are indexed.                                                                                       |
| REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS | Registry data, unnamed (classic) shadow data, and connectivity data are<br>indexed.                                                    |
| MULTI_INDEXING_MODE                         | Named shadow or Device Defender violations data is indexed, in addition<br>to registry, unnamed (classic) shadow or connectivity data. |

## Querying a thing index

Use the **search-index** CLI command to query data in the index.

```
aws iot search-index --index-name "AWS_Things" --query-string
          "thingName:mything*"
```

```
{
    "things":[{
         "thingName":"mything1",
         "thingGroupNames":[
            "mygroup1"
         ],
         "thingId":"a4b9f759-b0f2-4857-8a4b-967745ed9f4e",
         "attributes":{
            "attribute1":"abc"
         },
         "connectivity": {
            "connected":false,
            "timestamp":1556649874716,
            "disconnectReason": "CONNECTION_LOST"
         }
    },
    {
        "thingName":"mything2",
        "thingTypeName":"MyThingType",
        "thingGroupNames":[
            "mygroup1",
            "mygroup2"
        ],
        "thingId":"01014ef9-e97e-44c6-985a-d0b06924f2af",
        "attributes":{
            "model":"1.2",
            "country":"usa"
        },
        "shadow":{
            "desired":{
                "location":"new york",
                "myvalues":[3, 4, 5]
            },
            "reported":{
                "location":"new york",
                "myvalues":[1, 2, 3],
                "stats":{
                    "battery":78
                }
            },
            "metadata":{
                 "desired":{
                       "location":{
                            "timestamp":123456789
                        },
                       "myvalues":{
                             "timestamp":123456789
                       }
                  },
                  "reported":{
                        "location":{
                             "timestamp":34535454
                         },
                        "myvalues":{
                             "timestamp":34535454
                        },
                        "stats":{
                             "battery":{
                                   "timestamp":34535454
                             }
                        }
                 }
            },
            "version":10,
            "timestamp":34535454
        },
        "connectivity": {
            "connected":true,
            "timestamp":1556649855046
        }
    }],
    "nextToken":"AQFCuvk7zZ3D9pOYMbFCeHbdZ+h=G"
}
```

In the JSON response, `"connectivity"` (as enabled by the
`thingConnectivityIndexingMode=STATUS` setting) provides a Boolean value, a
timestamp, and a disconnectReason that indicates whether the device is connected to
AWS IoT Core. The device `"mything1"` disconnected (`false`) at POSIX
time `1556649874716` due to `CONNECTION_LOST`. For more information
about disconnect reasons, see [Lifecycle events](life-cycle-events.md "life-cycle-events.md").

```
"connectivity": {
    "connected":false,
    "timestamp":1556649874716,
    "disconnectReason": "CONNECTION_LOST"
}
```

The device `"mything2"` connected (`true`) at POSIX time
`1556649855046`:

```
"connectivity": {
    "connected":true,
    "timestamp":1556649855046
}
```

Timestamps are given in milliseconds since epoch, so `1556649855046`
represents 6:44:15.046 PM on Tuesday, April 30, 2019 (UTC).

###### Important

If a device has been disconnected for approximately an hour, the
`"timestamp"` value and the `"disconnectReason"` value of the
connectivity status might be missing.

## Restrictions and limitations

These are the restrictions and limitations for `AWS_Things`.

**Shadow fields with complex types**

A shadow field is indexed only if the value of the field is a simple type, such
as a JSON object that doesn't contain an array, or an array that consists entirely
of simple types. Simple type means a string, number, or one of the literals
`true` or `false`. For example, given the following shadow
state, the value of field `"palette"` isn't indexed because it's an array
that contains items of complex types. The value of field `"colors"` is
indexed because each value in the array is a string.

```
{
    "state": {
        "reported": {
            "switched": "ON",
            "colors": [ "RED", "GREEN", "BLUE" ],
            "palette": [
                {
                    "name": "RED",
                    "intensity": 124
                },
                {
                    "name": "GREEN",
                    "intensity": 68
                },
                {
                    "name": "BLUE",
                    "intensity": 201
                }
            ]
        }
    }
}
```

**Nested shadow field names**

The names of nested shadow fields are stored as a period (.) delimited string.
For example, given a shadow document:

```
{
  "state": {
    "desired": {
      "one": {
        "two": {
          "three": "v2"
        }
      }
    }
  }
}
```

The name of field `three` is stored as
`desired.one.two.three`. If you also have a shadow document, it's
stored like this:

```
{
  "state": {
    "desired": {
      "one.two.three": "v2"
    }
  }
}
```

Both match a query for `shadow.desired.one.two.three:v2`. As a best
practice, don't use periods in shadow field names.

**Shadow metadata**

A field in a shadow's metadata section is indexed, but only if the corresponding
field in the shadow's `"state"` section is indexed. (In the previous
example, the `"palette"` field in the shadow's metadata section isn't
indexed either.)

**Unregistered devices**

Fleet indexing indexes the connectivity status for a device whose connection
`clientId` is the same as the `thingName` of a registered
thing in [Registry](thing-registry.md "thing-registry.md").

**Unregistered shadows**

If you use [UpdateThingShadow](../apireference/API_iotdata_UpdateThingShadow.md "../apireference/API_iotdata_UpdateThingShadow.md") to create a shadow using a thing name that hasn't been
registered in your AWS IoT account, fields in this shadow aren't indexed. This applies
to both classic unnamed shadow and named shadow.

**Numeric values**

If any registry or shadow data is recognized by the service as a numeric value,
it's indexed as such. You can form queries involving ranges and comparison operators
on numeric values (for example, `"attribute.foo<5"` or
`"shadow.reported.foo:[75 TO 80]"`). To be recognized as numeric, the
value of the data must be a valid, literal type JSON number. The value can be an
integer in the range -2^53...2^53-1, a double-precision floating point with optional
exponential notation, or part of an array that contains only these values.

**Null values**

Null values aren't indexed.

**Maximum values**

The maximum number of custom fields for aggregation queries is 5.

The maximum number of requested percentiles for aggregation queries is 100.

## Authorization

You can specify the things index as an Amazon Resource Name (ARN) in an AWS IoT policy
action, as follows.

| Action              | Resource                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| `iot:SearchIndex`   | An index ARN (for example,<br>`arn:aws:iot:`your-aws-region``your-aws-account`:index/AWS_Things`). |
| `iot:DescribeIndex` | An index ARN (for example,<br>`arn:aws:iot:`your-aws-region`:index/AWS_Things`).                   |

###### Note

If you have permissions to query the fleet index, you can access the data of things
across the entire fleet.
