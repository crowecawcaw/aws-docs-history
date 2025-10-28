# Ingest alarm state data in AWS IoT SiteWise

Alarm state properties expect alarm state as a serialized JSON string. To ingest alarm
state to an external alarm in AWS IoT SiteWise, you ingest this serialized string as a timestamped
string value. The following example demonstrates a state data value for an active
alarm.

```
{\"stateName\":\"Active\"}
```

To identify an alarm state property, you can specify one of the following:

- The `assetId` and `propertyId` of the alarm property that you're
  sending data to.
- The `propertyAlias`, which is a data stream alias (for example,
  `/company/windfarm/3/turbine/7/temperature/high`). To use this option, you must first set your alarm property's
  alias. To learn how to set property aliases for alarm state properties, see [Map external alarm state streams in AWS IoT SiteWise](connect-alarm-data-streams.md "connect-alarm-data-streams.md").
  The following example [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") API payload demonstrates how to format the
  state of an external alarm. This external alarm reports when a wind turbine's rotations per
  minute (RPM) reading is too high.

###### Example BatchPutAssetPropertyValue payload for alarm state data

```
{
    "entries": [
      {
        "entryId": "`unique entry ID`",
        "propertyAlias": "/company/windfarm/3/turbine/7/temperature/high",
        "propertyValues": [
          {
            "value": {
              "stringValue": "{\"stateName\":\"Active\"}"
            },
            "timestamp": {
              "timeInSeconds": 1607550262
            }
          }
        ]
      }
    ]
  }
```

For more information about how to use the `BatchPutAssetPropertyValue` API to
ingest data, see [Ingest data with AWS IoT SiteWise APIs](ingest-api.md "ingest-api.md").

For more information about other ways to ingest data, see [Ingest data to AWS IoT SiteWise](industrial-data-ingestion.md "industrial-data-ingestion.md").
