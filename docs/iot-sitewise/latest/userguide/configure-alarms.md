# Configure alarms on assets in AWS IoT SiteWise

After you define an AWS IoT Events alarm on an asset model, you can
configure the alarm on each asset based on the asset model. You can edit the threshold value
and the notification settings for the alarm. Each of these values is an attribute on the
asset, so you can update the default value of the attribute to configure these values.

###### Note

You can configure these values for AWS IoT Events alarms, but not on external alarms.

###### Topics

- [Configure a threshold value
  (console)](#configure-alarm-threshold-value-console "#configure-alarm-threshold-value-console")
- [Configure a threshold value
  (AWS CLI)](#configure-alarm-threshold-value-cli "#configure-alarm-threshold-value-cli")
- [Configure notification settings in AWS IoT SiteWise](configure-alarm-notification-settings.md "configure-alarm-notification-settings.md")

## Configure a threshold value

(console)

You can use the AWS IoT SiteWise console to update the value of the attribute that specifies the
threshold value of an alarm.

###### To update an alarm's threshold value (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset for which you want to update an alarm threshold value.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose **Edit**. 5. Find the attribute that the alarm uses for its threshold value, and then enter its
new value. 6. Choose **Save**.

## Configure a threshold value

(AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to update the value of the attribute that specifies the threshold value of an alarm.

You must know your asset's `assetId` and property's
`propertyId` to complete this procedure. You can also use the external ID. If you created an
asset and don't know its `assetId`, use the [ListAssets](../APIReference/API_ListAssets.md "../APIReference/API_ListAssets.md") API to list all the assets
for a specific model. Use the [DescribeAsset](../APIReference/API_DescribeAsset.md "../APIReference/API_DescribeAsset.md") operation to view your asset's
properties including property IDs.

Use the [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") operation to assign attribute values to your asset. You
can use this operation to set multiple attributes at once. This operation's payload contains
a list of entries, and each entry contains the asset ID, property ID, and attribute
value.

###### To update an attribute's value (AWS CLI)

1. Create a file called `batch-put-payload.json` and copy the
   following JSON object into the file. This example payload demonstrates how to set a wind
   turbine's latitude and longitude. Update the IDs, values, and timestamps to modify the
   payload for your use case.

```
{
  "entries": [
    {
      "entryId": "windfarm3-turbine7-latitude",
      "assetId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
      "propertyId": "a1b2c3d4-5678-90ab-cdef-33333EXAMPLE",
      "propertyValues": [
        {
          "value": {
            "doubleValue": 47.6204
          },
          "timestamp": {
            "timeInSeconds": 1575691200
          }
        }
      ]
    },
    {
      "entryId": "windfarm3-turbine7-longitude",
      "assetId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
      "propertyId": "a1b2c3d4-5678-90ab-cdef-55555EXAMPLE",
      "propertyValues": [
        {
          "value": {
            "doubleValue": 122.3491
          },
          "timestamp": {
            "timeInSeconds": 1575691200
          }
        }
      ]
    }
  ]
}
```

    * Each entry in the payload contains an `entryId` that you can
     define as any unique string. If any request entries fail, each error will contain the
     `entryId` of the corresponding request so that you know which requests to retry.
    * To set an attribute value, you can include one timestamp-quality-value (TQV)
     structure in the list of `propertyValues` for each attribute property. This
     structure must contain the new `value` and the current
     `timestamp`.




    	+ `value` – A structure that contains one of the following fields, depending on the type of the property being set:




    		- `booleanValue`
    		- `doubleValue`
    		- `integerValue`
    		- `stringValue`
    		- `nullValue`
    	+ `timestamp` – A structure that contains the current Unix epoch
    	 time in seconds, `timeInSeconds`. AWS IoT SiteWise rejects any data points with
    	 timestamps that existed longer than 7 days in the past or newer than 5 minutes in
    	 the future.

For more information about how to prepare a payload for [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md"), see
[Ingest data with AWS IoT SiteWise APIs](ingest-api.md "ingest-api.md"). 2. Run the following command to send the attribute values to AWS IoT SiteWise:

```
aws iotsitewise batch-put-asset-property-value -\-cli-input-json file://batch-put-payload.json
```
