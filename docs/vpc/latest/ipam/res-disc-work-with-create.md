# Create a resource discovery to integrate with another IPAM

This section describes how to create a resource discovery. A resource discovery is
created by default when you create an IPAM. The default quota for resource discoveries per Region is 1. For more information about IPAM quotas, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").

###### Note

Creating, sharing, and associating resource discoveries is part of the process of integrating
IPAM with accounts outside of your organizations (see [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md "enable-integ-ipam-outside-org.md")). If you are not creating
an IPAM and integrating it with accounts outside your organization, you do not need to create, share, or associate resource discoveries.

If you are integrating an IPAM with accounts outside of your organizations, this is a
required step that must be completed by the **Secondary Org Admin
Account**. For more information about the roles involved in this process,
see [Process overview](enable-integ-ipam-outside-org-process.md "enable-integ-ipam-outside-org-process.md").

AWS Management Console

###### To create a resource discovery

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Resource discoveries**.
3. Choose **Create resource discovery**.
4. Select **Allow Amazon VPC IP Address Manager to replicate data from source account(s) into the IPAM delegate account**. If you do not select this option, you cannot create a resource discovery.
5. (Optional) Add a **Name** tag to the resource discovery. A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
6. (Optional) Add a description.
7. Under **Operating regions**, select the AWS Regions in which resources will be discovered. The current Region will automatically be set as one of the operating Regions. If you’re creating the resource discovery so that you can share it with an IPAM in operating Region `us-east-1`, make sure you select `us-east-1` here. If you forget an operating Region, you can return at a later time and edit your resource discovery settings.

###### Note

In most cases, the resource discovery should have the same operating Regions as the IPAM or you will only get resource discovery in that one Region. 8. (Optional) Choose any additional **Tags** for the pool. 9. Choose **Create**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

- Create a resource discovery: [create-ipam-resource-discovery](../../../cli/latest/reference/ec2/create-ipam-resource-discovery.md "../../../cli/latest/reference/ec2/create-ipam-resource-discovery.md")
