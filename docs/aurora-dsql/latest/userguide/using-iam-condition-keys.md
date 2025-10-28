# Using IAM condition keys with Amazon Aurora DSQL

When you grant permissions in Aurora DSQL you can specify conditions that determine how a permissions policy
takes effect. The following are examples of how you can use condition keys in Aurora DSQL permissions policies.

## Example 1: Grant permission to create a cluster in a specific AWS Region

The following policy grants permission to create clusters in the US East (N. Virginia) and US East (Ohio) Regions.
This policy uses the resource ARN to limit the allowed Regions, so Aurora DSQL can only create clusters only if
that ARN is specified in the `Resource` section of the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": ["dsql:CreateCluster"],
 "Resource": [
 "arn:aws:dsql:us-east-1:*:cluster/*",
 "arn:aws:dsql:us-east-2:*:cluster/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

## Example 2: Grant permission to create a multi-Region cluster in specific AWS Regions

The following policy grants permission to create multi-Region clusters in the
US East (N. Virginia) and US East (Ohio) Regions. This policy uses the resource ARN to
limit the allowed Regions, so Aurora DSQL can create multi-Region clusters only if this ARN is
specified in the `Resource` section of the policy. Note that creating
multi-Region clusters also requires the `PutMultiRegionProperties`,
`PutWitnessRegion`, and `AddPeerCluster` permissions in each
specified Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dsql:CreateCluster",
 "dsql:PutMultiRegionProperties",
 "dsql:PutWitnessRegion",
 "dsql:AddPeerCluster"
 ],
 "Resource": [
 "arn:aws:dsql:us-east-1:123456789012:cluster/*",
 "arn:aws:dsql:us-east-2:123456789012:cluster/*"
 ]
 }
 ]
}`

```

## Example 3: Grant permission to create a multi-Region cluster with a specific witness Region

The following policy uses an Aurora DSQL `dsql:WitnessRegion` condition key and lets a user create multi-Region clusters
with a witness Region in US West (Oregon). If you don't specify the `dsql:WitnessRegion` condition, you can use
any Region as the witness Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dsql:CreateCluster",
 "dsql:PutMultiRegionProperties",
 "dsql:AddPeerCluster"
 ],
 "Resource": "arn:aws:dsql:*:123456789012:cluster/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dsql:PutWitnessRegion"
 ],
 "Resource": "arn:aws:dsql:*:123456789012:cluster/*",
 "Condition": {
 "StringEquals": {
 "dsql:WitnessRegion": [
 "us-west-2"
 ]
 }
 }
 }
 ]
}`

```
