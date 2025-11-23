# Adding tags to Macie resources

A *tag* is a label that you can define and assign to
AWS resources, including certain types of Amazon Macie resources. By using tags, you can
identify, categorize, and manage resources in different ways, such as by purpose, owner,
environment, or other criteria. For example, you can use tags to: apply policies,
allocate costs, distinguish between versions of resources, or identify resources that
support certain compliance requirements or workflows.

You can add tags to the following types of Macie resources:

- Allow lists
- Custom data identifiers
- Filter rules and suppression rules for findings
- Sensitive data discovery jobs
  If you're the Macie administrator for an organization, you can also add tags to member
  accounts in your organization.

A resource can have as many as 50 tags. Each tag consists of a required _tag key_ and an optional _tag
value_. A _tag key_ is a general label
that acts as a category for a more specific tag value. A _tag
value_ acts as a descriptor for a tag key. For more information about
tagging options and requirements, see [Tagging fundamentals](tags-basics.md "tags-basics.md").

You can add tags to Macie resources in several ways. You can use Macie directly. You
can also use the Tag Editor on the AWS Resource Groups console or tagging operations of the
AWS Resource Groups Tagging API. AWS Resource Groups is a service that's designed to help you group and
manage AWS resources as a single unit instead of individually. If you use Macie, you
can add tags to a resource when you create the resource. You can also add tags to
individual existing resources. With AWS Resource Groups, you can add tags in bulk for multiple
existing resources spanning multiple AWS services, including Macie.

###### To add tags to a Macie resource

To add tags to an individual Macie resource, you can use the Amazon Macie console or
the Amazon Macie API. To add tags to multiple Macie resources at the same time, use the
AWS Resource Groups console or the AWS Resource Groups Tagging API. For more information, see the [Tagging
AWS Resources User Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Important

Adding tags to a resource can affect access to the resource. Before you add a tag
to a resource, review any AWS Identity and Access Management (IAM) policies that might use tags to control
access to resources. For more information, see [Controlling access to AWS
resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.

Console
When you create an allow list, custom data identifier, or sensitive data
discovery job, the Amazon Macie console provides options for adding tags to the
resource. Follow the instructions on the console to add tags to these types
of resources when you create the resources. To add tags to a filter rule,
suppression rule, or member account, you have to create the resource before
you can add tags to it.

To add one or more tags to an existing resource by using the Amazon Macie
console, follow these steps.

###### To add a tag to a resource

1.  Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2.  Depending on the type of resource that you want to add a tag to,
    do one of the following:

        * For an allow list, choose **Allow lists** in
         the navigation pane. In the table, select the checkbox for the list. Then choose
         **Manage tags** on the
         **Actions** menu.
        * For a custom data identifier, choose **Custom data identifiers** in
         the navigation pane. In the table, select the checkbox for the custom data identifier. Then choose
         **Manage tags** on the
         **Actions** menu.
        * For a filter or suppression rule, choose **Findings** in the
         navigation pane. In the **Saved rules** list, choose the edit icon
         (
        ![The edit icon, which is a blue pencil.](/images/macie/latest/user/images/icon-edit-resource-blue.png)
        ) next to the rule. Then choose
         **Manage tags**.
        * For a member account in your organization, choose **Accounts** in
         the navigation pane. In the table, select the checkbox for the account. Then choose
         **Manage tags** on the
         **Actions** menu.
        * For a sensitive data discovery job, choose **Jobs** in the
         navigation pane. In the table, select the checkbox for the job. Then choose **Manage
         tags** on the **Actions** menu.

    The **Manage tags** window lists all the tags
    that are currently assigned to the resource.

3.  In the **Manage tags** window, choose
    **Edit tags**.
4.  Choose **Add tag**.
5.  In the **Key** box, enter the tag key for the tag
    to add to the resource. Then, in the **Value** box,
    optionally enter a tag value for the key.

A tag key can contain as many as 128 characters. A tag value can
contain as many as 256 characters. The characters can be letters,
numbers, spaces, or the following symbols: \_ . : / = + - @ 6. To add another tag to the resource, choose **Add
tag**, and then repeat the preceding step. You can
assign as many as 50 tags to a resource. 7. When you finish adding tags, choose
**Save**.

API
To create a resource and add one or more tags to it programmatically, use
the appropriate `Create` operation for the type of resource that
you want to create:

- **Allow list** – Use the
  [CreateAllowList](../APIReference/allow-lists.md "../APIReference/allow-lists.md") operation. Or, if you're using the
  AWS Command Line Interface (AWS CLI), run the [create-allow-list](../../../cli/latest/reference/macie2/create-allow-list.md "../../../cli/latest/reference/macie2/create-allow-list.md") command.
- **Custom data identifier** –
  Use the [CreateCustomDataIdentifier](../APIReference/custom-data-identifiers.md "../APIReference/custom-data-identifiers.md") operation. Or, if you're
  using the AWS CLI, run the [create-custom-data-identifier](../../../cli/latest/reference/macie2/create-custom-data-identifier.md "../../../cli/latest/reference/macie2/create-custom-data-identifier.md") command.
- **Filter or suppression rule**
  – Use the [CreateFindingsFilter](../APIReference/findingsfilters.md "../APIReference/findingsfilters.md") operation. Or, if you're using the
  AWS CLI, run the [create-findings-filter](../../../cli/latest/reference/macie2/create-findings-filter.md "../../../cli/latest/reference/macie2/create-findings-filter.md") command.
- **Member account** – Use the
  [CreateMember](../APIReference/members.md "../APIReference/members.md") operation. Or, if you're using the AWS CLI,
  run the [create-member](../../../cli/latest/reference/macie2/create-member.md "../../../cli/latest/reference/macie2/create-member.md") command.
- **Sensitive data discovery job**
  – Use the [CreateClassificationJob](../APIReference/jobs.md "../APIReference/jobs.md") operation. Or, if you're using
  the AWS CLI, run the [create-classification-job](../../../cli/latest/reference/macie2/create-classification-job.md "../../../cli/latest/reference/macie2/create-classification-job.md") command.

In your request, use the `tags` parameter to specify the tag
key (`key`) and optional tag value (`value`) for each
tag to add to the resource. The `tags` parameter specifies a
string-to-string map of tag keys and their associated tag values.

To add one or more tags to an existing resource, use the [TagResource](../APIReference/tags-resourcearn.md "../APIReference/tags-resourcearn.md") operation of the Amazon Macie API or, if you're using
the AWS CLI, run the [tag-resource](../../../cli/latest/reference/macie2/tag-resource.md "../../../cli/latest/reference/macie2/tag-resource.md")
command. In your request, specify the Amazon Resource Name (ARN) of the
resource that you want to add a tag to. Use the `tags` parameter
to specify the tag key (`key`) and optional tag value
(`value`) for each tag to add to the resource. As is the case
for `Create` operations and commands, the `tags`
parameter specifies a string-to-string map of tag keys and their associated
tag values.

For example, the following AWS CLI command adds a `Stack` tag key
with a `Production` tag value to the specified job.
This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 tag-resource ^
--resource-arn `arn:aws:macie2:us-east-1:123456789012:classification-job/3ce05dbb7ec5505def334104bexample` ^
--tags={\"`Stack`\":\"`Production`\"}`
```

Where:

- `resource-arn` specifies the ARN of the job to add a
  tag to.
- `Stack` is the tag key of
  the tag to add to the job.
- `Production` is the tag
  value for the specified tag key
  (`Stack`).

In the following example, the command adds several tags to the job:

```
`C:\>` `aws macie2 tag-resource ^
--resource-arn `arn:aws:macie2:us-east-1:123456789012:classification-job/3ce05dbb7ec5505def334104bexample` ^
--tags={\"`Stack`\":\"`Production`\",\"`CostCenter`\":\"`12345`\",\"`Owner`\":\"`jane-doe`\"}`
```

For each tag in a `tags` map, both the `key` and
`value` arguments are required. However, the value for the
`value` argument can be an empty string. If you don’t want to
associate a tag value with a tag key, don't specify a value for the
`value` argument. For example, the following AWS CLI command
adds an `Owner` tag key with no associated tag value:

```
`C:\>` `aws macie2 tag-resource ^
--resource-arn `arn:aws:macie2:us-east-1:123456789012:classification-job/3ce05dbb7ec5505def334104bexample` ^
--tags={\"`Owner`\":\"\"}`
```

If a tagging operation succeeds, Macie returns an empty HTTP 204 response.
Otherwise, Macie returns an HTTP 4*xx* or
500 response that indicates why the operation failed.
