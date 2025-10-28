# Best practices and strategies

These sections provide information about best practices and strategies when tagging your
AWS resources and using Tag Editor.

## Tagging best practices

As you create a tagging strategy for AWS resources, follow best practices:

- Do not add personally identifiable information (PII) or other confidential or
  sensitive information in tags. Tags are accessible to many AWS services,
  including billing. Tags are not intended to be used for private or sensitive
  data.
- Use a standardized, case-sensitive format for tags, and apply it consistently
  across all resource types.
- Consider tag guidelines that support multiple purposes, like managing resource
  access control, cost tracking, automation, and organization.
- Use automated tools to help manage resource tags. Tag Editor and the [Resource Groups Tagging API](../../../resourcegroupstagging/latest/APIReference.md "../../../resourcegroupstagging/latest/APIReference.md") enable programmatic control of tags,
  making it easier to automatically manage, search, and filter tags and
  resources.
- Use too many tags rather than too few tags.
- Remember that it is easy to change tags to accommodate changing business
  requirements, but consider the consequences of future changes. For example,
  changing access control tags means you must also update the policies that
  reference those tags and control access to your resources.
- You can automatically enforce the tagging standards that your organization
  chooses to adopt by creating and deploying tag policies using AWS Organizations. Tag
  policies let you specify tagging rules that define valid key names and the
  values that are valid for each key. You can choose to only monitor, giving you
  an opportunity to evaluate and clean up your existing tags. Once your tags are
  in compliance with your chosen standards, you can then turn on enforcement in
  the tag policies to prevent non-compliant tags from being created. For more
  information, see [Tag policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") in the _AWS Organizations User Guide_.

## Tag naming best practices

These are several best practices and naming conventions that we recommend that you use
with your tags. Refer to [Naming tags](../../../IAM/latest/UserGuide/id_tags.md#id_tags_rules "../../../IAM/latest/UserGuide/id_tags.md#id_tags_rules")
in the _IAM User Guide_ for more information.

A number of tags are predefined by AWS or created automatically by various
AWS services. Many _AWS generated tags_ use key
names that are all lowercase, with hyphens separating words in the name, and prefixes
followed by colons to identify the source service for the tag. For example, see the
following:

- `aws:ec2spot:fleet-request-id` is a tag that identifies the Amazon EC2
  Spot Instance Request that launched the instance.
- `aws:cloudformation:stack-name` is a tag that identifies the AWS CloudFormation
  stack that created the resource.
- `elasticbeanstalk:environment-name` is a tag that identifies the
  application that created the resource.

Consider naming your tags using the following rules:

- Use all lowercase for the words.
- Use hyphens to separate words.
- Use a prefix followed by a colon to identify the organization name or
  abbreviated name.

For example, for a fictitious company named _AnyCompany_, you might
define tags such as:

- `anycompany:cost-center` to identify the internal Cost Center code.
- `anycompany:environment-type` to identify whether the environment
  is development, test, or production.
- `anycompany:application-id` to identify the application that the
  resource was created for.

The prefix ensures that tags are clearly recognizable as defined by your organization
and not by AWS or a third-party tool that you might be using. Using all lowercase with
hyphens for separators avoids confusion about how to capitalize a tag name. For example,
`anycompany:project-id` is simpler to remember than
`ANYCOMPANY:ProjectID`, `anycompany:projectID`, or
`Anycompany:ProjectId`.

### Tag naming limits and requirements

The following basic naming and usage requirements apply to tags:

- Each resource can have a maximum of 50 user created tags.
- System created tags that begin with `aws:` are reserved for AWS
  use, and do not count against this limit. You can't edit or delete a tag that
  begins with the `aws:` prefix.
- For each resource, each tag key must be unique, and each tag key can have only
  one value.
- The tag key must be a minimum of 1 and a maximum of 128 Unicode characters in
  UTF-8.
- The tag value must be a minimum of 0 and a maximum of 256 Unicode characters
  in UTF-8.
- Allowed characters can vary by AWS service. For information about what
  characters you can use to tag resources in a particular AWS service, see its
  documentation. In general, the allowed characters are letters, numbers, spaces
  representable in UTF-8, and the following characters: \_ . : / = + - @.
- Tag keys and values are case sensitive. As a best practice, decide on a
  strategy for capitalizing tags, and consistently implement that strategy across
  all resource types. For example, decide whether to use `Costcenter`,
  `costcenter`, or `CostCenter`, and use the same
  convention for all tags. Avoid using similar tags with inconsistent case
  treatment.

## Common tagging strategies

Use the following tagging strategies to help identify and manage AWS
resources.

###### Contents

- [Tags for resource organization](#tag-strategies-console "#tag-strategies-console")
- [Tags for cost allocation](#tag-strategies-cost-allocation "#tag-strategies-cost-allocation")
- [Tags for automation](#tag-strategies-automation "#tag-strategies-automation")
- [Tags for access control](#tag-strategies-access-control "#tag-strategies-access-control")
- [Tagging governance](#tag-strategies-governance "#tag-strategies-governance")

### Tags for resource organization

Tags are a good way to organize AWS resources in the AWS Management Console. You can
configure tags to be displayed with resources, and can search and filter by tag.
With the AWS Resource Groups service, you can create groups of AWS resources based on one or
more tags or portions of tags. You can also create groups based on their occurrence
in an AWS CloudFormation stack. Using Resource Groups and Tag Editor, you can consolidate and view data
for applications that consist of multiple services, resources, and Regions in one
place.

### Tags for cost allocation

AWS Cost Explorer and detailed billing reports let you break down AWS costs by
tag. Typically, you use business tags such as _cost
center/business unit_, _customer_, or
_project_ to associate AWS costs with
traditional cost-allocation dimensions. But a cost allocation report can include any
tag. This lets you associate costs with technical or security dimensions, such as
specific applications, environments, or compliance programs.

For some services, you can use an AWS-generated `createdBy` tag for
cost allocation purposes, to help account for resources that might otherwise go
uncategorized. The `createdBy` tag is available only for supported AWS
services and resources. Its value contains data associated with specific API or
console events. For more information, see [AWS-Generated Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/aws-tags.md "../../../awsaccountbilling/latest/aboutv2/aws-tags.md") in the _AWS Billing and Cost Management User
Guide_.

### Tags for automation

Resource or service-specific tags are often used to filter resources during
automation activities. Automation tags are used to opt in or opt out of automated
tasks or to identify specific versions of resources to archive, update, or delete.
For example, you can run automated `start` or `stop` scripts
that turn off development environments during nonbusiness hours to reduce costs. In
this scenario, Amazon Elastic Compute Cloud (Amazon EC2) instance tags are a simple way to identify
instances to opt out of this action. For scripts that find and delete stale,
out-of-date, or rolling Amazon EBS snapshots, snapshot tags can add an extra dimension of
search criteria.

### Tags for access control

IAM policies support tag-based conditions, letting you constrain IAM
permissions based on specific tags or tag values. For example, IAM user or role
permissions can include conditions to limit EC2 API calls to specific environments
(such as development, test, or production) based on their tags. The same strategy
can be used to limit API calls to specific Amazon Virtual Private Cloud (Amazon VPC) networks. Support for
tag-based, resource-level IAM permissions is service specific. When you use
tag-based conditions for access control, be sure to define and restrict who can
modify the tags. For more information about using tags to control API access to
AWS resources, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

### Tagging governance

An effective tagging strategy uses standardized tags and applies them consistently and
programmatically across AWS resources. You can use both reactive and proactive
approaches for governing tags in your AWS environment.

- **Reactive governance** is for finding resources
  that are not properly tagged using tools such as the Resource Groups Tagging
  API, AWS Config Rules, and custom scripts. To find resources manually, you can use Tag
  Editor and detailed billing reports.
- **Proactive governance** uses tools such as
  AWS CloudFormation, Service Catalog, tag policies in AWS Organizations, or IAM resource-level permissions to
  ensure standardized tags are consistently applied at resource creation.

For example, you can use the AWS CloudFormation `Resource Tags` property to
apply tags to resource types. In Service Catalog, you can add portfolio and product tags
that are combined and applied to a product automatically when it is launched.
More rigorous forms of proactive governance include automated tasks. For
example, you can use the Resource Groups Tagging API to search an AWS
environment’s tags, or run scripts to quarantine or delete improperly tagged
resources.
