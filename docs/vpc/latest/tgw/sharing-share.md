

# Share a multicast domain in AWS Transit Gateway
<a name="sharing-share"></a>

When an owner shares a multicast domain with you, you can do the following:
+ Register and deregister group members or group sources
+ Associate and disassociate subnets

**Note**  
To share a multicast domain, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. When you share a multicast domain using the Amazon Virtual Private Cloud Console, you add it to an existing resource share. To add the multicast domain to a new resource share, you must first create the resource share using the [AWS RAM console](https://console.aws.amazon.com/ram).  
If you are part of an organization in AWS Organizations and sharing within your organization is enabled, consumers in your organization are automatically granted access to the shared multicast domain. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared multicast domain after accepting the invitation.

You can share a multicast domain that you own using the Amazon Virtual Private Cloud console, AWS RAM console, or the AWS CLI.

**To share a multicast domain that you own using the \*Amazon Virtual Private Cloud Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Multicast Domains**.

1. Select your multicast domain, and then choose **Actions**, **Share multicast domain**. 

1. Select your resource share and choose **Share multicast domain**. 

**To share a multicast domain that you own using the AWS RAM console**  
See [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

**To share a multicast domain that you own using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command.