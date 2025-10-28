# Message payload format for the

EMQX broker on AWS IoT SiteWise Edge

For the IoT SiteWise publisher component to consume data from your external
application and publish it to the AWS IoT SiteWise cloud, the payload sent to the broker
must meet specific requirements.

Understanding the payload format is key to successful MQTT communication with
AWS IoT SiteWise Edge. While the connection setup process is covered in later sections, we
present the payload requirements first to help you plan your
implementation.

## MQTT topic

requirements

There are no restrictions on MQTT topic structure, including the number of
levels or characters used. However, we recommend that the topic matches the
`propertyAlias` field in the payload.

###### Example property alias

If the MQTT topic is `site1/line1/compressor1/temperature`,
ensure the `propertyAlias` matches.

```
{
  "assetId": "compressor_asset_01",
  "propertyAlias": "`site1/line1/compressor1/temperature`",
  "propertyId": "temperature_sensor_01",
  "propertyValues": [
    {
      "quality": "GOOD",
      "timestamp": {
        "offsetInNanos": 0,
        "timeInSeconds": 1683000000
      },
      "value": {
        "doubleValue": 23.5
      }
    }
  ]
}
```

## JSON payload structure

The MQTT message payload are written in JSON and follow the
`PutAssetPropertyValueEntry` message format defined in the
[AWS IoT SiteWise API Reference](../APIReference/API_PutAssetPropertyValueEntry.md "../APIReference/API_PutAssetPropertyValueEntry.md").

```
{
   "assetId": "string",
   "propertyAlias": "string",
   "propertyId": "string",
   "propertyValues": [
      {
         "quality": "string",
         "timestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "value": {
            "booleanValue": boolean,
            "doubleValue": number,
            "integerValue": number,
            "stringValue": "string"
         }
      }
   ]
}
```

###### Note

For a message to be considered valid, only one of the following
conditions can be true:

- The `propertyAlias` is set, or
- Both `assetId` and `propertyId` are
  set
  The `PutAssetPropertyValueEntry` has an
  `entryId` field that is not required in this
  context.
