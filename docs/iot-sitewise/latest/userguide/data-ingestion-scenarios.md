# Common scenarios

## Move a data stream

To change a data stream’s association to another asset property, first disassociate
the data stream from the current asset property. When disassociating a data stream
from an asset property, there must be an alias assigned to that asset property.

```

    aws iotsitewise disassociate-time-series-from-asset-property \
        --alias <asset-property-alias> \
        --assetId <asset-ID> \
        --propertyId <property-ID>

```

Now re-assign the data stream to the new asset property.

```

    aws iotsitewise associate-time-series-from-asset-property \
        --alias <data-stream-alias> \
        --assetId <new-asset-ID> \
        --propertyId <new-property-ID>

```

## Error when assigning an alias to an asset property

When using the `UpdateAssetProperty` API to assign an
alias to a property, you may see the following error message:

```
Given alias <data-stream-alias> for property <property-name> with ID <property-ID> already in use by another property or data stream

```

This error message indicates the alias is not assigned to the property,
because it is currently used by another property or a data stream.

This happens if data is being ingested to AWS IoT SiteWise with an alias.
When data is sent with an alias not being used by another data stream or asset property,
a new data stream is created with that alias.
The below two options resolve the issue.

- Use `AssociateTimeSeriesToAssetProperty` API to associate the data stream with its alias to the asset property.
- Temporarily stop the data ingestion and delete the data stream. Use `UpdateAssetProperty` API
  to assign the alias to the asset property, and then turn data ingestion back on.

## Error when associating a data stream to an asset property

When associating a data stream to an asset property, the following error message is seen.

```
assetProperty <property-name> with assetId <asset-ID> propertyId <property-ID> contains data

```

This error message indicates the asset property already is associated with a data stream containing data.
That data stream must be disassociated or deleted, before associating an other data stream to that asset property.

###### Note

When disassociating a data stream from an asset property, the alias assigned to the property is given
to the data stream. For that alias to remain assigned to the property,
assign a new alias to that property before disassociating the data stream.

To preserve the data stored in the asset property do the following:

- Ensure no data is being ingested to the asset property, to prevent creating a new data stream.
- Use `UpdateAssetProperty` API to set a new alias that is given to the currently assigned data stream.
- Use `DisassociateTimeSeriesFromAssetProperty` API to disassociate the current data stream from the asset property.
- Use `AssociateTimeSeriesToAssetProperty` API to associate the desired data stream to the asset property.

If the data stored in the asset property must be deleted, do the following:

- Ensure no data is being ingested to the asset property, to prevent creating a new data stream.
- Use `DeleteTimeSeries` API to delete the currently assigned data stream.
- Use `AssociateTimeSeriesToAssetProperty` API to associate the desired data stream to the asset property.
