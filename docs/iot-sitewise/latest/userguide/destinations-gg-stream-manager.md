# Destinations and AWS IoT Greengrass stream manager

AWS IoT Greengrass stream manager allows you to send data to the following AWS Cloud
destinations: channels in AWS IoT Analytics, streams in Amazon Kinesis Data Streams, asset properties in AWS IoT SiteWise,
or objects in Amazon Simple Storage Service (Amazon S3). For more information, see [Manage data streams on the AWS IoT Greengrass
Core](../../../greengrass/v2/developerguide/manage-data-streams.md "../../../greengrass/v2/developerguide/manage-data-streams.md") in _AWS IoT Greengrass Version 2 Developer Guide_.

###### Example: Data stream message structure

The following example shows the required data stream message structure
transmitted by the AWS IoT Greengrass stream manager.

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

The data stream message must include either (`assetId` and
`propertyId`) or `propertyAlias` in its structure.

`assetId`

(Optional) The ID of the asset to update.

`propertyAlias`

(Optional) The alias that identifies the property, such as an OPC UA
server data stream path. For example:

```
/company/windfarm/3/turbine/7/temperature
```

For more information, see [Manage data streams](manage-data-streams.md "manage-data-streams.md") in the _AWS IoT SiteWise User
Guide_.

`propertyId`

(Optional) The ID of the asset property for this entry.

`propertyValues`

(Required) The list of property values to upload. You can specify up
to 10 `propertyValues` array elements.

`quality`

(Optional) The quality of the asset property value.

`timestamp`

(Required) The timestamp of the asset property
value.

`offsetInNanos`

(Optional) The nanosecond offset from
`timeInSeconds`.

`timeInSeconds`

(Required) The timestamp date, in seconds, in
the Unix epoch format. Fractional nanosecond data
is provided by `offsetInNanos`.

`value`

(Required) The value of the asset property.

###### Note

Only one of the following values can exist in the
`value` field.

`booleanValue`

(Optional) Asset property data of type Boolean
(`true` or `false`).

`doubleValue`

(Optional) Asset property data of type double
(floating point number).

`integerValue`

(Optional) Asset property data of type integer
(whole number).

`stringValue`

(Optional) Asset property data of type string
(sequence of characters).
