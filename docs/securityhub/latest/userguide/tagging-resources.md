# Tagging

Security Hub
resources

A _tag_ is an optional label that you can define and assign
to AWS resources, including certain types of AWS Security Hub CSPM resources. Tags can help you
identify, categorize, and manage resources in different ways, such as by purpose, owner,
environment, or other criteria. For example, you can use tags to distinguish between resources,
identify resources that support certain compliance requirements or workflows, or allocate
costs.

You can add tags to the following types of Security Hub CSPM resources:

- Automation rules
- Configuration policies
- `Hub` resource

## Tagging fundamentals

A resource can have as many as 50 tags. Each tag consists of a required _tag key_ and an optional _tag
value_, both of which you define. A _tag
key_ is a general label that acts as a category for a more specific tag
value. A _tag value_ acts as a descriptor for a tag
key.

For example, if you create different automation rules for different environments
(one set of automation rules for test accounts and another for production accounts), you might
assign an `Environment` tag key to those rules. The associated tag
value might be `Test` for the rules that are associated with test accounts,
and `Prod` for the rules that are associated with production accounts and OUs.

As you define and assign tags to AWS Security Hub CSPM resources, keep the following in mind:

- Each resource can have a maximum of 50 tags.
- For each resource, each tag key must be unique and it can have only one tag
  value.
- Tag keys and values are case sensitive. As a best practice, we recommend that
  you define a strategy for capitalizing tags and implement that strategy
  consistently across your resources.
- A tag key can have a maximum of 128 UTF-8 characters. A tag value can have a maximum of
  256 UTF-8 characters. The characters can be letters, numbers, spaces, or the
  following symbols: \_ . : / = + - @
- The `aws:` prefix is reserved for use by AWS. You can’t use it in
  any tag keys or values that you define. In addition, you can't change or remove
  tag keys or values that use this prefix. Tags that use this prefix don’t count
  against the quota of 50 tags per resource.
- Any tags that you assign are available only for your AWS account and only in the
  AWS Region in which you assign them.
- If you assign tags to a resource by using Security Hub CSPM, the tags are applied only to the
  resource that's stored directly in Security Hub CSPM in the applicable AWS Region.
  They aren't applied to any associated, supporting resources that Security Hub CSPM
  creates, uses, or maintains for you in other AWS services. For example, if you assign tags to an
  automation rule that updates findings related to Amazon Simple Storage Service (Amazon S3), the tags are applied only to your automation rule in Security Hub CSPM for
  the specified Region. They aren't applied to your S3 buckets. To also assign tags
  to an associated resource, you can use AWS Resource Groups or the AWS service that
  stores the resource—for example, Amazon S3 for an S3 bucket. Assigning tags to
  associated resources can help you identify supporting resources for your Security Hub CSPM resources.
- If you delete a resource, any tags that are assigned to the resource are also
  deleted.

###### Important

Do not store confidential or other types of sensitive data in tags. Tags are
accessible from many AWS services, including AWS Billing and Cost Management. They aren't intended to be
used for sensitive data.

To add and manage tags for Security Hub CSPM resources, you can use the Security Hub CSPM console, the Security Hub CSPM
API, or the AWS Resource Groups Tagging API. With Security Hub CSPM,
you can add tags to a resource when you create the resource. You can also add and manage
tags for individual existing resources. With Resource Groups, you can add and manage tags in bulk
for multiple existing resources spanning multiple AWS services, including Security Hub CSPM.

For additional tagging tips and best practices, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md")
in the _Tagging AWS Resources User Guide_.

## Using tags in IAM policies

After you start tagging resources, you can define tag-based, resource-level permissions in
AWS Identity and Access Management (IAM) policies. By using tags in this way, you can implement granular
control of which users and roles in your AWS account have permission to create and tag
resources, and which users and roles have permission to add, edit, and remove tags more
generally. To control access based on tags, you can use [tag-related condition keys](../../../service-authorization/latest/reference/list_awssecurityhub.md#awssecurityhub-policy-keys "../../../service-authorization/latest/reference/list_awssecurityhub.md#awssecurityhub-policy-keys") in the [Condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of IAM policies.

For example, you can create an IAM policy that allows a user to have full access to all
AWS Security Hub CSPM resources, if the `Owner` tag for the resource specifies their
username:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ModifyResourceIfOwner",
 "Effect": "Allow",
 "Action": "securityhub:*",
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

If you define tag-based, resource-level permissions, the permissions take effect
immediately. This means that your resources are more secure as soon as they're created,
and you can quickly start enforcing the use of tags for new resources. You can also use
resource-level permissions to control which tag keys and values can be associated with
new and existing resources. For more information, see [Controlling access to AWS resources
using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.
