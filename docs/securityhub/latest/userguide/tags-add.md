# Adding tags to Security Hub CSPM resources

A _tag_ is a label that you can define and assign to
AWS resources, including certain types of AWS Security Hub CSPM resources. By using tags, you can
identify, categorize, and manage resources in different ways, such as by purpose, owner,
environment, or other criteria. For example, you can use tags to: apply policies,
allocate costs, distinguish between versions of resources, or identify resources that
support certain compliance requirements or workflows.

You can add tags to the following types of Security Hub CSPM resources:

- Automation rules
- Configuration policies
- `Hub` resource
  A resource can have as many as 50 tags. Each tag consists of a required _tag key_ and an optional _tag
  value_. A _tag key_ is a general label
  that acts as a category for a more specific tag value. A _tag
  value_ acts as a descriptor for a tag key. For more information about
  tagging options and requirements, see [Tagging fundamentals](tagging-resources.md#tags-basics "tagging-resources.md#tags-basics").

To add tags to a Security Hub CSPM
resource, you can use the Security Hub CSPM console or the Security Hub CSPM
API. However, the console doesn't support adding tags to the `Hub` resource.

After adding tags, you can edit the tag and change the tag key or tag value.

To add or edit tags for multiple Security Hub CSPM
resources at the same time, use the tagging operations of the [AWS Resource Groups Tagging
API](../../../resourcegroupstagging/latest/APIReference/overview.md "../../../resourcegroupstagging/latest/APIReference/overview.md").

###### Important

Adding tags to a resource can affect access to the resource. Before you add a tag
to a resource, review any AWS Identity and Access Management (IAM) policies that might use tags to control
access to resources.

Console
**To add tags to a Security Hub CSPM resource (console)**

When you create an automation rule or a configuration policy, the Security Hub CSPM
console provides options for adding tags to it. You can provide the tag key
and tag value in the **Tags** section.

Security Hub CSPM API
**To add tags to a Security Hub CSPM resource (API)**

To create a resource and add one or more tags to it programmatically, use the appropriate operation for
the type of resource that you want to create:

- To create a configuration policy and add one or more tags to it, invoke the [CreateConfigurationPolicy](../../1.0/APIReference/API_CreateConfigurationPolicy.md "../../1.0/APIReference/API_CreateConfigurationPolicy.md") API or, if you're using the
  AWS CLI, run the [create-configuration-policy](../../../cli/latest/reference/securityhub/create-configuration-policy.md "../../../cli/latest/reference/securityhub/create-configuration-policy.md") command.
- To create an automation rule and add one or more tags to it, invoke the [CreateAutomationRule](../../1.0/APIReference/API_CreateAutomationRule.md "../../1.0/APIReference/API_CreateAutomationRule.md") API or, if you're using the
  AWS CLI, run the [create-automation-rule](../../../cli/latest/reference/securityhub/create-automation-rule.md "../../../cli/latest/reference/securityhub/create-automation-rule.md") command.
- To enable Security Hub CSPM and add one or more tags to your `Hub` resource, invoke the [EnableSecurityHub](../../1.0/APIReference/API_EnableSecurityHub.md "../../1.0/APIReference/API_EnableSecurityHub.md") API or, if you're using the
  AWS Command Line Interface (AWS CLI), run the [enable-security-hub](../../../cli/latest/reference/securityhub/enable-security-hub.md "../../../cli/latest/reference/securityhub/enable-security-hub.md") command.

In your request, use the `tags` parameter to specify the tag key
and optional tag value for each
tag to add to the resource. The `tags` parameter specifies an
array of objects. Each object specifies a tag key and its associated tag
value.

To add one or more tags to an existing resource, use the [TagResource](../../1.0/APIReference/API_TagResource.md "../../1.0/APIReference/API_TagResource.md") operation of the Security Hub CSPM API or, if you're using
the AWS CLI, run the [tag-resource](../../../cli/latest/reference/securityhub/tag-resource.md "../../../cli/latest/reference/securityhub/tag-resource.md") command. In your request, specify the Amazon
Resource Name (ARN) of the resource that you want to add a tag to. Use the
`tags` parameter to specify the tag key (`key`)
and optional tag value (`value`) for each tag to add. The `tags`
parameter specifies an array of objects, one object for each tag key and its
associated tag value.

For example, the following AWS CLI command adds an `Environment` tag key with a
`Prod` tag value to the specified configuration policy. This example
is formatted for Linux, macOS, or Unix, and it uses the backslash (\)
line-continuation character to improve readability.

**Example CLI command:**

```
`$` `aws securityhub tag-resource \
--resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
--tags '{"`Environment`":"`Prod`"}'`
```

Where:

- `resource-arn` specifies the ARN of the configuration policy to
  add a tag to.
- `Environment` is the tag key
  of the tag to add to the rule.
- `Prod` is the tag value for
  the specified tag key (`Environment`).

In the following example, the command adds several tags to the configuration policy.

```
`$` `aws securityhub tag-resource \
--resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
--tags '{"`Environment`":"`Prod`", "`CostCenter`":"`12345`", "`Owner`":"`jane-doe`"}'`
```

For each object in a `tags` array, both the `key` and
`value` arguments are required. However, the value for the
`value` argument can be an empty string. If you don’t want to
associate a tag value with a tag key, don't specify a value for the
`value` argument. For example, the following command adds an
`Owner` tag key with no associated tag value:

```
`$` `aws securityhub tag-resource \
--resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
--tags '{"`Owner`":""}'`
```

If a tagging operation succeeds, Security Hub CSPM returns an empty HTTP 200 response. Otherwise,
Security Hub CSPM returns an HTTP 4*xx* or 500
response that indicates why the operation failed.
