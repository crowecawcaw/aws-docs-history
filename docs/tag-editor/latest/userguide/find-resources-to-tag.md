# Finding resources to tag

With Tag Editor, you build a query to find resources in one or more AWS Regions that are
available for tagging. You can choose up to 20 individual resource types, or build a query
on **All resource types**. Your query can include resources that already
have tags, or resources that have no tags. For more information, see the **Tag Editor Tagging** column at [Supported resource types](../../../ARG/latest/userguide/supported-resources.md "../../../ARG/latest/userguide/supported-resources.md") in the
_AWS Resource Groups User Guide_.

After you find resources to tag, you can use Tag Editor to add tags, or view, edit, or delete
tags.

###### To find resources to tag

1. Open the [Tag Editor
   console](https://console.aws.amazon.com/resource-groups/tag-editor "https://console.aws.amazon.com/resource-groups/tag-editor").
2. _(Optional)_ Choose the AWS Regions in which to search for
   resources to tag. By default, your current Region is used. For this procedure,
   choose **us-east-1** and **us-west-2**.
3. Choose at least one resource type from the **Resource types**
   dropdown list. You can add or edit tags for up to 20 individual resource types at a
   time, or choose **All resource types**. For this procedure, choose
   **AWS::EC2::Instance** and
   **AWS::S3::Bucket**.
4. _(Optional)_ In the **Tags** fields, enter a
   tag key, or a tag key and value pair, to limit the resources in the current
   AWS Region to only those that are tagged with your specified values. As you enter a
   tag key, matching tag keys in the current Region appear in a list. You can
   choose a tag key from the list. Tag Editor auto-completes the tag key for you as you
   type enough characters to match an existing key. Choose **Add** or
   press **Enter** when you've finished your tag. In this example,
   filter for resources that have a tag key of **Stage**. The tag
   value is optional but narrows the results of the query further. To add more tags,
   choose **Add**. Queries assign an `AND` operator to
   tags, so only resources that match both the specified resource type and all
   specified tags are returned by the query.

###### Note

The Tag Editor console doesn't currently support wildcards.

To find resources with multiple values for a tag key, add another tag with the
same key to the query, but specify a different value. The results include all
resources that are tagged with the same tag key and that have any of the selected
values. The search is case sensitive.

Leave the **Tags** boxes empty to find all resources of the
specified type in the selected AWS Regions. This query returns resources that have
any tags, and includes those that have no tags. To remove a tag from your query,
choose **X** on the tag's label.

To find resources that have a tag, but with an empty value, choose
**(empty value)**.

###### Note

Before you can find resources with the specified tags, they must have been
applied to at least one resource of the specified type in the current
AWS Region. 5. When your query is ready, choose **Search resources**. Results
are displayed as a table in the **Resource search results**
area.

To filter a large number of resources, enter any filter text, such as part of the
name of a resource, in **Filter resources**.

###### Note

You can use substrings to filter your results. 6. _(Optional)_ To configure the columns that Tag Editor displays in
your resource search results, choose the **Preferences** gear icon in the
**Resource search results**.

On the **Preferences** page, choose the number of rows that you
want displayed in your search results. If you'd like to see all the text in the
table, select the **Wrap lines** check box.

Turn on columns that you want Tag Editor to display in your results. You can show a
column for each tag that occurs in your search results or a selected subset of your
search results. You can do this anytime after you find resources to tag. To enable a
column, choose the switch icon next to the tag and change it from off
to on.

When you are finished configuring visible columns and number of displayed rows,
choose **Confirm**.
