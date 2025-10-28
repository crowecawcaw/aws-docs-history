# Reviewing tags for Security Hub CSPM resources

After you add or edit tags for AWS Security Hub CSPM resources, you can view what tag keys and tag values a resource currently has.
A _tag_ is a label that you define and assign to one or more AWS
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
  You can review the tags for a Security Hub CSPM automation rule or configuration policy by
  using the Security Hub CSPM console or the Security Hub CSPM API. The console doesn't support reviewing tags for the `Hub` resource.
  Programmatically, you can review tags for any resource.

To review tags for multiple Security Hub CSPM
resources at the same time, use the tagging operations of the [AWS Resource Groups Tagging
API](../../../resourcegroupstagging/latest/APIReference/overview.md "../../../resourcegroupstagging/latest/APIReference/overview.md").

Console

###### To review tags for a Security Hub CSPM resource (console)

1. Using the credentials of the Security Hub CSPM administrator, open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. Depending on the type of resource that you want to add a tag to, do one of the following:
   - To review the tags for an automation rule, choose **Automations** in the navigation pane.
     Then, choose an automation rule.
   - To review the tags for a configuration policy, choose **Configuration** in the navigation pane.
     Then, on the **Policies** tab, select the option next to a configuration policy. A side panel opens that
     shows you the number of tags assigned to the policy. You can expand the **Tags** header to see the tag keys and tag values.

The **Tags** section lists all the tags that are currently assigned to the resource.

Security Hub CSPM API
**To review tags for a Security Hub CSPM resource (API)**

To retrieve and review the tags for an existing resource, invoke the [ListTagsForResource](../../1.0/APIReference/API_ListTagsForResource.md "../../1.0/APIReference/API_ListTagsForResource.md") API. In your
request, use the `resourceArn` parameter to specify the Amazon
Resource Name (ARN) of the resource.

If you're using the AWS CLI, run the [list-tags-for-resource](../../../cli/latest/reference/securityhub/list-tags-for-resource.md "../../../cli/latest/reference/securityhub/list-tags-for-resource.md") command and use the
`resource-arn` parameter to specify the ARN of the resource.
For example:

```
`$` `aws securityhub list-tags-for-resource --resource-arn `arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``
```

If the operation succeeds, Security Hub CSPM returns a `tags` array. Each object in
the array specifies a tag (both the tag key and tag value) that's currently
assigned to the resource. For example:

```
`{
 "tags": [
 {
 "key": "Environment",
 "value": "Prod"
 },
 {
 "key": "CostCenter",
 "value": "12345"
 },
 {
 "key": "Owner",
 "value": ""
 }
 ]
}`
```

Where `Environment`, `CostCenter`, and
`Owner` are the tag keys that are assigned to the resource.
`Prod` is the tag value that's associated with the
`Environment` tag key. `12345` is the tag value
that's associated with the `CostCenter` tag key. The
`Owner` tag key doesn't have an associated tag value.

To retrieve a list of all the Security Hub CSPM resources that have tags and all
the tags that are assigned to each of those resources, use the [GetResources](../../../resourcegroupstagging/latest/APIReference/API_GetResources.md "../../../resourcegroupstagging/latest/APIReference/API_GetResources.md") operation of the AWS Resource Groups Tagging API. In your
request, set the value for the `ResourceTypeFilters` parameter to
`securityhub`. To do this using the AWS CLI, run the [get-resources](../../../cli/latest/reference/resourcegroupstaggingapi/get-resources.md "../../../cli/latest/reference/resourcegroupstaggingapi/get-resources.md") command and set the value for the
`resource-type-filters` parameter to
`securityhub`. For example:

```
`$` `aws resourcegroupstaggingapi get-resources -\-resource-type-filters "securityhub"`
```

If the operation succeeds, Resource Groups returns a `ResourceTagMappingList` array. The
array contains one object for each Security Hub CSPM resource that has tags. Each
object specifies the ARN of a Security Hub CSPM resource, and the tag keys and
values that are assigned to the resource.
