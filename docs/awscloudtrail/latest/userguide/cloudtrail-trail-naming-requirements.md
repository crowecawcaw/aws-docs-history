# Naming requirements for CloudTrail resources, S3 buckets, and KMS keys

This section provides information about the naming requirements for CloudTrail resources, Amazon S3 buckets, and KMS keys.

###### Topics

- [CloudTrail resource naming requirements](#cloudtrail-resource-naming-requirements "#cloudtrail-resource-naming-requirements")
- [Amazon S3 bucket naming requirements](#cloudtrail-s3-bucket-naming-requirements "#cloudtrail-s3-bucket-naming-requirements")
- [AWS KMS alias naming requirements](#KMS-key-naming-requirements "#KMS-key-naming-requirements")

## CloudTrail resource naming requirements

CloudTrail resource names must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.),
  underscores (\_), or dashes (-).
- Start with a letter or number, and end with a letter or number.
- Be between 3 and 128 characters.
- Have no adjacent periods, underscores or dashes. Names like my-\_namespace
  and my-\-namespace are invalid.
- Not be in IP address format (for example,
  `192.168.5.4`).

## Amazon S3 bucket naming requirements

The Amazon S3 bucket that you use to store CloudTrail log files must have a name that conforms
with naming requirements for non-US Standard regions. Amazon S3 defines a bucket name as a
series of one or more labels, separated by periods. For a complete list of naming rules,
see [Bucket naming rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md") in the _Amazon Simple Storage Service User Guide_.

The following are some of the rules:

- The bucket name can be between 3 and 63 characters long, and can contain
  only lower-case characters, numbers, periods, and dashes.
- Each label in the bucket name must start with a lowercase letter or
  number.
- The bucket name cannot contain underscores, end with a dash, have
  consecutive periods, or use dashes adjacent to periods.
- The bucket name cannot be formatted as an IP address (198.51.100.24).

###### Warning

Because S3 allows your bucket to be used as a URL that can be accessed publicly, the bucket name that you choose must be globally unique.
If some other account has already created a bucket with the name that you chose, you must use another name. For more information, see
[Bucket restrictions and limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md")
in the _Amazon Simple Storage Service User Guide_.

## AWS KMS alias naming requirements

When you create an AWS KMS key, you can choose an alias to identify it. For
example, you might choose the alias "KMS-CloudTrail-us-west-2" to encrypt the logs for a
specific trail.

The alias must meet the following requirements:

- Between 1 and 256 characters, inclusive
- Contain alphanumeric characters (A-Z, a-z, 0-9), hyphens (-), forward slashes (/),
  and underscores (\_)
- Cannot begin with **aws**

For more information, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md")
in the _AWS Key Management Service Developer Guide_.
