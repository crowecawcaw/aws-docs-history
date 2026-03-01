# Tagging your API Gateway resources

A _tag_ is a metadata label that you assign or that AWS assigns to an
AWS resource. Each tag has two parts:

- A _tag key_ (for example, `CostCenter`,
  `Environment`, or `Project`). Tag keys are case
  sensitive.
- An optional field known as a _tag value_ (for example,
  `111122223333` or `Production`). Omitting the
  tag value is the same as using an empty string. Like tag keys, tag values are
  case-sensitive.
  Tags help you do the following:

- Control access to your resources based on the tags that are assigned to them. You
  control access by specifying tag keys and values in the conditions for an AWS Identity and Access Management
  (IAM) policy. For more information about tag-based access
  control, see [Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User
  Guide_.
- Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses
  the tags to categorize your costs and deliver a monthly cost allocation report to
  you. For more information, see [Use Cost Allocation
  Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- Identify and organize your AWS resources. Many AWS services support tagging, so
  you can assign the same tag to resources from different services to indicate that
  the resources are related. For example, you could assign the same tag to an API Gateway
  stage that you assign to a CloudWatch Events rule.
  For tips on using tags, see the whitepaper [AWS
  Tagging Strategies](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").

The following sections provide more information about tags for Amazon API Gateway.

###### Topics

- [API Gateway resources that can be tagged](apigateway-tagging-supported-resources.md "apigateway-tagging-supported-resources.md")
- [Using tags to control access to API Gateway REST API resources](apigateway-tagging-iam-policy.md "apigateway-tagging-iam-policy.md")
