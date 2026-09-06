

# Share a resource discovery with another AWS account
<a name="res-disc-work-with-share"></a>

Follow the steps in this section to share a resource discovery using AWS Resource Access Manager. For more information about AWS RAM, see [Sharing your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html) in the *AWS RAM User Guide*.

**Note**  
Creating, sharing, and associating resource discoveries is part of the process of integrating IPAM with accounts outside of your organizations (see [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md)). If you are not creating an IPAM and integrating it with accounts outside your organization, you do not need to create, share, or associate resource discoveries.

When you create an IPAM that monitors accounts outside your organization, the Secondary Org Admin Account shares their resource discovery with the Primary Org IPAM Account using AWS RAM. You must first share a resource discovery with the Primary Org IPAM Account before the Primary Org IPAM Account can associate the resource discovery with their IPAM. For more information about the roles involved in this process, see [Process overview](enable-integ-ipam-outside-org-process.md). 

**Note**  
When you create a resource share using AWS RAM to share a resource discovery, you must create the resource share in the home Region of the Primary Org IPAM.
The account that creates and deletes a resource share for a resource discovery must have the following permissions in their IAM policy:  
ec2:PutResourcePolicy
ec2:DeleteResourcePolicy
If you share a resource discovery with another account, that account can see any [OU exclusions](exclude-ous.md) on it, which contains information such as the Org ID, Root ID, and organizational unit IDs of the resource discovery owner's Organization.

If you are integrating an IPAM with accounts outside of your organizations, this is a required step that must be completed by the **Secondary Org Admin Account**.

------
#### [ AWS Management Console ]

**To share a resource discovery**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Resource discoveries**.

1. Choose the **Resource sharing** tab.

1. Choose **Create resource share**. The AWS RAM console opens, which is where you will create the resource share. 

1. In the AWS RAM console, choose **Settings**.

1. Choose **Enable sharing with AWS Organizations**, and then choose **Save settings**.

1. Choose **Create a resource share**.

1. Add a **Name** for the shared resource.

1. Under **Select resource type**, select **IPAM Resource Discovery**, and choose the resource discovery.

1. Choose **Next**.

1. Under **Associate permissions**, you can view the default permission that will be enabled for principals that are granted access to this resource share:
   + AWSRAMPermissionIpamResourceDiscovery
   + Actions allowed by this permission:
     + ec2:AssociateIpamResourceDiscovery
     + ec2:GetIpamDiscoveredAccounts
     + ec2:GetIpamDiscoveredPublicAddresses
     + ec2:GetIpamDiscoveredResourceCidrs

1. Specify the principals that are allowed access to the shared resource. For **Principals**, choose the Primary Org IPAM Account, and then choose **Add**.

1. Choose **Next**.

1. Review the resource share options and the principals that you'll be sharing with. Then choose **Create resource share**.

1. After a resource discovery is shared, it must be accepted by the Primary Org IPAM Account and then associated with an IPAM by the Primary Org IPAM Account. For more information, see [Associate a resource discovery with an IPAM](res-disc-work-with-associate.md).

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

1. Create the resource share: [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html)

1. View the resource share: [get-resource-shares](https://docs.aws.amazon.com/cli/latest/reference/ram/get-resource-shares.html)

------