# Editing tags for Security Hub CSPM resources

As your environment or requirements change over time, you can evaluate existing tags
for your AWS Security Hub CSPM resources and change the tags as necessary. A _tag_ is a label that you define and assign to one or more AWS
resources, including certain types of Macie resources. Each tag consists of a required
_tag key_ and an optional _tag value_. A _tag key_ is a general
label that acts as a category for a more specific tag value. A _tag value_ acts as a descriptor for a tag key.

Tags can help you identify, categorize, and manage resources in different ways, such
as by purpose, owner, environment, or other criteria. For example, you can use tags to:
apply policies, allocate costs, distinguish between versions of resources, or identify
resources that support certain compliance requirements or workflows.

You can add tags to the following types of Security Hub CSPM resources:

- Automation rules
- Configuration policies
- `Hub` resource
  To edit tag keys or tag values for a Security Hub CSPM resource, you can use the
  Security Hub CSPM API. The Security Hub CSPM console currently doesn't support tag editing.

###### Important

Editing tags for a resource can affect access to the resource. Before you edit a tag
for a resource, review any AWS Identity and Access Management (IAM) policies that might use tags to control
access to resources.

Security Hub CSPM API
**To edit tags for a Security Hub CSPM resource (API)**

When you edit a tag for a resource programmatically, you overwrite the
existing tag with new values. Therefore, the best way to edit a tag depends
on whether you want to edit a tag key, a tag value, or both. To edit a tag
key, [remove the current tag](tags-remove.md "tags-remove.md") and [add a new tag](tags-add.md "tags-add.md").

To edit or remove only the tag value that's associated with a tag key, overwrite the
existing value by using the [TagResource](../../1.0/APIReference/API_TagResource.md "../../1.0/APIReference/API_TagResource.md") operation of the Security Hub CSPM API. If you're using the
AWS CLI, run the [tag-resource](../../../cli/latest/reference/securityhub/tag-resource.md "../../../cli/latest/reference/securityhub/tag-resource.md") command. In your request, specify the Amazon
Resource Name (ARN) of the resource whose tag value you want to edit or
remove.

To edit a tag value, use the `tags` parameter to specify the tag key whose tag
value you want to change. You should also specify the new tag value for the key. For
example, the following AWS CLI command changes the tag value from
`Prod` to `Test` for the
`Environment` tag key that's assigned to the specified
automation rule. This example is formatted for Linux, macOS, or Unix, and it uses
the backslash (\) line-continuation character to improve readability.

```
`$` `aws securityhub tag-resource \
--resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
--tags '{"`Environment`":"`Test`"}'`
```

Where:

- `resource-arn` specifies the ARN of the configuration policy.
- `Environment` is the tag key
  that's associated with the tag value to change.
- `Test` is the new tag
  value for the specified tag key (`Environment`).

To remove a tag value from a tag key, don’t specify a value for the `value`
argument of the key in the `tags` parameter. For example:

```
`$` `aws securityhub tag-resource \
--resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
--tags '{"`Owner`":""}'`
```

If the operation succeeds, Security Hub CSPM returns an empty HTTP 200 response. Otherwise,
Security Hub CSPM returns an HTTP 4*xx* or 500
response that indicates why the operation failed.
