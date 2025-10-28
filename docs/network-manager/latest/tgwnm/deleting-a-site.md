# Delete a site using AWS Network Manager

Delete sites from your global network if the site is no longer valid or you no longer want to return any information about the site. You must first disassociate the
site from any devices and delete any links for the site.

###### To delete a site

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Sites**.
5. Select the site and choose **Delete**.
6. In the confirmation dialog box, choose **Delete**.

###### Deleting a site using the AWS CLI

Use the [delete-site](../../../cli/latest/reference/networkmanager/delete-site.md "../../../cli/latest/reference/networkmanager/delete-site.md") command.
