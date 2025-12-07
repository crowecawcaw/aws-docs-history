# Using tags with S3 vector buckets

An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3
vector buckets. You can tag S3 vector buckets when you create them or manage tags on existing
vector buckets. For general information about tags, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md "tagging.md").

###### Note

There is no additional charge for using tags on vector buckets beyond the standard S3 API
request rates. For more information, see [Amazon S3
pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Common ways to use tags with vector

buckets

Use tags on your S3 vector buckets for:

- **Attribute-based access control (ABAC)** – Scale
  access permissions and grant access to S3 vector buckets based on their tags. For more
  information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

### ABAC for S3 vector buckets

Amazon S3 vector buckets support attribute-based access control (ABAC) using tags. Use
tag-based condition keys in your AWS organizations, IAM, and S3 vector bucket policies.
For enterprises, ABAC inAmazon S3 supports authorization across multiple AWS accounts.

In your IAM policies, you can control access to S3 vector buckets based on the vector
bucket's tags by using the following global condition keys:

`aws:ResourceTag/key-name`

Use this key to compare the tag key-value pair that you specify in the policy with
the key-value pair attached to the resource. For example, you could require that
access to a resource is allowed only if the resource has the attached tag key
`Dept` with the value `Marketing`. For more information, see
[Controlling access to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources").

`aws:RequestTag/key-name`

Use this key to compare the tag key-value pair that was passed in the request with
the tag pair that you specify in the policy. For example, you could check whether the
request includes the tag key `Dept` and that it has the value
`Accounting`. For more information, see [Controlling
access during AWS requests](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-requests "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-requests"). You can use this condition key to restrict
which tag key-value pairs can be passed during the `TagResource` and
`CreateVectorBucket` API operations.

`aws:TagKeys`

Use this key to compare the tag keys in a request with the keys that you specify
in the policy. We recommend that when you use policies to control access using tags,
use the `aws:TagKeys` condition key to define what tag keys are allowed.
For example policies and more information, see [Controlling
access based on tag keys](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys"). You can create an S3 vector bucket with tags. To
allow tagging during the `CreateVectorBucket` API operation, you must
create a policy that includes both the `s3vectors:TagResource` and
`s3vectors:CreateVectorBucket` actions. You can then use the
`aws:TagKeys` condition key to enforce using specific tags in the
`CreateVectorBucket` request.

`s3vectors:VectorBucketTag/tag-key`

Use this condition key to grant permissions to specific data in vector buckets
using tags. This condition key acts on the tags assigned to the vector bucket for all
S3 Vectors actions. Even when you create a index with tags, this condition key acts on
the tags applied to the vector bucket that contains that index. For example, you could
require that access to a bucket is allowed only if the bucket has the attached tag key
`Dept` with the value `Marketing`. When accessing indexes,
this condition references tags associated with the vector bucket containing that
index, while the `aws:ResourceTag/tag-key` will reference the tags of the
index itself.

### Example ABAC policies for vector

buckets

See the following example ABAC policies for Amazon S3 vector buckets.

#### 1.1 - IAM policy to create or

modify vector buckets with specific tags

In this IAM policy, users or roles with this policy can only create S3 vector buckets
if they tag the vector bucket with the tag key `project` and tag value
`Trinity` in the vector bucket creation request. They can also add or modify
tags on existing S3 vector buckets as long as the `TagResource` request
includes the tag key-value pair `project:Trinity`. This policy does not grant
read, write, or delete permissions on the vector buckets or its objects.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateVectorBucketWithTags",
      "Effect": "Allow",
      "Action": [
        "s3vectors:CreateVectorBucket",
        "s3vectors:TagResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/`project`": [
            "`Trinity`"
          ]
        }
      }
    }
  ]
}
```

#### 1.2 - Vector bucket policy to

restrict operations on the vector bucket using tags

In this vector bucket policy, IAM principals (users and roles) can perform operations
using the `PutVectorBucketPolicy` action on the vector bucket only if the value
of the vector bucket's `project` tag matches the value of the principal's
`project` tag.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowObjectOperations",
      "Effect": "Allow",
      "Principal": {
        "AWS": "`111122223333`"
      },
      "Action": "s3vectors:PutVectorBucketPolicy",
      "Resource": "arn:aws::s3vectors:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/`project`": "${aws:PrincipalTag/`project`}"
        }
      }
    }
  ]
}
```

#### 1.3 - IAM policy to modify tags on

existing resources maintaining tagging governance

In this IAM policy, IAM principals (users or roles) can modify tags on a vector bucket
only if the value of the vector bucket's `project` tag matches the value of the
principal's `project` tag. Only the four tags `project`,
`environment`, `owner`, and `cost-center` specified in
the `aws:TagKeys` condition keys are permitted for these vector buckets. This
helps enforce tag governance, prevents unauthorized tag modifications, and keeps the
tagging schema consistent across your vector buckets.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceTaggingRulesOnModification",
      "Effect": "Allow",
      "Action": [
        "s3vectors:TagResource"
      ],
      "Resource": "arn:aws::s3vectors:`us-west-2`:`111122223333`:bucket/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/`project`": "${aws:PrincipalTag/`project`}"
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "`project`",
            "`environment`",
            "`owner`",
            "`cost-center`"
          ]
        }
      }
    }
  ]
}
```

#### 1.4 - Using the

`s3vectors:VectorBucketTag` condition key

In this IAM policy, the condition statement allows access to the vector bucket's and
vector index's operations only if the vector bucket has the tag key
`Environment` and tag value `Production`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccessToTaggedBucket",
      "Effect": "Allow",
      "Action": "*",
      "Resource": "arn:aws::s3vectors:`us-west-2`:`111122223333`:bucket/*",
      "Condition": {
        "StringEquals": {
          "s3vectors:VectorBucketTag/`Environment`": "`Production`"
        }
      }
    }
  ]
}
```

## Managing tags for vector buckets

You can add or manage tags for S3 vector buckets using the Amazon S3 Console, the AWS Command Line Interface
(AWS CLI), the AWS SDKs, or using the S3 APIs: [TagResource](../../../index.md "../../../index.md"), [UntagResource](../../../index.md "../../../index.md"), and [ListTagsForResource](../../../index.md "../../../index.md"). For more information, see:

###### Topics

- [Creating vector buckets with
  tags](creating-vector-buckets-with-tags.md "creating-vector-buckets-with-tags.md")
- [Adding a tag to a vector bucket](adding-tag-vector-bucket.md "adding-tag-vector-bucket.md")
- [Viewing vector bucket tags](viewing-vector-bucket-tags.md "viewing-vector-bucket-tags.md")
- [Deleting a tag from a vector bucket](deleting-tag-vector-bucket.md "deleting-tag-vector-bucket.md")
