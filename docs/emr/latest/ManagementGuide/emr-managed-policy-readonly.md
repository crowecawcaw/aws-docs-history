# IAM managed policy for read-only

access (on path to deprecation)

The `AmazonElasticMapReduceReadOnlyAccess` managed policy is on the
path to deprecation. You cannot attach this policy when launching new clusters.
`AmazonElasticMapReduceReadOnlyAccess` has been replaced with
[AmazonEMRReadOnlyAccessPolicy_v2](emr-managed-policy-readonly-v2.md "emr-managed-policy-readonly-v2.md") as the Amazon EMR
default managed policy. The content of this policy statement is shown in the
following snippet. Wildcard characters for the `elasticmapreduce`
element specify that only actions that begin with the specified strings are
allowed. Keep in mind that because this policy does not explicitly deny actions,
a different policy statement may still be used to grant access to specified
actions.

###### Note

You can also use the AWS Management Console to view the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:Describe*",
 "elasticmapreduce:List*",
 "elasticmapreduce:ViewEventsFromAllClustersInConsole",
 "s3:GetObject",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "sdb:Select",
 "cloudwatch:GetMetricStatistics"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowELASTICMAPREDUCEDescribe"
 }
 ]
}`

```
