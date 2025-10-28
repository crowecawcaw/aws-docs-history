# Add tags to selected resources

You can use Tag Editor to add tags to selected resources that are in the results of your
**Find resources to tag** query.

###### Note

This topic describes how to bulk edit the tags for _multiple_ resources. You can also edit the tag values for an
individual resource. For more information, see [View and edit existing tags for a selected
resource](tagging-resources-view.md "tagging-resources-view.md").

1. Open the [Tag Editor console](https://console.aws.amazon.com/resource-groups/tag-editor "https://console.aws.amazon.com/resource-groups/tag-editor"), and submit a query that returns multiple resources
   that you want to tag.
2. In the results table of your **Find resources to tag** query,
   select the check boxes next to the resources that you want to add tags to. Enter
   a text string in **Filter resources** at the top of the table
   to filter for part of a resource's name, ID, tag keys, or tag values. In the
   **Tags** column, note that resources in the results already
   have tags applied to them.
3. Select the check box for one or more resources, and then choose
   **Manage tags of the selected resources**.
4. On the **Manage tags** page, view the tags on
   the resources that you selected. Although your original query returned more
   resources, you're adding tags to only those resources that you selected in step
5. Choose **Add tag**.
6. Enter a tag key and an optional tag value. For this procedure, you'll add the
   tag key `Team` and the tag value
   `Development`.

###### Note

A resource can have a maximum of 50 user-applied tags. You might not be
able to add new tags to a resource if you're approaching 50 user-applied
tags. AWS generated tags don't apply to the 50-tag limit. Tag keys must
also be unique within your selected resources. You can't add a new tag with
a key that matches a tag key that already exists in your selected resources. 6. When you're finished adding tags, choose **Review and apply
changes**. 7. If you accept the changes, choose **Apply changes to all
selected**. 8. Depending on the number of resources you select, applying new tags can take a
few minutes. Don't leave the page or open a different page in the same browser
tab. If changes were successful, a green success banner is displayed at the top
of the page. Wait for a success or failure banner to appear on the page before
you continue.

If tag changes to some or all resources were not successful, see [Troubleshooting tag changes](troubleshooting-tags.md "troubleshooting-tags.md"). After you resolve the unsuccessful tag
changes (such as insufficient permissions), you can retry the tag changes on
resources for which tag changes failed. For more information, see [Retry failed tag changes](troubleshooting-tags.md#tagging-resources-retry "troubleshooting-tags.md#tagging-resources-retry").
