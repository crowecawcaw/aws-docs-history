# Prerequisites

Before you create an ID mapping workflow for one AWS account using either the
**Rule-based** or the **Provider services** ID mapping
method, you must first do the following:

- Complete the tasks in [Setting up AWS Entity Resolution](setting-up.md "setting-up.md").
- Complete the tasks in [Prepare input data tables](prepare-data-tables.md "prepare-data-tables.md"), depending on the type of input data you are
  using.
- [Create a
  schema mapping](create-schema-mapping.md "create-schema-mapping.md") or [Create a matching workflow](create-matching-workflow.md "create-matching-workflow.md").
- (**Provider services** ID mapping only) Before you create an ID
  mapping workflow with LiveRamp, you must choose an Amazon Simple Storage Service (Amazon S3) data staging bucket
  where you want to temporarily write the ID mapping workflow output.

If you are using the LiveRamp provider service to translate third-party data, add
the following permissions policy, which allows you to access the data staging
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::715724997226:root"

 },
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`<staging-bucket>`",
 "arn:aws:s3:::`<staging-bucket>`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::715724997226:root"
 },
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:GetBucketPolicy",
 "s3:ListBucketVersions",
 "s3:GetBucketAcl"
 ],
 "Resource": [
 "arn:aws:s3:::`<staging-bucket>`",
 "arn:aws:s3:::`<staging-bucket>`/*"
 ]
 }
 ]
}`

```

In the preceding permissions policy, replace each `<user input
 placeholder>` with your own information.

|                  |                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| `staging-bucket` | The Amazon S3 bucket that temporarily stores your data while running a provider service-based workflow. |
