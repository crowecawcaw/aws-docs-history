# Cross-service

confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

## When AWS B2B Data Interchange accesses other services on your behalf

AWS B2B Data Interchange accesses other services on your behalf in the following scenarios:

- **Amazon S3 access:** AWS B2B Data Interchange reads input files from your Amazon S3 buckets and writes transformed output files to your Amazon S3 buckets. This occurs during EDI transformation workflows when processing documents through trading capabilities.
- **AWS KMS access:** When your Amazon S3 buckets use AWS KMS encryption, AWS B2B Data Interchange accesses AWS KMS to decrypt input files and encrypt output files during transformation processes.

AWS B2B Data Interchange includes the appropriate `aws:SourceArn` and `aws:SourceAccount` condition context keys when making these cross-service calls, enabling you to implement confused deputy protection in your resource policies.

###### Note

AWS B2B Data Interchange uses Forward Access Sessions (FAS) when accessing for generative AI-assisted EDI mapping features, which provides built-in protection against the confused deputy problem. No additional confused deputy protection is needed for access.

## Implementing confused deputy protection

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that AWS B2B Data Interchange gives another service to the
resource. Use `aws:SourceArn` if you want only one resource to be associated with
the cross-service access. Use `aws:SourceAccount` if you want to allow any
resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are specifying multiple
resources, use the `aws:SourceArn` global context condition key with wildcard
characters (`*`) for the unknown portions of the ARN. For example,
`arn:aws:b2bi:*:`123456789012`:*`.

If the `aws:SourceArn` value does not contain the account ID, such as an Amazon S3
bucket ARN, you must use both global condition context keys to limit permissions.

The value of `aws:SourceArn` must be the AWS B2B Data Interchange resource (such as a profile, transformer, trading capability, or partnership) that is accessing the cross-service resource.

## Example policies

The following examples show how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys to prevent
the confused deputy problem when AWS B2B Data Interchange accesses your resources.

### Amazon S3 bucket policy example

The following example shows an Amazon S3 bucket policy that allows AWS B2B Data Interchange to access your bucket while preventing the confused deputy problem:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowB2BIAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "b2bi.amazonaws.com"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`123456789012`"
        },
        "StringLike": {
          "aws:SourceArn": "arn:aws:b2bi:*:`123456789012`:*"
        }
      }
    }
  ]
}
```

### AWS KMS key policy example

The following example shows a AWS KMS key policy that allows AWS B2B Data Interchange to use your key for encryption and decryption while preventing the confused deputy problem:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowB2BIKMSAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "b2bi.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`123456789012`"
        },
        "StringLike": {
          "aws:SourceArn": "arn:aws:b2bi:*:`123456789012`:*"
        }
      }
    }
  ]
}
```
