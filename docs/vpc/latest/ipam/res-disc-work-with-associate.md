# Associate a resource discovery with an IPAM

This section describes how to associate a resource discovery with an IPAM. When you
associate a resource discovery with an IPAM, the IPAM monitors all resources CIDRs and
accounts discovered under the resource discovery. When you create an IPAM, a default
resource discovery is created for your IPAM and automatically associated with your
IPAM.

The default quota for resource discovery associations is 5. For more information (including how to adjust this quota), see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").

###### Note

Creating, sharing, and associating resource discoveries is part of the process of integrating
IPAM with accounts outside of your organizations (see [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md "enable-integ-ipam-outside-org.md")). If you are not creating
an IPAM and integrating it with accounts outside your organization, you do not need to create, share, or associate resource discoveries.

If you are integrating an IPAM with accounts outside of your organizations, this is a
required step that must be completed by the **Primary Org IPAM
Account**. For more information about the roles involved in this process,
see [Process overview](enable-integ-ipam-outside-org-process.md "enable-integ-ipam-outside-org-process.md").

AWS Management Console

###### To associate a resource discovery

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **IPAMs**.
3. Select **Associated discoveries**, and then choose **Associate resource discoveries**.
4. Under **IPAM resource discoveries**, choose a resource discovery that’s been shared with you by the **Secondary Org Admin Account**.
5. Choose **Associate**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

- Associate a resource discovery: [associate-ipam-resource-discovery](../../../cli/latest/reference/ec2/associate-ipam-resource-discovery.md "../../../cli/latest/reference/ec2/associate-ipam-resource-discovery.md")
