

# Delete a site using AWS Network Manager
<a name="deleting-a-site"></a>

Delete sites from your global network if the site is no longer valid or you no longer want to return any information about the site. You must first disassociate the site from any devices and delete any links for the site.

**To delete a site**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Sites**.

1. Select the site and choose **Delete**.

1. In the confirmation dialog box, choose **Delete**.

**Deleting a site using the AWS CLI**  
Use the [delete-site](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/delete-site.html) command.