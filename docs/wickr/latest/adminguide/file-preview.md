

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# File preview for AWS Wickr
<a name="file-preview"></a>

Organizations using the Wickr Premium tier (including Premium free trial), can now manage file download permissions at the security group level.

File downloads are enabled by default in security groups. Administrators can enable or disable file downloads through the administrator panel. This setting is applied to the entire Wickr network. 

To enable or disable file download, complete the following procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **Security groups**.

1. Select the name of the security group that you want to edit.

   The security group details page displays the settings for the security group in different tabs.

1. Under the **Messaging** tab, in the **Media and links** section, choose **Edit**.

1. On the **Edit media and links** page, check or uncheck the **File downloads** option.

1. Choose **Save changes**.

When file downloads are enabled for a security group, users can download files shared in direct messages and rooms. If downloads are disabled, they can only preview these files and upload to the **Files** tab, but cannot download them. Users are also restricted from taking screenshots; attempts will result in a black screen.

**Note**  
When File downloads are disabled, all the users in that security group will need to be on Wickr versions 6.54 and above for this file setting to apply.

**Note**  
In rooms where users from different networks (due to federation) and security groups are present, the ability of each user to preview or download files is based on their specific security group settings. As a result, some users can download files in a room while others can only preview them.