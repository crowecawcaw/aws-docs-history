# Viewing all cross-account grants using

the GetResourceShares API operation

If your enterprise grants cross-account permissions using both an AWS Glue Data Catalog resource
policy and Lake Formation grants, the only way to view all cross-account grants in one place is to
use the `glue:GetResourceShares` API operation.

When you grant Lake Formation permissions across
accounts by using the
named resource method, AWS Resource Access Manager (AWS RAM) creates an AWS Identity and Access Management (IAM)
resource policy and stores it in your AWS account. The policy grants the permissions
required to access the resource. AWS RAM creates a separate resource policy for each
cross-account grant. You can view all of these policies by using the
`glue:GetResourceShares` API operation.

###### Note

This operation also returns the Data Catalog resource policy. However, if you enabled
meta data encryption in Data Catalog settings, and you don't have permission on the AWS KMS key,
the operation won't return the Data Catalog resource policy.

###### To view all cross-account grants

- Enter the following AWS CLI command.

```
aws glue get-resource-policies
```

The following is an example resource policy that AWS RAM creates and stores when you
grant permissions on table `t` in database `db1` to AWS account
1111-2222-3333.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetTableVersion",
 "glue:GetTableVersions",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:SearchTables"
 ],
 "Principal": {"AWS": [
 "111122223333"
 ]},
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/t"
 ]
 }
 ]
}`

```

###### See also:

- [GetResourceShares Action (Python: get_resource_policies)](../../../glue/latest/dg/aws-glue-api-jobs-security.md#aws-glue-api-jobs-security-GetResourcePolicies "../../../glue/latest/dg/aws-glue-api-jobs-security.md#aws-glue-api-jobs-security-GetResourcePolicies") in the
  _AWS Glue Developer Guide_
