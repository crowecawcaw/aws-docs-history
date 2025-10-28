# ARN formats

ARNs are delimited by colons, and composed of segments, which are the parts separated by colons `(:)`. The specific components and values used in the segments of an ARN depend on which AWS service the ARN is for. The following example shows how ARNs are constructed.

```
arn:`partition`:`service`:`region`:`account-id`:`resource-id`
        arn:partition:`service`:`region`:`account-id`:`resource-type`/`resource-id`
        arn:partition:`service`:`region`:`account-id`:`resource-type`:`resource-id`
```

These ARNs contain the following segments:

`partition` – The partition that the resource is in. For standard AWS Regions, the partition is `aws`. If you have resources in other partitions, the partition is `aws-partitionname`. For example, the partition for resources in the China (Beijing) Region is `aws-cn`.

`service` – The service namespace that identifies the AWS product. For example, `quicksight` identifies Quick Sight, `s3` identifies Amazon S3, `iam` identifies IAM, and so on.

`region` – The AWS Region that the resource resides in. The ARNs for some resources don't require an AWS Region, so this component might be omitted in some cases, like in the case of S3. Quick Sight ARNs require an AWS Region.

`account-id` – The ID of the AWS account that owns the resource. When you use the account number in an ARN or an API operation, you omit the hyphens (for example, 123456789012). The ARNs for some resources don't require an account number, so this component might be omitted. Quick Sight ARNs require an AWS account number. However, the account number and the AWS Region are omitted from S3 bucket ARNs, as shown following.

```
arn:aws:s3:::`bucket_name`
arn:aws:s3:::`bucket_name/key_name`
```

`resource` or
`resource-type` – The content of this part
of the ARN varies by service. A resource identifier can be the name or ID of the
resource (for example, `user/Bob` or
`instance/i-1234567890abcdef0`) or a resource path. For example, some
resource identifiers include a parent resource (
`sub-resource-type/parent-resource/sub-resource`)
or a qualifier such as a version (
`resource-type:resource-name:qualifier`).

Some resource ARNs can include a path, variable, or wildcard.

You can use wildcard characters (`*` and `?`) within any ARN
segment. An asterisk (`*`) represents any combination of zero or more
characters, and a question mark (`?`) represents any single character. You
can use multiple `*` or `?` characters in each segment. If you're using the ARN for permissions, avoid using
`*` wildcards if possible, to limit access to only the required elements.
Following are some examples of using paths, wildcards, and variables.

For the following example, we use an S3 ARN. You might use this when you give
permissions to S3 in an IAM policy. This S3 ARN shows a path and file are
specified.

###### Note

The term key name is used to describe what looks like a path and file after
`bucketname/`. These are called key names because a bucket doesn't
actually contain folder structures like those used in your computer's file system.
Instead the slash (`/`) is a delimiter that helps to make the
organization of the bucket more intuitive. In this case, the bucket name is
`amzn-s3-demo-bucket`, and the key name is
`developers/design_info.doc`.

```
arn:aws:s3:::`amzn-s3-demo-bucket`/`my-data/sales-export-2019-q4.json`
```

To identify all the objects in the bucket, you can use a wildcard to indicate that all
key names (or paths and files) are included in the ARN, as follows.

```
arn:aws:s3:::`amzn-s3-demo-bucket`/`*`
```

You can use part of a key name plus the wildcard to identify all the objects that begin with a specific pattern. In this case, it resembles a folder name plus a wildcard, as shown following. However, this ARN also includes any "subfolders" inside of `my-data`.

```
arn:aws:s3:::`amzn-s3-demo-bucket`/`my-data/sales-export*`
```

In this case, specifying using this wildcard includes the objects with names like the following:

- `my-data/sales-export-1.xlsx`
- `my-data/sales-export-new.txt`
- `my-data/sales-export-2019/file1.txt`
  You can use wildcards of both types (asterisks and question marks) in combination or separately, as shown following.

```
arn:aws:s3:::`amzn-s3-demo-bucket`/`my-data/sales-export-2019-q?.*`

arn:aws:s3:::`amzn-s3-demo-bucket`/`my-data/sales-export-20??-q?.*`
```

Or, if you want to future-proof the ARN, you can replace the entire year with a wildcard, rather than just using wildcards for the last two digits.

```
arn:aws:s3:::`amzn-s3-demo-bucket`/`my-data/sales-export-????-q?.*`
arn:aws:s3:::`amzn-s3-demo-bucket`/`my-data/sales-export-*-q?.*`
```

To read more about S3 ARNs, see [Specifying Resources in a
Policy](../../../AmazonS3/latest/userguide/s3-arn-format.md "../../../AmazonS3/latest/userguide/s3-arn-format.md") and [Object Key and Metadata](../../../AmazonS3/latest/userguide/UsingMetadata.md "../../../AmazonS3/latest/userguide/UsingMetadata.md")
in the _Amazon S3 User Guide_.
