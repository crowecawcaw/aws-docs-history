# Delete a resource discovery

This section describes how to delete a resource discovery.

###### Note

You cannot delete a default resource discovery. A default resource discovery is one that is
created automatically when you create an IPAM. The default resource discovery is
deleted, however, if you delete the IPAM.

This step must be completed by the **Secondary Org Admin
Account**. For more information about the roles involved in this process,
see [Process overview](enable-integ-ipam-outside-org-process.md "enable-integ-ipam-outside-org-process.md").

AWS Management Console

###### To delete a resource discovery

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Resource discoveries**.
3. Select a resource discovery and choose **Actions** > **Delete resource discovery**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

- To delete a resource discovery: [delete-ipam-resource-discovery](../../../cli/latest/reference/ec2/delete-ipam-resource-discovery.md "../../../cli/latest/reference/ec2/delete-ipam-resource-discovery.md")
