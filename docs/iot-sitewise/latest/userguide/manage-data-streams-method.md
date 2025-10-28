# Associate a data stream to an asset property

Manage your data streams using the AWS IoT SiteWise console or AWS CLI.

Console
Use the AWS IoT SiteWise console to manage your data streams.

###### To manage data streams (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Data
   streams**.
3. Choose a data stream by either filtering on data stream alias,
   or selecting **Disassociated data streams** in
   the filter drop down menu.
4. Select the data stream to update. You may select multiple data streams.
   Click **Manage data streams** on the upper right.
5. Select the data stream to be associated from
   **Update data stream associations**, and
   click the **Choose measurement** button.
6. In the **Choose measurement** section,
   find the corresponding asset measurement property.
   Select the measurement then click **Choose**.
7. Perform steps 4 and 5 for other data streams
   selected in step 3. Assign asset properties to all
   the data streams.
8. Choose **Update** to commit the changes. A
   successful confirmation banner is displayed to confirm the update.

AWS CLI

To associate a data stream (identified by its alias) to an asset property (identified by its IDs),
run the following command:

```

aws iotsitewise associate-time-series-to-asset-property \
    --alias <data-stream-alias> \
    --assetId <asset-ID> \
    --propertyId <property-ID>

```
