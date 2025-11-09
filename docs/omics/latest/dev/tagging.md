# Tagging resources in HealthOmics

###### Topics

- [Important notice](#important-notice-tagging "#important-notice-tagging")
- [Tagging HealthOmics resources](#tagging-using-Omics "#tagging-using-Omics")
- [Sequence store read set tags](#sequence-store-read-tags "#sequence-store-read-tags")
- [Adding a tag to a HealthOmics resource](add-a-tag.md "add-a-tag.md")
- [Listing tags for a resource](list-tags.md "list-tags.md")
- [Removing tags from a data store](remove-tags.md "remove-tags.md")

## Important notice

HealthOmics protects customer data under the AWS Shared Responsibility Model
policies. This means that all customer data is encrypted both in transition and at-rest.
However, not all customer-inputed names for resources such as data stores or job-based
operations are encrypted. They should never contain Personally Identifiable Information
or Protected Health Information. For more information, see [Security in AWS HealthOmics](security.md "security.md").

## Tagging HealthOmics resources

You can assign metadata to your AWS resources using _tags_. Each
tag is a label consisting of a user-defined key and value. Tags can help you manage,
identify, organize, search for, and filter resources.

This topic describes commonly used tagging categories and strategies to help you
implement a consistent and effective tagging strategy. The following sections assume
basic knowledge of AWS resources, tagging, detailed billing, and AWS Identity and Access Management.

Each tag has two parts:

- A _tag key_ (for example, CostCenter, Environment, or
  Project). Tag keys are case sensitive.
- A _tag value_ (for example, 111122223333 or Production).
  Like tag keys, tag values are case sensitive.

You can use tags to categorize resources by purpose, owner, environment, or other
criteria. For more information, see [AWS
Tagging Strategies](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf").

You can add, change, or remove tags for a resource from the resource’s
service console, service API, or the AWS CLI.

To enable tagging, make sure TagResources is authorized. You can authorize
TagResources by attaching an IAM policy like the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "omics:Create*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "omics:Start*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "omics:Tag*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "omics:Untag*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "omics:List*",
 "Resource": "*"
 }
 ]
}`

```

### Best practices

As you create a tagging strategy for AWS resources, follow best practices:

- Do not store Personally Identifiable Information (PII), Protected Health
  Information(PHI) or other sensitive information in tags.
- Use a standardized, case-sensitive format for tags, and apply it consistently
  across all resource types.
- Consider tag guidelines that support multiple purposes, like managing resource
  access control, cost tracking, automation, and organization.
- Use automated tools to help manage resource tags. [AWS
  Resource Groups](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md") and the [Resource Groups Tagging API](../../../resourcegroupstagging/latest/APIReference/overview.md "../../../resourcegroupstagging/latest/APIReference/overview.md") enable programmatic control of tags,
  making it possible to automatically manage, search, and filter tags and
  resources.
- Tagging is more effective when you use more tags.
- Tags can be edited or modified as user needs change. However to update access
  control tags, you must also update the policies that reference those tags to
  control access to your resources.

### Tagging requirements

Tags have the following requirements:

- Keys can't be prefixed with aws:.
- Keys must be unique per tag set.
- A key must be between 1 and 128 allowed characters.
- A value must be between 0 and 256 allowed characters.
- Values don't need to be unique per tag set.
- Allowed characters for keys and values are Unicode letters, digits, white
  space, and any of the following symbols: \_ . : / = + - @.
- Keys and values are case sensitive.

## Sequence store read set tags

For sequence stores, tags created on the read set sit at the read set resource level. Read sets also contain
objects under them that can be accessed, searched, and restricted using S3 APIs. By default, the sample ID
(omics:sampleId) and subject ID (omics:subjectId) are added to the object.

Additionally, up to five tags can be synchronized between the read set and the objects under it. The
configuration for which tags to sync is a store level configuration set during store creation or update using the
`propogatedSetLevelTags` parameter.

If there is data already in the store, updating the keys may take time. During this update, HealthOmics changes the
store status to **Updating**. On completion, HealthOmics sets the store status to
**Active**. While the tags are propagating, permissions relying on the tags may not be enforced.
Permissions will be enforced after the tag propagation is completed.

When tags are set or updated on the read set, the system decides whether to update the objects for that read
set, based on the store configuration.
