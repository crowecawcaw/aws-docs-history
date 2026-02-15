# Updating LF-Tags

You update a LF-Tag that you have the `Alter` permission on by adding
or deleting permitted key values. You can't change the LF-Tag key. To change the key,
delete the LF-Tag and add one with the required key. In addition to `Alter`
permission, you also need the `lakeformation:UpdateLFTag` IAM permission to update values.

When you delete a LF-Tag value, no check is performed for the presence of that LF-Tag
value on any Data Catalog resource. If the deleted LF-Tag value is associated with a resource, it
is no longer visible for the resource, and any principals that were granted permissions on
that key-value pair no longer have the permissions.

Before deleting a LF-Tag value, you can optionally use the [remove-lf-tags-from-resource command](TBAC-assigning-tags.md#remove-tag-command "TBAC-assigning-tags.md#remove-tag-command")
command to remove the LF-Tag from Data Catalog resources that have the value that you want to
delete, and then retag the resource with the values that you want to keep.

Only data lake administrators, the LF-Tag creator, and principals that have
`Alter` permissions on the LF-Tag can update a LF-Tag.

You can update a LF-Tag by using the AWS Lake Formation console, the API, or the AWS Command Line Interface
(AWS CLI).

Console

###### To update a LF-Tag (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator, LF-Tag creator or a principal with `Alter` permission on the LF-Tag. 2. In the navigation pane, under **Permissions**, **LF-Tags and permissions**, choose
**LF-Tags**. 3. On the **LF-Tags** page, select a LF-Tag, and then
choose **Edit**. 4. In the **Edit LF-Tag** dialog box, add or remove
LF-Tag values.

To add multiple values, in the **Values** field, either enter a
comma-delimited list and press **Enter**, or enter one value at a
time or choose **Add** after each one. 5. Choose **Save**.

AWS CLI

###### To update a LF-Tag (AWS CLI)

- Enter an `update-lf-tag` command. Provide one or both of the
  following arguments:
  - `--tag-values-to-add`
  - `--tag-values-to-delete`

###### Example

The following example replaces the value `vp` with the value
`vice-president` for the LF-Tag key `level`.

```
aws lakeformation update-lf-tag --tag-key level --tag-values-to-add vice-president
--tag-values-to-delete vp

```
