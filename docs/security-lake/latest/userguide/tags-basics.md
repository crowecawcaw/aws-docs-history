# Tagging fundamentals

A resource can have as many as 50 tags. Each tag consists of a required _tag key_ and an optional _tag
value_, both of which you define. A _tag
key_ is a general label that acts as a category for a more specific tag
value. A _tag value_ acts as a descriptor for a tag
key.

For example, if you add subscribers to analyze security data from different environments
(one set of subscribers for cloud data and another set for on-premises data), you might
assign an `Environment` tag key to those subscribers. The associated tag
value might be `Cloud` for subscribers that analyze data from AWS services,
and `On-Premises` for the others.

As you define and assign tags to Amazon Security Lake resources, keep the following in mind:

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
- If you assign tags to a resource by using Security Lake, the tags are applied only to the
  resource that's stored directly in Security Lake in the applicable AWS Region.
  They aren't applied to any associated, supporting resources that Security Lake
  creates, uses, or maintains for you in other AWS services. For example, if you
  assign tags to your data lake, the tags are applied only to your data lake
  configuration in Security Lake for the specified Region. They aren't applied to the
  Amazon Simple Storage Service (Amazon S3) bucket that stores your log and event data. To also assign tags
  to an associated resource, you can use AWS Resource Groups or the AWS service that
  stores the resource—for example, Amazon S3 for an S3 bucket. Assigning tags to
  associated resources can help you identify supporting resources for your data
  lake.
- If you delete a resource, any tags that are assigned to the resource are also
  deleted.
  For additional restrictions, tips, and best practices, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md")
  in the _Tagging AWS Resources User Guide_.

###### Important

Do not store confidential or other types of sensitive data in tags. Tags are
accessible from many AWS services, including AWS Billing and Cost Management. They aren't intended to be
used for sensitive data.

To add and manage tags for Security Lake resources, you can use the Security Lake console or the
Security Lake API.
