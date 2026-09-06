

# Work with shared prefix lists
<a name="work-with-shared-prefixes"></a>

AWS prefix lists provide a convenient way to manage and reference the IP address ranges used by various AWS services. In addition to the AWS-managed prefix lists, you also can create and share your own customer-managed prefix lists with other AWS accounts.

Sharing prefix lists can be particularly useful for organizations with complex networking requirements or those that need to coordinate IP address usage across multiple AWS workloads. By sharing a prefix list, you can ensure consistent IP address management and simplify networking configurations for your collaborators.

This section describes and how to share prefix lists and how to identify and use prefix lists that have been shared with your account.

**Topics**
+ [Share a prefix list](#sharing-share)
+ [Unshare a shared prefix list](#sharing-unshare)
+ [Identify a shared prefix list](#sharing-identify)
+ [Identify references to a shared prefix list](#sharing-identify-references)

## Share a prefix list
<a name="sharing-share"></a>

To share a prefix list, you must add it to a resource share. If you do not have a resource share, you must first create one using the [AWS RAM console](https://console.aws.amazon.com/ram).

If you are part of an organization in AWS Organizations, and sharing within your organization is enabled, consumers in your organization are automatically granted access to the shared prefix list. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared prefix list after accepting the invitation.

You can create a resource share and share a prefix list that you own using the AWS RAM console, or the AWS CLI.

**Important**  
To share a prefix list, you must own it. You cannot share a prefix list that has been shared with you. You cannot share an AWS-managed prefix list.
To share a prefix list with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [ Enable sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

**To create a resource share and share a prefix list using the AWS RAM console**  
Follow the steps in [Create a resource share](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-create) in the *AWS RAM User Guide*. For **Select resource type**, choose **Prefix Lists**, and then select the check box for your prefix list.

**To add a prefix list to an existing resource share using the AWS RAM console**  
To add a managed prefix that you own to an existing resource share, follow the steps in [Updating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*. For **Select resource type**, choose **Prefix Lists**, and then select the check box for your prefix list.

**To share a prefix list that you own using the AWS CLI**  
Use the following commands to create and update a resource share:
+ [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) 
+ [associate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/associate-resource-share.html) 
+ [update-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/update-resource-share.html) 

## Unshare a shared prefix list
<a name="sharing-unshare"></a>

When you unshare a prefix list, consumers can no longer view the prefix list or its entries in their account, and they cannot reference the prefix list in their resources. If the prefix list is already referenced in the consumer's resources, those references continue to function as normal, and you can continue to [view those references](#sharing-identify-references). If you update the prefix list to a new version, the references use the latest version.

To unshare a shared prefix list that you own, you must remove it from the resource share using AWS RAM.

**To unshare a shared prefix list that you own using the AWS RAM console**  
See [Updating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared prefix list that you own using the AWS CLI**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

## Identify a shared prefix list
<a name="sharing-identify"></a>

Owners and consumers can identify shared prefix lists using the Amazon VPC console and AWS CLI.

**To identify a shared prefix list using the Amazon VPC console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Managed Prefix Lists**.

1. The page displays the prefix lists that you own and the prefix lists that are shared with you. The **Owner ID** column shows the AWS account ID of the prefix list owner.

1. To view the resource share information for a prefix list, select the prefix list and choose **Sharing** in the lower pane.

**To identify a shared prefix list using the AWS CLI**  
Use the [describe-managed-prefix-lists](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-managed-prefix-lists.html) command. The command returns the prefix lists that you own and the prefix lists that are shared with you. `OwnerId` shows the AWS account ID of the prefix list owner.

## Identify references to a shared prefix list
<a name="sharing-identify-references"></a>

Owners can identify the consumer-owned resources that are referencing a shared prefix list.

**To identify references to a shared prefix list using the Amazon VPC console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Managed Prefix Lists**.

1. Select the prefix list and choose **Associations** in the lower pane.

1. The IDs of the resources that are referencing the prefix list are listed in the **Resource ID** column. The owners of the resources are listed in the **Resource Owner** column.

**To identify references to a shared prefix list using the AWS CLI**  
Use the [get-managed-prefix-list-associations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-managed-prefix-list-associations.html) command.