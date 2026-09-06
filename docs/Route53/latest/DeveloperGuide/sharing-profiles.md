

# Working with shared Route 53 Profiles
<a name="sharing-profiles"></a>

You can share a Profile with other accounts by:
+ Granting read-only permissions, which means the other account can associate the Profile to their VPCs. In this case all the DNS resources and configurations will be in effect on the associated VPCs.
+ Granting admin permissions. In this case the accounts with the shared Profile can modify the Profile and then associate it with their VPCs. An owner can also create customer managed permissions that can be used to specify which actions can be performed by the consumer account. For more information, see [Customer managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/create-customer-managed-permissions.html) in the *AWS RAM User Guide*.

Amazon Route 53 Profile integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a service that enables you to share some Route 53 resources with other AWS accounts or through AWS Organizations. With AWS RAM, you share resources that you own by creating a *resource share*. A resource share specifies the resources to share, and the consumers with whom to share them. Consumers can include:
+ Specific AWS accounts 
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations

For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.

This topic explains how to share resources that you own, and how to use resources that are shared with you.

**Topics**
+ [Granting permissions for sharing Route 53 Profiles](#sharing-prereqs)
+ [Prerequisites for sharing Route 53 Profiles](#sharing-prereqs)
+ [Sharing a Route 53 Profile](#sharing-share)
+ [Unsharing a shared Route 53 Profile](#sharing-unshare)
+ [Identifying a shared Route 53 Profile](#sharing-identify)
+ [Responsibilities and permissions for shared Route 53 Profiles](#sharing-perms)
+ [Billing and metering](#sharing-billing)
+ [Instance quotas](#sharing-quotas)

## Granting permissions for sharing Route 53 Profiles
<a name="sharing-prereqs"></a>

A minimum set of permissions is required for an IAM principal to share a Profile. We recommend using the `AmazonRoute53ProfilesFullAccess` managed IAM policy to make sure your IAM principals have the required permissions to share and use shared Profiles.

If you use a custom IAM policy, the `route53profiles:GetProfilePolicy` and `route53profiles:PutProfilePolicy` actions are required. These are permission-only IAM actions. If an IAM principal doesn't have these permissions granted, an error will occur when attempting to share the Profile using the AWS RAM service.

## Prerequisites for sharing Route 53 Profiles
<a name="sharing-prereqs"></a>
+ To share a Route 53 Profile, you must own it in your AWS account. This means that the resource must be allocated or provisioned in your account. You cannot share a Route 53 Profile that has been shared with you.
+ To share a Route 53 Profile with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [ Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

## Sharing a Route 53 Profile
<a name="sharing-share"></a>

When you share a Profile that you own with another AWS account, you enable them to apply the DNS-related settings of the Profile to their VPCs. This makes it easier to apply uniform DNS configurations across thousands of VPCs with minimal management overhead. 

To share a Route 53 Profile, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. When you share a Route 53 Profile using the Route 53 console, you add it to an existing resource share. To add the Route 53 Profile to a new resource share, you must first create the resource share using the [AWS RAM console](https://console.aws.amazon.com/ram).

If you are part of an organization in AWS Organizations and sharing within your organization is enabled, consumers in your organization are automatically granted access to the shared Route 53 Profile. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared Route 53 Profile after accepting the invitation.

You can get started sharing a Route 53 Profile that you own on the Route 53 console and continue on the AWS RAM console.

**To share a Route 53 Profile that you own using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Profiles**.

1. Select the Profile you want to share, and on the **Profile details** page, choose **Share profile**.

1. You're taken to the AWS RAM console where you can follow these steps: [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

1. If a Profile is shared to you, the **Profiles** table includes the text **Shared with me**.

   When you have shared a Profile, it is listed as **Shared** in the **Profiles** table.

**To share a Route 53 Profile that you own using the AWS RAM console**  
See [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

**To share a Route 53 Profile that you own using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command.

## Unsharing a shared Route 53 Profile
<a name="sharing-unshare"></a>

When you unshare a Profile, and VPCs that have that Profile's configurations associated to them, will lose them, and default to the VPC-specific configurations.

To unshare a shared Route 53 Profile that you own, you must remove it from the resource share. You can do this using the Route 53 console, AWS RAM console, or the AWS CLI.

**To unshare a shared Route 53 Profile that you own using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Profiles**.

1. Select the linked name of the Profile you want to unshare, and on the **<Profile name>** page, choose **Manage sharing**.

1. You're taken to the AWS RAM console where you can follow these steps: [Updating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared Route 53 Profile that you own using the AWS RAM console**  
See [Updating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared Route 53 Profile that you own using the AWS CLI**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

## Identifying a shared Route 53 Profile
<a name="sharing-identify"></a>

Owners and consumers can identify shared Route 53 Profiles using the Route 53 console and AWS CLI.

**To identify a shared Route 53 Profile using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Profiles**.

1. If a Profile is shared to you, the **Profiles** table includes the text **Shared with me**.

   When you have shared a Profile, it is listed as **Shared** in the **Profiles** table.

**To identify a shared Route 53 Profile using the AWS CLI**  
Use the [get-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/get-profile.html) or the [list-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/_route53profiles/list-profile.html) command. The commands returns information about the Route 53 Profiles that you own and the Route 53 Profiles sharing status. 

## Responsibilities and permissions for shared Route 53 Profiles
<a name="sharing-perms"></a>

### Permissions for owners
<a name="perms-owner"></a>

A Profile owner can view, manage, and delete Profile resource associations, including resource associations made by the consumer accounts. The owner is able to view and delete the VPC associations they own. Additionally, only a Profile owner can delete a Profile they own, and this also automatically removes all resource associations of the Profile.

**Note**  
You must create a custom managed permission which includes the `route53profiles:AssociateResourceToProfile` action in addition to the default ones to associate any resources from the accounts the Profile is shared to, because the default policy `AWSRAMPermissionRoute53ProfileAllowAssociation` does not include it.

### Permissions for consumers
<a name="perms-consumer"></a>

 Default permission for consumers of a shared Profile is read-only. With read-only permission they can see the associated resources and associate it to VPCs, but can't manage the resource associations.

An owner can also create customer managed permissions on the AWS RAM console. For more information, see [Creating and using customer managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/create-customer-managed-permissions.html) in the *AWS RAM User Guide*.

## Billing and metering
<a name="sharing-billing"></a>

Route 53 Profiles are billed based on the number of VPC associations. The Profile owner is responsible for the bill for the VPC associations by the customer.

## Instance quotas
<a name="sharing-quotas"></a>

The Profile owners and consumers share the same quota, except for the number of Route 53 Profiles per account in a Region. For more information, see [Quotas on Route 53 Profiles](DNSLimitations.md#limits-api-entities-route53-profiles)