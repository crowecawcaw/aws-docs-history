

# Map external alarm state streams in AWS IoT SiteWise
<a name="connect-alarm-data-streams"></a>

You can define property aliases to map your data streams to your alarm state properties. This helps you easily identify an alarm state property when you ingest or retrieve data. For more information about property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md).

**Topics**
+ [Map external alarm state streams (console)](#connect-alarm-data-stream-console)
+ [Map external alarm state streams (AWS CLI)](#connect-alarm-data-stream-cli)

## Map external alarm state streams (console)
<a name="connect-alarm-data-stream-console"></a>

You can define property aliases to map your data streams to your alarm state properties. This helps you easily identify an alarm state property when you ingest or retrieve data. For more information about property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md).

You can use the AWS IoT SiteWise console to set an alias for an alarm state property.

**To set a property alias for an alarm state property (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-assets"></a>In the navigation pane, choose **Assets**.

1. Choose the asset for which you want to set a property alias.
**Tip**  <a name="sitewise-expand-asset-hierarchy"></a>
You can choose the arrow icon to expand an asset hierarchy to find your asset.

1. Choose **Edit**.

1. Scroll to **Alarms** and expand the section.

1. Under **External Alarms**, enter the alias in **Property alias – *optional***.

1. Choose **Save**.

## Map external alarm state streams (AWS CLI)
<a name="connect-alarm-data-stream-cli"></a>

You can define property aliases to map your data streams to your alarm state properties. This helps you easily identify an alarm state property when you ingest or retrieve data. For more information about property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md).

You can use the AWS Command Line Interface (AWS CLI) to set an alias for an alarm state property.

You must know your asset's `assetId` and property's `propertyId` to complete this procedure. You can also use the external ID. If you created an asset and don't know its `assetId`, use the [ListAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssets.html) API to list all the assets for a specific model. Use the [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html) operation to view your asset's properties including property IDs.

**Note**  
The [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html) response includes the list of composite asset models for the asset. Each alarm is a composite model. To find the `propertyId`, find the composite model for the alarm, and then find the `AWS/ALARM_STATE` property in that composite model.

For more information about how to set the property alias, see [Update an asset property alias](update-data-streams-method.md).