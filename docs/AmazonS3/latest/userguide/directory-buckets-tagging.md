# Using tags with S3 directory buckets

An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3 directory buckets. You can tag S3 directory buckets when you create them or manage tags on existing directory buckets. For general information about tags, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md "tagging.md").

###### Note

There is no additional charge for using tags on directory buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").


## Common ways to use tags with directory buckets


Use tags on your S3 directory buckets for:



1. **Cost allocation** – Track storage costs by bucket tag in AWS Billing and Cost Management. For more information, see [Using tags for cost allocation](tagging.md#using-tags-for-cost-allocation "tagging.md#using-tags-for-cost-allocation").
2. **Attribute-based access control (ABAC)** – Scale access permissions and grant access to S3 directory buckets based on their tags. For more information, see [Using tags for ABAC](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

###### Note

You can use the same tags for both cost allocation and access control.


### ABAC for S3 directory buckets


Amazon S3 directory buckets support attribute-based access control (ABAC) using tags. Use tag-based condition keys in your AWS organizations, IAM, and S3 directory bucket policies. For enterprises, ABAC in Amazon S3 supports authorization across multiple AWS accounts. 


In your IAM policies, you can control access to S3 directory buckets based on the bucket's tags by using the following [global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys"):



* `aws:ResourceTag/key-name`




	+ Use this key to compare the tag key-value pair that you specify in the policy with the key-value pair attached to the resource. For example, you could require that access to a resource is allowed only if the resource has the attached tag key `Dept` with the value `Marketing`. For more information, see [Controlling access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources").
* `aws:RequestTag/key-name`




	+ Use this key to compare the tag key-value pair that was passed in the request with the tag pair that you specify in the policy. For example, you could check whether the request includes the tag key `Dept` and that it has the value `Accounting`. For more information, see [Controlling access during AWS requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-requests "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-requests"). You can use this condition key to restrict which tag key-value pairs can be passed during the `TagResource` and `CreateBucket` API operations.
* `aws:TagKeys`




	+ Use this key to compare the tag keys in a request with the keys that you specify in the policy. We recommend that when you use policies to control access using tags, use the `aws:TagKeys` condition key to define what tag keys are allowed. For example policies and more information, see [Controlling access based on tag keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-tag-keys "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-tag-keys"). You can create an S3 directory bucket with tags. To allow tagging during the `CreateBucket` API operation, you must create a policy that includes both the `s3express:TagResource` and `s3express:CreateBucket` actions. You can then use the `aws:TagKeys` condition key to enforce using specific tags in the `CreateBucket` request.
* `s3express:BucketTag/tag-key`




	+ Use this condition key to grant permissions to specific data in directory buckets using tags. When accessing a directory bucket by using an access point, this condition key references the tags on the directory bucket both when authorizing against the access point and the directory bucket, while the `aws:ResourceTag/tag-key` will reference the tags only of the resource it is being authorized against.

### Example ABAC policies for directory buckets


See the following example ABAC policies for Amazon S3 directory buckets.


#### 1.1 - IAM policy to create or modify buckets with specific tags


In this IAM policy, users or roles with this policy can only create S3 directory buckets if they tag the bucket with the tag key `project` and tag value `Trinity` in the bucket creation request. They can also add or modify tags on existing S3 directory buckets as long as the `TagResource` request includes the tag key-value pair `project:Trinity`. This policy does not grant read, write, or delete permissions on the buckets or its objects. 



```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "CreateBucketWithTags",
      "Effect": "Allow",
      "Action": [
        "s3express:CreateBucket",
        "s3express:TagResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/project": [
            "`Trinity`"
          ]
        }
      }
    }
  ]
}

```

#### 1.2 - Bucket policy to restrict operations on the bucket using tags


In this bucket policy, IAM principals (users and roles) can perform operations using the `CreateSession` action on the bucket only if the value of the bucket's `project` tag matches the value of the principal's `project` tag.



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
      "Action": "s3express:CreateSession",
      "Resource": "arn:aws::s3express:`us-west-2`:`111122223333`:bucket/``amzn-s3-demo-bucket--usw2-az1--x-s3``",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/project": "${aws:PrincipalTag/project}"
        }
      }
    }
  ]
}
```

#### 1.3 - IAM policy to modify tags on existing resources maintaining tagging governence


In this IAM policy, IAM principals (users or roles) can modify tags on a bucket only if the value of the bucket's `project` tag matches the value of the principal's `project` tag. Only the four tags `project`, `environment`, `owner`, and `cost-center` specified in the `aws:TagKeys` condition keys are permitted for these directory buckets. This helps enforce tag governance, prevents unauthorized tag modifications, and keeps the tagging schema consistent across your buckets.



```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "EnforceTaggingRulesOnModification",
      "Effect": "Allow",
      "Action": [
        "s3express:TagResource"
      ],
      "Resource": "arn:aws::s3express:`us-west-2`:`111122223333`:bucket/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/project": "${aws:PrincipalTag/project}"
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

#### 1.4 - Using the s3express:BucketTag condition key


In this IAM policy, the condition statement allows access to the bucket's data only if the bucket has the tag key `Environment` and tag value `Production`. 



```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowAccessToSpecificAccessPoint",
      "Effect": "Allow",
      "Action": "*",
      "Resource": "arn:aws::s3express:`us-west-2`:`111122223333`:accesspoint/*",
      "Condition": {
        "StringEquals": {
          "s3express:BucketTag/Environment": "Production"
        }
      }
    }
  ]
}

```

## Managing tags for directory buckets


You can add or manage tags for S3 directory buckets using the Amazon S3 Console, the AWS Command Line Interface (CLI), the AWS SDKs, or using the S3 APIs: [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md"), [UntagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md"), and [ListTagsForResource](../API/API_control_ListTagsForResource.md "../API/API_control_ListTagsForResource.md"). For more information, see:


###### Topics

* [Creating directory buckets with tags](directory-bucket-create-tag.md "directory-bucket-create-tag.md")
* [Adding a tag to a directory bucket](directory-bucket-tag-add.md "directory-bucket-tag-add.md")
* [Viewing directory bucket tags](directory-bucket-tag-view.md "directory-bucket-tag-view.md")
* [Deleting a tag from a directory bucket](directory-bucket-tag-delete.md "directory-bucket-tag-delete.md")
