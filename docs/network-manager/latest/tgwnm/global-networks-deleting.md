

# Delete a global network using AWS Network Manager
<a name="global-networks-deleting"></a>

Delete a global network framework. You cannot delete a global network if there are any network objects in the global network, including transit gateways, links, devices, and sites. You must first deregister or delete the network objects.

**To delete your global network**

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. In the navigation pane, choose **Global networks**.

1. Choose your global network and choose **Delete**.

1. In the confirmation dialog box, choose **Delete**.

**To delete a global network using the AWS CLI**  
Use the [delete-global-network](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/delete-global-network.html) command.