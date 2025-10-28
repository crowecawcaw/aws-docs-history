# Set file share visibility

File share visibility controls whether the shares on a gateway are visible when
listing shares to users, such as in a net view or browse list. If the file shares on
a gateway are visible, then clients can easily discover the shares using a file
browser if they know the gateway IP address or DNS name. If the file shares are not
visible, then clients need to know the file share name in addition to the gateway IP
or DNS name to be able to discover the shares.

###### Note

This setting is not an effective method for securing access to the file shares
in your deployment. For security, we recommend configuring permissions to limit
access to specific users and groups. For instructions, see [Limit user
and group access for your SMB file share](edit-file-share-access-smb.md "edit-file-share-access-smb.md").

###### To set file share visibility

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways**, then choose the gateway for which
   you want to edit SMB settings.
3. From the **Actions** drop-down menu, choose
   **Edit SMB settings**, then choose **File share
   visibility settings**.
4. For **Visibility status**, select the check box if you
   want the shares on this gateway to appear when the gateway lists shares to
   users. Keep the check box cleared if you do not want the shares on this
   gateway to appear when the gateway lists shares to users.
