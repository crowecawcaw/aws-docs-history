# Tagging fundamentals for Macie resources

To identify, categorize, and manage Amazon Macie resources for your account, you can
assign tags to the resources. A _tag_ is a label that
you define and assign to AWS resources, including certain types of Macie resources.
Each tag consists of a required _tag key_ and an
optional _tag value_. A _tag
key_ is a general label that acts as a category for a more specific tag
value. A _tag value_ acts as a descriptor for a tag
key. A resource can have as many as 50 tags.

You can assign tags to the following types of Macie resources:

- Allow lists
- Custom data identifiers
- Filter rules and suppression rules for findings
- Sensitive data discovery jobs
  If you're the Macie administrator for an organization, you can also assign tags to member
  accounts in your organization.

By assigning tags to Macie resources, you can identify and manage the resources in
different ways, such as by purpose, owner, environment, or other criteria. This can help
you perform tasks such as apply policies, allocate costs, distinguish between resources,
or identify resources that support certain compliance requirements or workflows. For
example, if you create custom data identifiers and sensitive data discovery jobs to
analyze data at different points in a workflow (one set for staged data and another for
production data), you might assign a `Stack` tag key to those resources. The
tag value for this tag key might be `Staging` for custom data identifiers and
jobs that analyze staged data, and `Production` for the others.

As you define and assign tags to Macie resources, keep the following in mind:

- Each resource can have a maximum of 50 tags.
- For each resource, each tag key must be unique and it can have only one tag
  value.
- Tag keys and values are case sensitive. As a best practice, we recommend that
  you define a strategy for capitalizing tags and implement that strategy
  consistently across your resources.
- A tag key can have a maximum of 128 UTF-8 characters. A tag value can have a
  maximum of 256 UTF-8 characters. The characters can be letters, numbers, spaces,
  or the following symbols: \_ . : / = + - @
- The `aws:` prefix is reserved for use by AWS. You can’t use it in
  any tag keys or values that you define. In addition, you can't change or remove
  tag keys or values that use this prefix. Tags that use this prefix don’t count
  against the quota of 50 tags for a resource.
- Any tags that you assign are available only for your AWS account and only in
  the AWS Region in which you assign them.
- If you delete a resource, any tags that are assigned to the resource are also
  deleted.
  For additional restrictions, tips, and best practices, see the [Tagging AWS
  Resources User Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Important

Do not store confidential or other types of sensitive data in tags. Tags are
accessible from many AWS services, including AWS Billing and Cost Management. They aren't intended to be
used for sensitive data.

To add and manage tags for Macie resources, you can use Macie or AWS Resource Groups. AWS Resource Groups
is a service that's designed to help you group and manage AWS resources as a single
unit instead of individually. If you use Macie, you can add tags to a resource when you
create the resource. You can also add and manage tags for individual existing resources.
If you use AWS Resource Groups, you can add and manage tags in bulk for multiple existing
resources spanning multiple AWS services, including Macie. For more information, see
the [Tagging
AWS Resources User Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").
