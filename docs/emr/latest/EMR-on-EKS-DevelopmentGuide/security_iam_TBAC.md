# Policies for tag-based access control

You can use conditions in your identity-based policy to control access to virtual clusters and job runs based on tags. For more information about tagging, see [Tagging your Amazon EMR on EKS resources](tag-resources.md "tag-resources.md").

The following examples demonstrate different scenarios and ways to use condition
operators with Amazon EMR on EKS condition keys. These IAM policy statements are intended
for demonstration purposes only and should not be used in production environments. There
are multiple ways to combine policy statements to grant and deny permissions according to
your requirements. For more information about planning and testing IAM policies, see the
[IAM user
Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

###### Important

Explicitly denying permission for tagging actions is an important consideration. This prevents users from tagging a resource and thereby granting themselves permissions that you did not intend to grant. If tagging actions for a resource are not denied, a user can modify tags and circumvent the intention of the tag-based policies. For an example of a policy that denies tagging actions, see [Deny access to add and remove tags](#security_iam_TBAC_deny "#security_iam_TBAC_deny").

The examples below demonstrate identity-based permissions policies that are used to control the actions that are allowed with Amazon EMR on EKS virtual clusters.

## Allow actions only on resources with specific tag

values

In the following policy example, the StringEquals condition operator tries to match dev with the value for the tag department. If the tag department hasn't been added to the virtual cluster, or doesn't contain the value dev, the policy doesn't apply, and the actions aren't allowed by this policy. If no other policy statements allow the actions, the user can only work with virtual clusters that have this tag with this value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:DescribeVirtualCluster"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "dev"
 }
 },
 "Sid": "AllowEMRCONTAINERDescribevirtualcluster"
 }
 ]
}`

```

You can also specify multiple tag values using a condition operator. For example, to allow actions on virtual clusters where the `department` tag contains the value `dev` or `test`, you could replace the condition block in the earlier example with the following.

```
"Condition": {
        "StringEquals": {
          "aws:ResourceTag/department": ["dev", "test"]
        }
      }
```

## Require tagging when a resource is created

In the example below, the tag needs to be applied when creating the virtual cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:CreateVirtualCluster"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/department": "dev"
 }
 },
 "Sid": "AllowEMRCONTAINERSCreatevirtualcluster"
 }
 ]
}`

```

The following policy statement allows a user to create a virtual cluster only if the cluster has a `department` tag, which can contain any value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-containers:CreateVirtualCluster"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "Null": {
 "aws:RequestTag/department": "false"
 }
 },
 "Sid": "AllowEMRCONTAINERSCreatevirtualcluster"
 }
 ]
}`

```

## Deny access to add and remove tags

The effect of this policy is to deny a user the permission to add or remove any tags on virtual clusters that are tagged with a `department` tag that contains the `dev` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "emr-containers:TagResource",
 "emr-containers:UntagResource"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:ResourceTag/department": "dev"
 }
 },
 "Sid": "AllowEMRCONTAINERSTagresource"
 }
 ]
}`

```
