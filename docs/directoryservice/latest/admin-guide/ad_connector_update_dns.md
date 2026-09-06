

# Updating the DNS address for your AD Connector
<a name="ad_connector_update_dns"></a>

Use the following steps to update the DNS addresses that your AD Connector is pointing to.

**Note**  
If you have an update in progress, you must wait until it is complete before submitting another update.  
If you are using WorkSpaces with your AD Connector, ensure that the DNS addresses for your WorkSpace are updated as well. For more information, see [Update DNS servers for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-dns-server.html).

**To update your DNS settings for AD Connector**

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, under **Active Directory**, choose **Directories**.

1. Choose the directory ID link for your directory.

1. On the **Directory details** page, choose the **Network & Security** tab. 

1. Scroll down to the **Existing DNS settings** section and choose **Update**.

1. In the **Update existing DNS addresses** dialog, type the updated DNS IP addresses, and then choose **Update**.

For more information on troubleshooting AD Connector, see [Troubleshooting AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_troubleshooting.html).