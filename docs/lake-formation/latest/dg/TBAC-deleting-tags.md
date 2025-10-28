# Deleting LF-Tags

You can delete LF-Tags that are no longer in use. No check is performed for the presence
of the LF-Tag on a Data Catalog resource. If the deleted LF-Tag is associated with a resource,
it is no longer visible for the resource, and any principals that were granted permissions on
that LF-Tag no longer have the permissions.

Before deleting a LF-Tag, you can optionally use the [remove-lf-tags-from-resource](TBAC-assigning-tags.md#remove-tag-command "TBAC-assigning-tags.md#remove-tag-command") command to remove the LF-Tag from all
resources.

Only data lake administrators, the LF-Tag creator, or a principal that has
`Drop` permission on the LF-Tag can delete a LF-Tag. In addition
to the `Drop` permission, the principal also need
`lakeformation:DeleteLFTag` IAM permission to delete a LF-Tag.

You can delete a LF-Tag by using the AWS Lake Formation console, the API, or the AWS Command Line Interface
(AWS CLI).

Console

###### To delete a LF-Tag (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator. 2. In the navigation pane, under **Permissions**,
**LF-Tags and permissions**, choose
**LF-Tags**. 3. On the **LF-Tags** page, select a LF-Tag, and then
choose **Delete**. 4. In the **Delete tag environment?** dialog box, to confirm the
deletion, enter the LF-Tag key value in the designated field and then choose
**Delete**.

AWS CLI

###### To delete a LF-Tag (AWS CLI)

- Enter a `delete-lf-tag` command. Provide the key of the LF-Tag to
  delete.

The following example deletes the LF-Tag with the key
`region`.

```
aws lakeformation delete-lf-tag --tag-key region
```
