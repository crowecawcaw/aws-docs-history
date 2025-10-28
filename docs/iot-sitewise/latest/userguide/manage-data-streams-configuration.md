# Configure permissions and settings

Data streams are automatically created in AWS IoT SiteWise when the first time
series data is received. If the data ingested is not associated with an asset property,
AWS IoT SiteWise creates a new disassociated data stream which is
configurable to be associated with an asset property.
Configure the access control of the gateway sending data to AWS IoT SiteWise,
using IAM policies to specify the type of data to be ingested.

The following IAM policy disables disassociated data ingestion from the gateway,
while still allowing data ingestion to data streams associated with an asset property:

###### Example IAM user policy that disables disassociated data ingestion from the gateway

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPutAssetPropertyValuesUsingAssetIdAndPropertyId",
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "arn:aws:iotsitewise:*:*:asset/*"
 },
 {
 "Sid": "AllowPutAssetPropertyValuesUsingAliasWithAssociatedAssetProperty",
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "arn:aws:iotsitewise:*:*:time-series/*",
 "Condition": {
 "StringLikeIfExists": {
 "iotsitewise:isAssociatedWithAssetProperty": "true"
 }
 }
 },
 {
 "Sid": "DenyPutAssetPropertyValuesUsingAliasWithNoAssociatedAssetProperty",
 "Effect": "Deny",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "arn:aws:iotsitewise:*:*:time-series/*",
 "Condition": {
 "StringLikeIfExists": {
 "iotsitewise:isAssociatedWithAssetProperty": "false"
 }
 }
 }
 ]
}`

```

###### Example IAM user policy that disables all data ingestion from the gateway

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyPutAssetPropertyValues",
 "Effect": "Deny",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": [
 "arn:aws:iotsitewise:*:*:asset/*",
 "arn:aws:iotsitewise:*:*:time-series/*"
 ]
 }
 ]
}`

```
