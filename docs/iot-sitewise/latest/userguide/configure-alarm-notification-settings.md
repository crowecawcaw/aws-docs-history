

# Configure notification settings in AWS IoT SiteWise
<a name="configure-alarm-notification-settings"></a>

You can configure alarm notification settings using either the AWS IoT SiteWise console or the AWS Command Line Interface (AWS CLI).

## Configure notification settings (console)
<a name="configure-alarm-notification-settings-console"></a>

You can use the AWS IoT SiteWise console to update the value of the attributes that specify the notification settings for an alarm.

**To update an alarm's notification settings (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-assets"></a>In the navigation pane, choose **Assets**.

1. Choose the asset for which you want to update the alarm settings.

1. Choose **Edit**.

1. Find the attribute that the alarm uses for the notification setting that you want to change, and then enter its new value.

1. Choose **Save**.

## Configure notification settings (CLI)
<a name="configure-alarm-notification-settings-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to update the value of the attribute that specifies the notification settings for an alarm.

You must know your asset's `assetId` and property's `propertyId` to complete this procedure. You can also use the external ID. If you created an asset and don't know its `assetId`, use the [ListAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssets.html) API to list all the assets for a specific model. Use the [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html) operation to view your asset's properties including property IDs.

Use the [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) operation to assign attribute values to your asset. You can use this operation to set multiple attributes at once. This operation's payload contains a list of entries, and each entry contains the asset ID, property ID, and attribute value.<a name="attribute-id-update-cli"></a>

**To update an attribute's value (AWS CLI)**

1. Create a file called `batch-put-payload.json` and copy the following JSON object into the file. This example payload demonstrates how to set a wind turbine's latitude and longitude. Update the IDs, values, and timestamps to modify the payload for your use case.

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
   + Each entry in the payload contains an `entryId` that you can define as any unique string. If any request entries fail, each error will contain the `entryId` of the corresponding request so that you know which requests to retry.
   + To set an attribute value, you can include one timestamp-quality-value (TQV) structure in the list of `propertyValues` for each attribute property. This structure must contain the new `value` and the current `timestamp`.
     + `value` – A structure that contains one of the following fields, depending on the type of the property being set:
       + `booleanValue`
       + `doubleValue`
       + `integerValue`
       + `stringValue`
       + `nullValue`
     + `timestamp` – A structure that contains the current Unix epoch time in seconds, `timeInSeconds`. AWS IoT SiteWise rejects any data points with timestamps that existed longer than 7 days in the past or newer than 5 minutes in the future.

   For more information about how to prepare a payload for [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html), see [Ingest data with AWS IoT SiteWise APIs](ingest-api.md).

1. Run the following command to send the attribute values to AWS IoT SiteWise:

   ```
   aws iotsitewise batch-put-asset-property-value -\-cli-input-json file://batch-put-payload.json
   ```