# Amazon S3 Bucket Policies for Amazon AppFlow

By default, all Amazon S3 buckets and objects are private. Only the resource owner, the
AWS account that created the bucket, can access the bucket and any objects that it
contains. However, the resource owner can choose to grant access permissions to
other resources and users by writing an access policy.

If you want to create or modify an Amazon S3 bucket to be used as a source or destination in a flow,
you must further modify the bucket policy. To read from or write to an Amazon S3 bucket, Amazon AppFlow must have the
the following permissions. Amazon AppFlow automatically attaches the required permissions to a bucket
when you select an Amazon S3 bucket as either the source or destination in a flow in the Amazon AppFlow console.
If using the Amazon AppFlow SDK these policies must be added manually.

## Amazon AppFlow Required Amazon S3 Policies

Amazon AppFlow requires a permission policy with the following attributes:

- The statement SID
- The bucket name
- The service principal name for Amazon AppFlow.
- The resources required for Amazon AppFlow: the bucket and all of its contents
- The required actions that Amazon AppFlow needs to take, which varies depending on if the bucket
  is used as a source or destination

The following policy allows Amazon AppFlow to access an Amazon S3 bucket used as the source in a flow. It contains
all of the necessary actions Amazon AppFlow needs to read objects from the specified bucket.

**Amazon S3
bucket policy**

```

{
    "Statement": [
        {
            "Effect": "Allow",
            "Sid": "AllowAppFlowSourceActions",
            "Principal": {
                "Service": "appflow.amazonaws.com"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::`myBucketName`",
                "arn:aws:s3:::`myBucketName`/*"
            ]
        }
    ]
}

```

The following policy allows Amazon AppFlow to access an Amazon S3 bucket used as the destination in a flow.
It contains all of the necessary actions Amazon AppFlow needs to put objects into an Amazon S3 bucket.

```

{
    "Statement": [
        {
            "Effect": "Allow",
            "Sid": "AllowAppFlowDestinationActions",
            "Principal": {
                "Service": "appflow.amazonaws.com"
            },
            "Action": [
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts",
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketAcl",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::`myBucketName`",
                "arn:aws:s3:::`myBucketName`/*"
            ]
        }
    ]
}

```

## Cross-service confused deputy prevention

The Confused Deputy problem is a security issue where an entity that doesn't have permission to
perform an action can coerce a more-privileged entity to perform that action in AWS. Cross-service
impersonation is one means of creating a confused deputy problem. Cross-service impersonation can occur
when one service (the _calling service_) calls another service
(the _called service_). The called service can be manipulated to use its permissions
to act on another customer's resources in a way it should not otherwise have permission to do.
To prevent this, AWS provides tools that help you protect your data for all services with service
principals that have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that Amazon AppFlow gives another service to the
resource. If you use both global condition context keys, the `aws:SourceAccount`
value and the account in the `aws:SourceArn` value must use the same account ID
when used in the same policy statement.

The value of `aws:SourceArn` must be the resource that is accessing
the Amazon S3 bucket. The most effective way to protect against the confused deputy problem
is to use the `aws:SourceArn` global condition context key with the full ARN
of the resource. For Amazon AppFlow, these will be the ARNs of the flows created with Amazon S3
as a source or destination. If you would like to specify multiple different flows, you
may use a list of different ARNs for the `aws:SourceArn` context key.
Additionally, you may use the `aws:SourceArn` global context condition key
with wildcards (\*). For example,
`arn:aws:`servicename`::`123456789012`:*`.
The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in Amazon S3 to prevent the
confused deputy problem when Amazon S3 is the destination. (Note that, when Amazon AppFlow
creates the policy for you during flow creation, it automatically populates the
`aws:SourceAccount` condition key.)

```

{
    "Statement": [
        {
            "Effect": "Allow",
            "Sid": "AllowAppFlowDestinationActions",
            "Principal": {
                "Service": "appflow.amazonaws.com"
            },
            "Action": [
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts",
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketAcl",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::`myBucketName`",
                "arn:aws:s3:::`myBucketName`/*"
            ],
            "Condition" : {
                "StringEquals" : {
                    "aws:SourceAccount" : "`myAccountId`"
                },
                "ArnLike" : {
                    "aws:SourceArn": ["arn:aws:appflow::`myAccountId`:flow/`flow-name-1`",
                                      "arn:aws:appflow::`myAccountId`:flow/`flow-name-2`"]
                }
            }
        }
    ]
}

```

## Cross-service confused deputy prevention for DescribeConnectorEntity

As part of its DescribeConnectorEntity API, Amazon AppFlow will make calls to Amazon S3 in order to get information
about specific objects in a customer’s Amazon S3 bucket. The DescribeConnectorEntity API is invoked either
through the direct usage of the Amazon AppFlow SDK, or via the Amazon AppFlow console when using an Amazon S3 bucket as the
source during flow creation. This API requires the following permissions:

- `S3:GetObject`
- `S3:ListBucket`

These calls are not associated with a particular resource. As such, when using
`aws:SourceArn` in a bucket policy granting these permissions to Amazon AppFlow, one should use
the global context condition key with wildcard if planning to use Amazon AppFlow's console or
DescribeConnectorEntity API with the Amazon S3 bucket the policy is attached to.
