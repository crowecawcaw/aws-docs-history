# Edit tags of selected resources

You can use Tag Editor to change existing tag values on selected resources that are in
the results of your [Find resources to
tag](find-resources-to-tag.md "find-resources-to-tag.md") query. Editing a tag changes the tag's value on all selected
resources that have the same tag key. You can't rename a tag key, but you can delete a
tag and create a tag with a new name to replace the original tag key. This deletes all
tags with that key on selected resources.

###### Important

Do not store personally identifiable information (PII) or other confidential or
sensitive information in tags. We use tags to provide you with billing and
administration services. Tags are not intended to be used for private or sensitive
data.

1. In the results of your **Find resources to tag** query,
   select the check boxes next to the resources for which you want to change
   existing tags. Enter a text string in **Filter resources** to
   filter for part of a resource's name or ID. In the **Tags**
   column, note that resources in the results already have tags applied to them.
2. Choose **Manage tags of the selected resources**.
3. On the **Manage tags** page, in **Edit tags of
   selected resources**, view the tags on the resource that you
   selected. Although your original query might have returned more resources, you
   are changing tags for only those resources that you selected in step 1.
4. Change, add, or delete tag values. Existing tags must have a tag key, but tag
   values are optional.

In this procedure, we change the value of the
`Team` tag to `QA`.

If resources in your selection have different values for the same key,
**Selected resources have different tag values** is
displayed in the **Tag value** field. In this case, placing
your cursor in the box opens a dropdown list of all available values for this
tag key in your selected resources.

If resources in your selection have the tag value you want, the tag value is
highlighted as you type it. For example, if resources in your selection already
have the tag value `QA`, the value is highlighted as you
type `Q`. The values in the dropdown list help keep tag
values consistent across resources. The tag value is changed on all selected
resources. In this example, the tag value is changed to
`QA` for all selected resources that had a
`Team` tag key. For selected resources that don't have
the `Team` tag, the `Team` tag with
the value `QA` is added. 5. When you're finished changing tags, choose **Review and apply
changes**. 6. If you accept the changes, choose **Apply changes to all
selected**. 7. Depending on the number of resources you selected, editing tags can take a few
minutes. Don't leave the page or open a different page in the same browser tab.
If changes were successful, a green success banner is displayed at the top of
the page. Wait for a success or failure banner to appear on the page before you
continue.

If tag changes to some or all resources were not successful, see [Troubleshooting tag changes](troubleshooting-tags.md "troubleshooting-tags.md"). After you resolve the root causes of
unsuccessful tag changes (such as insufficient permissions), you can retry tag
changes on resources for which tag changes failed. For more information, see
[Retry failed tag changes](troubleshooting-tags.md#tagging-resources-retry "troubleshooting-tags.md#tagging-resources-retry").
