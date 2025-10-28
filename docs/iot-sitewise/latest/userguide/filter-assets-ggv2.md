# Filter assets on a SiteWise Edge gateway

You can use edge filtering to more efficiently manage your assets by sending only a
subset of assets to a specific SiteWise Edge gateway for use in data processing. If your
assets are arranged in a tree, or parent-child, structure, you can set up an IAM
policy attached to a SiteWise Edge gateway’s IAM role that only allows the root of the tree,
or parent, and its children to be sent to a specific SiteWise Edge gateway.

###### Note

If you’re arranging existing assets into a tree structure, after you’ve created
the structure, go into each existing asset that you added to the structure and
choose **Edit** and then choose **Save** to make
sure AWS IoT SiteWise recognizes the new structure.

## Set up edge filtering

Set up edge filtering on your SiteWise Edge gateway by adding the following IAM policy
to the SiteWise Edge gateway’s IAM role, replacing
`<root-asset-id>` with the ID of the root asset
you want to send to the SiteWise Edge gateway.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "iotsitewise:DescribeAsset",
 "iotsitewise:ListAssociatedAssets"
 ],
 "Resource": "arn:aws:iotsitewise:*:*:asset/*",
 "Condition": {
 "StringNotLike": {
 "iotsitewise:assetHierarchyPath": "/`<root-asset-id>`*"
 }
 }
 }
 ]
}`

```

If there are assets currently on your SiteWise Edge gateway that you'd like to remove,
log into your SiteWise Edge gateway and run the following command to force the SiteWise Edge
gateway to sync with AWS IoT SiteWise by deleting the cache.

```
sudo rm /greengrass/v2/work/aws.iot.SiteWiseEdgeProcessor/sync-app/sync_resource_bundles/edge.json
```
