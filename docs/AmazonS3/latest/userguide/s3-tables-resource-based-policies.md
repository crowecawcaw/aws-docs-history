# Resource-based policies for
 S3 Tables

S3 Tables provides resource-based policies for managing access to table buckets and
 tables: table bucket policies and table policies. You can use a table bucket policy to grant
 API access permissions at the table bucket, namespace, or table-level. The permissions
 attached to the table bucket can apply to all tables in the bucket or to specific tables in
 the bucket, depending on the policy definition. You can use a table policy to grant
 permissions at the table-level. 

When S3 Tables receives a request, it first verifies that the requester has the necessary
 permissions. It evaluates all the relevant access policies, user policies, and
 resource-based policies in deciding whether to authorize the request (IAM user policy,
 IAM role policy, table bucket policy, and table policy). For example, if a table bucket
 policy grants a user permissions to perform all actions on the tables in the bucket
 (including `DeleteTable`), but an individual table has a table policy that denies
 the `DeleteTable` action for all users, then the user cannot delete the
 table.

The following topic includes examples of table and table bucket policies. To use these policies,
 replace the `user input placeholders` with your own
 information.

###### Note


* Every policy that grants permissions to modify tables should include permissions
 for `GetTableMetadataLocation` to access the table root file.
 For more information, see [`GetTableMetadataLocation`](../API/API_s3TableBuckets_GetTableMetadataLocation.md "../API/API_s3TableBuckets_GetTableMetadataLocation.md").
* Every time that you perform a write or delete activity on your table, include
 permissions to `UpdateTableMetadataLocation` in your access
 policy.
* We recommend using a table bucket policy for governing access to bucket-level
 actions and a table policy for governing access to table-level actions.
 In cases where you want to define the same set of permissions across
 multiple tables, then we recommend using a table bucket policy.
###### Topics

* [Example 1: Table bucket policy allows access to PutBucketMaintenanceConfiguration for buckets in an account](#table-bucket-policy-1 "#table-bucket-policy-1")
* [Example 2: Table bucket policy to allows read (SELECT) access to tables stored in the hrnamespace](#table-bucket-policy-2 "#table-bucket-policy-2")
* [Example 3: Table policy to allow user to delete a table](#table-bucket-policy-3 "#table-bucket-policy-3")

## Example 1: Table bucket policy allows access to `PutBucketMaintenanceConfiguration` for buckets in an account


The following example table bucket policy allows the IAM `data steward` to delete unreferenced objects for all the buckets in an account by allowing access to `PutBucketMaintenanceConfiguration`.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/datasteward"
 },
 "Action": [
 "s3tables:PutTableBucketMaintenanceConfiguration"
 ],
 "Resource": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/*"
 }
 ]
}`

```





## Example 2: Table bucket policy to allows read (SELECT) access to tables stored in the `hr`namespace


The following an example table bucket policy allows Jane, a user from
 AWS account ID `123456789012` to access tables stored in the `hr` namespace in a
 table bucket.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:user/Jane"
 },
 "Action": [
 "s3tables:GetTableData",
 "s3tables:GetTableMetadataLocation"
 ],
 "Resource": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/*",
 "Condition": {
 "StringLike": {
 "s3tables:namespace": "hr"
 }
 }
 }
 ]
}`

```





## Example 3: Table policy to allow user to delete a table


The following example table policy that allows the IAM role `data steward` to delete a table.



JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "DeleteTable",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`datasteward`"
 },
 "Action": [
 "s3tables:DeleteTable",
 "s3tables:UpdateTableMetadataLocation",
 "s3tables:PutTableData",
 "s3tables:GetTableMetadataLocation"
 ],
 "Resource": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-bucket/table/`tableUUID`"
 }
 ]
}`

```
