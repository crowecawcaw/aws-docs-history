# Query asset property notifications in AWS IoT SiteWise

To query asset property notifications, create AWS IoT Core rules made up of SQL statements.

AWS IoT SiteWise publishes asset property data updates to AWS IoT Core in the following format.

```
{
  "type": "PropertyValueUpdate",
  "payload": {
    "assetId": "`String`",
    "propertyId": "`String`",
    "values": [
      {
        "timestamp": {
          "timeInSeconds": `Number`,
          "offsetInNanos": `Number`
        },
        "quality": "`String`",
        "value": {
          "booleanValue": `Boolean`,
          "doubleValue": `Number`,
          "integerValue": `Number`,
          "stringValue": "`String`",
          "nullValue": {
            "valueType": "`String`
            }
        }
      }
    ]
  }
}
```

Each structure in the `values` list is a timestamp-quality-value (TQV)
structure.

- The `timestamp` contains the current Unix epoch time in seconds
  with nanosecond offset.
- The `quality` contains one of the following strings that indicate the quality
  of the data point:
  - `GOOD` – The data isn't affected by any issues.
  - `BAD` – The data is affected by an issue such as sensor
    failure.
  - `UNCERTAIN` – The data is affected by an issue such as sensor
    inaccuracy.

- The `value` contains one of the following fields, depending on the type of the property:

      + `booleanValue`
      + `doubleValue`
      + `integerValue`
      + `stringValue`
      + `nullValue`

  `nullValue` – A structure with the following field denoting the
  type of the property value with value Null and quality of `BAD` or `UNCERTAIN`.

- `valueType` – Enum of {"B", "D", "S", "I"}
  To parse values out of the `values` array, you need to use complex nested
  object queries in your rules' SQL statements. For more information, see [Nested object queries](../../../iot/latest/developerguide/iot-sql-nested-queries.md "../../../iot/latest/developerguide/iot-sql-nested-queries.md") in the
  _AWS IoT Developer Guide_, or see the [Publish property value updates to Amazon DynamoDB](publish-to-amazon-dynamodb.md "publish-to-amazon-dynamodb.md")
  tutorial for a specific example of parsing asset property notification messages.

###### Example query to extract the array of values

The following statement demonstrates how to query the array of updated property values
for a specific double-type property on all assets with that property.

```
SELECT
  (SELECT VALUE (value.doubleValue) FROM payload.values) AS windspeed
FROM
  '$aws/sitewise/asset-models/`a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`/assets/+/properties/`a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`'
WHERE
  type = 'PropertyValueUpdate'
```

The previous rule query statement outputs data in the following format.

```
{
  "windspeed": [
    26.32020195042838,
    26.282584572975477,
    26.352566977372508,
    26.283084346171442,
    26.571883739599322,
    26.60684140743005,
    26.628738636715045,
    26.273486932802125,
    26.436379105473964,
    26.600590095377303
  ]
}
```

###### Example query to extract a single value

The following statement demonstrates how to query the first value from the array of
property values for a specific double-type property on all assets with that property.

```
SELECT
  get((SELECT VALUE (value.doubleValue) FROM payload.values), 0) AS windspeed
FROM
  '$aws/sitewise/asset-models/`a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`/assets/+/properties/`a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`'
WHERE
  type = 'PropertyValueUpdate'
```

The previous rule query statement outputs data in the following format.

```
{
  "windspeed": 26.32020195042838
}
```

###### Important

This rule query statement ignores value updates other than the first in each batch. Each
batch can contain up to 10 values. If you need to include the remaining values, you must set
up a more complex solution to output asset property values to other services. For example,
you can set up a rule with an AWS Lambda action to republish each value in the array to
another topic, and set up another rule to query that topic and publish each value to the
desired rule action.
