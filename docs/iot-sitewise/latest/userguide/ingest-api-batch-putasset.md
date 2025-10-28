# BatchPutAssetPropertyValue API

Use the [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") operation to upload your data. With this operation, you can
upload multiple data entries at a time to collect data from several devices and
send it all in a single request.

###### Important

The [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") operation is subject to the following quotas:

- Up to 10 [entries](../APIReference/API_BatchPutAssetPropertyValue.md#API_BatchPutAssetPropertyValue_RequestSyntax "../APIReference/API_BatchPutAssetPropertyValue.md#API_BatchPutAssetPropertyValue_RequestSyntax")
  per request.
- Up to 10 [property values](../APIReference/API_PutAssetPropertyValueEntry.md#iotsitewise-Type-PutAssetPropertyValueEntry-propertyValues "../APIReference/API_PutAssetPropertyValueEntry.md#iotsitewise-Type-PutAssetPropertyValueEntry-propertyValues")
  (TQV data points) per entry.
- AWS IoT SiteWise rejects any data with a timestamp dated to more than 7 days in the past or more than 10 minutes in the future.

For more information about these quotas, see [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") in the _AWS IoT SiteWise API
Reference_.

To identify an asset property, specify one of the following:

- The `assetId` and `propertyId` of the asset property that data is sent to.
- The `propertyAlias`, which is a data stream alias (for example,
  `/company/windfarm/3/turbine/7/temperature`). To use this option, you must first set your asset property's alias.
  To set property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").
  The following example demonstrates how to send a
  wind turbine's temperature and rotations per minute (RPM) readings from a payload stored in a
  JSON file.

```
aws iotsitewise batch-put-asset-property-value --cli-input-json file://batch-put-payload.json
```

The example payload in `batch-put-payload.json` has the following
content.

```
{
  "enablePartialEntryProcessing": true,
  "entries": [
    {
      "entryId": "`unique entry ID`",
      "propertyAlias": "/company/windfarm/3/turbine/7/temperature",
      "propertyValues": [
        {
          "value": {
            "integerValue": 38
          },
          "timestamp": {
            "timeInSeconds": 1575691200
          }
        }
      ]
    },
    {
      "entryId": "`unique entry ID`",
      "propertyAlias": "/company/windfarm/3/turbine/7/rpm",
      "propertyValues": [
        {
          "value": {
            "doubleValue": 15.09
          },
          "timestamp": {
            "timeInSeconds": 1575691200
          },
          "quality": "GOOD"
        }
      ]
    },
    {
  "entryId": "unique entry ID",
      "propertyAlias": "/company/windfarm/3/turbine/7/rpm",
      "propertyValues": [
        {
  "value": {
  "nullValue":{"valueType": "D"}
          },
          "timestamp": {
  "timeInSeconds": 1575691200
          },
          "quality": "BAD"
        }
      ]
    }
  ]
}
```

Specifying `enablePartialEntryProcessing` as `true`
allows ingestion of all values that do not result in failure. The default behavior is `false`.
If a value is invalid, the entire entry fails ingestion.

Each entry in the payload contains an `entryId` that you can
define as any unique string. If any request entries fail, each error will contain the
`entryId` of the corresponding request so that you know which requests to retry.

Each structure in the list of `propertyValues` is a timestamp-quality-value (TQV)
structure that contains a `value`, a `timestamp`, and optionally a
`quality`.

- `value` – A structure that contains one of the following fields, depending on the type of the property being set:
  - `booleanValue`
  - `doubleValue`
  - `integerValue`
  - `stringValue`
  - `nullValue`

- `nullValue` – A structure with the following field denoting the
  type of the property value with value Null and quality of `BAD` or `UNCERTAIN`.
  - `valueType` – Enum of {"B", "D", "S", "I"}

- `timestamp` – A structure that contains the current Unix epoch time
  in seconds, `timeInSeconds`. You can also set the `offsetInNanos` key in
  the `timestamp` structure if you have temporally precise data. AWS IoT SiteWise rejects any
  data points with timestamps older than 7 days in the past or newer than 10 minutes in the
  future.
- `quality` – (Optional) One of the following quality strings:

      + `GOOD` – (Default) The data isn't affected by any issues.
      + `BAD` – The data is affected by an issue such as sensor
       failure.
      + `UNCERTAIN` – The data is affected by an issue such as sensor
       inaccuracy.

  For more information about how AWS IoT SiteWise handles data quality in computations, see
  [Data quality in formula expressions](expression-tutorials.md#data-quality "expression-tutorials.md#data-quality").
