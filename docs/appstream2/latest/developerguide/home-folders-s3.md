# Amazon S3 Bucket Storage

WorkSpaces Applications manages user content stored in home folders by using Amazon S3 buckets
created in your account. For every AWS Region, WorkSpaces Applications creates a bucket in your
account. All user content generated from streaming sessions of stacks in that
Region is stored in that bucket. The buckets are fully managed by the service
without any input or configuration from an administrator.

The new enhanced buckets are named in a specific format (Version 2) as
follows:

```
appstream2-36fb080bb8-`region-code`-`account-id-without-hyphens`-`random-identifier`
```

Where `region-code` is the AWS Region
code in which the stack is created and
`account-id-without-hyphens` is
your Amazon Web Services account ID. The first part of the bucket name,
`appstream2-36fb080bb8-`, does not change across accounts or
Regions.

For example, if you enable home folders for stacks in the US West (Oregon)
Region (us-west-2) on account number 123456789012, the service creates an Amazon S3
bucket in that Region with the name shown. Only an administrator with sufficient
permissions can delete this bucket.

```
appstream2-36fb080bb8-us-west-2-123456789012-abcdefg
```

The old version buckets are named as follows. Accounts created before WorkSpaces Applications
introduced the new enhanced bucket naming (Version 2) will follow the old naming
format.

```
appstream2-36fb080bb8-`region-code`-`account-id-without-hyphens`
```

Where `region-code` is the AWS Region
code in which the stack is created and
`account-id-without-hyphens` is
your Amazon Web Services account ID. The first part of the bucket name,
`appstream2-36fb080bb8-`, does not change across accounts or
Regions.

For example, if you enable home folders for stacks in the US West (Oregon)
Region (us-west-2) on account number 123456789012, the service creates an Amazon S3
bucket in that Region with the name shown. Only an administrator with sufficient
permissions can delete this bucket.

```
appstream2-36fb080bb8-us-west-2-123456789012
```

As mentioned earlier, disabling home folders for stacks does not delete any
user content stored in the Amazon S3 bucket. To permanently delete user content, an
administrator with adequate access must do so from the Amazon S3 console. WorkSpaces Applications adds
a bucket policy that prevents accidental deletion of the bucket. For more
information, see [Using IAM Policies to Manage Administrator Access to the Amazon S3 Bucket for Home Folders and Application Settings Persistence](s3-iam-policy.md "s3-iam-policy.md").
