# Using tags with S3 general purpose buckets

An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3 general purpose buckets. You can tag S3 buckets when you create them or manage tags on existing buckets. For general information about tags, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md "tagging.md").

###### Note

There is no additional charge for using tags on buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Common ways to use tags with buckets

Use tags on your S3 buckets for:

1. **Cost allocation** – Track storage costs by bucket tag in AWS Billing and Cost Management. For more information, see [Using tags for cost allocation](tagging.md#using-tags-for-cost-allocation "tagging.md#using-tags-for-cost-allocation").
2. **Attribute-based access control (ABAC)** – Scale access permissions and grant access to S3 buckets based on their tags. For more information, see [Using tags for ABAC](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

###### Note

For general purpose buckets, ABAC is not enabled by default. To enable ABAC for general purpose buckets, see [Enabling ABAC in general purpose buckets](buckets-tagging-enable-abac.md "buckets-tagging-enable-abac.md"). For Amazon S3 resources such as access points and directory buckets, ABAC is enabled by default. You can use the same tags for both cost allocation and access control.

### ABAC for S3 general purpose buckets

Amazon S3 general purpose buckets support attribute-based access control (ABAC) using tags. Use tag-based condition keys in your AWS organizations, IAM, and S3 bucket policies. For enterprises, ABAC in Amazon S3 supports authorization across multiple AWS accounts.

In your IAM policies, you can control access to S3 buckets based on the bucket's tags by using the following [global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys"):

- `aws:ResourceTag/key-name`
  - Use this condition key to compare the tag key-value pair that you specify in the policy with the key-value pair attached to the resource. S3 evaluates this condition key only after you enable ABAC on your bucket. For example, you could require that access to a resource is allowed only if the resource has the attached tag key `Dept` with the value `Marketing`. For more information, see [Controlling access to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources").

- `aws:RequestTag/key-name`
  - Use this condition key to compare the tag key-value pair that was passed in the request with the tag pair that you specify in the policy. For example, you could check whether the request includes the tag key `Dept` and that it has the value `Accounting`. For more information, see [Controlling access during AWS requests](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-requests "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-requests"). You can use this condition key to restrict which tag key-value pairs can be passed during the `TagResource` and `CreateBucket` API operations.

- `aws:TagKeys`
  - Use this condition key to compare the tag keys in a request with the keys that you specify in the policy. We recommend that when you use policies to control access using tags, use the `aws:TagKeys` condition key to define what tag keys are allowed. For example policies and more information, see [Controlling access based on tag keys](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys").

- `s3:BucketTag/tag-key`
  - Use this condition key to grant permissions to specific data in buckets using tags. This condition key is applicable only after ABAC is enabled on your bucket. When accessing a bucket by using an access point, the `aws:ResourceTag/tag-key` condition key references the tags on the bucket both when authorizing against the access point and the bucket. The `s3:BucketTag/tag-key` will reference the tags only of the bucket it is being authorized against.

###### Note

When creating buckets with tags, note that tag-based conditions to access your bucket using
aws:ResourceTag and s3:BucketTag condition keys are applicable only after you enable ABAC
on the bucket. To learn more, see [Enabling ABAC in general purpose buckets](buckets-tagging-enable-abac.md "buckets-tagging-enable-abac.md").

### Example ABAC policies for buckets

See the following example ABAC policies for Amazon S3 buckets.

#### 1.1 - IAM policy to create or modify buckets with specific tags

In this IAM policy, users or roles with this policy can only create S3 buckets if they tag the bucket with the tag key `project` and tag value `Trinity` in the bucket creation request. They can also add or modify tags on existing S3 buckets as long as the `TagResource` request includes the tag key-value pair `project:Trinity`. This policy does not grant read, write, or delete permissions on the buckets or its objects.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateBucketWithTags",
      "Effect": "Allow",
      "Action": [
        "s3:CreateBucket",
        "s3:TagResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/project": [
            "Trinity"
          ]
        }
      }
    }
  ]
}
```

#### 1.2 - Bucket policy to restrict operations

In this bucket policy, IAM principals (users and roles) are denied `s3:ListBucket`, `s3:GetObject`, and `s3:PutObject` actions on the bucket only if value of the `project` tag on the bucket matches the value of the `project` tag on the principal.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyObjectOperations",
            "Effect": "Deny",
            "Principal": "*",
            "Action": ["s3:ListBucket",
                       "s3:GetObject",
                       "s3:PutObject"],
            "Resource": "arn:aws:s3:::aws-s3-demo/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/project": "${aws:PrincipalTag/project}"
                }
            }
        }
    ]
}
```

#### 1.3 - IAM policy to modify tags on existing resources

In this IAM policy, IAM principals (users or roles) can modify tags on a bucket only if the value of the bucket's `project` tag matches the value of the principal's `project` tag. Only the four tags `project`, `environment`, `owner`, and `cost-center` specified in the `aws:TagKeys` condition keys are permitted for these buckets. This helps enforce tag governance, prevents unauthorized tag modifications, and keeps the tagging schema consistent across your buckets.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceTaggingRulesOnModification",
      "Effect": "Allow",
      "Action": [
        "s3:TagResource",
        "s3:CreateBucket"
      ],
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "project",
            "environment",
            "owner",
            "cost-center"
          ]
        }
      }
    }
  ]
}
```

#### 1.4 - Using the s3:BucketTag condition key

In this IAM policy, the condition statement allows access to the `aws-s3-demo` bucket's data only if the bucket has the tag key `Environment` and tag value `Production`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccessViaSpecificBucket",
      "Effect": "Allow",
      "Action": "*",
      "Resource": ["arn:aws:s3:::aws-s3-demo","arn:aws:s3:::aws-s3-demo/*"],
      "Condition": {
        "StringEquals": {
          "s3:BucketTag/Environment": "Production"
        }
      }
    }
  ]
}

```

## Managing tags for general purpose buckets

You can add or manage tags for S3 buckets using the Amazon S3 Console, the AWS Command Line Interface (CLI), the AWS SDKs, or using the S3 APIs: [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md"), [UntagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md"), and [ListTagsForResource](../API/API_control_ListTagsForResource.md "../API/API_control_ListTagsForResource.md"). For more information, see:

###### Topics
