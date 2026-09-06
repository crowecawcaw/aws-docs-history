

# Delete a server host key
<a name="server-host-key-delete"></a>

On the AWS Transfer Family console, you can delete a server host key.

**To delete a server host key**

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/).

1. In the left navigation pane, choose **Servers**, and then choose a server that uses the SFTP protocol.

1. On the server details page, scroll down to the **Server host keys** section.  
![The Server host keys console section.](http://docs.aws.amazon.com/transfer/latest/userguide/images/server-host-keys.png)

1. In the **Server Host Keys** section, select a key, and then under **Actions**, choose **Delete**.

1. In the confirmation dialog box that appears, enter the word **delete**, and then choose **Delete** to confirm that you want to delete the host key.

The host key is deleted from the **Servers** page.

To delete the host key by using the AWS CLI, use the [DeleteHostKey](https://docs.aws.amazon.com/transfer/latest/APIReference/API_DeleteHostKey) API operation and provide the server ID and host key ID.

The following example `delete-host-key` AWS CLI command deletes a host key for the specified SFTP-enabled server.

```
aws transfer delete-host-key --server-id {{your-server-id}} --host-key-id {{your-host-key-id}}
```