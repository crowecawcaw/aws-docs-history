# Disassociate a data stream from an asset property

Console
Use the AWS IoT SiteWise console to disassociate your data stream from an asset property.

###### To disassociate data streams from an asset property (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Data
   streams**.
3. Choose a data stream by either filtering on data stream alias,
   or selecting **Associated data streams** in
   the filter drop down menu.
4. Select the data stream to disassociate. The
   **Data stream alias** column must contain an
   alias. The **Asset name** and **Asset property name**
   columns must contain the values of the asset property the data stream is associated with.
   You can select multiple data streams.
5. Click **Manage data streams** on the upper right.
6. In the **Update data stream associations** section,
   click **X** in the **Measurement name** column.
   A `submitted` status should appear in the **Status** column.
7. Choose **Update** to commit the changes. The data stream
   is now disassociated from the asset property,
   and the alias is now used to identify the data stream.

AWS CLI
To disassociate a data stream from an asset property,
(identified by its `ID`s and its alias), run the following command:

```

    aws iotsitewise disassociate-time-series-from-asset-property \
        --alias <asset-property-alias> \
        --assetId <asset-ID> \
        --propertyId <property-ID>

```

The data stream is now disassociated from the asset property,
and the alias is used to identify the data stream.
The alias is no longer associated with the asset property,
as it is now associated with the data stream.
