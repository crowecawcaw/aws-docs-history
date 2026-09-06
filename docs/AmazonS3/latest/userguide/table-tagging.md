

# Using tags with S3 tables
<a name="table-tagging"></a>

An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3 tables. You can tag S3 tables when you create them or manage tags on existing tables. For general information about tags, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md).

**Note**  
There is no additional charge for using tags on tables beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

## Common ways to use tags with tables
<a name="common-ways-to-use-tags-table"></a>

Use tags on your S3 tables for:

1. **Cost allocation** – Track storage costs by table tag in AWS Billing and Cost Management. For more information, see [Using tags for cost allocation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#using-tags-for-cost-allocation).

1. **Attribute-based access control (ABAC)** – Scale access permissions and grant access to S3 tables based on their tags. For more information, see [Using tags for ABAC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#using-tags-for-abac).

**Note**  
You can use the same tags for both cost allocation and access control.

### ABAC for S3 tables
<a name="abac-for-tables"></a>

Amazon S3 tables support attribute-based access control (ABAC) using tags. Use tag-based condition keys in your AWS organizations, AWS Identity and Access Management (IAM), and S3 table policies. ABAC in Amazon S3 supports authorization across multiple AWS accounts. 

In your IAM policies, you can control access to S3 tables based on the table's tags by using the `s3tables:TableBucketTag/tag-key` condition key or the [AWS global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys): `aws:ResourceTag/key-name`, `aws:RequestTag/key-name`, or `aws:TagKeys`. 

#### aws:ResourceTag/key-name
<a name="table-condition-key-resource-tag"></a>

Use this condition key to compare the tag key-value pair that you specify in the policy with the key-value pair attached to the resource. For example, you could require that access to a table is allowed only if the table has the tag key `Department` with the value `Marketing`.

This condition key applies to table actions performed using the Amazon S3 Console, the AWS Command Line Interface (CLI), S3 APIs, or the AWS SDKs,.

For an example policy, see [1.1 - table policy to restrict operations on the table using tags](#example-policy-table-resource-tag).

For additional example policies and more information, see [Controlling access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources) in the *AWS Identity and Access Management User Guide*.

**Note**  
For actions performed on tables, this condition key acts on the tags applied to the table and not on the tags applied to the table bucket containing the table. Use the `s3tables:TableBucketTag/tag-key` instead if you would like your ABAC policies to act on the tags of the table bucket when performaing table actions. 

#### aws:RequestTag/key-name
<a name="table-condition-key-request-tag"></a>

Use this condition key to compare the tag key-value pair that was passed in the request with the tag pair that you specify in the policy. For example, you could check whether the request to tag a table includes the tag key `Department` and that it has the value `Accounting`. 

This condition key applies when tag keys are passed in a `TagResource` or `CreateTable` API operation request, or when tagging or creating a table with tags using the Amazon S3 Console, the AWS Command Line Interface (CLI), or the AWS SDKs. 

For an example policy, see [1.2 - IAM policy to create or modify tables with specific tags](#example-policy-table-request-tag).

For additional example policies and more information, see [Controlling access during AWS requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-requests) in the *AWS Identity and Access Management User Guide*.

#### aws:TagKeys
<a name="table-condition-key-tag-keys"></a>

Use this condition key to compare the tag keys in a request with the keys that you specify in the policy to define what tag keys are allowed for access. For example, to allow tagging during the `CreateTable` action, you must create a policy that allows both the `s3tables:TagResource` and `s3tables:CreateTable` actions. You can then use the `aws:TagKeys` condition key to enforce that only specific tags are used in the `CreateTable` request. 

This condition key applies when tag keys are passed in a `TagResource`, `UntagResource`, or `CreateTable` API operations or when tagging, untagging, or creating a table with tags using the AWS Command Line Interface (CLI), or the AWS SDKs. 

For an example policy, see [1.3 - IAM policy to control the modification of tags on existing resources maintaining tagging governance](#example-policy-table-tag-keys).

For additional example policies and more information, see [Controlling access based on tag keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-tag-keys) in the *AWS Identity and Access Management User Guide*.

#### s3tables:TableBucketTag/tag-key
<a name="table-bucket-tag-condition-key"></a>

Use this condition key to grant permissions to specific data in table buckets using tags. This condition key acts, on the most part, on the tags assigned to the table bucket for all S3 tables actions. Even when you create a table with tags, this condition key acts on the tags applied to the table bucket that contains that table. The exceptions are: 
+ When you create a table bucket with tags, this condition key acts on the tags in the request.

For an example policy, see [1.4 - Using the s3tables:TableBucketTag condition key](#example-policy-table-bucket-tag-tables).

#### Example ABAC policies for tables
<a name="example-table-abac-policies"></a>

See the following example ABAC policies for Amazon S3 tables.

**Note**  
If you have an IAM or S3 Tables resource-based policy that restricts IAM users and IAM roles based on principal tags, you must attach the same principal tags to the IAM role that Lake Formation uses to access your Amazon S3 data (for example, LakeFormationDataAccessRole) and grant this role the necessary permissions. This is required for your tag-based access control policy to work correctly with your S3 Tables analytics integration. 

##### 1.1 - table policy to restrict operations on the table using tags
<a name="example-policy-table-resource-tag"></a>

In this table policy, the specified IAM principals (users and roles) can perform the `GetTable` action only if the value of the table's `project` tag matches the value of the principal's `project` tag.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowGetTable",
      "Effect": "Allow",
      "Principal": {
        "AWS": "{{111122223333}}"
      },
      "Action": "s3tables:GetTable",
      "Resource": "arn:aws::s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/{{my_example_tab;e}}",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/{{project}}": "${aws:PrincipalTag/{{project}}}"
        }
      }
    }
  ]
}
```

##### 1.2 - IAM policy to create or modify tables with specific tags
<a name="example-policy-table-request-tag"></a>

In this IAM policy, users or roles with this policy can only create S3 tables if they tag the table with the tag key `project` and tag value `Trinity` in the table creation request. They can also add or modify tags on existing S3 tables as long as the `TagResource` request includes the tag key-value pair `project:Trinity`. This policy does not grant read, write, or delete permissions on the tables or its objects. 

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "CreateTableWithTags",
      "Effect": "Allow",
      "Action": [
        "s3tables:CreateTable",
        "s3tables:TagResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/{{project}}": [
            "{{Trinity}}"
          ]
        }
      }
    }
  ]
}
```

##### 1.3 - IAM policy to control the modification of tags on existing resources maintaining tagging governance
<a name="example-policy-table-tag-keys"></a>

In this IAM policy, IAM principals (users or roles) can modify tags on a table only if the value of the table's `project` tag matches the value of the principal's `project` tag. Only the four tags `project`, `environment`, `owner`, and `cost-center` specified in the `aws:TagKeys` condition keys are permitted for these tables. This helps enforce tag governance, prevents unauthorized tag modifications, and keeps the tagging schema consistent across your tables.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "EnforceTaggingRulesOnModification",
      "Effect": "Allow",
      "Action": [
        "s3tables:TagResource",
        "s3tables:UntagResource"
      ],
      "Resource": "arn:aws::s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/{{my_example_table}}",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/project": "${aws:PrincipalTag/project}"
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "{{project}}",
            "{{environment}}",
            "{{owner}}",
            "{{cost-center}}"
          ]
        }
      }
    }
  ]
}
```

##### 1.4 - Using the s3tables:TableBucketTag condition key
<a name="example-policy-table-bucket-tag-tables"></a>

In this IAM policy, the condition statement allows access to the table bucket's data only if the table bucket has the tag key `Environment` and tag value `Production`. The `s3tables:TableBucketTag/<tag-key>` differs from the `aws:ResourceTag/<tag-key>` condition key because, in addition to controlling access to table buckets depending on their tags, it allows you to control access to tables based on the tags on their parent table bucket.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowAccessToSpecificTables",
      "Effect": "Allow",
      "Action": "*",
      "Resource": "arn:aws::s3tables:{{us-west-2}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/*",
      "Condition": {
        "StringEquals": {
          "s3tables:TableBucketTag/Environment": "Production"
        }
      }
    }
  ]
}
```

## Managing tags for tables
<a name="table-working-with-tags"></a>

You can add or manage tags for S3 tables using the Amazon S3 Console, the AWS Command Line Interface (CLI), the AWS SDKs, or using the S3 APIs: [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html), [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html). For more information, see:

**Topics**
+ [Common ways to use tags with tables](#common-ways-to-use-tags-table)
+ [Managing tags for tables](#table-working-with-tags)
+ [Creating tables with tags](table-create-tag.md)
+ [Adding a tag to a table](table-tag-add.md)
+ [Viewing table tags](table-tag-view.md)
+ [Deleting a tag from a table](table-tag-delete.md)