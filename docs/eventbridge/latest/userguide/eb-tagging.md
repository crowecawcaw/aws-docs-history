# Tagging resources in Amazon EventBridge

A _tag_ is a custom attribute label that you or AWS assigns to an
AWS resource. In EventBridge, you can assign tags to [rule](eb-rules.md "eb-rules.md") and
[event buses](eb-event-bus.md "eb-event-bus.md"). Each resource can have a
maximum of 50 tags.

You use tags to identify and organize your AWS resources. Many AWS services support
tagging, so you can assign the same tag to resources from different services to indicate
that the resources are related. For example, you could assign the same tag to an EventBridge rule
that you assign to an EC2 instance.

A tag has two parts:

- A _tag key_, for example, `CostCenter`,
  `Environment`, or `Project`.
  - Tag keys are case sensitive.
  - The maximum tag key length is 128 Unicode characters in UTF-8.
  - For each resource, each tag key must be unique.
  - Allowed characters are letters, numbers, spaces representable in UTF-8,
    and the following characters: **_. : + = @ \_ / - (hyphen)_**.
  - The `aws:` prefix is prohibited for tags because it's reserved
    for AWS use. You can't edit or delete tag keys or values with this prefix.
    Tags with this prefix don't count against your tags per resource
    limit.

- An optional _tag value_ field, for example,
  `111122223333` or `Production`.
  - Each tag key can have only one value.
  - Tag values are case sensitive.
  - Omitting the tag value is the same as using an empty string.
  - The maximum tag value length is 256 Unicode characters in UTF-8.

  - Allowed characters are letters, numbers, spaces representable in UTF-8,
    and the following characters: **_. : + = @ \_ / - (hyphen)_**.

###### Tip

As a best practice, decide on a strategy for capitalizing tags and consistently
implement that strategy across all resource types. For example, decide whether to use
`Costcenter`, `costcenter`, or `CostCenter` and
then use the same convention for all tags.

For more information on managing tags, see [Working with Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") in the
_Resource Groups User Guide_.

## Adding or removing tags on event

buses

You can add or remove tags on event buses.

###### To add or remove tags on an event bus (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Event buses**.
3. Choose the event bus you want to update.
4. On the events bus details page, choose the **Tags** tab,
   and then choose **Manage tags**.
5. Do one of the following:
   - To add a tag:
     1. Choose **Add new tag**.
     2. Specify the key and value for the tag
     3. Choose **Update**.

   - To remove a tag:
     1. For the tag you want to remove, choose
        **Remove**.
     2. Choose **Update**.

###### To add or remove tags from an event bus (AWS CLI)

- To add tags, use [tag-resource](../../../cli/latest/reference/events/tag-resource.md "../../../cli/latest/reference/events/tag-resource.md").

To remove tags, use [untag-resource](../../../cli/latest/reference/events/untag-resource.md "../../../cli/latest/reference/events/untag-resource.md").

You can also determine the tags on an event bus by using [list-tags-for-resource](../../../cli/latest/reference/events/list-tags-for-resource.md "../../../cli/latest/reference/events/list-tags-for-resource.md").
