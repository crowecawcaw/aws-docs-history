# Removing tags from Macie resources

If you add tags to an Amazon Macie resource, you can subsequently remove one or more of
them. A *tag* is a label that you define and assign to
AWS resources, including certain types of Macie resources. You can add, edit, and
remove tags from the following types of Macie resources: allow lists, custom data
identifiers, filter rules and suppression rules for findings, member accounts in an
organization, and sensitive data discovery jobs.

You can remove tags from a Macie resource by using Macie or AWS Resource Groups. AWS Resource Groups is a
service that's designed to help you group and manage AWS resources as a single unit
instead of individually. If you use Macie, you can remove tags from one resource at a
time. With AWS Resource Groups, you can remove tags in bulk for multiple existing resources
spanning multiple AWS services, including Macie.

###### To remove tags from a Macie resource

To remove tags from a Macie resource, you can use the Amazon Macie console or the
Amazon Macie API. To do this for multiple Macie resources at the same time, use the Tag
Editor on the AWS Resource Groups console or the tagging operations of the AWS Resource Groups Tagging
API. For more information, see the [Tagging AWS Resources User
Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Important

Removing tags from a resource can affect access to the resource. Before you remove
a tag, review any AWS Identity and Access Management (IAM) policies that might use the tag to control
access to resources. For more information, see [Controlling access to AWS
resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.

Console
Follow these steps to remove one or more tags from a resource by using the
Amazon Macie console.

###### To remove a tag from a resource

1.  Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2.  Depending on the type of resource that you want to remove a tag
    from, do one of the following:

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
        ![The edit icon, which is a blue pencil.](images/icon-edit-resource-blue.png)
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
4.  Do any of the following:
    - To remove only the tag value for a tag, choose
      **X** in the **Value**
      box that contains the value to remove.
    - To remove both the tag key and tag value (as a pair) for a
      tag, choose **Remove** next to the tag to
      remove.

5.  To remove additional tags from the resource, repeat the preceding
    step for each additional tag to remove.
6.  When you finish removing tags, choose
    **Save**.

API
To remove one or more tags from a resource programmatically, use the
[UntagResource](../APIReference/tags-resourcearn.md "../APIReference/tags-resourcearn.md") operation of the Amazon Macie API. In your request,
use the `resourceArn` parameter to specify the Amazon Resource
Name (ARN) of the resource to remove a tag from. Use the
`tagKeys` parameter to specify the tag key of the tag to
remove. To remove only a specific tag value (not a tag key) from a resource,
[edit the tag](tags-retrieve-update.md#tags-update "tags-retrieve-update.md#tags-update") instead of removing the
tag.

If you're using the AWS Command Line Interface (AWS CLI), run the [untag-resource](../../../cli/latest/reference/macie2/untag-resource.md "../../../cli/latest/reference/macie2/untag-resource.md") command and use the `resource-arn`
parameter to specify the ARN of the resource to remove a tag from. Use the
`tag-keys` parameter to specify the tag key of the tag to
remove. For example, the following command removes the `Stack`
tag (both the tag key and tag value) from the specified sensitive data
discovery job:

```
`C:\>` `aws macie2 untag-resource ^
--resource-arn `arn:aws:macie2:us-east-1:123456789012:classification-job/3ce05dbb7ec5505def334104bexample` ^
--tag-keys `Stack``
```

Where `resource-arn` specifies the ARN of the job to remove a
tag from, and `Stack` is the tag key
of the tag to remove.

To remove multiple tags from a resource, add each additional tag key as an
argument for the `tag-keys` parameter. For example:

```
`C:\>` `aws macie2 untag-resource ^
--resource-arn `arn:aws:macie2:us-east-1:123456789012:classification-job/3ce05dbb7ec5505def334104bexample` ^
--tag-keys `Stack` `Owner``
```

Where `resource-arn` specifies the ARN of the job to remove
tags from, and `Stack` and
`Owner` are the tag keys of
the tags to remove.

If the operation succeeds, Macie returns an empty HTTP 204 response.
Otherwise, Macie returns an HTTP 4*xx* or
500 response that indicates why the operation failed.
