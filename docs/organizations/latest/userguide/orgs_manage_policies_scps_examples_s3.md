# Example SCPs for Amazon S3

###### Note

Amazon Simple Storage Service (Amazon S3) automatically applies server-side encryption (SSE-S3) for each new object, unless you specify a different encryption option.
For more information, see [Amazon S3
now automatically encrypts all new objects](../../../AmazonS3/latest/userguide/default-encryption-faq.md "../../../AmazonS3/latest/userguide/default-encryption-faq.md") in the _Amazon S3 User Guide_.

###### Topics

- [Prevent Amazon S3 unencrypted object uploads](#example-s3-1 "#example-s3-1")

## Prevent Amazon S3 unencrypted object uploads

The following policy restricts all users from uploading unencrypted objects to S3
buckets.

```


{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "s3:PutObject",
      "Resource": "*",
      "Condition": {
        "Null": {
          "s3:x-amz-server-side-encryption": "true"
        }
      }
    }
  ]
}

```

The following policy restricts all users from uploading unencrypted objects to S3
buckets and also enforces a specified encryption type (either AES256 or aws:kms) for object upload
in their buckets.

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "s3:PutObject",
      "Resource": "*",
      "Condition": {
        "Null": {
          "s3:x-amz-server-side-encryption": "true"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": "s3:PutObject",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "AES256"
        }
      }
    }
  ]
}

```
