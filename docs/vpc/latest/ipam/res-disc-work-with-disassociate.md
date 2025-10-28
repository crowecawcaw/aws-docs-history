# Disassociate a resource discovery

This section describes how to disassociate a resource discovery from an IPAM. When you
disassociate a resource discovery from an IPAM, the IPAM no longer monitors all
resources CIDRs and accounts discovered under the resource discovery.

###### Note

You cannot disassociate a default resource discovery association. A default resource discovery
association is one that is created automatically when you create an IPAM. The
default resource discovery association is deleted, however, if you delete the
IPAM.

This step must be completed by the **Primary Org IPAM Account**. For more information about the roles involved in this process, see [Process overview](enable-integ-ipam-outside-org-process.md "enable-integ-ipam-outside-org-process.md").

AWS Management Console

###### To disassociate a resource discovery

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **IPAMs**.
3. Select **Associated discoveries,** and then choose **Disassociate resource discoveries**.
4. Under **IPAM resource discoveries**, choose a resource discovery that’s been shared with you by the **Secondary Org Admin Account**.
5. Choose **Disassociate**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

- To disassociate a resource discovery: [disassociate-ipam-resource-discovery](../../../cli/latest/reference/ec2/disassociate-ipam-resource-discovery.md "../../../cli/latest/reference/ec2/disassociate-ipam-resource-discovery.md")
