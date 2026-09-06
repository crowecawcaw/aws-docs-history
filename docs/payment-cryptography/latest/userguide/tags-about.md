

# About tags in AWS Payment Cryptography
<a name="tags-about"></a>

A *tag* is an optional metadata label that you can assign (or AWS can assign) to an AWS resource. Each tag consists of a *tag key* and a *tag value*, both of which are case-sensitive strings. The tag value can be an empty (null) string. Each tag on a resource must have a different tag key, but you can add the same tag to multiple AWS resources. Each resource can have up to 50 user-created tags.

Do not include confidential or sensitive information in the tag key or tag value. Tags are accessible to many AWS services, including billing.

In AWS Payment Cryptography, you can add tags to a key when you [create the key](create-keys.md), and tag or untag existing keys unless they are pending deletion. You cannot tag aliases. Tags are optional, but they can be very useful.

For example, you can add a `"Project"="Alpha"` tag to all AWS Payment Cryptography keys and Amazon S3 buckets that you use for the Alpha project. Another example is to add `"BIN"="20130622"` tag to all keys associated to a specific bank identification number(BIN).

```
      [
      {
        "Key": "Project",
        "Value": "Alpha"
      },
      {
        "Key": "BIN",
        "Value": "20130622"
      }
    ]
```

For general information about tags, including the format and syntax, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference*.

Tags help you do the following:
+ Identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an AWS Payment Cryptography keys and an Amazon Elastic Block Store (Amazon EBS) volume or AWS Secrets Manager secret. You can also use tags to identify keys for automation.
+ Track your AWS costs. When you add tags to your AWS resources, AWS generates a cost allocation report with usage and costs aggregated by tags. You can use this feature to track AWS Payment Cryptography costs for a project, application, or cost center.

  For more information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*. For information about the rules for tag keys and tag values, see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html) in the *AWS Billing User Guide*.
+ Control access to your AWS resources. Allowing and denying access to keys based on their tags is part of AWS Payment Cryptography support for attribute-based access control (ABAC). For information about controlling access to AWS Payment Cryptography based on their tags, see [Authorization based on AWS Payment Cryptography tags](security_iam_service-with-iam.md#security_iam_service-with-iam-tags). For more general information about using tags to control access to AWS resources, see [Controlling Access to AWS Resources Using Resource Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.

AWS Payment Cryptography writes an entry to your AWS CloudTrail log when you use the TagResource, UntagResource, or ListTagsForResource operations.