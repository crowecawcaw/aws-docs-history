# Tagging AWS Elemental MediaTailor resources

A _tag_ is a metadata label that you assign or that AWS assigns to an
AWS resource. Each tag consists of a _key_ and a _value_. For tags that you assign, you define the key and value. For
example, you might define the key as `stage` and the value for one resource as
`test`.

Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging, so you can
  assign the same tag to resources from different services to indicate that the resources are
  related. For example, you could assign the same tag to an AWS Elemental MediaPackage channel and endpoint that
  you assign to an AWS Elemental MediaTailor configuration.
- Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the
  tags to categorize your costs and deliver a monthly cost allocation report to you. For more
  information, see [Use cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in
  the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- Control access to your AWS resources. For more information, see [Controlling access using
  tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the [IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").
  The following sections provide more information about tags for AWS Elemental MediaTailor.

## Supported resources in AWS Elemental MediaTailor

The following resources in AWS Elemental MediaTailor supports tagging:

- Channels
- Configurations
- SourceLocations
- VodSources

## Tag restrictions

The following basic restrictions apply to tags on AWS Elemental MediaTailor resources:

- Maximum number of tags that you can assign to a resource – 50
- Maximum key length – 128 Unicode characters
- Maximum value length – 256 Unicode characters
- Valid characters for key and value – a-z, A-Z, 0-9, space, and the following
  characters: \_ . : / = + - and @
- Keys and values are case sensitive
- Don't use `aws:` as a prefix for keys; it's reserved for AWS use

## Managing tags in AWS Elemental MediaTailor

You set tags as properties on a resource. You can add, edit, and delete tags through the
AWS Elemental MediaTailor API or the AWS Command Line Interface (AWS CLI). For more information, see the [AWS Elemental MediaTailor API
reference](../apireference/Welcome.md "../apireference/Welcome.md").
