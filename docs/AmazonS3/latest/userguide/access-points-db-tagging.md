# Using tags with S3 Access Points for directory buckets

An AWS tag is a key-value pair that holds metadata about resources, in this case Amazon S3 Access Points for directory buckets. You can tag access points when you create them or manage tags on existing access points. For general information about tags, see [Tagging for cost allocation or attribute-based access control (ABAC)](tagging.md "tagging.md").

###### Note

There is no additional charge for using tags on access points for directory buckets beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").


## Common ways to use tags with access points for directory buckets


Attribute-based access control (ABAC) allows you to scale access permissions and grant access to access points for directory buckets based on their tags. For more information about ABAC in Amazon S3, see [Using tags for ABAC](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").


### ABAC for S3 Access Points


Amazon S3 Access Points support attribute-based access control (ABAC) using tags. Use tag-based condition keys in your AWS organizations, IAM, and Access Points policies. For enterprises, ABAC in Amazon S3 supports authorization across multiple AWS accounts. 


In your IAM policies, you can control access to access points for directory buckets based on the bucket's tags by using the following [global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys"):



* `aws:ResourceTag/key-name`




	+ Use this key to compare the tag key-value pair that you specify in the policy with the key-value pair attached to the resource. For example, you could require that access to a resource is allowed only if the resource has the attached tag key `Dept` with the value `Marketing`. For more information, see [Controlling access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources").
* `aws:RequestTag/key-name`




	+ Use this key to compare the tag key-value pair that was passed in the request with the tag pair that you specify in the policy. For example, you could check whether the request includes the tag key `Dept` and that it has the value `Accounting`. For more information, see [Controlling access during AWS requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-requests "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-requests"). You can use this condition key to restrict which tag key-value pairs can be passed during the `TagResource` and `CreateAccessPoint` API operations.
* `aws:TagKeys`




	+ Use this key to compare the tag keys in a request with the keys that you specify in the policy. We recommend that when you use policies to control access using tags, use the `aws:TagKeys` condition key to define what tag keys are allowed. For example policies and more information, see [Controlling access based on tag keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-tag-keys "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-tag-keys"). You can create an access point for directory buckets with tags. To allow tagging during the `CreateAccessPoint` API operation, you must create a policy that includes both the `s3express:TagResource` and `s3express:CreateAccessPoint` actions. You can then use the `aws:TagKeys` condition key to enforce using specific tags in the `CreateAccessPoint` request.
* `s3express:AccessPointTag/tag-key`




	+ Use this condition key to grant permissions to specific data via access points using tags. When using `aws:ResourceTag/tag-key` in an IAM policy, both the access point as well as the bucket to which the access point points to are required to have the same tag as they are both considered during authorization. If you want to control access to your data specifically via the access-point tag only, you can use `s3express:AccessPointTag/tag-key` condition key.

### Example ABAC policies for access points for directory buckets


See the following example ABAC policies for access points for directory buckets.


#### 1.1 - IAM policy to create or modify access points with specific tags


In this IAM policy, users or roles with this policy can only create access points if they tag the access points with the tag key `project` and tag value `Trinity` in the access point creation request. They can also add or modify tags on existing access points for directory buckets as long as the `TagResource` request includes the tag key-value pair `project:Trinity`. 



```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "CreateAccessPointWithTags",
      "Effect": "Allow",
      "Action": [
        "s3express:CreateAccessPoint",
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

#### 1.2 - Access Point policy to restrict operations on the bucket using tags


In this Access Point policy, IAM principals (users and roles) can perform operations using the `CreateSession` action on the access point only if the value of the access point's `project` tag matches the value of the principal's `project` tag.



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
      "Resource": "arn:aws::s3express:`region`:`111122223333`:access-point/``my-access-point``",
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


In this IAM policy, IAM principals (users or roles) can modify tags on an access point only if the value of the access point's `project` tag matches the value of the principal's `project` tag. Only the four tags `project`, `environment`, `owner`, and `cost-center` specified in the `aws:TagKeys` condition keys are permitted for these access points. This helps enforce tag governance, prevents unauthorized tag modifications, and keeps the tagging schema consistent across your access points.



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
      "Resource": "arn:aws::s3express:`region`:`111122223333`:accesspoint/``my-access-point``",
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

#### 1.4 - Using the s3express:AccessPointTag condition key


In this IAM policy, the condition statement allows access to the bucket's data only if the access point used to access the bucket has the tag key `Environment` and tag value `Production`. 



```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowAccessToSpecificAccessPoint",
      "Effect": "Allow",
      "Action": "*",
      "Resource": "arn:aws::s3express:`region`:`111122223333`:accesspoint/``my-access-point``",
      "Condition": {
        "StringEquals": {
          "s3express:AccessPointTag/Environment": "Production"
        }
      }
    }
  ]
}

```

## Working with tags for access points for directory buckets


You can add or manage tags for access points for directory buckets using the Amazon S3 Console, the AWS Command Line Interface (CLI), the AWS SDKs, or using the S3 APIs: [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md"), [UntagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md"), and [ListTagsForResource](../API/API_control_ListTagsForResource.md "../API/API_control_ListTagsForResource.md"). For more information, see:


###### Topics

* [Creating access points for directory buckets with tags](access-points-db-create-tag.md "access-points-db-create-tag.md")
* [Adding a tag to an access point for directory buckets](access-points-db-tag-add.md "access-points-db-tag-add.md")
* [Viewing the tags of an access point for directory buckets](access-points-db-tag-view.md "access-points-db-tag-view.md")
* [Deleting a tag from an access point for directory buckets](access-points-db-tag-delete.md "access-points-db-tag-delete.md")
