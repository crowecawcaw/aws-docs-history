# Tags in AWS KMS

A _tag_ is an optional metadata label that you can assign
(or AWS can assign) to an AWS resource. Each tag consists of a _tag
key_ and a _tag value_, both of which are
case-sensitive strings. The tag value can be an empty (null) string. Each tag on a resource must
have a different tag key, but you can add the same tag to multiple AWS resources. Each
resource can have up to 50 user-created tags.

Do not include confidential or sensitive information in the tag key or tag value. Tags are
accessible to many AWS services, including billing.

In AWS KMS, you can add tags to a customer managed key when you create the KMS key, and tag or untag
existing KMS keys unless they are [pending deletion](key-state.md "key-state.md"). You
cannot tag aliases, custom key stores, AWS managed keys,AWS owned keys, or KMS keys in
other AWS accounts. Tags are optional, but they can be very useful.

For example, you can add a `"Project"="Alpha"` tag to all KMS keys and Amazon S3
buckets that you use for the Alpha project.

```
TagKey   = "Project"
TagValue = "Alpha"
```

For general information about tags, including the format and syntax, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
_Amazon Web Services General Reference_.

Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging, so you
  can assign the same tag to resources from different services to indicate that the resources
  are related. For example, you can assign the same tag to a KMS key and an Amazon Elastic Block Store (Amazon EBS) volume or AWS Secrets Manager secret. You can also use
  tags to identify KMS keys for automation.
- Track your AWS costs. When you add tags to your AWS resources, AWS generates a
  cost allocation report with usage and costs aggregated by tags. You can use this feature to
  track AWS KMS costs for a project, application, or cost center.

For more information about using tags for cost allocation, see [Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing User Guide_. For information about the rules for tag keys and
tag values, see [User-Defined Tag
Restrictions](../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md "../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md") in the _AWS Billing User Guide_.

- Control access to your AWS resources. Allowing and denying access to KMS keys based
  on their tags is part of AWS KMS support for [attribute-based access
  control](abac.md "abac.md") (ABAC). For information about controlling access to AWS KMS keys based
  on their tags, see [Use tags to control access to KMS keys](tag-authorization.md "tag-authorization.md").
  For more general information about using tags to control access to AWS resources, see
  [Controlling Access to AWS Resources Using
  Resource Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.
  AWS KMS writes an entry to your AWS CloudTrail log when you use the [TagResource](ct-tagresource.md "ct-tagresource.md"), [UntagResource](ct-untagresource.md "ct-untagresource.md"), or [ListResourceTags](../APIReference/API_ListResourceTags.md "../APIReference/API_ListResourceTags.md") operations.

###### Topics

- [Controlling access to tags](tag-permissions.md "tag-permissions.md")
- [Add tags to a KMS key](add-tags.md "add-tags.md")
- [Edit tags associated with a KMS key](edit-tags.md "edit-tags.md")
- [Remove tags associated with a KMS key](remove-tags.md "remove-tags.md")
- [View tags associated with a KMS key](view-tags.md "view-tags.md")
- [Use tags to control access to KMS keys](tag-authorization.md "tag-authorization.md")
