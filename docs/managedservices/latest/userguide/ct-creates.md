# Create change types

Create change types are matched version-to-version with the Update change types. That is, the change type
version that you use to provision a resource must match the version of the Update change type that you would use
later to modify that resource. For example, if you create an S3 bucket with the Create S3 Bucket change type version 2.0,
and later want to submit an RFC to modify that S3 bucket, you must use the Update S3 Bucket change type version 2.0
as well, even if there is an Update S3 Bucket change type with version 3.0.

We recommend keeping a record of the change type ID and version that you use when provisioning a resource
with a Create change type in case you later want to use an Update change type to modify it.
