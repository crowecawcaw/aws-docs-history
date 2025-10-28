# Manage data streams for AWS IoT SiteWise

A data stream is the resource that contains historical time series data.
Each data stream is identified by a unique alias, making it easier to
keep track of the origin for each piece of data. Data streams are
automatically created in AWS IoT SiteWise when the first time series data is received.
If the first time series data is identified with an alias, AWS IoT SiteWise creates a
new data stream with that alias, provided no asset properties are already
assigned that alias. Alternatively, if the first time series data is
identified with an asset ID and property ID, AWS IoT SiteWise creates a new data stream
and associates that data stream with the asset property.

There are two ways to assign an alias to an asset property. The method used depends
on if data is sent to AWS IoT SiteWise first, or an asset is created first.

- If data is sent to AWS IoT SiteWise first, this automatically creates a data stream with the assigned alias.
  When the asset is created later, use the
  [AssociateTimeSeriesToAssetProperty](../APIReference/API_AssociateTimeSeriesToAssetProperty.md "../APIReference/API_AssociateTimeSeriesToAssetProperty.md") API to associate the data stream and its alias to the asset property.
- If an asset is created first, use the
  [UpdateAssetProperty](../APIReference/API_UpdateAssetProperty.md "../APIReference/API_UpdateAssetProperty.md") API to assign an alias to an asset property. When data is later sent to AWS IoT SiteWise,
  the data stream is automatically created and associated with the asset property.
  Currently, you can only associate data streams with measurements. _Measurements_ are a type of asset property that represent devices' raw sensor
  data streams, such as timestamped temperature values or timestamped rotations per minute
  (RPM) values.

When these measurements define metrics or transformations, the incoming data triggers
specific calculations. It’s important to note that an asset property can only be linked to
one data stream at a time.

AWS IoT SiteWise uses `TimeSeries` for the Amazon Resource Name (ARN) resource to
determine your storage charges. For more information, see [AWS IoT SiteWise Pricing](https://aws.amazon.com/iot-sitewise/pricing/ "https://aws.amazon.com/iot-sitewise/pricing/").

The following sections show you how to use the AWS IoT SiteWise console or API to manage data
streams.

###### Topics

- [Configure permissions and settings](manage-data-streams-configuration.md "manage-data-streams-configuration.md")
- [Associate a data stream to an asset property](manage-data-streams-method.md "manage-data-streams-method.md")
- [Disassociate a data stream from an asset property](disassociate-data-streams-method.md "disassociate-data-streams-method.md")
- [Delete a data stream](delete-data-streams-method.md "delete-data-streams-method.md")
- [Update an asset property alias](update-data-streams-method.md "update-data-streams-method.md")
- [Common scenarios](data-ingestion-scenarios.md "data-ingestion-scenarios.md")
