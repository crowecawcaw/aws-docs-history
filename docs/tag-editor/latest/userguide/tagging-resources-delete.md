# Remove tags from selected resources

You can use Tag Editor to remove tags from selected resources that are in the results of
your [Find resources to tag](find-resources-to-tag.md "find-resources-to-tag.md") query. Removing a tag deletes
the tag from all selected resources that have the tag. Because you can't edit tag keys,
you can remove tags and replace them with new tags if you need to edit a tag key. This
deletes all tags with that key on selected resources.

1. In the results of your **Find resources to tag** query,
   select the check boxes next to the resources you want to remove tags from. Enter
   a text string in **Filter resources** to filter for part of a
   resource's name or ID.
2. Choose **Manage tags of the selected resources**.
3. On the **Manage tags** page, in **Edit tags of
   selected resources**, view the tags on the resources that you
   selected. Although your original query might have returned more resources,
   you're changing tags for only those resources that you selected in step
4.
5. Choose **Remove tag** next to any tags that you want to
   delete. In this procedure, we remove the `Team` tag.

###### Note

Choosing **Remove tag** removes a tag from all selected
resources that have the tag. 5. Choose **Review and apply changes**. 6. On the confirmation page, choose **Apply changes to all
selected**. 7. Depending on the number of resources you selected, removing tags can take a
few minutes. Don't leave the page or open a different page in the same browser
tab. If changes were successful, a green success banner is displayed at the top
of the page. Wait for a success or failure banner to appear on the page before
you continue.

If tag changes to some or all resources were not successful, see [Troubleshooting Tag Changes](troubleshooting-tags.md "troubleshooting-tags.md"). After you resolve the root causes of
unsuccessful tag changes (such as insufficient permissions), you can retry tag
changes on resources for which tag changes failed. For more information, see
[Retry failed tag changes](troubleshooting-tags.md#tagging-resources-retry "troubleshooting-tags.md#tagging-resources-retry").
