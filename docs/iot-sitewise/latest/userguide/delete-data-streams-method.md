# Delete a data stream

When a property is removed from an asset model, AWS IoT SiteWise deletes the properties and their data streams
from all assets that are managed by the asset model. It also deletes all properties and their data streams
of an asset when the asset is deleted. If a data stream data must be preserved, it must be
disassociated from the asset property before it is deleted.

###### Warning

When a property is deleted from an asset, the associated data stream is also deleted.
To preserve the data stream, disassociate it from the asset property first,
before deleting the property from the asset model, or deleting the asset.

Console
Use the AWS IoT SiteWise console to disassociate your data stream from an asset property.

###### To delete a data stream (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Data
   streams**.
3. Choose a data stream by filtering on data stream alias.
4. Select the data stream to delete. You may select multiple data streams.
5. Choose the **Delete** button to delete the data stream.

AWS CLI

Use the [DeleteTimeSeries](../APIReference/API_DeleteTimeSeries.md "../APIReference/API_DeleteTimeSeries.md") API to delete a specific data stream, by its alias.

```

    aws iotsitewise delete-time-series \
        --alias <data-stream-alias>

```
