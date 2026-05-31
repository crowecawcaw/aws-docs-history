# Managing tags

You can add, edit, and delete tags by using the AWS Management Console, the
AWS Command Line Interface, or the AWS Certificate Manager API.

## Managing tags (console)

You can use the AWS Management Console to add, delete, or edit tags. You can also display tags
in columns.

### Adding a tag

Use the following procedure to add tags by using the ACM console.

###### To add a tag to a certificate (console)

1. Sign into the AWS Management Console and open the AWS Certificate Manager console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").
2. Choose the arrow next to the certificate that you want to tag.
3. In the details pane, scroll down to **Tags**.
4. Choose **Edit** and **Add
   Tag**.
5. Type a key and a value for the tag.
6. Choose **Save**.

### Deleting a tag

Use the following procedure to delete tags by using the ACM console.

###### To delete a tag (console)

1. Sign into the AWS Management Console and open the AWS Certificate Manager console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").
2. Choose the arrow next to the certificate with a tag that you want to
   delete.
3. In the details pane, scroll down to **Tags**.
4. Choose **Edit**.
5. Choose the **X** next to the tag you want to delete.
6. Choose **Save**.

### Editing a tag

Use the following procedure to edit tags by using the ACM console.

###### To edit a tag (console)

1. Sign into the AWS Management Console and open the AWS Certificate Manager console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").
2. Choose the arrow next to certificate you want to edit.
3. In the details pane, scroll down to **Tags**.
4. Choose **Edit**.
5. Modify the key or value of the tag you want to change.
6. Choose **Save**.

### Showing tags in columns

Use the following procedure to show tags in columns in the ACM
console.

###### To display tags in columns (console)

1. Sign into the AWS Management Console and open the AWS Certificate Manager console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").
2. Choose the tags that you want to display as columns by choosing the
   gear icon
   ![Gear or settings icon, represented by a simple cog wheel symbol.](images/acm-gear-icon-console.png)
   in the upper right corner of the console.
3. Select the check box beside the tag that you want to display in a
   column.

## Managing tags (CLI)

Refer to the following topics to learn how to add, list, and delete tags by using
the AWS CLI.

- [add-tags-to-certificate](../../../cli/latest/reference/acm/add-tags-to-certificate.md "../../../cli/latest/reference/acm/add-tags-to-certificate.md")

- [list-tags-for-certificate](../../../cli/latest/reference/acm/list-tags-for-certificate.md "../../../cli/latest/reference/acm/list-tags-for-certificate.md")

- [remove-tags-from-certificate](../../../cli/latest/reference/acm/remove-tags-from-certificate.md "../../../cli/latest/reference/acm/remove-tags-from-certificate.md")

## Managing tags (ACM API)

Refer to the following topics to learn how to add, list, and delete tags by using
the API.

- [AddTagsToCertificate](../APIReference/API_AddTagsToCertificate.md "../APIReference/API_AddTagsToCertificate.md")

- [ListTagsForCertificate](../APIReference/API_ListTagsForCertificate.md "../APIReference/API_ListTagsForCertificate.md")

- [RemoveTagsFromCertificate](../APIReference/API_RemoveTagsFromCertificate.md "../APIReference/API_RemoveTagsFromCertificate.md")
