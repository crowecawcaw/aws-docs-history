Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Tagging Storage Gateway resources

In Storage Gateway, you can use tags to manage your resources. Tags let you add metadata to your
resources and categorize your resources to make them easier to manage. Each tag consists of
a key-value pair, which you define. You can add tags to gateways, volumes, and virtual
tapes. You can search and filter these resources based on the tags you add.

As an example, you can use tags to identify Storage Gateway resources used by each department
in your organization. You might tag gateways and volumes used by your accounting department
like this: (`key=department` and `value=accounting`). You can then
filter with this tag to identify all gateways and volumes used by your accounting department
and use the information to determine cost. For more information, see [Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") and [Working with Tag
Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md").

If you archive a virtual tape that is tagged, the tape maintains its tags in the archive.
Similarly, if you retrieve a tape from the archive to another gateway, the tags are
maintained in the new gateway.

For File Gateway, you can use tags to control access to resources. For information about
how to do this, see [Using tags to control access to your gateway and
resources](restrict-fgw-access.md "restrict-fgw-access.md").

Tags don’t have any semantic meaning but rather are interpreted as strings of
characters.

The following restrictions apply to tags:

- Tag keys and values are case-sensitive.
- The maximum number of tags for each resource is 50.
- Tag keys cannot begin with `aws:`. This prefix is reserved for AWS
  use.
- Valid characters for the key property are UTF-8 letters and numbers, space, and
  special characters + - = . \_ : / and @.

## Working with tags

You can work with tags by using the Storage Gateway console, the Storage Gateway API, or the
[Storage Gateway
Command Line Interface (CLI)](../../../cli/latest/reference/storagegateway/index.md "../../../cli/latest/reference/storagegateway/index.md"). The following procedures show you how to add,
edit, and delete a tag on the console.

###### To add a tag

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose the resource you want to tag.

For example, to tag a gateway, choose **Gateways**, and then
choose the gateway you want to tag from the list of gateways. 3. Choose **Tags**, and then choose **Add/edit
tags**. 4. In the **Add/edit tags** dialog box, choose **Create
tag**. 5. Type a key for **Key** and a value for
**Value**. For example, you can type
`Department` for the key and
`Accounting` for the value.

###### Note

You can leave the **Value** box blank. 6. Choose **Create Tag** to add more tags. You can add multiple
tags to a resource. 7. When you’re done adding tags, choose **Save**.

###### To edit a tag

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose the resource whose tag you want to edit.
3. Choose **Tags** to open the **Add/edit
   tags** dialog box.
4. Choose the pencil icon next to the tag you want to edit, and then edit the
   tag.
5. When you’re done editing the tag, choose **Save**.

###### To delete a tag

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose the resource whose tag you want to delete.
3. Choose **Tags**, and then choose **Add/edit
   tags** to open the **Add/edit tags** dialog
   box.
4. Choose the **X** icon next to the tag you want to delete, and
   then choose **Save**.
