# Turn on asset property notifications in AWS IoT SiteWise

You can enable property notifications to publish asset data updates to AWS IoT Core,
and then run queries on your data. With asset property notifications,
AWS IoT SiteWise provides an CloudFormation template that you can use to export AWS IoT SiteWise data to Amazon S3.

###### Note

Asset data is sent to AWS IoT Core every time it's received by AWS IoT SiteWise, regardless of if the value has changed.

###### Topics

- [Turn on asset property
  notifications (console)](#enable-property-notifications-console "#enable-property-notifications-console")
- [Turn on asset property notifications (AWS CLI)](#enable-property-notifications-cli "#enable-property-notifications-cli")

## Turn on asset property

notifications (console)

By default, AWS IoT SiteWise doesn't publish property value updates. You can use the AWS IoT SiteWise console to enable notifications for an asset property.

###### To enable or disable notifications for an asset property (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset to enable a property's notifications.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose **Edit**. 5. For the asset property's **Notification status**, choose
**ENABLED**.

![AWS IoT SiteWise "Edit asset" page screenshot with "Notification status" highlighted.](images/sitewise-enable-property-notifications-console.png)

You can also choose **DISABLED** to disable notifications for the
asset property. 6. Choose **Save**.

## Turn on asset property notifications (AWS CLI)

By default, AWS IoT SiteWise doesn't publish property value updates. You can use the AWS Command Line Interface (AWS CLI) to enable or disable notifications for an asset
property.

You must know your asset's `assetId` and property's
`propertyId` to complete this procedure. You can also use the external ID. If you created an
asset and don't know its `assetId`, use the [ListAssets](../APIReference/API_ListAssets.md "../APIReference/API_ListAssets.md") API to list all the assets
for a specific model. Use the [DescribeAsset](../APIReference/API_DescribeAsset.md "../APIReference/API_DescribeAsset.md") operation to view your asset's
properties including property IDs.

Use the [UpdateAssetProperty](../APIReference/API_UpdateAssetProperty.md "../APIReference/API_UpdateAssetProperty.md") operation to enable or disable notifications for an asset
property. Specify the following parameters:

- `assetId` – The asset's ID.
- `propertyId` – The asset property's ID.
- `propertyNotificationState` – The property value notification state:
  `ENABLED` or `DISABLED`.
- `propertyAlias` – The alias of the property. Specify the property's
  existing alias when you update the notification state. If you omit this parameter, the
  property's existing alias is removed.

###### To enable or disable notifications for an asset property (CLI)

1. Run the following command to retrieve the asset property's alias. Replace
   `asset-id` with the ID of the asset and
   `property-id` with the ID of the property.

```
aws iotsitewise describe-asset-property \
  --asset-id `asset-id` \
  --property-id `property-id`
```

The operation returns a response that contains the asset property's details in the
following format. The property alias is in `assetProperty.alias` in the JSON
object.

```
{
  "assetId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
  "assetName": "Wind Turbine 7",
  "assetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
  "assetProperty": {
    "id": "a1b2c3d4-5678-90ab-cdef-33333EXAMPLE",
    "name": "Wind Speed",
    "alias": "`/company/windfarm/3/turbine/7/windspeed`",
    "notification": {
      "topic": "$aws/sitewise/asset-models/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE/assets/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE/properties/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE",
      "state": "DISABLED"
    },
    "dataType": "DOUBLE",
    "unit": "m/s",
    "type": {
      "measurement": {}
    }
  }
}
```

2. Run the following command to enable notifications for the asset property. Replace
   `property-alias` with the property alias from the previous
   command's response, or omit `--property-alias` to update the property without
   an alias.

```
aws iotsitewise update-asset-property \
  --asset-id `asset-id` \
  --property-id `property-id` \
  --property-notification-state ENABLED \
  --property-alias `property-alias`
```

You can also pass `--property-notification-state DISABLED` to disable
notifications for the asset property.
