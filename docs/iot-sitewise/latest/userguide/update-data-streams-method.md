# Update an asset property alias

Aliases must be unique within an AWS region.
This includes aliases of both asset properties and data streams.
Do not assign an alias to an asset property, if another property or data stream is using that alias.

Console
Use the AWS IoT SiteWise console to update an asset property alias.

###### To update an asset property alias (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets** .
3. Select the asset from the table.
4. Click the **Edit** button.
5. Select the **Property type** in the **Properties**
   table.
6. Find the property, and type the new alias in the property alias text field.
7. Click the **Save** button to save the changes.

AWS CLI

To update an alias on an asset property, run the following command:

```

    aws iotsitewise update-asset-property \
        --asset-id <asset-ID> \
        --property-id <property-ID> \
        --property-alias <asset-property-alias> \
        --property-notification-state <ENABLED|DISABLED>

```

###### Note

If property notifications are currently enabled, it must be provided again to ensure it continues to be enabled.
