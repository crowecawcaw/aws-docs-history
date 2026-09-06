

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Tagging servers in the AWS Migration Hub console
<a name="tag-servers"></a>

To assist migration planning and help stay organized, you can create multiple tags for each server. *Tags* are user-defined key-value pairs that can store any custom data or metadata about servers. You can tag an individual server or multiple servers in a single operation. AWS Application Discovery Service (Application Discovery Service) tags are similar to AWS tags, but the two types of tag cannot be used interchangeably. 

You can add or remove multiple tags for one or more servers from the main **Servers** page. On a server's detail page, you can add or remove one or more tags for the selected server. You can do any type of tagging task involving multiple servers or tags in a single operation. You can also remove tags.<a name="add-tags"></a>

**To add tags to one or more servers**

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane under **Discover**, choose **Servers**.

1. In the **Server info** column, choose the server link for the server that you want to add tags for. To add tags to more than one server at a time, click inside the check boxes of multiple servers.

1. Choose **Add tags**, and then choose **Add new tag**.

1. In the dialog box, type a key in the **Key** field, and optionally a value in the **Value** field.

   Add more tags by choosing **Add new tag** and adding more information.

1. Choose **Save**.<a name="remove-tags"></a>

**To remove tags from one or more servers**

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane under **Discover**, choose **Servers**.

1. In the **Server info** column, choose the server link for the server that you want to remove tags from. Select the check boxes of multiple servers to remove tags from more than one server at a time.

1. Choose **Remove tags**.

1. Select each tag that you want to remove.

1. Choose **Confirm**.