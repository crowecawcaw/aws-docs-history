# Using tags with S3 vector indexes

An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3
vector indexes. You can tag S3 vector indexes when you create them or manage tags on existing
vector indexes. For general information about tags, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md "tagging.md").

###### Note

There is no additional charge for using tags on vector indexes beyond the standard S3 API
request rates. For more information, see [Amazon S3
pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Common ways to use tags with vector

indexes

Use tags on your S3 vector indexes for:

- **Cost allocation** – Track storage costs by
  vector index tag in AWS Billing and Cost Management. For more information, see [Using tags for cost allocation](tagging.md#using-tags-for-cost-allocation "tagging.md#using-tags-for-cost-allocation").
- **Attribute-based access control (ABAC)** – Scale
  access permissions and grant access to S3 vector indexes based on their tags. For more
  information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

###### Note

You can use the same tags for both cost allocation and access control.

### ABAC for S3 vector indexes

Amazon S3 vector indexes support attribute-based access control (ABAC) using tags. Use
tag-based condition keys in your AWS organizations, IAM, and S3 vector index policies.
For enterprises, ABAC inAmazon S3 supports authorization across multiple AWS accounts.

In your IAM policies, you can control access to S3 vector indexes based on the vector
index's tags by using the following global condition keys:

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
`CreateIndex` API operations.

`aws:TagKeys`

Use this key to compare the tag keys in a request with the keys that you specify
in the policy. We recommend that when you use policies to control access using tags,
use the `aws:TagKeys` condition key to define what tag keys are allowed.
For example policies and more information, see [Controlling
access based on tag keys](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys"). You can create an S3 vector index with tags. To
allow tagging during the `CreateVectorBucket` API operation, you must
create a policy that includes both the `s3vectors:TagResource` and
`s3vectors:CreateVectorBucket` actions. You can then use the
`aws:TagKeys` condition key to enforce using specific tags in the
`CreateVectorBucket` request.

### Example ABAC policies for vector

indexes

See the following example ABAC policies for Amazon S3 vector indexes.

#### 1.1 - IAM policy to create or

modify vector indexes with specific tags

In this IAM policy, users or roles with this policy can only create S3 vector indexes
if they tag the vector index with the tag key `project` and tag value
`Trinity` in the vector index creation request. They can also add or modify
tags on existing S3 vector indexes as long as the `TagResource` request
includes the tag key-value pair `project:Trinity`. This policy does not grant
read, write, or delete permissions on the vector indexes or its objects.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateVectorIndexWithTags",
      "Effect": "Allow",
      "Action": [
        "s3vectors:CreateIndex",
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

#### 1.2 - IAM policy to modify tags on

existing resources maintaining tagging governance

In this IAM policy, IAM principals (users or roles) can modify tags on a vector index
only if the value of the vector index's `project` tag matches the value of the
principal's `project` tag. Only the four tags `project`,
`environment`, `owner`, and `cost-center` specified in
the `aws:TagKeys` condition keys are permitted for these vector indexes. This
helps enforce tag governance, prevents unauthorized tag modifications, and keeps the
tagging schema consistent across your vector indexes.

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
