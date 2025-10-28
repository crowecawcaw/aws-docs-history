# Export metadata examples

When you perform a bulk export of your AWS IoT SiteWise content to Amazon S3, you can specify _filters_ to
limit which specific asset models and assets you'd like to export.

You specify the filters in an `iotSiteWiseConfiguration` section within the `sources`
section of your request body.

###### Note

You can include multiple filters. The bulk operation will export any asset model or asset that matches any
of the filters.

If you don't provide any filters, then the operation will export all of your asset models and assets.

```
{
    "metadataTransferJobId": "`your-transfer-job-id`",
    "sources": [{
        "type": "iotsitewise",
        "iotSiteWiseConfiguration": {
            "filters": [{
                `list of filters`
            }]
        }
    }],
    "destination": {
        "type": "s3",
        "s3Configuration": {
            "location": "arn:aws:s3:::`amzn-s3-demo-bucket`"
        }
    }
}
```

## Filter by asset model

You can filter a specific asset model. You can also include all assets using that model, or all asset models
within its hierarchy. You can't include both assets and hierarchy.

For more information about hierarchies, see [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").

Asset model
This filter includes the specified asset model:

```
"filterByAssetModel": {
    "assetModelId": "`asset model ID`"
}
```

Asset model and its assets
This filter includes the specified asset model, along with all assets using that asset model:

```
"filterByAssetModel": {
    "assetModelId": "`asset model ID`",
    "includeAssets": true
}
```

Asset model and its hierarchy
This filter includes the specified asset model, along with all associated asset models in its
hierarchy:

```
"filterByAssetModel": {
    "assetModelId": "`asset model ID`",
    "includeOffspring": true
}
```

## Filter by asset

You can filter a specific asset. You can also include its asset model, or all associated assets within its
hierarchy. You can't include both asset model and hierarchy.

For more information about hierarchies, see [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").

Asset
This filter includes the specified asset:

```
"filterByAsset": {
    "assetId": "`asset ID`"
}
```

Asset and its asset model
This filter includes the specified asset, along with the asset model it uses:

```
"filterByAsset": {
    "assetId": "`asset ID`",
    "includeAssetModel": true
}
```

Asset and its hierarchy
This filter includes the specified asset, along with all associated assets in its hierarchy:

```
"filterByAsset": {
    "assetId": "`asset ID`",
    "includeOffspring": true
}
```
